import csv
from random import randint,choice
student_list = []
def add_data_file(file_name):
    with open(file_name ,"r", newline="", encoding="utf-8-sig") as f:
        fr = csv.reader(f)
        for data in fr:
            student_list.append(data)
def add_data_list(data,):
        student_list.append(data)

def find_data(ID):
    for data in student_list:
        if int(data[0]) == ID:
            print("Here is",data)
            return
    print("NOTFOUND")


def edit_data(ID,new_data):
    for data in student_list:
        if int(data[0]) == ID:
            student_list[data] = new_data



def view_all():
    for data in student_list:
        print(data)



add_data_file("data.csv")


n = int(input("How many groups do you need? :"))
number_group_list = []
for number in range(n):
    number_group_list.append(len(student_list)//n)
for number in range(n):
    if sum(number_group_list) != len(student_list):
        number_group_list[number] += 1


std = student_list[:]
group_list = []
for num_group in range(n):
    group = []
    for i in range(number_group_list[num_group]):
        student = choice(std)
        if student not in group:
            group.append(student)
            del std[std.index(student)]
    group_list.append(group)
head = []
for group in group_list:
    head.append(choice(group))
def manage():
    print(f"Press 1 for view everyone \nPress 2 for Look at everyone in each group \nPress 3 for view each person in the selected group \nPress 4 for search your group\nPress 5 for number of student each group \nPress 6 for view header \nPress 0 finsihed")
    while True:
        t = int(input("What do you want to press?: "))
        if t == 1:
                for student in student_list:
                    print(student[0],student[1])

        elif t == 2:
            for i in range(len(group_list)):
                print(f"Group {i+1} is")
                for student in group_list[i]:
                    print(student[0],student[1])
        elif t ==3:
            n = int(input("Choose your group:"))
            n -= 1
            for student in group_list[n]:
                print(student[0],student[1])
        elif t == 4:
            n = int(input("What is number of ID: "))
            for group in group_list:
                for student in group:
                    if n == int(student[0]):
                        print(f"{student[1]} is in group {group_list.index(group)+1}")
        elif t ==5:
            for i in range(len(number_group_list)):
                print(f"There are in {number_group_list[i]} people in group {i}")
        elif t ==6:
            for i in range(len(number_group_list)):
                print(f"In group {i+1} has header name {head[i][1]}")
        elif t ==0:
            return
manage()