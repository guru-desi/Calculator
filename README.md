# Tkinter Calculator

## Overview

This project is a simple Calculator application developed using Python's Tkinter library. The calculator provides a graphical user interface (GUI) for performing basic arithmetic operations such as addition, subtraction, multiplication, division, percentages, and decimal calculations.

The application also supports keyboard input, backspace functionality, and error handling for invalid expressions.

---

## Features

- User-friendly GUI built with Tkinter
- Basic arithmetic operations (+, -, *, /)
- Percentage (%) calculations
- Decimal number support
- Clear (C) button
- Backspace (⌫) button
- Keyboard input support
- Error handling for invalid expressions
- Responsive button layout using Grid Manager

---

## Technologies Used

- Python 3.x
- Tkinter
- ttk (Themed Tkinter Widgets)

---

## Project Structure

```text
Project Folder/
│
├── calculator.py
└── README.md
```

---

## How It Works

1. The user enters numbers and operators using the buttons or keyboard.
2. The expression is displayed on the calculator screen.
3. When the '=' button is pressed, the expression is evaluated.
4. The result is displayed on the screen.
5. Invalid expressions display an "Error" message.

---

## Functionalities

### Number Buttons

Allows users to enter digits from 0 to 9 along with "00".

### Arithmetic Operators

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

### Percentage

Converts percentage values into their mathematical equivalent.

Example:

```text
50% = 0.5
```

### Clear Button

Resets the calculator display and clears the current expression.

### Backspace Button

Removes the last entered character.

### Keyboard Support

Supported keys:

```text
0 - 9
+
-
*
/
%
.
Enter      → Calculate Result
Backspace  → Delete Last Character
Escape     → Clear Display
```

---

## Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Verify Installation

```bash
python --version
```

### Step 3: Run the Program

Navigate to the project directory and execute:

```bash
python calculator.py
```

---

## Sample Calculations

```text
10 + 20 = 30
50 - 15 = 35
8 * 5 = 40
100 / 4 = 25
50% = 0.5
```

---

## Error Handling

If an invalid expression is entered, the calculator displays:

```text
Error
```

Examples:

```text
10++
5//2
(Invalid Expression)
```

---

## Main Components

### Calculator Class

The main application class that creates the calculator window and manages all operations.

### Methods

- `_build_ui()` → Creates the interface.
- `append()` → Adds characters to the expression.
- `clear()` → Clears the display.
- `backspace()` → Deletes the last character.
- `calculate()` → Evaluates the expression.
- `_normalize_percent()` → Handles percentage calculations.
- `_on_key()` → Processes keyboard input.

---

## Output

The application launches a calculator window where users can perform calculations interactively through buttons or keyboard shortcuts.

---

## Author

Developed in Python using Tkinter GUI framework as part of **Assignment 6 - Create Calculator Using Tkinter GUI**.
