import customtkinter


class App(customtkinter.CTk):
    def __init__(self,):
        super().__init__()

        self.title("Recipe Builder")
        self.geometry("1000x500")

        self.row = 0
        self.item_count = 0
        self.textfield_values = {}

        self.add_button = customtkinter.CTkButton(
            self, text="Add Ingredient", command=self.generate_textfields
        )

        self.generate_textfields()

    def new_ingredient_button(self):
        add_button = customtkinter.CTkButton(self, text="Add Ingredient",
                                             command=self.generate_textfields)

        add_button.grid(row=self.row, column=3, columnspan=2, pady=15)

    def generate_textfields(self,):
        keys_labels = [("ingredient", "Ingredient"), ("calories", "Calories (kcal)"), ("protein", "Protein (g)"),
                       ("fibre", "Fibre (g)"), ("carbs", "Carbs (g)"), ("serve", "Serving Size")]

        self.item_count += 1
        customtkinter.CTkLabel(self, text="#"+str(self.item_count)).grid(
            row=self.row, column=0, padx=15, pady=5, sticky="w", rowspan=2
        )

        for i, (key, lbl) in enumerate(keys_labels):
            col = i % 6

            customtkinter.CTkLabel(self, text=lbl).grid(
                row=self.row, column=col+1, padx=15, pady=5, sticky="w"
            )

            e_data = customtkinter.CTkEntry(self,)
            e_data.grid(row=self.row+1, column=col+1,
                        padx=10, pady=5, sticky="w")

            self.textfield_values[key] = e_data

        self.row += 2

        self.add_button.grid(
            row=self.row, column=3, columnspan=2, pady=15, sticky="ew"
        )


app = App()
app.mainloop()
