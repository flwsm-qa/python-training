 #archivos, actualida. Json

import json

with open("persona.json") as fi:
	persona = json.loads(fi.read())

mica = {
	'nombre': "Mica",
	'edad': 25,
	'hobbies': [
		"series",
		"milanesa",
		"fotos"
	],
	'hijos': None
}

with open("persona_mica.json", "w") as fo:
 	json.dump(mica, fo)

