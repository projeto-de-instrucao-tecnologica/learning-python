import questionary # Doc: https://pypi.org/project/questionary/
import os
import pprint


questionary.print("Welcome to Questions finder! 💡", style="bold italic")

keep_searching = True

while keep_searching:

    selected_search_option = questionary.checkbox(
        message="Select what you want to search.",
        choices=["single questions", "question lists"],
        validate=lambda a: True if len(a) else "Should select at least one option",
    ).ask()

    key_word = questionary.text(
        message="Enter the keyword to be searched for:",
        validate=lambda a: True if len(a) >= 3 else "Should write at least a 3 chars word"
    ).ask()

    result_questions = []
    result_questions_lists = []

    if "single questions" in selected_search_option:
        all_questions = os.listdir("single_questions")
        result_questions = [single_question for single_question in all_questions if key_word in single_question]
    if "question lists" in selected_search_option:
        all_questions_lists = os.listdir("lists")
        result_questions_lists = [questions_list for questions_list in all_questions_lists if key_word in questions_list]

    result = result_questions + result_questions_lists

    if result:
        questionary.print("🔥 Search Results:", style="bold italic fg:green")
        pprint.pprint(result)
    else:
        questionary.print("🐛 No results found", style="bold italic fg:red")

    keep_searching = questionary.confirm("Do you want to keep searching?").ask()
