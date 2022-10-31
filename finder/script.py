from email import message
from tkinter import SINGLE
import questionary # Doc: https://pypi.org/project/questionary/
import os
import pprint


WELCOME_MESSAGE = "Welcome to Questions finder! 💡"
WELCOME_STYLE = "bold italic"
SINGLE_QUESTIONS_FOLDER_NAME = "single_questions"
LISTS_FOLDER_NAME = "lists"
SEARCH_RESULT_SUCCESS_MESSAGE = "🔥 Search Results:"
SEARCH_RESULT_SUCCESS_STYLE = "bold italic fg:green"
SEARCH_RESULT_FAIL_MESSAGE = "🐛 No results found"
SEARCH_RESULT_FAIL_STYLE = "bold italic fg:red"
KEEP_SEARCHING_MESSAGE= "Do you want to keep searching?"
CONFIG = {
    "MAIN_SEARCH_TYPE": {
        "message": "Select what you want to search.",
        "choices": ["single questions", "question lists"],
        "validation": lambda a: True if len(a) else "Should select at least one option"
    },
    "KEY_WORD_SEARCH": {
        "message": "Enter the keyword to be searched for:",
        "validation": lambda a: True if len(a) >= 3 else "Should write at least a 3 chars word"
    }
}

def welcome():
    questionary.print(text=WELCOME_MESSAGE, style=WELCOME_STYLE)

def get_main_search_type():
    return questionary.checkbox(
            message=CONFIG["MAIN_SEARCH_TYPE"]["message"],
            choices=CONFIG["MAIN_SEARCH_TYPE"]["choices"],
            validate=CONFIG["MAIN_SEARCH_TYPE"]["validation"]
        ).ask()

def get_search_key_word():
    return questionary.text(
            message=CONFIG["KEY_WORD_SEARCH"]["message"],
            validate=CONFIG["KEY_WORD_SEARCH"]["validation"]
        ).ask()

def _get_search_target_names(main_search_options):
    all_names = []

    if CONFIG["MAIN_SEARCH_TYPE"]["choices"][0] in main_search_options:
        all_names = os.listdir(SINGLE_QUESTIONS_FOLDER_NAME)
    if CONFIG["MAIN_SEARCH_TYPE"]["choices"][1] in main_search_options:
        all_names = all_names + os.listdir(LISTS_FOLDER_NAME)

    return all_names

def perform_search(main_search_options, key_word):
    all_names = _get_search_target_names(main_search_options)
    # TODO Perform difficulty filter
    search_result = [name for name in all_names if key_word in name]
    return search_result

def show_search_result(search_result):
    if search_result:
        questionary.print(text=SEARCH_RESULT_SUCCESS_MESSAGE, style=SEARCH_RESULT_SUCCESS_STYLE)
        pprint.pprint(search_result)
    else:
        questionary.print(text=SEARCH_RESULT_FAIL_MESSAGE, style=SEARCH_RESULT_FAIL_STYLE)

def get_keep_searching():
    return questionary.confirm(message=KEEP_SEARCHING_MESSAGE).ask()

if __name__ == "__main__":
    welcome()

    keep_searching = True

    while keep_searching:

        selected_main_search_options = get_main_search_type()

        search_key_word = get_search_key_word()

        result = perform_search(selected_main_search_options, search_key_word)

        show_search_result(result)

        keep_searching = get_keep_searching()
