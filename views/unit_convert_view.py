import customtkinter


class UnitConvertFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.title("Unit Conversion")
        # self.geometry("800x600")

        customtkinter.CTkLabel(self, text="Weight (KG)").grid(
            row=1, column=0, padx=15, pady=5, sticky="w")
        self.weight1_e = customtkinter.CTkEntry(self).grid(
            row=2, column=0, padx=15, pady=5, sticky="w")

        self.convert_weight_btn = customtkinter.CTkButton(
            self, text="=", command=self.convert_weight)
        self.convert_weight_btn.grid(row=2, column=1)

        customtkinter.CTkLabel(self, text="Weight (LBS)").grid(
            row=1, column=2, padx=15, pady=5, sticky="w")
        self.weight2_e = customtkinter.CTkEntry(self).grid(
            row=2, column=2, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Height (CM)").grid(
            row=3, column=0, padx=15, pady=5, sticky="w")
        self.height1_e = customtkinter.CTkEntry(self).grid(
            row=4, column=0, padx=15, pady=5, sticky="w")

        self.convert_height_btn = customtkinter.CTkButton(
            self, text="=", command=self.convert_height)
        self.convert_height_btn.grid(row=4, column=1)

        customtkinter.CTkLabel(self, text="Height (Feet)").grid(
            row=3, column=2, padx=15, pady=5, sticky="w")
        self.height2_e = customtkinter.CTkEntry(self).grid(
            row=4, column=2, padx=15, pady=5, sticky="w")

    def convert_weight(self, data):
        data = self.num_checker(data)
        return data * 2.205

    def convert_height(self, data):
        data = self.num_checker(data)
        total_inches = data / 2.54
        feet = total_inches // 12

        inches = total_inches - 12 * feet

        # print(total_inches, feet, inches)

        return (f"{int(feet)}'{int(inches)}")

    def num_checker(self, data: str) -> bool | float:
        if data:
            try:
                data = float(data)
                return data
            except ValueError:
                return False


# app = UnitConvert()
# # app.mainloop()
# print(app.convert_height("167.7"))
