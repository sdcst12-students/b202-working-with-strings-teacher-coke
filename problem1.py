"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

x = input("Enter your sentence: ")
y = len(x.split())
print(f"There are {y} words in your sentence")