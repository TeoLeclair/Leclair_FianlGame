import tkinter as tk
from tkinter import messagebox
import random

class MemoryCardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")

        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.card_values = self.cards * 2
        random.shuffle(self.card_values)

        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(4):
            for j in range(4):
                button = tk.Button(self.root, text=" ", width=5, height=2, command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def flip_card(self, row, col):
        index = row * 4 + col
        self.buttons[index].config(text=self.card_values[index], state=tk.DISABLED)
        self.root.update()

        if not hasattr(self, 'first_card_index'):
            self.first_card_index = index
        else:
            if self.card_values[index] == self.card_values[self.first_card_index] and index != self.first_card_index:
                messagebox.showinfo("Match", "You found a match!")
                self.buttons[index].config(state=tk.DISABLED)
                self.buttons[self.first_card_index].config(state=tk.DISABLED)
            else:
                messagebox.showinfo("No Match", "Try again!")
                self.buttons[index].config(text=" ")
                self.buttons[self.first_card_index].config(text=" ")

            delattr(self, 'first_card_index')

        if all(button['state'] == tk.DISABLED for button in self.buttons):
            messagebox.showinfo("Congratulations", "You've matched all the pairs!")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryCardGame(root)
    root.mainloop()