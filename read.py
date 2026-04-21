with open("diary.txt", "r") as file:
    content = file.read()
    print(content)


with open("diary.txt", "r") as file:
#                       "r" = read mode
    content = file.read()  # file ka saara content uthao
    print(content)         # screen pe dikha do