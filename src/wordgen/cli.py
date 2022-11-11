import click
import pyperclip as clip
from . import words

@click.command(context_settings={
    'help_option_names': ['-h', '--help']
})
@click.option('-c', '--course',
              default="colemak_DHm", show_default=True,
              help="Which course to prepare")
@click.option('-s', '--wordset',
              default=["english"], show_default=True, multiple=True,
              help="Which wordset(s) to use")
@click.option('-n', '--words', 'amount',
              default=50, show_default=True,
              help="Amount of words to output")
@click.option('-l', '--level',
              default=1, show_default=True,
              help="Level of difficulty (amount of levels may vary per course)")
@click.option('-o', '--copy',
              is_flag=True,
              help="Copy output to clipboard")
def cli(course:str,
        wordset:list[str],
        amount:int,
        level:int,
        copy:bool):
    w = words.from_data(words=wordset,
                        course=course,
                        level=level)

    output = ' '.join(w.get_words(amount))

    click.echo(output)
    if copy: clip.copy(output)
