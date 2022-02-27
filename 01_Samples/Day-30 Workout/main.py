# FileNotFoundError
# with open("no_file.txt") as file:
#     file.read()

# key error
# my_dict={"name": "Ranga", "age": 43}
# print(my_dict["address"])

# IndexError
# names = ["Kokila", "Rani", "muthu"]
# print(names[4])

# typerror
# s = "Ranga"
# print(s + 23)

# try:
#     s = "Ranga"
#     print(s + 2)
# except TypeError as e:
#    print(e)
# else:
#     print("Hurray")
# finally:
#     # raise an exception
#     raise KeyError
#     # print("Relaxed")

#raise our exception
name = input("Enter your name: ")
if len(name) == 0:
    raise ValueError("Name not found")
print(name)