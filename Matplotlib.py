# -*- coding: cp1251 -*-

# Выполнили: Кобзарев Данил, Алексеев Александр

import matplotlib.pyplot as plt
import numpy as np
import string

data1 = {simvol:0 for simvol in string.ascii_uppercase} # Âûæèâøèå
data2 = {simvol:0 for simvol in string.ascii_uppercase} # Ïîãèáøèå
print(data1)

with open("tested.csv") as f:
    lines = f.readlines()
    for line in lines:
        params = line.split(',')
        name = params[3]
        first_simvol = (name[1]).upper()
        isSurvived = params[1]
        if isSurvived == '1':
            data1[first_simvol] += 1
            print('Âûæèâøèé')
        else:
            data2[first_simvol] += 1
            print('Ïîãèáøèé')
        

x = list(data1.keys())
y1 = [i for i in data1.values()]

fig, ax = plt.subplots()

color_rectangle = np.random.rand(7,4)
ax.bar(x, y1, color = color_rectangle, width = 0.5)

x = list(data2.keys())
y2 = [i for i in data2.values()]

color_rectangle[3] = 0.5
ax.bar(x, y2, color = color_rectangle, width=1)
ax.set_title("Ïðîçðà÷íûå - ïîãèáøèå, íåïðîçðàí÷íûå - âûæèâøèå")

plt.show()

