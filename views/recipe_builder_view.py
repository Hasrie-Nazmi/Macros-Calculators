import customtkinter


class RecipeBuilderFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # self.title("Recipe Builder")
        # self.geometry("1000x500")

        self.row = 0
        self.item_count = 0
        self.textfield_values = []

        self.add_button = customtkinter.CTkButton(
            self, text="Add Ingredient", command=self.generate_textfields
        )

        self.save_button = customtkinter.CTkButton(
            self, text="Save Recipe", command=self.save_recipe_button)

        total_macros = self.total_macros()

        self.total_calories_lbl = customtkinter.CTkLabel(
            self, text=f"Total: {total_macros['calories']}")
        self.total_protein_lbl = customtkinter.CTkLabel(
            self, text=f"Total: {total_macros['protein']}")
        self.total_fibre_lbl = customtkinter.CTkLabel(
            self, text=f"Total: {total_macros['fibre']}")
        self.total_carbs_lbl = customtkinter.CTkLabel(
            self, text=f"Total: {total_macros['carbs']}")

        self.generate_textfields()

    def new_ingredient_button(self):
        add_button = customtkinter.CTkButton(self, text="Add Ingredient",
                                             command=self.generate_textfields)

        add_button.grid(row=self.row, column=3, columnspan=2, pady=15)

    def save_recipe_button(self):
        print(self.get_recipes_data())
        print(self.total_macros())

    def get_recipes_data(self):
        recipes_data = []

        for text_value_row in self.textfield_values:
            text_value = {
                key: entry_widget.get().strip()
                for key, entry_widget in text_value_row.items()
            }
            recipes_data.append(text_value)

        return recipes_data

    def total_macros(self):
        total_macros = {
            "calories": 0.0,
            "protein": 0.0,
            "fibre": 0.0,
            "carbs": 0.0
        }

        recipes_data = self.get_recipes_data()

        for row_dict in recipes_data:
            for key in total_macros:
                value = row_dict.get(key, "0")
                try:
                    value = float(value) if value else 0.0

                    total_macros[key] += value * int(row_dict["serve"])
                except ValueError:
                    pass

        return total_macros

    def generate_textfields(self,):
        keys_labels = [("ingredient", "Ingredient"), ("calories", "Calories (kcal)"), ("protein", "Protein (g)"),
                       ("fibre", "Fibre (g)"), ("carbs", "Carbs (g)"), ("serve", "Serving Size")]

        row_values = {}

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

            # macro_list[i-1].append(e_data)
            row_values[key] = e_data

        self.textfield_values.append(row_values)

        self.row += 2

        total_macros = self.total_macros()

        self.total_calories_lbl.grid(
            row=self.row, column=2, padx=15, pady=5, sticky="w")
        self.total_calories_lbl.configure(
            text=f"Total: {total_macros['calories']}")

        self.total_protein_lbl.grid(
            row=self.row, column=3, padx=15, pady=5, sticky="w")
        self.total_protein_lbl.configure(
            text=f"Total: {total_macros['protein']}")

        self.total_fibre_lbl.grid(
            row=self.row, column=4, padx=15, pady=5, sticky="w")
        self.total_fibre_lbl.configure(text=f"Total: {total_macros['fibre']}")

        self.total_carbs_lbl.grid(
            row=self.row, column=5, padx=15, pady=5, sticky="w")
        self.total_carbs_lbl.configure(
            text=f"Total: {total_macros['carbs']}")

        self.add_button.grid(
            row=self.row+1, column=3, columnspan=2, pady=15, sticky="ew"
        )

        self.save_button.grid(
            row=self.row+2, column=3, columnspan=2, pady=15, sticky="ew"
        )


# app = RecipeBuilderFrame()
# app.mainloop()
