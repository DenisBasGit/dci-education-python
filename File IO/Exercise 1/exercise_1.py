# Reading mode is default, so it’s not necessary to specify file opening mode
with open('exercise_1.txt') as f:
    # will print whole text
    print(f.read())
    # will not print anything
    print(f.read())

