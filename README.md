# Substitution Cipher #
#### This is a simple python script to convert English to another format via dictionaries. ####
```
usage: translate.py [-h] [-l] [-r] [-u] [-D DIR] [-d DICT] [input_string]

Convert english to runes

positional arguments:
  input_string          Input string to be translated.

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List all avaliable dictionaries.
  -r, --reverse         Convert translated string back.
  -u, --use_case        Do not ignore capitalization of letters.
  -D DIR, --dir DIR     Path of dictionaries directory.
  -d DICT, --dict DICT  Dictionary to use.
```
I currently only have the runic dictionary made.<br>
The runes of choice for the letters j and k where added in Unicode version 11 which is not widely used at this time so I'm using ᛃ and ᚲ instead, unlike Tolkien's runic language.<br>
I've also created a base 10 counting system using runic symbols.<br>
<br>
You can change the translation to any rune you want in the `runes.csv` file.<br>
