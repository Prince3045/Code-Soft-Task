import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")


        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('AC', 5, 1)
        ]


        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)


        self.current_number = ""
        self.operator = None
        self.first_number = None
        self.result_shown = False

    def button_click(self, value):
        if value.isdigit() or value == '.':

            self.current_number += value
            self.update_entry(self.current_number)
            self.result_shown = False
        elif value in ['+', '-', '*', '/']:

            if self.current_number:
                self.first_number = float(self.current_number)
                self.operator = value
                self.current_number = ""
        elif value == '=':

            if self.operator and self.current_number:
                second_number = float(self.current_number)
                result = self.calculate_result(self.first_number, second_number, self.operator)
                self.update_entry(result)
                self.current_number = str(result)
                self.result_shown = True
        elif value == 'C':

            if self.current_number:
                self.current_number = self.current_number[:-1]
                self.update_entry(self.current_number)
        elif value == 'AC':
  
            self.current_number = ""
            self.operator = None
            self.first_number = None
            self.update_entry("")

    def update_entry(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def calculate_result(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero!")
                return None
            else:
                return num1 / num2

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
