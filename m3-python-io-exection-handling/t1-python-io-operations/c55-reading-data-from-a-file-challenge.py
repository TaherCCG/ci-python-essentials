# Reading Data from a File Challenge

def get_content(file):
    f = open(file, 'r')
    lines =f.read()
    f.close()
    return lines

lyrics = get_content('lyrics.txt')

print(lyrics)