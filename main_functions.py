from typing import Any


def quit_program():
    """
    Allows the user to quit the program by typing 'q' or 'quit'.
    """
    while True:
        user_input = input("Type 'q' or 'quit' to exit the program: ").lower()
        if user_input in ["q", "quit"]:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'q' or 'quit' to exit.")


def get_user_choice(option1, option2):
    while True:
        user_input = input(f"Choose curve {option1} / {option2}: ").lower()
        if user_input.lower() == option1.lower():
            # print(f"You chose {option1}!")
            # Your code for option 1 goes here
            return user_input  # Return the choice
        elif user_input.lower() == option2.lower():
            # print(f"You chose {option2}!")
            # Your code for option 2 goes here
            return user_input  # Return the choice
        else:
            print("Invalid choice. Please enter a valid option.")


def calculate_operating_time_iec(tms, k, psm, a):
    try:
        operating_time: float | Any = tms * (k / ((psm ** a) - 1))
        return operating_time
    except ZeroDivisionError:
        return "Error: Division by zero occurred. Please check the values of 'psm' and 'a'."


def calculate_operating_time_ieee(tms, k, psm, a):
    try:
        operating_time: float | Any = tms * (((k*(psm ** a)) - 1)/(k-1))
        return operating_time
    except ZeroDivisionError:
        return "Error: Division by zero occurred. Please check the values of 'psm' and 'a'."


def select_iec_curve_type():
    print("Choose a curve: \n 1.Standard inverse \n 2.Very \n 3.Extremely inverse \n 4.Longtime standard inverse")
    while True:
        try:
            choice = int(input("enter the number of your curve between 1-4: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def select_ieee_curve_type():
    print("Choose a curve: \n 1.Moderately inverse \n 2.Very inverse \n 3.Extremely inverse")
    while True:
        try:
            choice = int(input("enter the number of your curve between 1-3: "))
            if 1 <= choice < 4:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def ask_to_continue():
    """
    Asks the user if they wish to continue.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    while True:
        user_input = input("Do you wish to continue? (yes/no): ").lower()
        if user_input == "yes" or user_input == "y":
            return True
        elif user_input == "no" or user_input == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
