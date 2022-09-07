from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pygments.styles.colorful import ColorfulStyle
from prompt_toolkit.styles import style_from_pygments_cls

STYLES = {
    "separator": '#cc5454',
    "questionmark": '#673ab7 bold',
    "selected": '#cc5454',  # default
    "pointer": '#673ab7 bold',
    "instruction": '',  # default
    "answer": '#f44336 bold',
    "question": '',
    "warn": '#ff0000 bold'
}

session = PromptSession(history=FileHistory('./.prompthistory'))

def print(text: str, style=None) -> None:
    if style is None:
        print_formatted_text(text)
        return
    text = FormattedText([(STYLES[style], text)])
    print_formatted_text(text)

def prompt(text: str, is_password=False) -> str:
    return session.prompt(text, style=style_from_pygments_cls(ColorfulStyle),
                          auto_suggest=AutoSuggestFromHistory(), is_password=is_password)

