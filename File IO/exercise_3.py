# Open the file in binary mode
with open('exercise_3.txt', 'rb') as f:
    # Read all from it
    bin_text = f.read()

# Open other file to write a normal text
with open('exercise_3_out.txt', 'w') as f:
    # To convert a bytes-like object, use decode()
    f.write(bin_text.decode('utf-8'))
