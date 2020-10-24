# xkcdpwgen

by Nicholas Fiorito  / github.com/fueg0

xkcd password generator is a password-generating script modeled after the method described in [xkcd 936](https://xkcd.com/936/)

![XKCD Comic 936](https://imgs.xkcd.com/comics/password_strength.png)

Randall Munroe describes the idea that we have been trained to create "secure" passwords that are in reality hard for *people* 
to remember yet easy for *computers* to guess at- making them not so secure. Instead, we could make passwords that are both 
easy for humans to remember, and quite difficult for a computer to guess at with as few as four words.

This script uses the 2048-word long bips wordlist that was designed for securing Bitcoin wallets by generating secret recovery 
phrases that are 12 words long. These words are for the most part lacking in excess complexity (making them good for memorizing 
as passwords) yet have a large enough sample size that an enormous amount of unique combinations are possible.

## Usage

The script itself can be run with a format as follows:  
On `Linux` (after running `dos2unix` and `chmod +x`)
either an argument-less command like `./xkcdpwgen`  
or one with flags such as `./xkcdpwgen -w 4 -c 0 -n 2 -s 1` are allowed in any order  

On `Windows`
an argument-less command like `C:\Users\you\pathToFile python xkcdpwgen.py`  
or one with flags such as `C:\Users\you\pathToFile python xkcdpwgen.py -w 4 -c 0 -n 2 -s 1` are allowed in any order  


In the flag form, `-w` is the number of words, `-n` is how many numbers you would like included, `-s` is the amount of special characters you would like, and `-c` is the value of how many words from `-w` you would like to start with a capital letter

If the script is executed simply as `./xkcdpwgen` then the default values are `w=4` `c=0` `n=0` `s=0`

## Behaviors

If any values are negative, they will be set to `0`  

If any flags are not included, they will be set to their defaults (`w=4` `n=0` `s=0` `c=0`)

If c > w, c will be set to equal w and each word will begin with a capital letter

Passwords are recommended to have at least the defaults in their construction (i.e. a bare minimum of 4 words without numbers/special characters/capitalization)

## Function

After being provided the numbers that go into the flags, the program will simply run a loop that will randomly select that amount of items from a preset array of words, numbers or special characters, then run a similar loop to capitalize some of the words (if c > 0). Finally, it will shuffle the array containing all of the selected elements to put them in a random order and concatenate them into one string.
