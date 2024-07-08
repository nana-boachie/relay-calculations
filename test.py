import main_functions as mf

# Curves:
curve1 = "IEC"
curve2 = "IEEE"

# Example usage:
tms = 10  # Replace with your actual value
k = 5  # Replace with your actual value
psm = 2  # Replace with your actual value
a = 3  # Replace with your actual value


chosen_curve = mf.get_user_choice(curve1, curve2)
if chosen_curve == "iec":
    curve_type = mf.select_iec_curve_type()

    while True:
        try:
            psm = float(input("Enter the pickup setting multiplier (psm): "))
            tms = float(input("Enter the time multiplier setting (tsm): "))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
            if mf.ask_to_continue():
                print("Continuing with the program...")
                continue
            else:
                print("Exiting. Goodbye!")
                break
        if curve_type == 1:
            a = .020
            k = 0.140
        elif curve_type == 2:
            a = 1
            k = 13.5
        elif curve_type == 3:
            a = 2
            k = 80
        elif curve_type == 4:
            a = 1
            k = 120
        operating_time = mf.calculate_operating_time_iec(tms, k, psm, a)
        print(operating_time)


elif chosen_curve == "ieee":
    curve_type = mf.select_ieee_curve_type()
    while True:
        try:
            psm = float(input("Enter the pickup setting multiplier (psm): "))
            tms = float(input("Enter the time multiplier setting (tsm): "))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
            if mf.ask_to_continue():
                print("Continuing with the program...")
                continue
            else:
                print("Exiting. Goodbye!")
                break
        if curve_type == 1:
            a = .020
            k = 0.0515
        elif curve_type == 2:
            a = .491
            k = 19.61
        elif curve_type == 3:
            a = .1217
            k = 28.2
        operating_time = mf.calculate_operating_time_ieee(tms, k, psm, a)
        print(operating_time)

