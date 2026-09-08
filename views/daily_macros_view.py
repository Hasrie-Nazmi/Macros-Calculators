import customtkinter
import calculations as calc


class DailyMacrosFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        customtkinter.CTkLabel(self, text="Height").grid(
            row=1, column=0, padx=15, pady=5, sticky="w")

        self.height_e = customtkinter.CTkEntry(self)
        self.height_e.grid(
            row=2, column=0, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Weight").grid(
            row=1, column=1, padx=15, pady=5, sticky="w")

        self.weight_e = customtkinter.CTkEntry(self)
        self.weight_e.grid(
            row=2, column=1, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Age").grid(
            row=1, column=2, padx=15, pady=5, sticky="w")

        self.age_e = customtkinter.CTkEntry(self)
        self.age_e.grid(
            row=2, column=2, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Gender").grid(
            row=3, column=0, padx=15, pady=5, sticky="w")
        self.gender_menu = customtkinter.CTkOptionMenu(
            self, values=["Male", "Female"])
        self.gender_menu.grid(
            row=4, column=0, padx=15, pady=5, sticky="w")

        self.activity_lvl_dict = {
            "Little exercise": 1.2,
            "1-3 times/week": 1.375,
            "4-5 times/week": 1.55,
            "Intense 3-4 times/week": 1.725,
            "Intense 6-7 times/week": 1.9
        }
        customtkinter.CTkLabel(self, text="Activity Level").grid(
            row=3, column=1, padx=15, pady=5, sticky="w")
        self.active_menu = customtkinter.CTkOptionMenu(
            self, values=list(self.activity_lvl_dict.keys()))
        self.active_menu.grid(
            row=4, column=1, padx=15, pady=5, sticky="w")

        calculate_btn = customtkinter.CTkButton(self, text="Calculate",
                                                command=self.calculate_daily_macros)
        calculate_btn.grid(
            row=5, column=0, padx=15, pady=15, sticky="w")

    def calculate_daily_macros(self,):
        calories = calc.calculate_daily_calories(
            weight=float(self.weight_e.get()), height=float(self.height_e.get()), age=int(self.age_e.get()), gender=self.gender_menu.get(), activity_lvl=self.activity_lvl_dict[self.active_menu.get()])

        protein = calc.calculate_daily_protein(
            weight=float(self.weight_e.get()))
        fibre = calc.calculate_daily_fibre(calories[0])

        self.display_daily_macros(
            calories=calories, protein=round(protein, 1), fibre=round(fibre, 1))

    def display_daily_macros(self, calories: list[float, float], protein: float, fibre: float):
        labels = {"BMR: ": calories[1],
                  "TDEE: ": calories[0],
                  "Protein: ": protein,
                  "Fibre: ": fibre}
        fontsize = 20

        customtkinter.CTkLabel(self, text="Total Daily Macros:", font=("", fontsize)).grid(
            row=2, column=3, rowspan=3, padx=15, pady=5, sticky="w")

        for i, (k, v) in enumerate(labels.items()):
            col = (i % 2) + 3
            row = (i // 2) + 4

            customtkinter.CTkLabel(self, text=f"{k}{v}", font=("", fontsize)).grid(
                row=row, column=col, padx=15, pady=5, sticky="w")
