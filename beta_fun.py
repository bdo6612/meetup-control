from itertools import product

def optimal_selector(teachers, hours_avalible):
    all_teacherwtimetable = []
    for teacher in teachers:
        templist = [[teacher, i] for i in teacher.timetable]
        templist.sort()
        all_teacherwtimetable.append(templist)
    combinations = list(product(*templist))
    updatedcombinations = []
    for i in combinations:
        if i not in updatedcombinations:
            updatedcombinations.append(i)














