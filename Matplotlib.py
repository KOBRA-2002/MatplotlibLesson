# -*- coding: cp1251 -*-

import matplotlib.pyplot as plt
import numpy as np
import string

data1 = {simvol:0 for simvol in string.ascii_uppercase} # Here: servivor passengers (key - first simvol of name, value - number servivor passengers)
data2 = {simvol:0 for simvol in string.ascii_uppercase} # Here: non servivor passengers

with open("tested.csv") as f:
    lines = f.readlines()
    for line in lines:
        params = line.split(',')
        name = params[3]
        first_simvol = (name[1]).upper()
        isSurvived = params[1]
        if isSurvived == '1':
            data1[first_simvol] += 1
            print('survivor')
        else:
            data2[first_simvol] += 1
            print('non survivor')
        

x = list(data1.keys())
y1 = [i for i in data1.values()]

fig, ax = plt.subplots()

color_rectangle = np.random.rand(7,4)
ax.bar(x, y1, color = color_rectangle, width = 0.5)

x = list(data2.keys())
y2 = [i for i in data2.values()]

color_rectangle[3] = 0.5
ax.bar(x, y2, color = color_rectangle, width=1)
ax.set_title("Transparent columns - survivors , Opaque columns - non survivors")

plt.show()

