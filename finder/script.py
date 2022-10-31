import questionary # Doc: https://pypi.org/project/questionary/
import os


questionary.print("Welcome to Questions finder! 💡", style="bold italic")

keep_searching = True

while keep_searching:

    selected_search_option = questionary.checkbox(
        message="Select what you want to search.",
        choices=["question lists", "single questions"],
        validate=lambda a: True if len(a) else "Should select at least one option",
    ).ask()

    key_word = questionary.text(
        message="Enter the keyword to be searched for:",
        validate=lambda a: True if len(a) >= 3 else "Should write at least a 3 chars word"
    ).ask()

    print(os.listdir("lists"))
    print(os.listdir("single_questions"))

    keep_searching = questionary.confirm("Do you want to keep searching?").ask()
