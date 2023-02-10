my_file = open('./files.txt')
text = my_file.read()
print(text)
my_file.close()

assert my_file.closed
