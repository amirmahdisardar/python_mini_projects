# this app is a simple unit converter that converts between different units of length, weight, time, and temperature.

class UnitConverter:

    def __init__(self):
        """
        Initialize all unit dictionaries.
        Each unit is defined relative to a base unit.
        """
        self.length_types = {
            "m": 1, "cm": 0.01, "km": 1000,
            "mm": 0.001, "mi": 1609.34
        }

        self.weight_types = {
            "g": 1, "kg": 1000, "mg": 0.001
        }

        self.time_types = {
            "hr": 1, "min": 1/60, "sec": 1/3600
        }

    # ---------------------- LENGTH ----------------------
    def length_converter(self):
        """Convert units of length."""

        value = float(input("Enter your value to convert: "))
        origin = input("Enter your origin unit (m, cm, km, mm, mi): ").lower().strip()
        destination = input("Enter your destination unit (m, cm, km, mm, mi): ").lower().strip()

        # Validate input units
        if origin not in self.length_types or destination not in self.length_types:
            return "Invalid length unit!"

        # Convert value to destination unit
        new_value = value * (self.length_types[origin] / self.length_types[destination])
        return new_value


    # ---------------------- WEIGHT -----------------------
    def weight_converter(self):
        """Convert units of weight."""

        value = float(input("Enter your value to convert: "))
        origin = input("Enter your origin unit (g, kg, mg): ").lower().strip()
        destination = input("Enter your destination unit (g, kg, mg): ").lower().strip()

        # Validate input units
        if origin not in self.weight_types or destination not in self.weight_types:
            return "Invalid weight unit!"

        new_value = value * (self.weight_types[origin] / self.weight_types[destination])
        return new_value


    # ----------------------- TIME ------------------------
    def time_converter(self):
        """Convert units of time."""

        value = float(input("Enter your value to convert: "))
        origin = input("Enter your origin unit (hr, min, sec): ").lower().strip()
        destination = input("Enter your destination unit (hr, min, sec): ").lower().strip()

        # Validate input units
        if origin not in self.time_types or destination not in self.time_types:
            return "Invalid time unit!"

        new_value = value * (self.time_types[origin] / self.time_types[destination])
        return new_value


    # ------------------- TEMPERATURE ---------------------
    def temperature_converter(self):
        """
        Convert temperature between Celsius, Fahrenheit, and Kelvin.

        Formulas:
            C → F : (C * 9/5) + 32
            F → C : (F - 32) * 5/9
            C → K : C + 273.15
            K → C : K - 273.15
        """

        value = float(input("Enter your value to convert: "))
        origin = input("Enter your origin unit (c, f, k): ").lower().strip()
        destination = input("Enter your destination unit (c, f, k): ").lower().strip()

        # Validate input units
        if origin not in ["c", "f", "k"] or destination not in ["c", "f", "k"]:
            return "Invalid temperature unit!"

        # ---- Step 1: Convert origin unit to Celsius ----
        if origin == "c":
            c = value
        elif origin == "f":
            c = (value - 32) * 5 / 9
        elif origin == "k":
            c = value - 273.15

        # ---- Step 2: Convert Celsius to destination unit ----
        if destination == "c":
            return c
        elif destination == "f":
            return c * 9/5 + 32
        elif destination == "k":
            return c + 273.15


    # --------------------- MAIN APP ----------------------
    def run(self):
        """Main function to run the unit converter."""

        unit = input("What unit do you want to convert (length, weight, time, temperature)? ").lower().strip()

        if unit == "length":
            print(f"your converted value is : {self.length_converter()}")

        elif unit == "weight":
            print(f"your converted value is : {self.weight_converter()}")

        elif unit == "time":
            print(f"your converted value is : {self.time_converter()}")

        elif unit == "temperature":
            print(f"your converted value is : {self.temperature_converter()}")

        else:
            print("Invalid type! Choose from (length, weight, time, temperature).")


# Create object and run the app
app = UnitConverter()
app.run()
