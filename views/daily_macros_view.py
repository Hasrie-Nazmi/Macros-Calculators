import customtkinter


class DailyMacros(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Daily Macros Calculator")
        self.geometry("800x600")

        customtkinter.CTkLabel(self, text="Height").grid(
            row=1, column=0, padx=15, pady=5, sticky="w")
        self.height_e = customtkinter.CTkEntry(self).grid(
            row=2, column=0, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Weight").grid(
            row=1, column=1, padx=15, pady=5, sticky="w")
        self.weight_e = customtkinter.CTkEntry(self).grid(
            row=2, column=1, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Age").grid(
            row=1, column=2, padx=15, pady=5, sticky="w")
        self.age_e = customtkinter.CTkEntry(self).grid(
            row=2, column=2, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Gender").grid(
            row=3, column=0, padx=15, pady=5, sticky="w")
        gender_menu = customtkinter.CTkOptionMenu(
            self, values=["Male", "Female"])
        gender_menu.grid(
            row=4, column=0, padx=15, pady=5, sticky="w")

        activity_lvl_dict = {
            "Little exercise": 1.2,
            "1-3 times/week": 1.375,
            "4-5 times/week": 1.55,
            "Intense 3-4 times/week": 1.725,
            "Intense 6-7 times/week": 1.9
        }
        customtkinter.CTkLabel(self, text="Activity Level").grid(
            row=3, column=1, padx=15, pady=5, sticky="w")
        active_menu = customtkinter.CTkOptionMenu(
            self, values=list(activity_lvl_dict.keys()))
        active_menu.grid(
            row=4, column=1, padx=15, pady=5, sticky="w")

        self.display_daily_macros()

    def display_daily_macros(self):
        labels = ["BMR: ", "TDEE: ", "Protein: ", "Fibre: "]
        fontsize = 20

        customtkinter.CTkLabel(self, text="Total Daily Macros:", font=("", fontsize)).grid(
            row=2, column=3, rowspan=3, padx=15, pady=5, sticky="w")

        for i, lbl in enumerate(labels):
            col = (i % 2) + 3
            row = (i // 2) + 4

            customtkinter.CTkLabel(self, text=lbl, font=("", fontsize)).grid(
                row=row, column=col, padx=15, pady=5, sticky="w")

# BMR, TDEE, Protein, Fibre


app = DailyMacros()
app.mainloop()
