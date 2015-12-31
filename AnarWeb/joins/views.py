# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from anarapp.models import Estado, Piedra, Yacimiento, ManifestacionYacimiento
from joins.forms import CrucesYYForm


def index(request):
	#Estados = Estado.objects.all()
	forma = CrucesYYForm
	return render(request, 'joins/inicioCruces.html',{'forma':forma})

def cruces(request,cruce_id):
	entrada = "joins/cruce"+str(cruce_id)+".html"
	return render(request,entrada)

def consulta(request):
	# Se realiza la consula:
	estadoElegido = request.GET['estado']
	nombreElegido = request.GET['nombre']
	manifestacionElegido = request.GET['manifestacion']

	#yacimiento=Yacimiento.objects.filter(codigo__iexact="327")
	#yacimiento=Yacimiento.objects.filter(tipos_de_manifestaciones__iexact=manifestacionElegido)
	
	#manifestacion = ManifestacionYacimiento.objects.filter(esGeoglifo=True)
	# manifestacion = ManifestacionYacimiento.objects.filter(esPintura=True)

	# for m in manifestacion:
	# 	yacimiento=Yacimiento.objects.filter(id= m.yacimiento.id)+yacimiento



	if(nombreElegido=="" and estadoElegido=="---"):
		# Se supone que tiene que redireccionar a un .html
		yacimiento=""
		#yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

	elif(nombreElegido!="" and estadoElegido=="---"):

		yacimiento=Yacimiento.objects.filter(nombre__icontains=nombreElegido)

	elif(nombreElegido=="" and estadoElegido!="---"):

		yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

	elif(nombreElegido!="" and estadoElegido!="---"):

		# Conculta encadenada
		yacimiento = Yacimiento.objects.filter(nombre__icontains=nombreElegido,
			estado__nombre__exact=estadoElegido)

	
	return render(request,'joins/salidaConsulta.html', {'yacimiento':yacimiento})
	


# def imagenes1(request):
#     return render(request, 'imagenes/1.html')

# def inicio(request):
#     return render(request, 'inicio.html')

# def quienessomosOrigenytrayectoria(request):
# 	return render(request, 'quienessomos/origenytrayectoria.html')

# def quienessomosAreasdeespecializacion(request):
# 	return render(request, 'quienessomos/areasdeespecializacion.html')

# def quienessomosProyectosactuales(request):
# 	return render(request, 'quienessomos/proyectosactuales.html')

# def quienessomosProfesionalesadjuntos(request):
# 	return render(request, 'quienessomos/profesionalesadjuntos.html')

# def patrimoniorupestreNota(request):
# 	return render(request, 'patrimoniorupestrevenezolano/nota.html')

# def patrimoniorupestreLeydeproteccion(request):
# 	return render(request, 'patrimoniorupestrevenezolano/leydeproteccion.html')

# def patrimoniorupestrePinturasrupestres(request):
# 	return render(request, 'patrimoniorupestrevenezolano/pinturasrupestres.html')

# def patrimoniorupestreGeoglifo(request):
# 	return render(request, 'patrimoniorupestrevenezolano/geoglifo.html')

# def patrimoniorupestrePetroglifo(request):
# 	return render(request, 'patrimoniorupestrevenezolano/petroglifo.html')

# def patrimoniorupestreAmoladores(request):
# 	return render(request, 'patrimoniorupestrevenezolano/amoladores.html')

# def patrimoniorupestreMonumentosmegaliticos(request):
# 	return render(request, 'patrimoniorupestrevenezolano/monumentosmegaliticos.html')

# def patrimoniorupestreMicropetroglifos(request):
# 	return render(request, 'patrimoniorupestrevenezolano/micropetroglifos.html')

# def patrimoniorupestrePiedrasycerrosmiticos(request):
# 	return render(request, 'patrimoniorupestrevenezolano/piedrasycerrosmiticos.html')

# def patrimoniorupestreGeoportal(request):
# 	return render(request, 'patrimoniorupestrevenezolano/geoportal.html')

# def programadeeducacionLasmanifestacionesylaescuela(request):
# 	return render(request, 'programadeeducacion/manifestacionesylaescuela.html')

# def programadeeducacionComunidadAcademica(request):
# 	return render(request, 'programadeeducacion/comunidadacademica.html')

# def programadeeducacionConvenios(request):
# 	return render(request, 'programadeeducacion/convenios.html')

# def programadeeducacionMaterialdidactico(request):
# 	return render(request, 'programadeeducacion/materialdidactico.html')

# def productosyserviciosPublicaciones(request):
# 	return render(request, 'productosyservicios/publicaciones.html')

# def productosyserviciosProductos(request):
# 	return render(request, 'productosyservicios/productos.html')

# def productosyserviciosAsesorias(request):
# 	return render(request, 'productosyservicios/asesorias.html')

# def productosyserviciosVisitasguiadas(request):
# 	return render(request, 'productosyservicios/visitasguiadas.html')

# def contacto(request):
# 	return render(request, 'contacto.html')
