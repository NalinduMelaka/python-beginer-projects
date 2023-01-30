story = """
Hi, my name is {}.
I am {} years old.
I live in {}. It is a very beautiful place.
"""

name = input("Enter your name ")
age = input("Enter your age ")
place = input("Where are you living? ")

print(story.format(name, age , place))