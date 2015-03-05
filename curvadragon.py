__author__ = 'Palemon Vasquez'
def  curvaDragon(n):
	if (n == 0):
		return []
	else:
		l = curvaDragon(n - 1)
		revdel= invertir(l)
		cambio=[]
		for giro in revdel:
			if giro =='D':
				cambio.append('I')
			else:
				cambio.append('D')
	return l + ['I'] + cambio

def invertir(l):
	lista = []
	for e in l:
		lista = [e] + lista
	return lista

def salida(l):
	c=''
	for e in l:
		c = c+ e
	return c

n = raw_input("Dame el orden de fractal: ")
l = curvaDragon(int(n))
print("Resultado de orden = "+str(n)+":\n\n" + "\t"+str(salida(l))+"\n")


