from PyQt5.QtCore import QDate

date = QDate.currentDate()


# To determine the days in the year or the particular month from the date
d = QDate(2017, 12, 23)
print("Days in a month: {0}:".format(d.daysInMonth()))
print("Days in a year: {0}".format(d.daysInYear()))
