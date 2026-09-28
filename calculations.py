import re
import numpy as np


def calculate_daily_calories(weight: float, height: float, age: int, gender: str, activity_lvl: float) -> list[float, float]:
    if gender.upper() == "MALE":
        gender = 5
    elif gender.upper() == "FEMALE":
        gender = -161

    BMR = (10 * weight) + (6.25 * height) - (5 * age) + gender
    TDEE = BMR * activity_lvl

    return [round(TDEE, 1), round(BMR, 1)]


def calculate_daily_protein(weight: float) -> float:
    return weight * 1.6


def calculate_daily_fibre(TDEE: float) -> float:
    return (TDEE / 1000) * 14


def process_macros(ingredient: str, macros: list[float, float, float, float], serve: float) -> dict:
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


def exp_to_tokens(exp: str) -> list[str | int | float]:
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


def calculate_exp(exp: list[str | int]) -> float:
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
