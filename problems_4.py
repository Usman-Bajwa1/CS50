#############################################################################################################################
'''
Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby 
you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally support aliases, 
whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.
See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.
In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version
of that str, converting any codes (or aliases) therein to their corresponding emoji.
'''
#############################################################################################################################





#############################################################################################################################
'''
Among the fonts supported by FIGlet are those at figlet.org/examples.html.
FIGlet has since been ported to Python as a module called pyfiglet.
In a file called figlet.py, implement a program that:
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and
the second of the two should be the name of the font. Prompts the user for a str of text.Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the 
program should exit via sys.exit with an error message.
'''
#############################################################################################################################



            
#############################################################################################################################
'''
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:
Adieu, adieu, to yieu and yieu and yieu
Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:
Adieu, adieu, to yieu, yieu, and yieu
To be fair, “yieu” isn’t even a word; it just rhymes with “you”!
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. 
Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names
with two commas and one and, and 
 names with 
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
'''

#############################################################################################################################





#############################################################################################################################
'''
I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
'''
#############################################################################################################################

