from PyQt5.QtCore import QDateTime, QDate, QTime, Qt

# both date and time
datetime = QDateTime.currentDateTime()
print(datetime.toString())
print(datetime.toString(Qt.ISODate))    # ISO format
print(datetime.toString(Qt.DefaultLocaleLongDate))


# Only date
date = QDate.currentDate()
print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))

# Only time
time = QTime.currentTime()
print(time.toString())
print(time.toString(Qt.ISODate))
print(time.toString(Qt.DefaultLocaleLongDate))

