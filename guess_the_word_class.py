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

class Inputs:
    """
    A class that takes input from user and generates a random number to select question.
    ...
    Attributes
    ----------
    option: int
        The number representing the category selected
    num : int
        A random number that is used to pick the word to be guessed.
    """
    def __init__(self):
        print('''Category 1: Movies \n
Category 2:Capital Cities \n
Category 3: Languages \n''')
        self.option = int(input('Enter category number 1/2/3 to begin\n'))
        self.num = random.randint(0, 5)

class Questions:
    """
    A class that stores the questions and returns the question based on random number generated.
    ...
    Attributes
    ----------
    question : dict
        Contains a list of words to guessed with category number
        as key.

    Methods
    -------
    options(object1):
        Returns the word to be guessed by the user .
    """
    def __init__(self):
        self.question = {
            1: ['malang', 'panga', 'titanic', 'kites', 'raone', 'avatar'],
            2: ['paris', 'abudhabi', 'newdelhi', 'rome', 'athens', 'muscat'],
            3: ['french', 'hindi', 'japanese', 'english', 'german', 'greek'],
            }

    def options(self, object1):
        """Gets the category and the postion of the word to be guessed in the dictionary.
    Prints the length of the word to be guessed and returns the word to be guessed.

    Parameters
    ----------
    option : int
        The number representing the category selected
    question: dict
        Contains a list of words to guessed with category number
        as key.
    question_number : int
        A random number that is used to pick the word to be guessed.

    Returns
    -------
    string
        The word that is to be guessed by the user"""
        if object1.option == 1:
            print('Category:Movies')
            string_len = len(self.question[object1.option][object1.num])
            print(string_len*('_ '))
            print('Length=',string_len)
            return self.question[object1.option][object1.num]
        elif object1.option == 2:
            print('Category:Capital Cities')
            string_len = len(self.question[object1.option][object1.num])
            print(string_len*('_ '))
            print('Length=',string_len)
            return self.question[object1.option][object1.num]
        elif object1.option == 3:
            print('Category:Languages')
            string_len = len(self.question[object1.option][object1.num])
            print(string_len*('_ '))
            print('Length=',string_len)
            return self.question[object1.option][object1.num]
        else:
            print('Invalid Option')
            return 0

class ReturnQuestion:
    """
    A class to return the word returned by class questions.
    ...

    Attributes
    ----------
    object1: Object of class Input
    object2: Object of class Questions

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    def  get_input(self,object1,object2):
        """Returns the word to be guessed.

    Parameters
    ----------
    self : current object
    object1 :  Object of class Input
    object2: Object of class Questions

    Returns
    -------
    integer
        The word to be guessed"""
        self.input_string=object2.options(object1)
        return self.input_string

class CheckAnswer():
    """
    A class to compare the guessed word and the question.
    ...

    Attributes
    ----------
    questions : str
        word to be guessed
    guess : str
        word guessed by user

    Methods
    -------
    check():
        Checks if lengths of the input strings are equal.
    checkans():
        Checks if the two input strings are the same
    """
    def __init__(self,questions,guess):
        self.question=questions
        self.guess=guess

    def check(self):
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
        if len(self.question) == len(self.guess):
            return 1
        else:
            return 0

    def checkans(self):
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
        if self.check() == 1:
            print(self.guess)
            input_word = input('Enter the guessed word as a complete string\t')
            if self.question == input_word:
                print('Well Done !!')
                return 1
            else:
                print('Sorry wrong answer. Correct answer-', self.question)
                return  0
        else:
            print("Wrong Answer.Better luck next time.\nCorrect answer-", self.question)
            return 0

class Score:
    """
    A class to represent the score of current user.
    ...
    Attributes
    ----------
    value : int
        flag representing if current guess correct or not
    score : int
        current score of user

    Methods
    -------
    score1():
        Updates the current score.
    print_score():
        Prints the updated score
    """

    def __init__(self,value,score):
        self.value=value
        self.score=score

    def score1(self):
        """Updates the present score of the user.

    Parameters
    ----------
    self : current object
        The object has two attributes.
        value:integer
            Flag value that denotes if the current question was guessed correctly.
        score:integer
            Current score of user to be updated

    Returns
    -------
    integer
        The current score of the user"""
        present_score=self.score
        if self.value==1:
            present_score=present_score+1
        return present_score

    def print_score(self):
        """Prints the current score of user.

    Parameters
    ----------
    self : current object
        Used to access the class method score1.

    Prints
    -------
   The current score of user"""
        print("The current score=",self.score1())


def check_repeat(string):
    """Gets the word to be guessed and returns the number of unique characters in the word.

    Parameters
    ----------
    input_string : str
        The word to be guessed by the user.

    Returns
    -------
    integer
        The number of unique characters in the word"""
    string1=string
    length = len(string1)
    length1 = length
    for iter1 in range(0, length):
        count = 0
        for j in range(iter1+1, length):
            if string1[iter1] == string1[j]:
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

def compare1(question, guess, out):
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


TURN = 1
SCORE = 0
while(TURN != 0 and TURN < 11):
    i=Inputs()
    q=Questions()
    c=ReturnQuestion()
    r=c.get_input(i,q)
    l=check_repeat(r)
    o = []
    h = []
    print("Enter characters one by one:\n")
    for i in range(l+10):
        a = input('')
        a1 = convert_case(a)
        a2 = check_repeat_l(a1,h)
        t = compare1(r, a2, o)
        if len(o) == len(r):
            break
    p=CheckAnswer(r,t)
    CHECK=p.checkans()
    scores=Score(CHECK,SCORE)
    SCORE=scores.score1()
    scores.print_score()
    TURN = continue_play(TURN)
