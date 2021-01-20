import csv

class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = int(grade)

    def printAll(self):
        print(self.first_name, self.last_name, self.grade)

def partition(arr, low, high): # using Lomuto scheme
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j].grade < pivot.grade:
            i += 1
            arr[j], arr[i] = arr[i], arr[j] # swap
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def qsort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        qsort(arr, low, pi-1)
        qsort(arr, pi+1, high)

f = open("unsorted.txt", 'r')
reader = csv.reader(f)
students = []
for row in reader:
    student = Student(row[0], row[1], row[2])
    students.append(student)

qsort(students, 0, len(students)-1)

writefile = open("sorted.txt", 'w')
csvwriter = csv.writer(writefile, delimiter=',')
for student in students:
    csvwriter.writerow([student.first_name, student.last_name, student.grade])

# for student in students:
#     student.printAll()



