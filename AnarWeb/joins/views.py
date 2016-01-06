# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from anarapp.models import Estado, Piedra, Yacimiento, ManifestacionYacimiento,FotografiaYac
from joins.forms import CrucesYYForm,YacimientoRoca


def index(request):
	#Estados = Estado.objects.all()
	forma = YacimientoRoca
	return render(request, 'joins/inicio.html',{'forma':forma})

def seleccionTipoConsulta(request):
	#Estados = Estado.objects.all()
	forma = CrucesYYForm
	seleccionElegida = request.GET['tipoConsulta']

	if(seleccionElegida=="Yacimiento"):

		return render(request, 'joins/inicioCruces.html',{'forma':forma})

	else:
		pass

def cruces(request,cruce_id):
	entrada = "joins/cruce"+str(cruce_id)+".html"
	return render(request,entrada)

def consultaYacimiento(request):
	# Se realiza la consula:
	estadoElegido = request.GET['estado']
	nombreElegido = request.GET['nombre']
	manifestacionElegida = request.GET['manifestacion']

	#yacimiento=Yacimiento.objects.filter(codigo__iexact="327")
	#yacimiento=Yacimiento.objects.filter(tipos_de_manifestaciones__iexact=manifestacionElegida)
	
	
	#yacimiento=""
	#manifestacion1 = ManifestacionYacimiento.objects.filter(esPintura=True)

	#manifestacion = ManifestacionYacimiento.objects.filter(yacimiento__nombre__icontains='indio')
	#manifestacion = ManifestacionYacimiento.objects.filter(yacimiento__estado__nombre='Carabobo')
	#yacimiento1=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)


	#manifestacion = manifestacion1.objects.filter(yacimiento=F('yacimiento1') )


	#for m in manifestacion:
	#yacimiento=Yacimiento.objects.filter(id = manifestacion.yacimiento.id)
	forma = CrucesYYForm
	yacimiento=""
	manifestacion=""
	if(manifestacionElegida!="---"):
	 	
	 	# Se seleccionan las manifestaciones correspondientes
		if(manifestacionElegida=="Pinturas Rupestres"):
			manifestacion = ManifestacionYacimiento.objects.filter(esPintura=True)

		elif(manifestacionElegida=="Cerros y Piedras Miticas Naturales"):

			manifestacion = ManifestacionYacimiento.objects.filter(
				Q(esPiedraMiticaNatural=True)| Q(esCerroMiticoNatural=True))
			
		elif(manifestacionElegida=='Amoladores,Cupula,Puntos Acoplados'):
			manifestacion = ManifestacionYacimiento.objects.filter(
				Q(esAmolador=True)|Q(esCupulas=True)|Q(esPuntosAcoplados=True) )
			
		elif(manifestacionElegida=="Geoglifo"):
			manifestacion = ManifestacionYacimiento.objects.filter(esGeoglifo=True)

		elif(manifestacionElegida=="Micropentoglifos"):
			# Hay que agregar este atributo en el modelo de datos
			manifestacion = \
			ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)

		elif(manifestacionElegida=="Monumentos megaliticos"):
			manifestacion = \
			ManifestacionYacimiento.objects.filter(esMonumentosMegaliticos=True)

		elif(manifestacionElegida=="Petroglifos"):
			manifestacion = ManifestacionYacimiento.objects.filter(esPetroglifo=True)

		########################################################################	

		if(nombreElegido=="" and estadoElegido=="---"):
			pass

		elif(nombreElegido!="" and estadoElegido=="---"):

			manifestacion =\
			 manifestacion.filter(yacimiento__nombre__icontains=nombreElegido)

		elif(nombreElegido=="" and estadoElegido!="---"):

			manifestacion=\
			manifestacion.filter(yacimiento__estado__nombre=estadoElegido)

		elif(nombreElegido!="" and estadoElegido!="---"):

			# Conculta encadenada
			manifestacion = \
			manifestacion.filter(yacimiento__nombre__icontains=nombreElegido,
				yacimiento__estado__nombre=estadoElegido)

		#Foto = FotografiaYac.objects.filter(yacimiento__id__in = manifestacion.values_list('yacimiento'))
		#Foto = FotografiaYac.objects.filter(yacimiento__nombre__icontains="elefante")
		#Foto = FotografiaYac.objects.all()

	else:

		if(nombreElegido=="" and estadoElegido=="---"):
			# Se supone que tiene que redireccionar a un .html
			return render(request, 'joins/inicioCruces.html',{'forma':forma})
			#yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

		elif(nombreElegido!="" and estadoElegido=="---"):

			yacimiento=Yacimiento.objects.filter(nombre__icontains=nombreElegido)

		elif(nombreElegido=="" and estadoElegido!="---"):

			yacimiento=Yacimiento.objects.filter(estado__nombre__exact=estadoElegido)

		elif(nombreElegido!="" and estadoElegido!="---"):

			# Conculta encadenada
			yacimiento = Yacimiento.objects.filter(nombre__icontains=nombreElegido,
				estado__nombre__exact=estadoElegido)

	

	return render(request,'joins/salidaConsulta.html', 
		{'yacimiento':yacimiento,
		'manifestacion':manifestacion,'forma':forma,
		'estadoElegido':estadoElegido,
		'manifestacionElegida':manifestacionElegida,
		'nombreElegido':nombreElegido})


	


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
