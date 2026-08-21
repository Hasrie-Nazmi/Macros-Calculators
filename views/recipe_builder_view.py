import customtkinter


class App(customtkinter.CTk):
    def __init__(self,):
        super().__init__()

        self.title("Recipe Builder")
        self.geometry("475x800")
        self.row = 0
        for i in range(3):
            self.generate_textfields()

    def generate_textfields(self,):
        labels = ["Ingredient", "Calories", "Protein",
                  "Fibre", "Carbs", "Serving Size"]

        for i, lbl in enumerate(labels):
            col = i % 6

            customtkinter.CTkLabel(self, text=lbl).grid(
                row=self.row, column=col, padx=15, pady=20, sticky="w"
            )
        self.row += 1


app = App()
app.mainloop()
