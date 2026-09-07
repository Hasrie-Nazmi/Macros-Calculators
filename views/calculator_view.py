import customtkinter
from calculations import MacroCalculator

# todo:
# -Fix button alignments


class CalculatorFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.generate_calculator_buttons()
        self.exp_str = []

        # Display expressions
        self.exp_lbl = customtkinter.CTkLabel(self, text="", font=("", 30))
        self.exp_lbl.grid(row=0, column=5, padx=10, pady=10)

        # Display results
        self.result = customtkinter.CTkLabel(
            self, text="= ", font=("", 30))
        self.result.grid(
            row=1, column=5, padx=10, pady=10)

    def calc_btn_pressed(self, btn_value: str) -> str:
        if self.exp_str and self.exp_str[-1] in "+-/*" and btn_value in "+-/*":
            print(self.exp_str)
        else:
            self.exp_str.append(btn_value)
            print(self.exp_str)
            self.exp_lbl.configure(text="".join(self.exp_str))
            return "".join(btn_value)

    def delete_value(self,) -> bool:
        if self.exp_str:
            self.exp_str.pop()
            print(self.exp_str)
            return True
        else:
            return False

    def clear_calc(self):
        self.exp_str = []
        self.exp_lbl.configure(text="")
        self.result.configure(text="")

    def calculate_expression(self) -> float:

        # Checks if exp_str has an op in it to prevent multiple string elements from joining
        if any(op in self.exp_str for op in "+-*/"):
            calc = MacroCalculator()
            tokenization = calc.exp_to_tokens("".join(self.exp_str))
            result = calc.calculate_exp(tokenization)
            self.exp_str = [str(result)]

            print(result, self.exp_str)
            self.result.configure(text=f"= {result}")
        else:
            print("HERE")
            pass

    def generate_calculator_buttons(self,):
        calc_btn_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        calc_op_labels = ["+", "-", "*", "/"]
        width, height = 100, 80

        # Generate 1-9 calculator buttons
        for i, label in enumerate(calc_btn_labels):
            row = i // 3
            col = i % 3

            self.num_btn = customtkinter.CTkButton(
                self, text=label, width=width, height=height, command=lambda t=label: self.calc_btn_pressed(t))
            self.num_btn.grid(row=row, column=col, padx=5, pady=5)

        # Generate operation symbols
        for i, op in enumerate(calc_op_labels):
            self.op_btn = customtkinter.CTkButton(
                self, text=op, width=width, height=height, command=lambda t=op: self.calc_btn_pressed(t))
            self.op_btn.grid(row=i, column=4, padx=20, pady=5)

        # Offset 0 calculator button
        self.zero_btn = customtkinter.CTkButton(
            self, text="0", width=width, height=height, command=lambda t="0": self.calc_btn_pressed(t))
        self.zero_btn.grid(row=3, column=1, padx=5, pady=5)

        # Delete button
        self.del_btn = customtkinter.CTkButton(
            self, text="<-", width=width+20, height=height, command=self.delete_value)
        self.del_btn.grid(row=4, column=4, padx=5, pady=5)

        # Calculate button
        self.calc_btn = customtkinter.CTkButton(
            self, text="=", width=width+20, height=height, command=self.calculate_expression)
        self.calc_btn.grid(row=5, column=4, padx=5, pady=5)

        self.clr_btn = customtkinter.CTkButton(
            self, text="C", width=width+20, height=height, command=self.clear_calc)
        self.clr_btn.grid(row=5, column=3, padx=5, pady=5)


# app = CalculatorFrame()
# app.mainloop()
