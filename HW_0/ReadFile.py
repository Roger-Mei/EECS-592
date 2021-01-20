import csv

f = open("unsorted.txt", 'r')
reader = csv.reader(f)
first_names = []
last_names = []
grades = []
for row in reader:
    first_names.append(row[0]) # 使用[index]检索一行中的某列
    last_names.append(row[1])
    grades.append(row[2])

print("First name, last name and grade:")
for i in range(len(first_names)):
    print("%s, %s, %s" % (first_names[i], last_names[i], grades[i]))