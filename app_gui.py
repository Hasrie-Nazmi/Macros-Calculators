import customtkinter as ctk


def button_callback():
    print("button pressed")


app = ctk.CTk()
app.title("my app")
app.geometry("550x800")


def generate_calculator_buttons():
    for i in range(9):
        button1 = ctk.CTkButton(app, text="my button", command=button_callback)


# button1 = ctk.CTkButton(app, text="my button", command=button_callback)
# button2 = ctk.CTkButton(app, text="my button", command=button_callback)
# button3 = ctk.CTkButton(app, text="my button", command=button_callback)
# button1.grid(row=0, column=0, padx=20, pady=20)
# button2.grid(row=0, column=1, padx=20, pady=20)
# button3.grid(row=0, column=2, padx=20, pady=20)

app.mainloop()
