import main_functions

# Example usage:
curve1 = "IEC"
curve2 = "IEEE"

if __name__ == "__main__":
    chosen_option = main_functions.get_user_choice(curve1, curve2)
    print(f"User chose: {chosen_option.lower()}")
