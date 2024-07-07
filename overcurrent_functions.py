"""IEC and IEEE OVERCURRENT FUNCTIONS"""


def get_user_curve_selection(overcurrent_curve: str):
    option1: str = "IEC"
    option2: str = "IEEE"
    while True:
        user_input = input(f"Choose {option1} or {option2}: ")
        if user_input.lower() == option1.lower():
            return option1
        elif user_input.lower() == option2.lower():
            return option2
        else:
            print("Invalid choice. Please enter a valid option.")
        continue
    print("thank you")


if __name__ == "__main__":
    curve_selection()


    """
    while True:
        overcurrent_curve = input("Type 'iec' for IEC curve or 'ieee' for IEEE curve: ")
        if overcurrent_curve == "iec":
            return overcurrent_curve
        elif overcurrent_curve == "ieee":
            return overcurrent_curve
    else:
        print("please retry.")


if __name__ == "__main__":
    selected_curve = curve_selection("iec")
    print(f"Selected curve:  {selected_curve}")


    curve_selection()

    while curve_select != iec:
    curve_choice = input("Select curve from the following")


    while curve_select == iec:
    curve_choice = input("Select curve from the following")


    def iec_formulae(psm, tms, a, k):
    #Get user input for curve selection
    operating_time: float | Any = tms * (k / ((psm ** a) - 1))
    return operating_time


def long_time_inverse(psm, tms):  # A IEC
    operating_time = tms * (120 / (psm - 1))
    return operating_time


def standard_inverse(psm, tms):  # B IEC
    operating_time = tms * (0.14 / ((psm ** 0.02) - 1))
    return operating_time


def very_inverse(psm, tms):  # C IEC
    operating_time = tms * (13.5 / (psm - 1))
    return operating_time


def extremely_inverse(psm, tms):  # D IEC
    operating_time = tms * (80 / ((psm ** 2) - 1))
    return operating_time


#psm =I/IS

#tsm time multiplier setting


def xxx(psm, tms):  # IEEE
    operating_time = td * ((A / ((psm ** p) - 1)) + B)
"""
