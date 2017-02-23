from sys import argv

# sets the arguments for argv
script, filename = argv

# opens the txt file
txt = open(filename)

# prints the file name
print "Here's your file %r:" % filename
# prints the txt file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# it's important to close the files you have opened since it will 
# be kept open FOREVER (not really)s
txt.close()
txt_again.close()
