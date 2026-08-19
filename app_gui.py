import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("550x800")

        self.generate_calculator_buttons()

    def calc_btn_pressed(self, btn_value: str) -> str:
        print(btn_value)
        return btn_value

    def generate_calculator_buttons(self,):
        calc_btn_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i, label in enumerate(calc_btn_labels):
            row = i // 3
            col = i % 3

            self.calc_btn = customtkinter.CTkButton(
                self, text=label, width=40, height=20, command=lambda t=label: self.calc_btn_pressed(t))
            self.calc_btn.grid(row=row, column=col, padx=5, pady=5)

        self.calc_btn = customtkinter.CTkButton(
            self, text=0, width=40, height=20, command=lambda t=0: self.calc_btn_pressed(t))
        self.calc_btn.grid(row=4, column=1, padx=5, pady=5)


app = App()
app.mainloop()
