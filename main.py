import customtkinter

from views.calculator_view import CalculatorFrame
from views.recipe_builder_view import RecipeBuilderFrame
from views.daily_macros_view import DailyMacrosFrame
from views.unit_convert_view import UnitConvertFrame


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Assorted Fitness Tools")
        self.geometry("1000x600")

        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        self.tabview.add("Daily Macros")
        self.tabview.add("Recipe Builder")
        self.tabview.add("Unit Converter")
        self.tabview.add("Calculator")

        self.recipe_builder_view = RecipeBuilderFrame(
            self.tabview.tab("Recipe Builder"))
        self.recipe_builder_view.pack(fill="both", expand=True)

        self.calculator_view = CalculatorFrame(
            self.tabview.tab("Calculator"))
        self.calculator_view.pack(fill="both", expand=True)

        self.daily_macros_view = DailyMacrosFrame(
            self.tabview.tab("Daily Macros"))
        self.daily_macros_view.pack(fill="both", expand=True)

        self.unit_convert_view = UnitConvertFrame(
            self.tabview.tab("Unit Converter"))
        self.unit_convert_view.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
