

dict_tt = {
   0: '14:30',
   1: '15:30',
   2: '16:30'
}
class Teacher:
    def __init__(self, timetable, name):
       self.timetable = [] ## 0 - to be occupied, 1- not avalible, <string> - occupied
       for i in enumerate(dict_tt):
          if i in timetable:
             self.timetable.append(0)
          else :
             self.timetable.append(1)


       self.name = name
    def occupie(self, parent, hour):
      self.timetable[hour] = parent

nauczyciel1 = Teacher([1,2], 'imie1')
nauczyciel2 = Teacher([0, 2], 'imie2')


