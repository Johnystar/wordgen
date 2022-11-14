import click
import pyperclip as clip
from . import words
from .exceptions import NotEnoughWordsError
from .data import get_available_files, parse_file


def shell_completion(ctx, param, incomplete) -> list[str]:
    match param.name:
        case 'course':
            return [file for file in get_available_files('courses') if file.startswith(incomplete)]
        case 'wordset':
            return [file for file in get_available_files('words') if file.startswith(incomplete)]
        case 'level':
            try:
                return [
                    str(x)
                    for x in range(
                        1,
                        len(parse_file(get_available_files('courses')[ctx.params['course']]))+1
                    )]
            except KeyError as _:
                return []

@click.command(context_settings={
    'help_option_names': ['-h', '--help']
})
@click.option('-c', '--course',
              default="colemak_DHm", show_default=True,
              shell_complete=shell_completion,
              help="Which course to prepare")
@click.option('-s', '--wordset',
              default=["english"], show_default=True, multiple=True,
              shell_complete=shell_completion,
              help="Which wordset(s) to use")
@click.option('-n', '--words', 'amount',
              default=50, show_default=True,
              help="Amount of words to output, set to n<0 to output all (useful in combination with Monkeytype's randomiser)")
@click.option('-l', '--level',
              default=1, show_default=True,
              shell_complete=shell_completion,
              help="Level of difficulty (amount of levels may vary per course)")
@click.option('-o', '--copy',
              is_flag=True,
              help="Copy output to clipboard (xclip on Linux, pbcopy on MacOS, no additional dependencies on Windows)")
@click.option('-p', '--plain',
              is_flag=True,
              help="Only outputs actual data, no additional information provided (ideal for piping)")
def cli(course:str,
        wordset:list[str],
        amount:int,
        level:int,
        copy:bool,
        plain:bool):
    """Word training set generator for learning typing and improving your performance

    \b
    Custom courses and wordsets can be defined in the following places:
        - Linux:           $XDG_CONFIG_HOME/.config/wordgen/<courses or words>/
                           ($XDG_CONFIG_HOME defaults to ~/.config/)
        - Mac OS:          ~/Library/Preferences/wordgen/<courses or words>/
        - Win XP or older: C:\\Documents and Settings\\<username>\\Local Settings\\Application Data\\octelly\\wordgen\\<courses or words>\\
        - Win 7 or newer:  C:\\Users\\<username>\\AppData\\Roaming\\octelly\\wordgen\\<courses or words>\\

    Extensions (.txt, .md and other) for custom course and wordset files are ignored. Empty lines are ignored and everything following # characters is ignored.
    """
    w = words.from_data(words=wordset,
                        course=course,
                        level=level)

    if amount > 0:
        try:
            output = w.get_n_words(amount)
        except NotEnoughWordsError as _:
            click.echo("Not enough filtered words in wordset!", err=True)
            return
    else:
        output = w.get_words()

    output_text = ' '.join(output)

    click.echo(output_text)
    if copy: clip.copy(output_text)

    if not plain: click.echo("Word count: " + str(len(output)))
