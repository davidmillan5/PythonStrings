# Introduction
# A string method is called at the end of a string and each one has its own method specific arguments.

# Formating Methods

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

#Splitting String

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)