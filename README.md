### 🔠 **Hangman Game: Python Implementation**  

**Skills:** Python, Game Development, Algorithmic Thinking  

---

## 🚀 **Project Overview**  
This project is a **Python-based Hangman game**, a classic word-guessing challenge where players try to guess a randomly selected word within a limited number of attempts.  

The project demonstrates:  
✅ **Python fundamentals** – String manipulation, loops, conditionals  
✅ **Game logic design** – Managing player input, word selection, and win/loss conditions  
✅ **Randomization** – Selecting words dynamically from a word list  
✅ **User interaction** – Taking input, displaying progress, and handling errors  

This project is **ideal for showcasing Python proficiency** in entry-level software engineering and developer roles.  

---

## 🎯 **How the Game Works**  
1️⃣ A word is selected randomly from a predefined word list.  
2️⃣ The player guesses letters, one at a time.  
3️⃣ If the letter is in the word, it is revealed in the correct position.  
4️⃣ If incorrect, the player loses a life.  
5️⃣ The game ends when the player either **guesses the word correctly** or **runs out of lives**.  

---

## 🏗 **Project Structure**  
📂 **word_list.py** – Contains a list of words for the game.  
📂 **main.py** – The core logic for Hangman, including:  
- **Random word selection**  
- **User input handling**  
- **Checking guesses & updating progress**  
- **Tracking remaining attempts & displaying results**  

✅ **Example: Function to Select a Valid Word**  
```python
import random
from word_list import words

def get_valid_words(words):
    word = random.choice(words)  
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()
```

---

## 🎮 **Game Implementation**  
The game logic handles:  
✔ **Case sensitivity** – Converts input to uppercase for consistency  
✔ **Validations** – Ensures the input is a single letter  
✔ **Tracking attempts** – Limits incorrect guesses  
✔ **Displaying progress** – Shows the guessed letters and blanks  

✅ **Example: Checking User Guesses**  
```python
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])
```

✅ **Example: Game Loop**  
```python
word = get_valid_words(words)
guessed_letters = set()
attempts = 6  # Maximum incorrect guesses allowed

while attempts > 0 and "_" in display_word(word, guessed_letters):
    guess = input("Guess a letter: ").upper()
    
    if guess in word:
        guessed_letters.add(guess)
    else:
        attempts -= 1  # Decrease attempts if wrong

print(f"Game Over! The word was {word}.")
```

---

## 🎯 **Why This Project Stands Out for Python Developer Roles**  
✔ **Demonstrates Python proficiency** – String handling, loops, conditionals  
✔ **Uses game logic** – Interactive, real-time user input handling  
✔ **Applies fundamental CS concepts** – Randomization, conditionals, lists  
✔ **Modular & maintainable code** – Functions are well-structured for readability  

---

## 🔮 **Future Enhancements**  
🔹 **Multiplayer Mode** – Allow users to take turns guessing  
🔹 **GUI Version** – Implement using `tkinter` or `Pygame`  
🔹 **Word Categories** – Provide themed word lists (e.g., animals, cities)  
🔹 **Leaderboard** – Track user scores over multiple rounds  

---

## 🛠 **How to Run This Project**  
1️⃣ Clone the repo:  
   ```bash
   git clone https://github.com/shrunalisalian/python-hangman.git
   ```
2️⃣ Install dependencies (if required):  
   ```bash
   pip install -r requirements.txt
   ```
3️⃣ Run the game:  
   ```bash
   python main.py
   ```

---

## 📌 **Connect with Me**  
- **LinkedIn:** [Shrunali Salian](https://www.linkedin.com/in/shrunali-salian/)  
- **Portfolio:** [Your Portfolio Link](#)  
- **Email:** [Your Email](#)  

---
Reference: https://youtu.be/cJJTnI22IF8?si=tXM-FsHcKC0crz-e
