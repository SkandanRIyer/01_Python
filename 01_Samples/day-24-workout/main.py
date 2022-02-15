# myfile = open("my_file.txt")
# contents = myfile.read()
# print(contents)
# myfile.close()
#
# with open("my_file.txt") as myfile:
#     lines = myfile.read()
#     print(lines)

# with open("my_file.txt", "a") as myfile:
#     myfile.write("I am a devotee of Shiva!!!!!")

# myfile = open("C:\\Users\\Rajesh Ranganathan\\OneDrive\\Desktop\\my_file.txt")
# myfile = open("/Users/Rajesh Ranganathan/OneDrive/Desktop/my_file.txt")
myfile = open("..\\..\\..\\..\\..\\..\\..\\..\\Users\\Rajesh Ranganathan\\OneDrive\\Desktop\\my_file.txt")
print(myfile.read())

