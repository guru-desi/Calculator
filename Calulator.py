# Create Calculator Using Tkinter GUI 

import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Calculator")
        self.resizable(False, False)
        self._build_ui()
        self.expression = ""

    def _build_ui(self):
        # Display
        self.display_var = tk.StringVar(value="0")
        display = ttk.Entry(self, textvariable=self.display_var, font=("Consolas", 24), justify="right")
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)
        display.bind("<Key>", lambda e: "break")  # disable direct typing

        # Configure grid
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

        # Buttons layout
        buttons = [
            ("C", 1, 0, self.clear),
            ("⌫", 1, 1, self.backspace),
            ("%", 1, 2, lambda: self.append("%")),
            ("/", 1, 3, lambda: self.append("/")),

            ("7", 2, 0, lambda: self.append("7")),
            ("8", 2, 1, lambda: self.append("8")),
            ("9", 2, 2, lambda: self.append("9")),
            ("*", 2, 3, lambda: self.append("*")),

            ("4", 3, 0, lambda: self.append("4")),
            ("5", 3, 1, lambda: self.append("5")),
            ("6", 3, 2, lambda: self.append("6")),
            ("-", 3, 3, lambda: self.append("-")),

            ("1", 4, 0, lambda: self.append("1")),
            ("2", 4, 1, lambda: self.append("2")),
            ("3", 4, 2, lambda: self.append("3")),
            ("+", 4, 3, lambda: self.append("+")),

            ("00", 5, 0, lambda: self.append("00")),
            ("0", 5, 1, lambda: self.append("0")),
            (".", 5, 2, lambda: self.append(".")),
            ("=", 5, 3, self.calculate),
        ]

        style = ttk.Style(self)
        style.configure("TButton", font=("Segoe UI", 14))

        for text, r, c, cmd in buttons:
            btn = ttk.Button(self, text=text, command=cmd)
            btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

        # Keyboard bindings
        self.bind("<Key>", self._on_key)

    def append(self, char: str):
        if self.display_var.get() == "0" and char not in (".", "%"):
            self.display_var.set(char)
            self.expression = char
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("0")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression if self.expression else "0")

    def calculate(self):
        expr = self.expression or self.display_var.get()
        if not expr:
            return
        try:
            # Replace percent with divide-by-100 behavior
            safe_expr = self._normalize_percent(expr)
            result = eval(safe_expr, {"__builtins__": {}}, {})
            # Avoid scientific notation for integers
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def _normalize_percent(self, expr: str) -> str:
        # Converts "50%" -> "(50/100)" and "200+10%" -> "200+(200*10/100)"
        import re

        # Case 1: simple number% => (number/100)
        expr = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expr)

        # Case 2: a+b% where b% applies to previous term: convert prev + (prev*b/100)
        def apply_percent(m):
            prev = m.group(1)
            op = m.group(2)
            pct = m.group(3)
            return f"{prev}{op}({prev}*{pct}/100)"

        expr = re.sub(r'((?:\d+(?:\.\d+)?|\)))([+\-])(\d+(?:\.\d+)?)%$', apply_percent, expr)

        return expr

    def _on_key(self, event: tk.Event):
        ch = event.char
        keys_allowed = "0123456789.+-*/%"
        if ch in keys_allowed:
            self.append(ch)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "Escape":
            self.clear()
        elif event.keysym in ("BackSpace", "Delete"):
            self.backspace()
        # Prevent default entry behavior
        return "break"

if __name__ == "__main__":
    Calculator().mainloop()
