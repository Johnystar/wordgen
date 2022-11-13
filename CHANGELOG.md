# Changelog

## 2022.1.0
- **BREAKING**: program reports outputted word count by default, this along with any other piping-unfriendly additional texts can be muted with `--plain`
- `--words` can be sent to 0 or lower to output all filtered words, ideal for Monkeytype's built-in word randomiser in custom mode
- requesting more `--words` than available no longer prints a traceback
- added more helpful information to `--help`

## 2022.0.1
- multiple wordset flags can now be used to source multiple wordsets
- help flags are now both `--help` and `-h`

## 2022.0.0
- initial release
- released on PyPi and Test PyPi
