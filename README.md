# Number Guessing Game 🎲

## Overview
This repository contains a Python script for a Number Guessing Game. The script generates a random number between 1 and 100, and the user has up to three attempts to guess the number. The game provides feedback to help the user guess the number correctly and informs the user of the correct number if they run out of guesses.

## How It Works
1. The script uses Python's `random` module to generate a random number between 1 and 100.
2. The user is given up to three chances to guess the number.
3. After each guess, the script will indicate whether the guess is too low or too high.
4. The game ends either when the user guesses the correct number or exhausts all three attempts.
5. If the user does not guess the number within three attempts, the correct number is revealed.

## How to Run the Game
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```

2. **Navigate to the Directory:**
   ```bash
   cd number-guessing-game
   ```

3. **Run the Script:**
   ```bash
   python3 number_guessing_game.py
   ```

## Example Output
```
Guess a number between 1 to 100: 50
Your guess is too low!
You have 2 chances left. Guess again: 75
Your guess is too high!
You have 1 chances left. Guess again: 60
Congrats!!! 
You guessed it right!
```

## Requirements
- Python 3.x

## Contributing
Feel free to fork this repository, make improvements, and create a pull request. Contributions are always welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project is inspired by basic Python exercises often found in beginner programming courses.
```

### Breakdown:
- **Overview:** Describes what the game does and how many attempts the user has.
- **How It Works:** Details the script’s functionality and game flow.
- **How to Run the Game:** Provides steps to clone the repo, navigate to it, and run the script.
- **Example Output:** Shows sample interactions and responses from the game.
- **Requirements:** Specifies the necessary Python version.
- **Contributing:** Invites others to contribute to the project.
- **License:** Mentions the license type.
- **Acknowledgments:** Credits the inspiration for the project.

You can use this `README.md` to clearly communicate the purpose, usage, and details of your Number Guessing Game script.