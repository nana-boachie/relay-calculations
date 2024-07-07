def get_user_choice(option1, option2):
    while True:
        user_input = input(f"Choose {option1} or {option2}: ")
        if user_input.lower() == option1.lower():
            # print(f"You chose {option1}!")
            # Your code for option 1 goes here
            return user_input.lower()  # Return the choice
        elif user_input.lower() == option2.lower():
            # print(f"You chose {option2}!")
            # Your code for option 2 goes here
            return user_input.lower()  # Return the choice
        else:
            print("Invalid choice. Please enter a valid option.")


