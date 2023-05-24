# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#          temperatures.append(int(row[1]))
#
# print(temperatures)


# refer to https://pandas.pydata.org/docs/  https://pandas.pydata.org/docs/reference/index.html
import pandas
data = pandas.read_csv("weather_data.csv")
#print(type(data)) #Table is DataFrame
#print(type(data["day"])) #Column is Series

print(data)

# to dict
data_dict = data.to_dict()
print(data_dict)

# serial to list
temp_list = data.temp.to_list() # or data["temp"].to_list()
print(temp_list)
average = data["temp"].mean()
print(average)
max_value = data["temp"].max()
print(max_value)

# get data in row
row = data[data.day == "Monday"]
print(row)
print("=======")
monday_condition = row.condition
print(monday_condition)
print("========")

row_with_max_temp = data[data.temp == data.temp.max()]
print(row_with_max_temp)

# Create data frame from scratch
students_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(students_dict)
print(student_data)
student_data.to_csv("students.csv")


