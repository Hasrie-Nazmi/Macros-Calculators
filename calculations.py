import re
import numpy as np


class MacroCalculator:
    def __init__(self):
        self.ingredients = {}

        self.calorie_list = []
        self.protein_list = []
        self.fibre_list = []
        self.carbs_list = []

    def exp_to_tokens(self, exp: str) -> list[str | int | float]:
        raw_tokens = re.findall(r"\d+\.?\d*|[\+\-\*/]", exp)

        tokens = []

        for token in raw_tokens:
            if token in "+-*/":
                tokens.append(token)
            elif "." in token:
                tokens.append(float(token))
            else:
                tokens.append(int(token))

        return tokens

    def process_macros(self, ingredient: str, macros: list[float, float, float, float], serve: float) -> dict:

        macro_served = np.array(macros) * serve
        self.calorie_list.append(macro_served[0])
        self.protein_list.append(macro_served[1])
        self.fibre_list.append(macro_served[2])
        self.carbs_list.append(macro_served[3])

        cal, protein, fibre, carbs = macros
        self.ingredients[ingredient] = {
            "serve": serve,
            "cal": cal,
            "protein": protein,
            "fibre": fibre,
            "carbs": carbs
        }

        return self.ingredients

    def calculate_total_macros(self, recipe_name: str) -> dict:
        total_macros = {}

        total_calories = sum(self.calorie_list)
        total_protein = sum(self.protein_list)
        total_fibre = sum(self.fibre_list)
        total_carbs = sum(self.carbs_list)

        total_macros[recipe_name] = {
            "ingredients": self.ingredients,
            "total_macros": [total_calories, total_protein, total_fibre, total_carbs]
        }

        return total_macros

    def calculate_exp(self, exp: list[str | int]) -> float:
        exp_stack = []
        current_op = "+"

        if not exp:
            return 0

        for token in exp:
            if isinstance(token, str) and token in "+-*/":
                current_op = token

            else:
                num = token
                if current_op == "+":
                    exp_stack.append(num)
                elif current_op == "-":
                    exp_stack.append(-num)
                elif current_op == "*":
                    exp_stack.append(exp_stack.pop() * num)
                elif current_op == "/":
                    exp_stack.append(int(exp_stack.pop() / num))

        return sum(exp_stack)


exp = "5 + 2 * 3 - 4"
# [5, 2, 3, 4]
# ["+", "*", "-"]

calc = MacroCalculator()
tokens = calc.exp_to_tokens(exp)
print(calc.calculate_exp(tokens))
