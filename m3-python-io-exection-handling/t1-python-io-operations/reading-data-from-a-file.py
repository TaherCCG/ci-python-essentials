# Reading Data From a File

"""
The most uncomplicated persistent storage is a text file. You can save lines of text in the file then use python io to open the file and 
read the contents. There are several methods to do this. You can use readlines() which reads all the lines into a list, readline() which 
reads one line at a time, read() which reads the entire file or seek() which moves to a particular point in a file.

It’s important to understand that when you open a file, you are reading or writing to a particular position within the file. If you use 
readline to read a line, your location within the file is advanced by a line. The next time you read a line, the line will be read from 
the end of the last line. It’s also important to understand that files don’t have lines. A file is just one long sequence of bytes 
(the computer’s way to store characters), but when Python sees a line separator such as ‘\n’, it interprets that as marking the break 
between two lines.

reading file
In the runnable example, the code opens the file, reads the lines it contains into a variable called lines. When printed out, we see that 
it's a list of strings. The 'r means that the file is opened as read-only. We can also see that each line contains the newline character
'\n'. This makes sense because the file data.txt contains four separate lines. What is interesting is that the readlines method splits the 
data read from the files at those newline characters, to create a line of strings. Modify the program slightly and use the read method 
instead of readlines. All of the data will be read into a single string, including the newline characters. When the string is printed to 
the console now, it just appears as text, not a list of strings. The newline characters cause the string to be displayed over several lines.
"""

# Runnable Example 1

f = open('data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

"""
A straightforward, practical thing we can do with text files is to count the occurrences of words. Here's a runnable example. It uses two 
standard libraries, re and collections . The re library will allow us to identify the words in the file using regular expressions, and the 
collections library allows us to count occurrences of words. Notice that the entire contents of the file are read into a single string 
called text , and the findall method is then used to parse that string and find words. A full discussion of regular expressions is beyond 
the scope of this lesson; however, the findall method ensures that all occurrences of the pattern are found. The pattern for a word 
is ' \w+ '. The ' \w ' denotes 'not whitespace'. The ' + ' denotes 'one or more'. So, every occurrence of one or more characters that are 
not whitespace will be considered a word. It's not perfect, it may get some false positives, but it's fine for our purposes. The Counter
method of collections will count how many occurrences there are of each word. The most_common method will limit the results to the top 
10 words. When this is printed, we get a list of tuples where each tuple contains a word and a number of occurrences.
"""

# Runnable Example 2

import re
import collections

text = open('book.txt', 'r').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))


