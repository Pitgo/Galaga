stud_mark = {"Hepsiba": 100, "Mabel": 86}
stud_1 = input("Enter the name of student 1 from the team: ")
stud_2 = input("Enter the name of student 2 from the team: ")

try:
    print(f'The total of the team is: {stud_mark[stud_1] + stud_mark[stud_2]}')
except:
    print("1 or more students not found in the dictionary")
