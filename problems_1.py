#############################################################################################################################
'''
In deep.py, implement a program that prompts the user for the answer to the Great 
Question of Life, the Universe and Everything, outputting Yes if the user inputs
42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''
#############################################################################################################################
def deep():
    Question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")
    Ans = "Yes" if Question.lower() == '42' or Question.lower() == 'forty-two' or Question.lower() == 'forty two' else 'No'
    print(Ans)
deep()


#############################################################################################################################
'''
In deep.py, implement a program that prompts the user for the answer to the Great
Question of Life, the Universe and Everything, outputting Yes if the user inputs 
42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''
#############################################################################################################################


#############################################################################################################################
'''
Even though Windows and macOS sometimes hide them, most files have file extensions,
a suffix that starts with a period (.) at the end of their name. For instance, 
file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg.
When you double-click on a file to open it, your computer uses its file extension 
to determine which program to launch.
Web browsers, by contrast, rely on media types, formerly known as MIME types, 
to determine how to display files that live on the web. When you download a file 
from a web server, that server sends an HTTP header, along with the file itself, 
indicating the file’s media type. For instance, the media type for a GIF is 
image/gif, and the media type for a JPEG is image/jpeg. To determine the media 
type for a file, a web server typically looks at the file’s extension, mapping one 
to the other.
See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output 
application/octet-stream instead, which is a common default.
'''
#############################################################################################################################


#############################################################################################################################
'''
Python already supports math, whereby you can write code to add, subtract, 
multiply, or divide values and even variables. But let’s write a program that 
enables users to do math, even without knowing Python.
In a file called interpreter.py, implement a program that prompts the user for 
an arithmetic expression and then calculates and outputs the result as a 
floating-point value formatted to one decimal place. Assume that the user’s 
input will be formatted as x y z, with one space between x and y and one space 
between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. 
Assume that, if y is /, then z will not be 0.
Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
'''
#############################################################################################################################


#############################################################################################################################
'''

'''
#############################################################################################################################
