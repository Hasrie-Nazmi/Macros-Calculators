import customtkinter


class UnitConvertFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.weight_is_updating = False
        self.height_is_updating = False

        self.kg_var = customtkinter.StringVar(value="")
        self.lbs_var = customtkinter.StringVar(value="")

        self.cm_var = customtkinter.StringVar(value="")
        self.feet_var = customtkinter.StringVar(value="")
        self.inches_var = customtkinter.StringVar(value="")

        customtkinter.CTkLabel(self, text="Weight (kg)").grid(
            row=1, column=0, padx=15, pady=5, sticky="w")

        self.kg_e = customtkinter.CTkEntry(
            self, textvariable=self.kg_var, justify="center")
        self.kg_e.grid(
            row=2, column=0, padx=15, pady=5, sticky="w")

        self.convert_weight_btn = customtkinter.CTkButton(
            self, text="=", state="disabled")
        self.convert_weight_btn.grid(row=2, column=1)

        customtkinter.CTkLabel(self, text="Weight (lbs)").grid(
            row=1, column=2, padx=15, pady=5, sticky="w")

        self.lbs_e = customtkinter.CTkEntry(
            self, textvariable=self.lbs_var, justify="center")
        self.lbs_e.grid(
            row=2, column=2, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Height (cm)").grid(
            row=3, column=0, padx=15, pady=5, sticky="w")

        self.cm_e = customtkinter.CTkEntry(
            self, textvariable=self.cm_var, justify="center")
        self.cm_e.grid(
            row=4, column=0, padx=15, pady=5, sticky="w")

        self.convert_height_btn = customtkinter.CTkButton(
            self, text="=", state="disabled")
        self.convert_height_btn.grid(row=4, column=1)

        customtkinter.CTkLabel(self, text="Height (ft)").grid(
            row=3, column=2, padx=15, pady=5, sticky="w")
        self.feet_e = customtkinter.CTkEntry(
            self, textvariable=self.feet_var, justify="center")
        self.feet_e.grid(
            row=4, column=2, padx=15, pady=5, sticky="w")

        customtkinter.CTkLabel(self, text="Height (in)").grid(
            row=3, column=3, padx=15, pady=5, sticky="w")
        self.inches_e = customtkinter.CTkEntry(
            self, textvariable=self.inches_var, justify="center")
        self.inches_e.grid(
            row=4, column=3, padx=1, pady=5, sticky="w")

        self.kg_var.trace_add("write", self._on_kg_change)
        self.lbs_var.trace_add("write", self._on_lbs_change)

        self.cm_var.trace_add("write", self._on_cm_change)
        self.feet_var.trace_add("write", self._on_feet_inch_change)
        self.inches_var.trace_add("write", self._on_feet_inch_change)

    def convert_weight(self, value: float) -> float:
        value = self.num_checker(value)
        return value * 2.205

    def cm_to_feet_inches(self, value: float) -> float:
        total_inches = value / 2.54
        feet = total_inches // 12

        inches = total_inches - 12 * feet

        return feet, inches

    def feet_inches_to_cm(self, feet: float, inches: float = 0.0) -> float:
        total_inches = (feet * 12) + inches
        return round(total_inches * 2.54, 2)

    def _on_kg_change(self, *args):
        if self.weight_is_updating:
            return

        try:
            val_str = self.kg_e.get().strip()
            if not val_str:
                self.weight_update_var(self.lbs_var, "")

            kg = float(val_str)
            lbs = kg * 2.20462
            self.weight_update_var(self.lbs_var, f"{lbs:.2f}")

        except ValueError:
            pass

    def _on_lbs_change(self, *args):
        if self.weight_is_updating:
            return

        try:
            val_str = self.lbs_e.get().strip()
            if not val_str:
                self.weight_update_var(self.kg_var, "")
                return

            lbs = float(val_str)
            kg = lbs / 2.20462
            self.weight_update_var(self.kg_var, f"{kg:.2f}")
        except ValueError:
            pass

    def _on_cm_change(self, *args):
        if self.height_is_updating:
            return

        try:
            val_str = self.cm_e.get().strip()
            if not val_str:
                self.height_update_var(self.feet_var, "")
                self.height_update_var(self.inches_var, "")
                return

            cm = float(val_str)
            feet, inches = self.cm_to_feet_inches(cm)
            self.height_is_updating = True
            self.feet_var.set(str(feet))
            self.inches_var.set(str(f"{inches:.1f}"))
            self.height_is_updating = False

        except ValueError:
            pass

    def _on_feet_inch_change(self, *args):
        if self.height_is_updating:
            return

        try:
            ft = float(self.feet_var.get() or 0)
            inch = float(self.inches_var.get() or 0)
            total_inches = (ft * 12) + inch
            cm = total_inches * 2.54

            self.height_update_var(self.cm_var, f"{cm:.2f}")
        except ValueError:
            pass

        except ValueError:
            pass

    def weight_update_var(self, var: customtkinter.StringVar, new_val: str):
        self.weight_is_updating = True
        var.set(new_val)
        self.weight_is_updating = False

    def height_update_var(self, var: customtkinter.StringVar, new_val: str):
        self.height_is_updating = True
        var.set(new_val)
        self.height_is_updating = False
