# Strings

favorite_word = "Resilience"
print(favorite_word)

# They are all lists!

my_name = "David"
first_initial = my_name[0]
print(first_initial)

# Cut Me a Slice of Strings
# Syntax string[first_index:last_index]

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

print(new_account)
print(temp_password)

# Concatenating Strings

first_name = "Julie"
last_name = "Blevins"


def account_generator(first_name, last_name):
    account_name = first_name[:3] + last_name[:3]
    return account_name


new_account = account_generator(first_name, last_name)

print(new_account)

# More and More String Slicing (How Long is that String?)

first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    last_char = first_name[2:] + last_name[4:]
    return last_char


temp_password = password_generator(first_name, last_name)

print(temp_password)


#Negative Indices

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

print(second_to_last)
print(final_word)

#String are Inmmutable

first_name = "Bob"
last_name = "Daily"

fixed_first_name = 'R'+first_name[-2:]

print(fixed_first_name)

#Escape Characters

password = "theycallme\"crazy\"91"
print(password)


#Iterating through Strings

def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter


city_name = "Medellin"

function_getlength = get_length(city_name)

print(function_getlength)

#Strings and Conditionals


def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False


brand = "nintendo"
letter_to_check = "n"

letter_check_function = letter_check(brand, letter_to_check)
print(letter_check_function)


def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common



#Review

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i - 1]
    return password
