# #positive indexing
# my_string = "Hello, World!"

# # Accessing characters using positive indexing
# first_char = my_string[0]
# second_char = my_string[1]
# last_char = my_string[12]

# print("Positive indexing:")
# print("First character:", first_char)
# print("Second character:", second_char)
# print("Last character:", last_char)


# # Accessing characters using negative indexing
# last_char_negative = my_string[-1]
# second_last_char = my_string[-2]
# first_char_negative = my_string[-13]

# print("\nNegative indexing:")
# print("Last character:", last_char_negative)
# print("Second last character:", second_last_char)
# print("First character:", first_char_negative)

# multiline_text = '''This is a multiline string.
# It spans multiple lines.
# Printed using the print() function.'''
# print(multiline_text)


# # Example: newline (\n)
# print("Hello,\nWorld!")

# # Example: tab (\t)
# print("Name:\tJohn\nAge:\t25")

# # Example: backslash (\\)
# print("This is a backslash: \\")

# # Example: single quote (\')
# print('He said, \'Hello!\'')

# # Example: double quote (\")
# print("She exclaimed, \"Wow!\"")

# # Example: carriage return (\r)
# print("Overwrite\rThis text.")

# # Example: backspace (\b)
# print("Remove\b This")

# # Example: alert (\a)
# print("This is an alert!\a")

# # Example: octal representation (\ooo)
# print("Octal representation: \110")

# # Example: hexadecimal representation (\xhh)
# print("Hexadecimal representation: \x48")


# # We are given the following information about special characters in strings. 
# # Using this knowledge, create a multiline string that includes the following information:
# # Your name and age on the first line.
# # A sentence with a newline character to separate lines.
# # A sentence with a tab character to align text.
# # A sentence containing a backslash character.
# # A sentence containing both single and double quotes.
# # A sentence using the carriage return character to overwrite part of the text.
# # A sentence with a backspace character to remove the preceding character.

# multi_text = '''Name: Gitau Age: 20
# I love python
# Name:\tGitau\nAge:\t20
# Sentence with the backlash character \\
# \'Wow!\' and \"Wow!\"
# Nairobi\r is fun
# Nairobi is fun\bn
# '''

# print(multi_text)

# # reversing
# greeting = 'Hello, World!'
# print(greeting[::-1]) 

# # slicing
# language = 'Python'
# print(language[0:3])

# #skipping characters when slicing 
# language = 'Python'
# ph = language[0:6:3] #0:len_of_str:pattern
# pto = language[0:6:2] #0:len_of_str:pattern
# print(ph) # Ph
# print(pto) # Pto

# sentence = "Searching for a keyword in this sentence."
# index = sentence.find("keyword")
# print(index)


# Given the string below:
# Convert the entire string to uppercase.
# Capitalise the first letter of the string.
# Replace the word "string" with "text."

manipulation_string = "python string manipulation"
upper_case = manipulation_string.upper()
capitalised = manipulation_string.capitalize()
replaced = manipulation_string.replace("string", "text")
print(upper_case)
print(capitalised)
print(replaced)

# Given the following string, replace all occurrences of "apple" with "orange", and print the result.

complex_string = "apple pie, apple juice, apple tart"
replaced_str = complex_string.replace("apple","orange")
print(replaced_str)


# join() takes all items in an iterable and joins them into one string.
 #A string must be specified as the separator
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)