from PyQt5.QtCore import Qt, QDateTime

datetime = QDateTime.currentDateTime()

print("Local date and Time is: " + datetime.toString(Qt.DefaultLocaleLongDate))
print("Universal date and time is : " + datetime.toUTC().toString())

print("The offset From Utc is {0}: seconds".format(datetime.offsetFromUtc()))