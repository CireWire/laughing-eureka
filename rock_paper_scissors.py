#! /usr/bin/env python3

"""
Rock Paper Scissors Game

This program implements a simple Rock Paper Scissors game using Tkinter for the GUI.

Author: CireWire / The Helix Corporation
Date: 5/17/2025
License: The Unlicense

"""

import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import time

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["🪨", "📄", "✂️"]
        self.game_over = False
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            self.main_frame,
            text="Rock Paper Scissors",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=20)
        
        # Score display
        self.score_frame = ttk.Frame(self.main_frame)
        self.score_frame.pack(pady=10)
        
        self.score_label = ttk.Label(
            self.score_frame,
            text="Score: You 0 - 0 Computer",
            font=("Helvetica", 14)
        )
        self.score_label.pack()
        
        # Choices display
        self.choices_frame = ttk.Frame(self.main_frame)
        self.choices_frame.pack(pady=20)
        
        self.player_choice_label = ttk.Label(
            self.choices_frame,
            text="Your choice: ",
            font=("Helvetica", 16)
        )
        self.player_choice_label.pack()
        
        self.computer_choice_label = ttk.Label(
            self.choices_frame,
            text="Computer's choice: ",
            font=("Helvetica", 16)
        )
        self.computer_choice_label.pack()
        
        # Result display
        self.result_label = ttk.Label(
            self.main_frame,
            text="",
            font=("Helvetica", 16, "bold")
        )
        self.result_label.pack(pady=20)
        
        # Buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=20)
        
        # Create buttons with emojis
        for choice in self.choices:
            btn = ttk.Button(
                self.buttons_frame,
                text=choice,
                command=lambda c=choice: self.play_round(c),
                width=5
            )
            btn.pack(side=tk.LEFT, padx=10)
        
        # Restart button (initially hidden)
        self.restart_button = ttk.Button(
            self.main_frame,
            text="Play Again",
            command=self.restart_game,
            state=tk.DISABLED
        )
        self.restart_button.pack(pady=20)
        
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 20))
        style.configure("TLabel", background="#f0f0f0")
        
    def play_round(self, player_choice):
        if self.game_over:
            return
            
        # Computer's choice
        computer_choice = random.choice(self.choices)
        
        # Update display
        self.player_choice_label.config(text=f"Your choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update score
        if result == "win":
            self.player_score += 1
            self.result_label.config(text="You win this round! 🎉")
        elif result == "lose":
            self.computer_score += 1
            self.result_label.config(text="Computer wins this round! 😢")
        else:
            self.result_label.config(text="It's a tie! 🤝")
            
        # Update score display
        self.score_label.config(text=f"Score: You {self.player_score} - {self.computer_score} Computer")
        
        # Check for game over
        if self.player_score >= 3 or self.computer_score >= 3:
            self.end_game()
            
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
            
        winning_combinations = {
            "🪨": "✂️",
            "📄": "🪨",
            "✂️": "📄"
        }
        
        if winning_combinations[player_choice] == computer_choice:
            return "win"
        return "lose"
        
    def end_game(self):
        self.game_over = True
        if self.player_score > self.computer_score:
            self.result_label.config(text="Congratulations! You won the game! 🎉")
        else:
            self.result_label.config(text="Game Over! Computer wins! 😢")
            
        # Enable restart button
        self.restart_button.config(state=tk.NORMAL)
        
    def restart_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.game_over = False
        self.score_label.config(text="Score: You 0 - 0 Computer")
        self.player_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer's choice: ")
        self.result_label.config(text="")
        self.restart_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop() 
