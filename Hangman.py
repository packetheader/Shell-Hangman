from random import randint, random

words = ['wolke', 'baumstamm', 'mario', 'hauswand', 'himmel', 'auto', 'dusche']
x = 8

def main():
    word = calculateWord()
    print(f'Das Wort hat {len(word)} Zeichen.')
    guessWord(word)


def calculateWord():
    i = randint(0, len(words) - 1)
    return words[i]

def guessWord(word):
    tries = 0
    word_list = list(word)
    word_tries = []
    word_correct = []
    while tries < x:
        if tries > 0:
            print(f'Versuche Buchstaben: {word_tries}')
        userinput = input('Gebe einen Buchstaben ein: ')
        if word_list.count(userinput) > 0:
            print(f'Der Buchstabe {userinput} ist im Wort enthalten.')
            word_correct.append(userinput)
        else:
            print(f'Der Buchstabe {userinput} ist nicht im Wort enthalten.')
            word_tries.append(userinput)
            tries += 1

        if len(word_correct) == len(word_list):
            print('Du hast das Wort richtig erraten.')
            break

if __name__ == '__main__':
    main()
