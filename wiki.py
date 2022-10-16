import wikipedia
import rich
import banner
import os, sys

from rich.console import Console
from rich.prompt import Prompt

console = Console()

lang = Prompt.ask(
    "[bold red]Выберите язык[/]",
    choices=["be", "de", "uk"],
    default="ru"
)

wikipedia.set_lang(lang)

console.print(f"\n[bold white]Выбран язык: {lang}\n")

search = console.input('[bold magenta]Введите поисковой запрос[/]> ')

try:
   wiki = wikipedia.summary(search, sentences=10)

except:
      console.print('[bold red]Запрос выполнен не верно!')
      sys.exit()
      
console.print(f'\n[bold red]Результаты[/]:\n[italic dim]{wiki}')

