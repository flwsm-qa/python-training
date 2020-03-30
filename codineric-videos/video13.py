#Funciones 2

 def chance_var(b):
     b=5
     print(b)

a=[20]


def argumentos(*patitos):
	print(patitos)

def kwargumentos(**kwpatitos):
	print(kwpatitos)

op = {
	"suma": suma,
	"resta": res,
	"mul": mul,
	"div": div,
}

print(op["div"](12,3))

def change_var(v, l=[]):
	l.append(v)
	return l

change_var(2)
change_var(5)
change_var(6)
lst_2 = change_var(8)
print(lst_2) 