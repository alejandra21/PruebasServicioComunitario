# -*- coding: utf-8 -*-

from django import forms

########################################################################################
# Creando Cruces Yacimiento-Yacimiento Form
########################################################################################

OPCIONES_ESTADO = (
	('---', '---'),
	('Amazonas'	, 'Amazonas'),
	('Anzoategui', 'Anzoategui'),
	('Apure', 'Apure'),
	('Aragua', 'Aragua'),
	('Barinas', 'Barinas'),
	('Bolívar', 'Bolívar'),
	('Carabobo', 'Carabobo'),
	('Cojedes', 'Cojedes'),
	('Delta Amacuro', 'Delta Amacuro'),
	('Falcón', 'Falcón'),
	('Guárico', 'Guárico'),
	('Lara', 'Lara'),
	('Mérida', 'Mérida'),
	('Miranda', 'Miranda'),
	('Monagas', 'Monagas'),
	('Nueva Esparta', 'Nueva Esparta'),
	('Portuguesa', 'Portuguesa'),
	('Sucre', 'Sucre'),
	('Tachira', 'Tachira'),
	('Trujillo', 'Trujillo'),
	('Vargas', 'Vargas'),
	('Yaracuy', 'Yaracuy'),
	('Zulia', 'Zulia'),

)

OPCIONES_MANIFESTACIONES = (
	('---', '---'),
	('Pinturas Rupestres','Pinturas Rupestres'),
	('Cerros y Piedras Miticas Naturales','Cerros y Piedras Miticas Naturales'),
	('Amoladores,Cupula,Puntos Acoplados','Amoladores,Cúpula,Puntos Acoplados'),
	('Geoglifo','Geoglifo'),
	('Micropentoglifos','Micropentoglifos'),
	('Monumentos megaliticos','Monumentos megaliticos'),
	('Petroglifos','Petroglifos'),
)

OPCIONES_CONSULTA = (
	('Roca','Roca'),
	('Yacimiento','Yacimiento'),
)

class CrucesYYForm(forms.Form):
	nombre 	= forms.CharField(required=False, max_length=100)
	#codigo 	= forms.CharField(required=False, max_length=20)
	estado = forms.ChoiceField(required=False, choices=OPCIONES_ESTADO)
	#manifestacion = forms.ChoiceField(required=False, choices=OPCIONES_MANIFESTACIONES)
	manifestacion = forms.ChoiceField(required=False,widget=forms.Select,choices=OPCIONES_MANIFESTACIONES)
	#ubicacion = forms.CharField(required=False, max_length=20)
	#carasurcopetrotipo = forms.CharField(required=False, max_length=50)
	#material = forms.CharField(required=False, max_length=50)
	#manifasociadas = forms.CharField(required=False, max_length=50)
	nombre.widget.attrs    =  {'class':'special','placeholder':'Introduzca el nombre'}
	estado.widget.attrs 	= {'class':'chzn-select', 'placeholder':'Seleccione el estado'}

class YacimientoRoca(forms.Form):
	tipoConsulta = forms.ChoiceField(widget=forms.RadioSelect,choices=OPCIONES_CONSULTA)
