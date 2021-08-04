with open('exercise_2.txt', 'r+') as f:
    # reading all lines into a list
    lines = f.readlines()
    # If you want to easily reverse any list, use this trick
    # Here we use Python’s slices and negative indexes
    lines = lines[::-1]
    # You must use seek to write text right at the beginning
    # Otherwise, you will append text to an end of the file
    f.seek(0)
    f.writelines(lines)

# After the code execution you must observe that the order of lines in file was inverted
