#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################
def complemento(f):
	if f.label=="-":
		return f.right
	elif f.label==None:
		p=Tree("-",None,f)
		return p
	else:
		return "No es una formula"
def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
	aux=[inorder(x) for x in l]
	for i in l:
		if inoder(complemento(i)) in aux:
			return True
	return False

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
	if f.right==None:
		return True
	elif f.label="-":
		if f.right.right==None:
			return True
	else:
		return False

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	for i in l:
		if es_literal(i)==False:
			return False
	return True
def clasificacion(f):
	if f.label=="-":
		if f.right.label=="-":
			return "1ALFA"
		elif f.right.label=="O":
			return "3ALFA"
		elif f.right.label==">":
			return "4ALFA"
		elif f.right.label=="Y":
			return "1BETA"
	elif f.label=="Y":
		return "2ALFA"
	elif f.label=="O":
		return "2BETA"
	elif f.label==">":
		return "3BETA"

def clasifica_y_extiende(f):
	listaHojas.remove([f])
	if clasificacion(f)=="1ALFA":
		t=[f.right]
		listaHojas.append(t)
	elif clasificacion(f)=="2ALFA":
		t=[f.left,f.right]
		listaHojas.append(t)
	elif clasificacion(f)=="3ALFA":
		t=[Tree("-",None,f.left),Tree("-",None,f.right)]
		listaHojas.append(t)
	elif clasificacion(f)=="4ALFA":
		t=[f.left,Tree("-",None,f.right)
		listaHojas.append(t)
	elif clasificacion(f)=="1BETA":
		   t=[]
	elif clasificacion(f)=="2BETA":
		   t=[]
	elif clasificacion(f)=="3BETA":
		   t=[]
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
