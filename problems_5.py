#############################################################################################################################
'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, 
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of
shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
pytest test_twttr.py
'''
#############################################################################################################################

from problems_2 import vow

def test_twttr():
    out = vow("twitter")
    test = [i for i in out]
    assert 'a' not in test
    assert 'u' not in test
    assert 'o' not in test
    assert 'e' not in test
    assert 'i' not in test
    
#############################################################################################################################
'''
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below,
wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with
an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the 
value function will not contain any leading spaces. Only main should call print.

def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation
of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
pytest test_bank.py
'''
#############################################################################################################################

from problems_1 import helper

def bank():
    test_hello()
    test_hi()
    test_greatt()

def test_hello():
    assert helper("hello") == "$0"
def test_hi():
    assert helper("hi") == "$20"
def test_greatt():
    assert helper("greatt") == "$100"


     
#############################################################################################################################
'''
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid 
still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only 
called if the value of __name__ is "__main__":
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of 
is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
pytest test_plates.py
'''
#############################################################################################################################

from problems_2 import is_valid, num_check, check
def plates():
    test_check()
    test_numcheck()
    test_punctuation()
    test_character_limit()

def test_check():
    assert check(['s','b','0','1']) == False
    assert check(['S','2','0']) != False

def test_punctuation():
    assert is_valid("BP,40") == False
    assert is_valid("Bp40") != False

def test_character_limit():
    assert is_valid("aaaaaaa") == False
    assert is_valid("aa") != False
    assert is_valid("aaaa") != False
    assert is_valid("a") == False
    assert is_valid("aaaaaa") != False

def test_numcheck():
    assert num_check("pl50cc") == False
    assert num_check("Cs50") != False


#############################################################################################################################
'''
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage 
rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert
should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and 
gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
pytest test_fuel.py
'''
#############################################################################################################################

from problems_3 import fuel,str_split

def test_fuel():
    test_split()

def test_split():
    assert str_split("5/10") == ("5", "10")
    