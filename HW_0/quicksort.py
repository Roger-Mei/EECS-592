import csv

f = open("unsorted.txt", 'r')
reader = csv.reader(f)
first_names = []
last_names = []
grades = []
for row in reader:
    first_names.append(row[0]) 
    last_names.append(row[1])
    grades.append(int(row[2]))

class Student: # Define a class to make the sorting job easier later
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

database = [] # Create an empty list to store the class value
for k in range(len(grades)):
    data = Student(first_names[k], last_names[k], grades[k])
    database.append(data)

def quicksort(array): # the first function takes in a list and return the alternative funciton which is easier to implement code
    return _quicksort(array, 0, len(array) - 1)

def _quicksort(array, lo, hi): # Follow the guidance to do recursive quicksort
    if lo < hi:
        p = partition(array, lo, hi)
        _quicksort(array, lo, p - 1)
        _quicksort(array, p + 1, hi)
    return array

def partition(array, lo, hi):
    pivot = array[hi].grade
    list_ = []
    i = lo
    for j in range(lo, hi+1):
        if array[j].grade < pivot:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i = i + 1       
    temp = array[i]
    array[i] = array[hi]
    array[hi] = temp
    return i

a = quicksort(database)
f = open('sorted.txt', 'w').close()
g = open('sorted.txt','w+')
for i in range(len(database)):
    list1 = []
    list1 = [database[i].first_name,database[i].last_name,database[i].grade]
    str1 = ""
    for i in range(len(list1)):
        if i < 2:
            str1 += list1[i]
            str1 += ","
        else:
            str1 += str(list1[i])
            str1 += "\n"
    g.write(str1,)
g.close

