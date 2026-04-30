from pyscript import display, document
import numpy as np

import matplotlib.pyplot as plt
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close


def checkAttendance(e):
    plt.clf()
    plt.show()
    plt.title('Attendance Checker')
    plt.xlabel('Days')
    plt.ylabel('Absences')
    Monday = float(document.getElementById('monday').value)
    Tuesday = float(document.getElementById('tuesday').value)
    Wednesday = float(document.getElementById('wednesday').value)
    Thursday = float(document.getElementById('thursday').value)
    Friday = float(document.getElementById('friday').value)
    days = np.array([Monday, Tuesday, Wednesday, Thursday, Friday])
    numberAbsences = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
    attendance_graph = plt.plot(numberAbsences, days)