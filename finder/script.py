from email import message
from operator import le
from tkinter import SINGLE
import questionary # Doc: https://pypi.org/project/questionary/
import os
import pprint


WELCOME_MESSAGE = "Welcome to Questions finder! 💡"
WELCOME_STYLE = "bold italic"
SINGLE_QUESTIONS_FOLDER_NAME = "single_questions"
LISTS_FOLDER_NAME = "lists"
SEARCH_RESULT_SUCCESS_MESSAGE = "🔥 Search Results"
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
    "DIFFICULTY_SEARCH_TYPE": {
        "message": "Select the lists/questions difficulty you want to search.",
        "choices": ["baby", "basic", "intermediary", "advanced", "master"],
        "validation": lambda a: True if len(a) else "Should select at least one option"
    },
    "KEY_WORD_SEARCH": {
        "message": "Enter the keyword to be searched for:",
        "validation": lambda a: True if (len(a) >= 3 or len(a) == 0 ) else "Should write at least a 3 chars word or Nothing"
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

def get_difficulty_search_type():
    return questionary.checkbox(
            message=CONFIG["DIFFICULTY_SEARCH_TYPE"]["message"],
            choices=CONFIG["DIFFICULTY_SEARCH_TYPE"]["choices"],
            validate=CONFIG["DIFFICULTY_SEARCH_TYPE"]["validation"]
        ).ask()

def get_search_key_word():
    return questionary.text(
            message=CONFIG["KEY_WORD_SEARCH"]["message"],
            validate=CONFIG["KEY_WORD_SEARCH"]["validation"]
        ).ask()

def _mount_difficulty_file_pattern(difficulty_option):
    return "_" + difficulty_option + ".ipynb"

def _get_search_target_names(main_search_options):
    all_names = []

    if CONFIG["MAIN_SEARCH_TYPE"]["choices"][0] in main_search_options:
        all_names = os.listdir(SINGLE_QUESTIONS_FOLDER_NAME)
    if CONFIG["MAIN_SEARCH_TYPE"]["choices"][1] in main_search_options:
        all_names = all_names + os.listdir(LISTS_FOLDER_NAME)

    return all_names

def _filter_target_names_by_difficulty(all_names, difficulty_search_options):
    if len(difficulty_search_options) == len(CONFIG["DIFFICULTY_SEARCH_TYPE"]["choices"]):
        return all_names
    else:
        filtered_names = []
        for name in all_names:
            for difficulty_option in difficulty_search_options:
                if _mount_difficulty_file_pattern(difficulty_option) in name:
                    filtered_names.append(name)
                    break
        return filtered_names

def _apply_key_word_filter(names, key_word):
    if len(key_word) == 0:
        return names
    else:
        return [name for name in names if key_word in name]

def perform_search(main_search_options, difficulty_search_options, key_word):
    all_names = _get_search_target_names(main_search_options)
    filtered_names_by_difficulty = _filter_target_names_by_difficulty(all_names, difficulty_search_options)
    search_result = _apply_key_word_filter(filtered_names_by_difficulty, key_word)
    return search_result

def show_search_result(search_result):
    if search_result:
        questionary.print(text=SEARCH_RESULT_SUCCESS_MESSAGE + " [{}]:".format(len(search_result)), style=SEARCH_RESULT_SUCCESS_STYLE)
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

        selected_difficulty_search_options = get_difficulty_search_type()

        search_key_word = get_search_key_word()

        result = perform_search(selected_main_search_options, selected_difficulty_search_options, search_key_word)

        show_search_result(result)

        keep_searching = get_keep_searching()
