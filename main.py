# FUNCTIONS #



def translate1(sentence):
    translation = ''
    for letter in sentence:
        if letter.lower() in 'a':
            translation = translation + 'ᚨ'
        elif letter.lower() in 'b':
            translation = translation + 'ᛒ'
        elif letter.lower() in 'c':
            translation = translation + 'ᚲ'
        elif letter.lower() in 'd':
            translation = translation + 'ᛞ'
        elif letter.lower() in 'e':
            translation = translation + 'ᛖ'
        elif letter.lower() in 'f':
            translation = translation + 'ᚠ'
        elif letter.lower() in 'g':
            translation = translation + 'ᚷ'
        elif letter.lower() in 'h':
            translation = translation + 'ᚺ'
        elif letter.lower() in 'i':
            translation = translation + 'ᛁ'
        elif letter.lower() in 'j':
            translation = translation + 'ᛃ'
        elif letter.lower() in 'k':
            translation = translation + 'ᚴ'
        elif letter.lower() in 'l':
            translation = translation + 'ᛚ'
        elif letter.lower() in 'm':
            translation = translation + 'ᛗ'
        elif letter.lower() in 'n':
            translation = translation + 'ᚾ'
        elif letter.lower() in 'o':
            translation = translation + 'ᛟ'
        elif letter.lower() in 'p':
            translation = translation + 'ᛈ'
        elif letter.lower() in 'q':
            translation = translation + 'ᛩ'
        elif letter.lower() in 'r':
            translation = translation + 'ᚱ'
        elif letter.lower() in 's':
            translation = translation + 'ᛋ'
        elif letter.lower() in 't':
            translation = translation + 'ᛏ'
        elif letter.lower() in 'u':
            translation = translation + 'ᚢ'
        elif letter.lower() in 'v':
            translation = translation + 'ᚡ'
        elif letter.lower() in 'w':
            translation = translation + 'ᚹ'
        elif letter.lower() in 'x':
            translation = translation + 'ᛪ'
        elif letter.lower() in 'y':
            translation = translation + 'ᚤ'
        elif letter.lower() in 'z':
            translation = translation + 'ᛉ'
        elif letter.lower() in '?! ':
            translation = translation + letter
        else:
            print('\nERROR')
            print('\nOnly this characters are accepted >>>', end=" ")
            print('abcdefghijklmnopqrstuvwxyz?!')
    return translation

def translate2(sentence):
    translation = ''
    for letter in sentence:
        if letter.lower() in 'ᚨ':
            translation = translation + 'a'
        elif letter.lower() in 'ᛒ':
            translation = translation + 'b'
        elif letter.lower() in 'ᚲ':
            translation = translation + 'c'
        elif letter.lower() in 'ᛞ':
            translation = translation + 'd'
        elif letter.lower() in 'ᛖ':
            translation = translation + 'e'
        elif letter.lower() in 'ᚠ':
            translation = translation + 'f'
        elif letter.lower() in 'ᚷ':
            translation = translation + 'g'
        elif letter.lower() in 'ᚺ':
            translation = translation + 'h'
        elif letter.lower() in 'ᛁ':
            translation = translation + 'i'
        elif letter.lower() in 'ᛃ':
            translation = translation + 'j'
        elif letter.lower() in 'ᚴ':
            translation = translation + 'k'
        elif letter.lower() in 'ᛚ':
            translation = translation + 'l'
        elif letter.lower() in 'ᛗ':
            translation = translation + 'm'
        elif letter.lower() in 'ᚾ':
            translation = translation + 'n'
        elif letter.lower() in 'ᛟ':
            translation = translation + 'o'
        elif letter.lower() in 'ᛈ':
            translation = translation + 'p'
        elif letter.lower() in 'ᛩ':
            translation = translation + 'q'
        elif letter.lower() in 'ᚱ':
            translation = translation + 'r'
        elif letter.lower() in 'ᛋ':
            translation = translation + 's'
        elif letter.lower() in 'ᛏ':
            translation = translation + 't'
        elif letter.lower() in 'ᚢ':
            translation = translation + 'u'
        elif letter.lower() in 'ᚡ':
            translation = translation + 'v'
        elif letter.lower() in 'ᚹ':
            translation = translation + 'w'
        elif letter.lower() in 'ᛪ':
            translation = translation + 'x'
        elif letter.lower() in 'ᚤ':
            translation = translation + 'y'
        elif letter.lower() in 'ᛉ':
            translation = translation + 'z'
        elif letter.lower() in '?! ':
            translation = translation + letter
        else:
            print('\nERROR')
            print('\nOnly this characters are accepted >>>', end=" ")
            print('ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚴᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛪᚤᛉ?!')
    return translation

# FUNCTIONS #





# CONSTANTS #

n = 1

file = open('Runes.txt', 'w+')

# CONSTANTS #





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