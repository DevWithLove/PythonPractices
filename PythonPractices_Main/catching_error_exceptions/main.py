# try: #something that might cause an exception
#     file = open("a_file_not_exis.txt")
# except: #do this if there was ans exception
#     print("has exception")
# else: #do this if there were no exceptions
#     print("no exception")
# finally: #do this no matter what happens
#     print("finally after try")

# File not found
try:
    file = open("a_file.txt")
    dict = {"key": "value"}
    #print(dict["ddsts"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed.")

# Raise Error
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)

