# Learning Python

This repository is focused on python learning with exercise lists that correct itself for beginners.

## Contributing

You can contribute to this repository in the following ways:

- Adding single questions corresponding to some Python learning foundation;
- Adding lists full of questions corresponding to some Python learning foundation;
- Updating or Fixing lists and questions;
- Proposing useful changes, automations or corrections to this repository structure.

Be creative and playful in asking questions that draw attention positively.
Eg.: Create a function that receives a list of Pokemon from a Trainer and returns the amount of Pokemon he has.

Lists and questions must be self-correcting, that is, they must contain assertations to verify that the implementation returns the correct values. See [list_template_basic](https://github.com/projeto-de-instrucao-tecnologica/learning_python/blob/master/lists/list_template_basic.ipynb).

You can create questions and lists in English or Portuguese, but we prefer it to be in English (We accept Pull Requests for English translation :blush:).

Be careful :warning: when creating questions and lists to don't create duplicate ones. In order to help with this, a script was created to find questions and lists from a keyword and some filters, to know more check the Usage->Finder topic of this README.

### Structure

For **Lists** and **questions** respectively, do you have to create one with this name pattern:

- list_<LIST_NAME>_<LIST_DIFFICULTY>.ipynb

- question_<QUESTION_NAME>_<QUESTION_DIFFICULTY>.ipynb

The difficulty of lists and questions should be defined among these options:

- baby
- basic
- intermediary
- advanced
- master

### Commits Icons

Use these icons at the beginning of your commit phrase to help verify the type of change you make:

- :bulb: When adding something new (questions, lists or features)
- :repeat: When any changes are made
- :cool: When code format/structure improvements
- :racehorse: When improving performance
- :non-potable_water: When resolving memory leaks
- :memo: When writing documentation
- :bug: When fixing a problem
- :fire: When removing code or files
- :green_heart: When fixing Continuous Integration issues
- :white_check_mark: When adding tests
- :lock: When dealing with security
- :arrow_up: When upgrading dependencies
- :arrow_down: When downgrading dependencies
- :minidisc: When backing up data

## Usage

The usage of questions and lists in this repository is free for educational purposes and should not be marketed. Enjoy it!!!

### Collab

You can use Google Colab free tier to open the questions and lists to apply them to anyone or solve them by yourself.

Just go to [Colab](https://colab.research.google.com) and open the file with the desired question, either via GitHub directly or downloading the file and importing it into the tool.

Remember that you must have a Google account and you can download files or save them to Drive after changes and solutions.

### Docker Environment

You can use a docker image to open the questions and lists to apply them to anyone or solve them by yourself.

Just download the docker on your machine and use the this [jupyer-image](https://hub.docker.com/r/jupyter/datascience-notebook/) to run the required python notebook environment, mapping the volume where the questions/lists lie.

```
docker run --rm -e JUPYTER_ENABLE_LAB=yes -v $(pwd):/home/jovyan/work -p 8888:8888 --name jupyterlab jupyter/datascience-notebook
```

Run the command above in the question files folder to upload jupyter-notebook on port 8888 and access them through a browser to solve or edit them as you wish.

### Finder

You can search for questions and lists using the finder script created on [finder-folder](https://github.com/projeto-de-instrucao-tecnologica/learning-python/tree/master/finder). Execute and usage it is simple:

- Use Python 3.9 version or higher
- Install the dependencies with: ```pip install -r requirements.txt```
- Execute the script with command: ```python finder/script.py```
- The script is self explanatory, so the interaction with it is very simple:
    - Choose whether to search lists, questions, or both
    - Choose the difficulty of the questions/lists you want to find - you can select as many as you like
    - Enter the keyword you want to use as a filter - if you enter no word, no word filter will be applied, bringing all results based on previous filters
    - You can perform as many searches as you like
