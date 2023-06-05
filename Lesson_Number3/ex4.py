"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

# Solution
timpul_1 = int(input())
timpul_2 = int(input())
timpul_3 = int(input())
average_time = (timpul_1 + timpul_2 + timpul_3)/3
print('Timpul mediu este: ' + str(average_time)+str(' secunde'))
