def optimal_selector(teachers, hours_avalible):
    czy_znalezione = False
    opcje = []
    while not czy_znalezione:
        for i in hours_avalible:
            for y in teachers:
                if y.timetable[i] == 0:
                    

