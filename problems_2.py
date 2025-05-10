############################################################################################
'''
In some languages, it’s common to use camel case (otherwise known as “mixed case”)
for variables’ names when those names comprise multiple words, whereby the first 
letter of the first word is lowercase but the first letter of each subsequent word 
is uppercase. For instance, whereas a variable for a user’s name might be called 
name, a variable for a user’s first name might be called firstName, and a variable
for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.
Python, by contrast, recommends snake case, whereby words are instead separated 
by underscores (_), with all letters in lowercase. For instance, those same variables
would be called name, first_name, and preferred_first_name, respectively, in Python.
In a file called camel.py, implement a program that prompts the user for the name 
of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case.
'''
############################################################################################
def camel():
    camel_case = input("Enter the name of variable in camel case:\n")
    snake_case = change(camel_case)
    print(snake_case)

def change(cam = '') -> str:
    letters = []
    for ind,alphabet in enumerate(cam):
        if alphabet.islower():
            letters.append(alphabet)
        else:
            letters.append('_' + alphabet)
    snake = ''.join(letters)
    return snake.lower()


############################################################################################
'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and 
only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
In a file called coke.py, implement a program that prompts the user to insert a 
coin, one at a time, each time informing the user of the amount due. Once the user
has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t 
an accepted denomination.
'''
############################################################################################
def coke():
    amount = 50
    print(f"Amount Due: {amount}")
    while amount > 0:
        payment = int(input("Insert Coin: "))
        amount -= payment 
        if amount > 0:
            print(f"Amount Due: {amount}")
        else:
            print(f"Change Owed: {amount * -1}")
        

############################################################################################
'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr. In a file 
called twttr.py, implement a program that prompts the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted
in uppercase or lowercase.
'''
############################################################################################

def twttr():
    text = input("Input: ")
    out = vow(text)
    print(f"Output: {out}")

def vow(word = '') -> str:
    letters = []
    vowels = ['a','e','i','o','u']
    for alphabet in word:
        if alphabet.lower() not in vowels: 
            letters.append(alphabet)
    return ''.join(letters)


############################################################################################
'''
In Massachusetts, home to Harvard University, it’s possible to request a vanity 
license plate for your car, with your choice of letters and numbers instead of random
ones. Among the requirements, though, are:
- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and 
a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be 
acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and 
then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure your 
program per the below, wherein is_valid returns True if s meets all requirements 
and False if it does not. Assume that s will be a str. You’re welcome to implement
additional functions for is_valid to call (e.g., one function per requirement).
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()
'''
############################################################################################


def plates():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s =''):
  letters = []
  for l in s:
    letters.append(l)
  for l in letters:
    if l.isalpha() or l.isnumeric():                     # No period, space, punctuation
      pass
    else:
      return False
  if len(letters) > 6 or len(letters) < 2:               # Character condition
    return False
  elif letters[0].isnumeric() or letters[1].isnumeric(): # Two letter condition
    return False
  elif check(letters) is False:
    return False
  elif num_check(s) is False:
    return False
  else:
    return True  

def check(s = []):   
  '''
  Check if the first number is zero than returns False
  '''
  for i in range(len(s)):
    if s[i].isnumeric() and s[i] == '0':
      return False 
    elif s[i].isnumeric() and s[i] != '0':
      break
def num_check(s = ''):
  '''
  Check if numerical values are in the middle, so returns false
  '''
  for i in range(len(s)):
    if s[i].isnumeric() and s[i:].isnumeric() is False:
      return False 
    else:
      pass

plates()



############################################################################################
'''
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters 
that “show nutrition information for the 20 most frequently consumed raw fruits 
… in the United States. Retail stores are welcome to download the posters, print, 
display and/or distribute them to consumers in close proximity to the relevant 
foods in the stores.”
In a file called nutrition.py, implement a program that prompts consumers users 
to input a fruit (case-insensitively) and then outputs the number of calories in
one portion of that fruit, per the FDA’s poster for fruits, which is also available
as text. Capitalization aside, assume that users will input fruits exactly as written 
in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
'''
############################################################################################

def nutrition():
    fruit = input("Item: ")

    fruit_calories = {
        "apple":130, 
        "avocado":50,
        "banana":110,
        "cantaloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwifruit":90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine": 50,
        "watermelon":80
    }

    print("Calories:",fruit_calories[fruit.lower()])
        
