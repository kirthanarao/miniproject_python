import random


def options(option, dictionary, question_number):
    if option == 1:
        print('Movies')
        string_len = len(dictionary[option][question_number])
        print(string_len*('_ '))
        print('Length=',string_len)
        return dictionary[option][question_number]
    elif option == 2:
        print('Capital Cities')
        string_len = len(dictionary[option][question_number])
        print(string_len*('_ '))
        print('Length=',string_len)
        return dictionary[option][question_number]
    elif option == 3:
        print('Languages')
        string_len = len(dictionary[option][question_number])
        print(string_len*('_ '))
        print('Length=',string_len)
        return dictionary[option][question_number]
    else:
        print('Invalid Option')
        return 0


def menu():
    print('''Category 1: Movies \n
Category 2:Capital Cities \n
Category 3: Languages \n''')
    option = int(input('Enter category number 1/2/3 to begin\n'))
    return option


def check_repeat(input_string):
    length = len(input_string)
    length1 = length
    for iter1 in range(0, length):
        count = 0
        for j in range(iter1+1, length):
            if input_string[iter1] == input_string[j]:
                count = count + 1
                if count == 1:
                    length1 = length1 - 1
        return int(length1)

def check_repeat_l(character,list1):
    if character not in list1:
        list1.append(character)
        return character
    else:
        print("Don't repeat input characters")
        return " "

def convert_case(string):
    return string.lower()


def compare(question, guess, out):
    length1 = len(question)
    length2 = len(guess)
    for iterator in range(length1):
        num = iterator
        for j in range(length2):
            if question[iterator] == guess[j]:
                out.append(guess[j])
                print(num + 1, guess[j])
    return out


def check(string_1, string_2):
    if len(string_1) == len(string_2):
        return 1
    else:
        return 0

def checkans(question,guess):
    if check(question, guess) == 1:
        print(guess)
        input_word = input('Enter the guessed word \t')
        if question == input_word:
            print('Well Done !!')
        else:
            print('Sorry wrong answer. Correct answer-', question)
    else:
        print("Wrong Answer.Better luck next time.\nCorrect answer-", question)

def randomgen():
    num = random.randint(0, 5)
    return num


def continue_play(turns):
    print('Do you want to continue ?')
    choice = input('y-Yes n-No\t')
    choice_1 = convert_case(choice)
    if choice_1 == 'y':
        turns = turns+1
    else:
        turns = 0
    return turns

questions = {
    1: ['devdas', 'dhoom', 'titanic', 'kites', 'raone', 'avatar'],
    2: ['paris', 'newyork', 'newdelhi', 'rome', 'athens', 'muscat'],
    3: ['french', 'hindi', 'arabic', 'english', 'german', 'greek'],
    }
TURN = 1
while(TURN != 0 and TURN < 7):
    opt = menu()
    m = randomgen()
    q = options(opt, questions, m)
    l = check_repeat(q)
    o = []
    h = []
    print("Enter characters:\n")
    for i in range(l+10):
        a = input('')
        a1 = convert_case(a)
        a2 = check_repeat_l(a1,h)
        t = compare(q, a2, o)
        if len(o) == len(q):
            break
    checkans(q,t)
    TURN = continue_play(TURN)
