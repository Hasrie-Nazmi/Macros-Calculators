import re
import numpy as np


class MacroCalculator:
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

    def calculate_macros(self, ingredient: str, serve: float, macros: list[float, float, float, float]) -> dict:
        ingredients = {}

        calorie_list = []
        protein_list = []
        fibre_list = []
        carbs_list = []

        macro_served = np.array(macros) * serve
        calorie_list.append(macro_served[0])
        protein_list.append(macro_served[1])
        fibre_list.append(macro_served[2])
        carbs_list.append(macro_served[3])

        cal, protein, fibre, carbs = macros
        ingredients[ingredient] = {
            "serve": serve,
            "cal": cal,
            "protein": protein,
            "fibre": fibre,
            "carbs": carbs
        }

        return ingredients

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
