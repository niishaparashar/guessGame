
    import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x400")
        
        # Game variables
        self.low = 0
        self.high = 0
        self.num = 0
        self.chances = 7
        self.guess_count = 0
        
        # UI Elements
        tk.Label(root, text="Number Guessing Game", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(root, text="Lower Bound:").pack()
        self.entry_low = tk.Entry(root)
        self.entry_low.pack(pady=5)
        
        tk.Label(root, text="Upper Bound:").pack()
        self.entry_high = tk.Entry(root)
        self.entry_high.pack(pady=5)
        
        tk.Button(root, text="Set Range", command=self.set_bounds).pack(pady=10)
        
        tk.Label(root, text="Enter your guess:").pack()
        self.entry_guess = tk.Entry(root, state="disabled")
        self.entry_guess.pack(pady=5)
        
        self.button_guess = tk.Button(root, text="Guess", command=self.make_guess, state="disabled")
        self.button_guess.pack(pady=10)
        
        self.label_feedback = tk.Label(root, text="", font=("Arial", 12), wraplength=250)
        self.label_feedback.pack(pady=10)
        
        self.label_chances = tk.Label(root, text=f"Chances left: {self.chances}", font=("Arial", 12))
        self.label_chances.pack(pady=5)
    
    def set_bounds(self):
        try:
            self.low = int(self.entry_low.get())
            self.high = int(self.entry_high.get())
            if self.low >= self.high:
                messagebox.showerror("Error", "Lower bound must be less than upper bound!")
                return
            self.num = random.randint(self.low, self.high)
            self.label_feedback.config(text=f"Guess a number between {self.low} and {self.high}!")
            self.entry_low.config(state="disabled")
            self.entry_high.config(state="disabled")
            self.entry_guess.config(state="normal")
            self.button_guess.config(state="normal")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def make_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.guess_count += 1
            self.chances -= 1
            self.label_chances.config(text=f"Chances left: {self.chances}")
            
            if guess == self.num:
                self.label_feedback.config(text=f"Correct! The number is {self.num}. Guessed in {self.guess_count} tries.")
                self.end_game()
            elif self.chances == 0:
                self.label_feedback.config(text=f"Game Over! The number was {self.num}.")
                self.end_game()
            elif guess > self.num:
                self.label_feedback.config(text="Too high! Try lower.")
            else:
                self.label_feedback.config(text="Too low! Try higher.")
            
            self.entry_guess.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def end_game(self):
        self.entry_guess.config(state="disabled")
        self.button_guess.config(state="disabled")

if __name__ == "__main__":
    print("Starting the game...")  # Debug print
    root = tk.Tk()
    app = NumberGuessingGame(root)
    print("UI initialized, entering mainloop...")  # Debug print
    root.mainloop()
