#Strings

favorite_word = "Resilience"
print(favorite_word)

#They are all lists!

my_name = "David"
first_initial = my_name[0]
print(first_initial)

#Cut Me a Slice of Strings
#Syntax string[first_index:last_index]

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

print(new_account)
print(temp_password)

#Concatenating Strings

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)