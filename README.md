# Python Discord Bot Learning

Welcome to my Python learning journey! This repository is dedicated to building a Discord bot as I explore the world of programming and enhance my Python skills.

## Overview

In this project, I aim to:

- Learn Python fundamentals
- Gain hands-on experience with the Discord API
- Develop an interactive Discord bot

## Getting Started

1. **Install Visual Studio Code or VSCodium:**
   - Download and install Visual Studio Code or VSCodium from [Visual Studio Code website](https://code.visualstudio.com/) or [VSCodium website](https://vscodium.com/).

2. **Install virtualenv:**
   - Open the terminal in Visual Studio Code or VSCodium.
   - Run the command: `pip install virtualenv`

3. **Create a Virtual Environment:**
   - In the terminal, navigate to your repository folder.
   - Run the command: `virtualenv .venv`

4. **Select Python Interpreter:**
   - Press `Ctrl + Shift + P` to open the command palette.
   - Search for "Python: Select Interpreter" and select it.
   - Choose `your Python version ('.venv)` interpreter.

5. **Install Dependencies:**
   - Close existing terminals and open a new one (ensure it's in the .venv folder).
   - Run the commands:
     ```
     pip install discord.py[voice]
     pip install python-dotenv
     ```

6. **Update .gitignore:**
   - Open the .gitignore file.
   - Uncomment lines 123 and 124 to include the .venv folder in your gitignore.

Now, your environment is set up for developing the Discord bot using Python. Happy coding!

## Project Structure

- **.env** 
- **.gitignore**
- **.README.md**
- **logs**
- **main.py**
- **settings.py**
