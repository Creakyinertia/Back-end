# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)



# f = open("demofile.txt")
# The code above is the same as:

# f = open("demofile.txt", "rt")

# f = open("demofile.txt", "r")
# print(f.read(5))

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())

# import os
# os.remove("demofile.txt")

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# import os
# os.rmdir("myfolder")

