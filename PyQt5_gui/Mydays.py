from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()

print("Today date and time is: " + datetime.toString((Qt.ISODate)))

print("Adding 12 days to the date: {0}".format(datetime.addDays(12).toString(Qt.ISODate)))
print("Subtracting 25 days from date: {0}".format(datetime.addDays(-25).toString(Qt.ISODate)))

## CAn add seconds,

.addSecs(50)
.addMonths(3)
.addYears(2)
datetime.ad
