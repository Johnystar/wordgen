# Word generator (for all you goddam keeb nerds 🤓)

## The story

I finally got some time on my hands to learn different layouts and Colemak is what interested me the most. At this point I was already familiar with Monkeytype, but it didn't provide proper learning tools. I looked around for an alternative, but other sites and tools were buggy, limited, too complicated or I wasn't able to find them.

This was my solution. `wordgen` generates (well, filters out really) curated word lists for you based on your demands. Just starting out? Focusing on just `arst` and `neio` might be more efficient. Want a specific word set? English or anything custom can be loaded in and used as a source for the generator. It even features a convenient `--copy` flag, which makes Monkeytype's ability to save texts almost useless (although their word randomisation is still awesome).

## Installation

### From PyPi

- *nix: `pipx install wordgen` or `python3 -m pip install wordgen`
- Win: `pipx install wordgen` or `python -m pip install wordgen`

> **Note**: May differ based on your installation

### From source

If you want to do this, you can probably figure it out. If you can't, give me some time and I'll eventually rewrite this section to be more useful. (or someone can make a pr)

## Configuration

As of version `2022.0.1`, there isn't any config file, however, you can include your own custom courses and wordsets in these paths:

- Linux: `$XDG_CONFIG_HOME/.config/wordgen/<courses or wordsets>/` (`$XDG_CONFIG_HOME` default to `~/.config/`)
- Mac OS: `~/Library/Preferences/wordgen/<courses or wordsets>/`
- Win XP or older: `C:\Documents and Settings\<username>\Local Settings\Application Data\octelly\wordgen\<courses or wordsets>\`
- Win 7 or newer: `C:\Users\<username>\AppData\Roaming\octelly\wordgen\<courses or wordsets>\`

## Project versioning

`year.breaking.minor`

- `year` of release
- goes up in case there's a `breaking` change
- `minor` goes up with each update

## Credits

- code by Octelly
- the included English wordset is from here: https://gist.github.com/deekayen/4148741 
