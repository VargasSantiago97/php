from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader



import sqlite3
from sqlite3 import Error

def sql_connection():
	try:
		con = sqlite3.connect("/home/vargas/Escritorio/01-07-20/30-06-20/librerias/database/iltanohacienda.db")
		return con
	except Error:
		messagebox.showerror("ERROR", "Error conectando a la base de datos")
def actualizar_db(con, tabla, condiciones):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT * FROM " + str(tabla) + condiciones)
	rows = cursorObj.fetchall()

	return rows


def saludo(request): #Primera vista
	return HttpResponse("<h1>Holis</h1>")

def despedida(request): #Segunda vista
	return HttpResponse("<h1>Chausis</h1>")


def dameFecha(request): #Segunda vista
	fecha_actual = datetime.datetime.now()

	#<META HTTP-EQUIV="REFRESH" CONTENT="1">
	documento = """
	<html>
	<body>
	<h1>
	Fecha y hora actual %s
	</h1>
	</body>
	</html>
	""" % fecha_actual

	return HttpResponse(documento)

def calculaEdad(request, edad, agno):

	edadActu = edad
	periodo = int(agno) - 2020
	edadFutura = edadActu + periodo

	documento = """
	<html>
	<body>
	<h1>
	En el año %s tendrás %s años
	</h1>
	</body>
	</html>
	""" % (agno, edadFutura)

	return HttpResponse(documento)


def mostrarPlantilla(request):
	documento = open("Proyecto1/plantillas/plantilla.html", "r")

	plt = Template(documento.read())
	documento.close()
	ctx = Context()
	docRender = plt.render(ctx)

	return HttpResponse(docRender)


def mostrarPlantilla2(request):
	documento = open("Proyecto1/plantillas/plantilla.html", "r")

	plt = Template(documento.read())
	documento.close()
	ctx = Context({"nombre_persona" : "Juan"})
	docRender = plt.render(ctx)

	return HttpResponse(docRender)

def mostrarProductores(request):

	docEnviar = """
	<html>
		<head>
			<title>Productores</title>
		</head>
	<body>
		<h1>
			Listado de Productores
		</h1>
	"""

	con = sql_connection()
	condiciones = " WHERE estado = 'activo'"
	rows = actualizar_db(con, "productores", condiciones)

	for row in rows:
		docEnviar = docEnviar + """
		<a href="http://127.0.0.1:8000/mostrarProductor/%s">
			<h3>%s</h3>
		</a>
		<p>Razon Social: %s<br>Cuit: %s</p>
		<hr>
		<br>
		""" % (str(row[0]), str(row[1]), str(row[2]), str(row[3]))

	docEnviar = docEnviar + """
	</body>
	</html>
	"""

	return HttpResponse(docEnviar)

def mostrarProductor(request, idd):

	con = sql_connection()
	condiciones = " WHERE id = " + str(idd)
	rows = actualizar_db(con, "productores", condiciones)

	docEnviar = """
	<html>
		<head>
			<title>%s</title>
		</head>
	<body>
		<h1 style="text-align: center;">
			%s
		</h1>
	</body>
	</html>
	""" % (str(rows[0][1]), str(rows[0][2]))


	return HttpResponse(docEnviar)

def htmlCondicionalesNO(request):
	documento = open("Proyecto1/plantillas/plantilla2.html", "r")

	lista = ["val1", "val2", "val3"]
	for i in range(0, 10):
		lista.append("val" + str(i+4))

	plt = Template(documento.read())
	documento.close()
	ctx = Context({"nombre_persona" : "Juan", "lista":lista})
	docRender = plt.render(ctx)

	return HttpResponse(docRender)


def htmlCondicionales(request):
	doc_externo = loader.get_template("plantilla2.html")

	lista = ["val1", "val2", "val3"]
	for i in range(0, 7):
		lista.append("val" + str(i+4))


	docRender = doc_externo.render({"nombre_persona" : "Juan", "lista":lista})

	return HttpResponse(docRender)



def CursoC(request):
	doc_externo = loader.get_template("CursoC.html")

	docRender = doc_externo.render({"nombre_persona" : "Juan"})

	return HttpResponse(docRender)