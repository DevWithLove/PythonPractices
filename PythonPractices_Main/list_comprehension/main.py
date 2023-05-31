# sequences : list , range, string, tuple
import random

# numbers = range(1,5)
# double_numbers = [n*2 for n in numbers]
# print(double_numbers)

numbers = [1,1,2,3,5,8,13,21,34,55]
print(numbers)
# each number squared
squared = [n**2 for n in numbers]
print(squared)

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# find common numbers
num1 = [1,2,3,4,5,6,7,34,23,12]
num2 = [4,5,6,7,12]

common = [n for n in num1 if n in num2]
noCommon = [n for n in num1 if n not in num2]
print(common)
print(noCommon)

# Dictionary Comprehension

# Generate dict with student score
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(50,100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# count number of characters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_count = {word:len(word) for word in sentence.split()}
print(words_count)

# convert temp c into temp f
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_f = {day:(c * 9/5 + 32) for (day, c) in weather_c.items()}
print(weather_f)

# import pandas
#
# data_frame = pandas.DataFrame(weather_c)
# print(data_frame)
#
# #loop through data frame
# for (key, value) in data_frame.items():
#     print(value)
#
# #loop through rows of a data frame
# for (index, row) in data_frame.iterrows():
#     print(row.day)