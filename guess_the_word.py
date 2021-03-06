"""Guess the word game

This script mimics the popular hangman game.
All the characters given as input are of string data type.
Contains the fucntions:
    *options - retuns the word to be guessed
    *menu - displays the categories.
    *check_repeat - returns length of the word to be guessed
    *check_repeat_l - returns the input character if it is entered for the first time.
    *convert_case - returns a string converted to lower case
    *compare - returns a list containing correctly guessed characters.
    *check - returns 1 if length of the input strings equal.
    *check_ans - prints the right answer.
    *randomgen - returns a random number.
    *continue-play - returns the number turns of play done.

"""

import random


def options(option, dictionary, question_number):
    """Gets the category and the postion of the word to be guessed in the dictionary.
    Prints the length of the word to be guessed and returns the word to be guessed.

    Parameters
    ----------
    option : int
        The number representing the category selected
    dictionary : dict
        Contains a list of words to guessed with category number
        as key.
    question_number : int
        A random number that is used to pick the word to be guessed.

    Returns
    -------
    string
        The word that is to be guessed by the user"""
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
    """Prints the categories and the corresponding numbers.
    Returns the user entered category number.

    Returns
    -------
    integer
        The category number of the category chosen"""
    print('''Category 1: Movies \n
Category 2:Capital Cities \n
Category 3: Languages \n''')
    option = int(input('Enter category number 1/2/3 to begin\n'))
    return option


def check_repeat(input_string):
    """Gets the word to be guessed and returns the number of unique characters in the word.

    Parameters
    ----------
    input_string : str
        The word to be guessed by the user.

    Returns
    -------
    integer
        The number of unique characters in the word"""
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
    """Gets the user input character and an empty list,
    If a user input character is not already present in the list,
    the character is appended to the list and returned,
    else an empty character is returned.

    Parameters
    ----------
    character : str
        The user entered input.
    list1 : list
        An empty list initially, appended with user input.

    Returns
    -------
    string
        the user input character that has been entered only once"""
    if character not in list1:
        list1.append(character)
        return character
    else:
        print("Don't repeat input characters")
        return " "

def convert_case(string):
    """Gets the user input character and returns the character in lowercase.

    Parameters
    ----------
    string : str
        The user entered input.

    Returns
    -------
    string
        the user input character in lowercase"""
    return string.lower()


def compare(question, guess, out):
    """Gets the word to be guessed, the user input characters and an empty list.
    Compares the word to be guessed and the user input, in case a character matches,
    appends the matched character to the empty list and returns the list.

    Parameters
    ----------
    question : str
        The word to be guessed.
    guess : str
        User entered input.
    out : list
        An empty list initially,appended with matched characters.

    Returns
    -------
    list
        The list containing matched characters"""
    length1 = len(question)
    length2 = len(guess)
    for iterator in range(length1):
        num = iterator
        for j in range(length2):
            if question[iterator] == guess[j]:
                out.append(guess[j])
                print(num + 1, guess[j])
    return out


def check(string_1, list_1):
    """Gets two strings,returns 1 if lengths of both strings equal.
    This function is used in the checkans function.

    Parameters
    ----------
    string_1 : str
        The word to be guessed
    list_1 : list
        The list returned from compare function.

    Returns
    -------
    integer
        1 if the length of the string and list are equal,else returns 0."""
    if len(string_1) == len(list_1):
        return 1
    else:
        return 0

def checkans(question,guess):
    """Gets the word to be guessed and the list of correctly guessed characters.
    Prints the list if lengths of the two parameters equal and takes user input
    to guess the correct word and prints the result accordingly.

    Parameters
    ----------
    question : str
        The word to be guessed.
    guess : list
        Contains correctly guessed characters,not in the right order.

    Prints
    -------
    The result based on user inputs provided"""
    if check(question, guess) == 1:
        print(guess)
        input_word = input('Enter the guessed word as a complete string\t')
        if question == input_word:
            print('Well Done !!')
        else:
            print('Sorry wrong answer. Correct answer-', question)
    else:
        print("Wrong Answer.Better luck next time.\nCorrect answer-", question)

def randomgen():
    """Returns a random nuber in the range 0-5.

    Returns
    -------
    integer
        the random number that selects the word to be guessed."""
    num = random.randint(0, 5)
    return num


def continue_play(turns):
    """Gets the turns variable.Based on user input,
    if they want to contine or not the turns variable is updated.

    Parameters
    ----------
    turns : int
        The number representing the number of turns already taken by user.

    Returns
    -------
    integer
        The updated value of the variable turns"""
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
    2: ['paris', 'washingtondc', 'newdelhi', 'rome', 'athens', 'muscat'],
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
    print("Enter characters one by one:\n")
    for i in range(l+10):
        a = input('')
        a1 = convert_case(a)
        a2 = check_repeat_l(a1,h)
        t = compare(q, a2, o)
        if len(o) == len(q):
            break
    checkans(q,t)
    TURN = continue_play(TURN)
