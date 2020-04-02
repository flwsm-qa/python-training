import random

with open("alumnos.csv") as fi:
	alumnos = []
	ln = fi.readline()
	while ln != "":
		alumnos.append(ln.replace("\n", "").split(",")) #/n es el linebreak, y lo remueve
		ln = fi.readline()

print(alumnos)

alumbos = []

"""
for alumno in alumnos:
	alumno.append(random.randint(1,15))
	alumnos_nuevo.append(alumno)
"""

[alumno.append(str(random.randint(1,15))) for alumno in alumnos]

alumnos_nuevo = [",".join(alumno) for alumno in alumnos]

alumnos_nuevo = "\n".join(alumnos_nuevo)

with open("alumnos_nuevo.csv", "w") as fo:
	fo.write(alumnos_nuevo)