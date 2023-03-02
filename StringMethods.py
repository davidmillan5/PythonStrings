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

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

#Joining Strings

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)


#.join
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# .strip()
# Stripping a string removes all whitespace characters from the beginning and end.
# You can also use .strip() with a character argument, which will strip that character from either end of the string.


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  line_strip = line.strip()
  love_maybe_lines_stripped.append(line_strip)

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

# Replace .replace()
# Replace takes two arguments and replaces all instances of the first argument in a string with the second argument.
# string_name.replace(substring_being_replaced, new_substring)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

print(toomer_bio)
print(toomer_bio_fixed)


# .find()
# .find() takes a string as an argument and searching the string it was run on for that string.
# It then returns the first index value where that string is located.

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)


# .format()
# .format() takes variables as an argument and includes them in the string that it is run on.
# You include {} marks as placeholders for where those variables will be imported.

#Now you may be asking yourself, I could have written this function using string concatenation instead of .format(),
# why is this method better? The answer is legibility and reusability. It is much easier to picture the end result .format()
# than it is to picture the end result of string concatenation and legibility is everything. You can also reuse the same base
# string with different variables, allowing you to cut down on unnecessary, hard to interpret code.

