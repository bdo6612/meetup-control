

dict_tt = {
   1 : '14:30',
   2 : '15:30',
   3 : '16:30'
}
class Teacher:
    def __init__(self, timetable, name):
       self.timetable = [] ## 0 - to be occupied, 1- not avalible, <string> - occupied
       for i in enumerate(dict_tt):
          if i + 1 in timetable:
             self.timetable.append(1)

       self.name = name
       self.occupied = []


   def occupation_list(self):
print("d")



nauczyciel1 = Teacher([1,3], imie1)
