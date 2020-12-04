import string

# FUNCTIONS #

def translate1(sentence):
    translation = ''
    for letter in sentence:
        letter = letter.lower()
        if letter in string.ascii_lowercase:
            translation += runic[string.ascii_lowercase.find(letter)]
        else:
            translation += letter

    return translation

def translate2(sentence):
    translation = ''
    for letter in sentence:
        if letter in runic:
            translation += string.ascii_lowercase["".join(runic).find(letter)]
        else:
            translation += letter

    return translation


# CONSTANTS #

n = 1
file = open('Runes.txt', 'w+')
runic = ['ᚨ', 'ᛒ', 'ᚲ', 'ᛞ', 'ᛖ', 'ᚠ', 'ᚷ', 'ᚺ', 'ᛁ', 'ᛃ', 'ᚴ', 'ᛚ', 'ᛗ', 'ᚾ', 'ᛟ', 'ᛈ', 'ᛩ', 'ᚱ', 'ᛋ', 'ᛏ', 'ᚢ', 'ᚡ', 'ᚹ', 'ᛪ', 'ᚤ', 'ᛉ']


# PROGRAM #

while n != 0:
    print()
    print('-=-'*15)
    print('\nAvailable Translations:')
    print('###        0 - EXIT        ###')
    print('###  1 - LETTERS to RUNIC  ###')
    print('###  2 - RUNIC to LETTERS  ###')
    while True:
        try:
            answer = int(input('\nChoose the translation type: '))
        except ValueError:
            print('Invalid Choice. Try again.')
            continue
        if answer != 1 and answer != 2 and answer != 0:
            print('Invalid Choice. Try again.')
        else:
            if answer == 1:
                print(translate1(input('\nType what you want to translate: ').lower()))
            elif answer == 2:
                print(translate2(input('\nType what you want to translate: ').lower()))
            elif answer == 0:
                n = 1
                print('\nExiting!')
                break
    break

file.close()