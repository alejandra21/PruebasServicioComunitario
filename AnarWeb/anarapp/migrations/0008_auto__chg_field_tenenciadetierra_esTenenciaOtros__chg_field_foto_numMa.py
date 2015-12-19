# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TenenciaDeTierra.esTenenciaOtros'
        db.alter_column('anarapp_tenenciadetierra', 'esTenenciaOtros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.numMarcaNegativo'
        db.alter_column('anarapp_foto', 'numMarcaNegativo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.negativo'
        db.alter_column('anarapp_foto', 'negativo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.institucion'
        db.alter_column('anarapp_foto', 'institucion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.numFoto'
        db.alter_column('anarapp_foto', 'numFoto', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.numReferencia'
        db.alter_column('anarapp_foto', 'numReferencia', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.fotografo'
        db.alter_column('anarapp_foto', 'fotografo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Foto.numRollo'
        db.alter_column('anarapp_foto', 'numRollo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Yacimiento.pais'
        db.alter_column('anarapp_yacimiento', 'pais', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Yacimiento.nombre'
        db.alter_column('anarapp_yacimiento', 'nombre', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Yacimiento.estado'
        db.alter_column('anarapp_yacimiento', 'estado', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Yacimiento.municipio'
        db.alter_column('anarapp_yacimiento', 'municipio', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Piedra.nombreFiguras'
        db.alter_column('anarapp_piedra', 'nombreFiguras', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Piedra.nombre'
        db.alter_column('anarapp_piedra', 'nombre', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Piedra.estado'
        db.alter_column('anarapp_piedra', 'estado', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Piedra.manifiestacionAsociada'
        db.alter_column('anarapp_piedra', 'manifiestacionAsociada', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'SupervisadoPor.nombre'
        db.alter_column('anarapp_supervisadopor', 'nombre', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Observaciones.texto'
        db.alter_column('anarapp_observaciones', 'texto', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FotografiaYac.urlImagen'
        db.alter_column('anarapp_fotografiayac', 'urlImagen', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'LlenadoPor.nombre'
        db.alter_column('anarapp_llenadopor', 'nombre', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FloraYacimiento.flora'
        db.alter_column('anarapp_florayacimiento', 'flora', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Coordenadas.latitud'
        db.alter_column('anarapp_coordenadas', 'latitud', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Coordenadas.utmAdicional'
        db.alter_column('anarapp_coordenadas', 'utmAdicional', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Coordenadas.longitud'
        db.alter_column('anarapp_coordenadas', 'longitud', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'LocalidadYacimiento.nombrePoblado'
        db.alter_column('anarapp_localidadyacimiento', 'nombrePoblado', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'LocalidadYacimiento.nombreNoPoblado'
        db.alter_column('anarapp_localidadyacimiento', 'nombreNoPoblado', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.autor'
        db.alter_column('anarapp_cronologiatentativa', 'autor', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.fecha'
        db.alter_column('anarapp_cronologiatentativa', 'fecha', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.direccion'
        db.alter_column('anarapp_cronologiatentativa', 'direccion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.institucion'
        db.alter_column('anarapp_cronologiatentativa', 'institucion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.facebook'
        db.alter_column('anarapp_cronologiatentativa', 'facebook', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.pais'
        db.alter_column('anarapp_cronologiatentativa', 'pais', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.tecnica'
        db.alter_column('anarapp_cronologiatentativa', 'tecnica', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.mail'
        db.alter_column('anarapp_cronologiatentativa', 'mail', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.telefono'
        db.alter_column('anarapp_cronologiatentativa', 'telefono', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.twitter'
        db.alter_column('anarapp_cronologiatentativa', 'twitter', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CronologiaTentativa.bibliografia'
        db.alter_column('anarapp_cronologiatentativa', 'bibliografia', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoBateas.ancho'
        db.alter_column('anarapp_caracsurcobateas', 'ancho', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoBateas.profundidad'
        db.alter_column('anarapp_caracsurcobateas', 'profundidad', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoBateas.diametro'
        db.alter_column('anarapp_caracsurcobateas', 'diametro', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoBateas.largo'
        db.alter_column('anarapp_caracsurcobateas', 'largo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Multimedia.tecnica'
        db.alter_column('anarapp_multimedia', 'tecnica', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ConsiderTemp.otros'
        db.alter_column('anarapp_considertemp', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FotoBibliografia.descripcion'
        db.alter_column('anarapp_fotobibliografia', 'descripcion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoAmoladores.largo'
        db.alter_column('anarapp_caracsurcoamoladores', 'largo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoAmoladores.ancho'
        db.alter_column('anarapp_caracsurcoamoladores', 'ancho', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoAmoladores.diametro'
        db.alter_column('anarapp_caracsurcoamoladores', 'diametro', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Plano.numeroPlano'
        db.alter_column('anarapp_plano', 'numeroPlano', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TecnicaParaPintura.otros'
        db.alter_column('anarapp_tecnicaparapintura', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'NotasYacimiento.notas'
        db.alter_column('anarapp_notasyacimiento', 'notas', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPuntosAcopl.profundidad'
        db.alter_column('anarapp_caracsurcopuntosacopl', 'profundidad', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPuntosAcopl.diametro'
        db.alter_column('anarapp_caracsurcopuntosacopl', 'diametro', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPuntosAcopl.otros'
        db.alter_column('anarapp_caracsurcopuntosacopl', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoMortero.largo'
        db.alter_column('anarapp_caracsurcomortero', 'largo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoMortero.ancho'
        db.alter_column('anarapp_caracsurcomortero', 'ancho', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoCupulas.ancho'
        db.alter_column('anarapp_caracsurcocupulas', 'ancho', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoCupulas.profundidad'
        db.alter_column('anarapp_caracsurcocupulas', 'profundidad', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoCupulas.diametro'
        db.alter_column('anarapp_caracsurcocupulas', 'diametro', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoCupulas.largo'
        db.alter_column('anarapp_caracsurcocupulas', 'largo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoCupulas.otros'
        db.alter_column('anarapp_caracsurcocupulas', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Bibliografia.autor'
        db.alter_column('anarapp_bibliografia', 'autor', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Bibliografia.conDibujo'
        db.alter_column('anarapp_bibliografia', 'conDibujo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Bibliografia.institucion'
        db.alter_column('anarapp_bibliografia', 'institucion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Bibliografia.titulo'
        db.alter_column('anarapp_bibliografia', 'titulo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Bibliografia.codigo'
        db.alter_column('anarapp_bibliografia', 'codigo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaraTrabajada.numero'
        db.alter_column('anarapp_caratrabajada', 'numero', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TecnicaParaPetroglifo.otros'
        db.alter_column('anarapp_tecnicaparapetroglifo', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TipoExposicionYac.observaciones'
        db.alter_column('anarapp_tipoexposicionyac', 'observaciones', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionCeramica'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionCeramica', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionOseo'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionOseo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionMito'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionMito', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionCarbon'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionCarbon', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionCementerio'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionCementerio', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionMonticulo'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionMonticulo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionLitica'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionLitica', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.descripcionConcha'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionConcha', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ManifestacionesAsociadas.otros'
        db.alter_column('anarapp_manifestacionesasociadas', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'OtrosValores.texto'
        db.alter_column('anarapp_otrosvalores', 'texto', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Croquis.urlImagen'
        db.alter_column('anarapp_croquis', 'urlImagen', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracDeLaPintura.anchoDe'
        db.alter_column('anarapp_caracdelapintura', 'anchoDe', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracDeLaPintura.anchoA'
        db.alter_column('anarapp_caracdelapintura', 'anchoA', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracDeLaPintura.anchoDeComp'
        db.alter_column('anarapp_caracdelapintura', 'anchoDeComp', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracDeLaPintura.otros'
        db.alter_column('anarapp_caracdelapintura', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracDeLaPintura.anchoAComp'
        db.alter_column('anarapp_caracdelapintura', 'anchoAComp', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ObtencionInfo.nombre'
        db.alter_column('anarapp_obtencioninfo', 'nombre', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ObtencionInfo.telefono'
        db.alter_column('anarapp_obtencioninfo', 'telefono', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ObtencionInfo.twitter'
        db.alter_column('anarapp_obtencioninfo', 'twitter', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ObtencionInfo.direccion'
        db.alter_column('anarapp_obtencioninfo', 'direccion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ObtencionInfo.telefonoCel'
        db.alter_column('anarapp_obtencioninfo', 'telefonoCel', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ObtencionInfo.nombreFacebook'
        db.alter_column('anarapp_obtencioninfo', 'nombreFacebook', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'OrientacionYacimiento.orientacion'
        db.alter_column('anarapp_orientacionyacimiento', 'orientacion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'OrientacionYacimiento.otros'
        db.alter_column('anarapp_orientacionyacimiento', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EsquemaPorCara.posicion'
        db.alter_column('anarapp_esquemaporcara', 'posicion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EsquemaPorCara.numero'
        db.alter_column('anarapp_esquemaporcara', 'numero', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EsquemaPorCara.textoCara'
        db.alter_column('anarapp_esquemaporcara', 'textoCara', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'ConstitucionYacimiento.otros'
        db.alter_column('anarapp_constitucionyacimiento', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'MaterialYacimiento.tipo'
        db.alter_column('anarapp_materialyacimiento', 'tipo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'MaterialYacimiento.otros'
        db.alter_column('anarapp_materialyacimiento', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TexturaSuelo.mixto'
        db.alter_column('anarapp_texturasuelo', 'mixto', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'HidrologiaYacimiento.distancia'
        db.alter_column('anarapp_hidrologiayacimiento', 'distancia', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'HidrologiaYacimiento.observaciones'
        db.alter_column('anarapp_hidrologiayacimiento', 'observaciones', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'HidrologiaYacimiento.nombre'
        db.alter_column('anarapp_hidrologiayacimiento', 'nombre', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'HidrologiaYacimiento.otros'
        db.alter_column('anarapp_hidrologiayacimiento', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPetroglifo.anchoDe'
        db.alter_column('anarapp_caracsurcopetroglifo', 'anchoDe', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPetroglifo.profundidadA'
        db.alter_column('anarapp_caracsurcopetroglifo', 'profundidadA', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPetroglifo.anchoA'
        db.alter_column('anarapp_caracsurcopetroglifo', 'anchoA', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'CaracSurcoPetroglifo.produndidadDe'
        db.alter_column('anarapp_caracsurcopetroglifo', 'produndidadDe', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FigurasPorTipo.cantidad'
        db.alter_column('anarapp_figurasportipo', 'cantidad', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FigurasPorTipo.numero'
        db.alter_column('anarapp_figurasportipo', 'numero', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FigurasPorTipo.descripcion'
        db.alter_column('anarapp_figurasportipo', 'descripcion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TecnicaParaGeoglifo.tecnicas'
        db.alter_column('anarapp_tecnicaparageoglifo', 'tecnicas', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TratFoto.tratamientoDigital'
        db.alter_column('anarapp_tratfoto', 'tratamientoDigital', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TratFoto.rellenoSurcos'
        db.alter_column('anarapp_tratfoto', 'rellenoSurcos', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TratFoto.otrosTratamientos'
        db.alter_column('anarapp_tratfoto', 'otrosTratamientos', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TratFoto.limpiezaCon'
        db.alter_column('anarapp_tratfoto', 'limpiezaCon', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TratFoto.programaVersion'
        db.alter_column('anarapp_tratfoto', 'programaVersion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Altitud.desarrollo'
        db.alter_column('anarapp_altitud', 'desarrollo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Altitud.desnivel'
        db.alter_column('anarapp_altitud', 'desnivel', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Altitud.texto'
        db.alter_column('anarapp_altitud', 'texto', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Altitud.superficie'
        db.alter_column('anarapp_altitud', 'superficie', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Altitud.altura'
        db.alter_column('anarapp_altitud', 'altura', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'MatAudioVisual.formato'
        db.alter_column('anarapp_mataudiovisual', 'formato', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'MatAudioVisual.imagen'
        db.alter_column('anarapp_mataudiovisual', 'imagen', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'FaunaYacimiento.fauna'
        db.alter_column('anarapp_faunayacimiento', 'fauna', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Indicaciones.direcciones'
        db.alter_column('anarapp_indicaciones', 'direcciones', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Indicaciones.puntoDatum'
        db.alter_column('anarapp_indicaciones', 'puntoDatum', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'RepGrafPiedra.instituto'
        db.alter_column('anarapp_repgrafpiedra', 'instituto', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'RepGrafPiedra.persona'
        db.alter_column('anarapp_repgrafpiedra', 'persona', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TecnicaParaMicroPetro.otros'
        db.alter_column('anarapp_tecnicaparamicropetro', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Video.autor'
        db.alter_column('anarapp_video', 'autor', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Video.formato'
        db.alter_column('anarapp_video', 'formato', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Video.institucion'
        db.alter_column('anarapp_video', 'institucion', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'Video.titulo'
        db.alter_column('anarapp_video', 'titulo', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TecnicaParaMonumentos.tecnicas'
        db.alter_column('anarapp_tecnicaparamonumentos', 'tecnicas', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'TecnicaParaMonumentos.otros'
        db.alter_column('anarapp_tecnicaparamonumentos', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.enterradoPa'
        db.alter_column('anarapp_estadoconseryac', 'enterradoPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.crecimientoVegPa'
        db.alter_column('anarapp_estadoconseryac', 'crecimientoVegPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.otros'
        db.alter_column('anarapp_estadoconseryac', 'otros', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.patinaPa'
        db.alter_column('anarapp_estadoconseryac', 'patinaPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.sumergidoPa'
        db.alter_column('anarapp_estadoconseryac', 'sumergidoPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.especificar'
        db.alter_column('anarapp_estadoconseryac', 'especificar', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.mas'
        db.alter_column('anarapp_estadoconseryac', 'mas', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.observaciones'
        db.alter_column('anarapp_estadoconseryac', 'observaciones', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.erosionPa'
        db.alter_column('anarapp_estadoconseryac', 'erosionPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.perdidoPa'
        db.alter_column('anarapp_estadoconseryac', 'perdidoPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.trasladadoPa'
        db.alter_column('anarapp_estadoconseryac', 'trasladadoPa', self.gf('anarapp.models.CharField')(max_length=65000))

        # Changing field 'EstadoConserYac.destruidoPa'
        db.alter_column('anarapp_estadoconseryac', 'destruidoPa', self.gf('anarapp.models.CharField')(max_length=65000))

    def backwards(self, orm):

        # Changing field 'TenenciaDeTierra.esTenenciaOtros'
        db.alter_column('anarapp_tenenciadetierra', 'esTenenciaOtros', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Foto.numMarcaNegativo'
        db.alter_column('anarapp_foto', 'numMarcaNegativo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Foto.negativo'
        db.alter_column('anarapp_foto', 'negativo', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Foto.institucion'
        db.alter_column('anarapp_foto', 'institucion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Foto.numFoto'
        db.alter_column('anarapp_foto', 'numFoto', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Foto.numReferencia'
        db.alter_column('anarapp_foto', 'numReferencia', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Foto.fotografo'
        db.alter_column('anarapp_foto', 'fotografo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Foto.numRollo'
        db.alter_column('anarapp_foto', 'numRollo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Yacimiento.pais'
        db.alter_column('anarapp_yacimiento', 'pais', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Yacimiento.nombre'
        db.alter_column('anarapp_yacimiento', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Yacimiento.estado'
        db.alter_column('anarapp_yacimiento', 'estado', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Yacimiento.municipio'
        db.alter_column('anarapp_yacimiento', 'municipio', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Piedra.nombreFiguras'
        db.alter_column('anarapp_piedra', 'nombreFiguras', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Piedra.nombre'
        db.alter_column('anarapp_piedra', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Piedra.estado'
        db.alter_column('anarapp_piedra', 'estado', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Piedra.manifiestacionAsociada'
        db.alter_column('anarapp_piedra', 'manifiestacionAsociada', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'SupervisadoPor.nombre'
        db.alter_column('anarapp_supervisadopor', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Observaciones.texto'
        db.alter_column('anarapp_observaciones', 'texto', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'FotografiaYac.urlImagen'
        db.alter_column('anarapp_fotografiayac', 'urlImagen', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'LlenadoPor.nombre'
        db.alter_column('anarapp_llenadopor', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'FloraYacimiento.flora'
        db.alter_column('anarapp_florayacimiento', 'flora', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Coordenadas.latitud'
        db.alter_column('anarapp_coordenadas', 'latitud', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Coordenadas.utmAdicional'
        db.alter_column('anarapp_coordenadas', 'utmAdicional', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Coordenadas.longitud'
        db.alter_column('anarapp_coordenadas', 'longitud', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'LocalidadYacimiento.nombrePoblado'
        db.alter_column('anarapp_localidadyacimiento', 'nombrePoblado', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'LocalidadYacimiento.nombreNoPoblado'
        db.alter_column('anarapp_localidadyacimiento', 'nombreNoPoblado', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'CronologiaTentativa.autor'
        db.alter_column('anarapp_cronologiatentativa', 'autor', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.fecha'
        db.alter_column('anarapp_cronologiatentativa', 'fecha', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.direccion'
        db.alter_column('anarapp_cronologiatentativa', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.institucion'
        db.alter_column('anarapp_cronologiatentativa', 'institucion', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.facebook'
        db.alter_column('anarapp_cronologiatentativa', 'facebook', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.pais'
        db.alter_column('anarapp_cronologiatentativa', 'pais', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.tecnica'
        db.alter_column('anarapp_cronologiatentativa', 'tecnica', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.mail'
        db.alter_column('anarapp_cronologiatentativa', 'mail', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.telefono'
        db.alter_column('anarapp_cronologiatentativa', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.twitter'
        db.alter_column('anarapp_cronologiatentativa', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CronologiaTentativa.bibliografia'
        db.alter_column('anarapp_cronologiatentativa', 'bibliografia', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoBateas.ancho'
        db.alter_column('anarapp_caracsurcobateas', 'ancho', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoBateas.profundidad'
        db.alter_column('anarapp_caracsurcobateas', 'profundidad', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'CaracSurcoBateas.diametro'
        db.alter_column('anarapp_caracsurcobateas', 'diametro', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'CaracSurcoBateas.largo'
        db.alter_column('anarapp_caracsurcobateas', 'largo', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Multimedia.tecnica'
        db.alter_column('anarapp_multimedia', 'tecnica', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'ConsiderTemp.otros'
        db.alter_column('anarapp_considertemp', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'FotoBibliografia.descripcion'
        db.alter_column('anarapp_fotobibliografia', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'CaracSurcoAmoladores.largo'
        db.alter_column('anarapp_caracsurcoamoladores', 'largo', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoAmoladores.ancho'
        db.alter_column('anarapp_caracsurcoamoladores', 'ancho', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoAmoladores.diametro'
        db.alter_column('anarapp_caracsurcoamoladores', 'diametro', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Plano.numeroPlano'
        db.alter_column('anarapp_plano', 'numeroPlano', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'TecnicaParaPintura.otros'
        db.alter_column('anarapp_tecnicaparapintura', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'NotasYacimiento.notas'
        db.alter_column('anarapp_notasyacimiento', 'notas', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'CaracSurcoPuntosAcopl.profundidad'
        db.alter_column('anarapp_caracsurcopuntosacopl', 'profundidad', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'CaracSurcoPuntosAcopl.diametro'
        db.alter_column('anarapp_caracsurcopuntosacopl', 'diametro', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'CaracSurcoPuntosAcopl.otros'
        db.alter_column('anarapp_caracsurcopuntosacopl', 'otros', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'CaracSurcoMortero.largo'
        db.alter_column('anarapp_caracsurcomortero', 'largo', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoMortero.ancho'
        db.alter_column('anarapp_caracsurcomortero', 'ancho', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoCupulas.ancho'
        db.alter_column('anarapp_caracsurcocupulas', 'ancho', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoCupulas.profundidad'
        db.alter_column('anarapp_caracsurcocupulas', 'profundidad', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'CaracSurcoCupulas.diametro'
        db.alter_column('anarapp_caracsurcocupulas', 'diametro', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoCupulas.largo'
        db.alter_column('anarapp_caracsurcocupulas', 'largo', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoCupulas.otros'
        db.alter_column('anarapp_caracsurcocupulas', 'otros', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Bibliografia.autor'
        db.alter_column('anarapp_bibliografia', 'autor', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Bibliografia.conDibujo'
        db.alter_column('anarapp_bibliografia', 'conDibujo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Bibliografia.institucion'
        db.alter_column('anarapp_bibliografia', 'institucion', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Bibliografia.titulo'
        db.alter_column('anarapp_bibliografia', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Bibliografia.codigo'
        db.alter_column('anarapp_bibliografia', 'codigo', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'CaraTrabajada.numero'
        db.alter_column('anarapp_caratrabajada', 'numero', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TecnicaParaPetroglifo.otros'
        db.alter_column('anarapp_tecnicaparapetroglifo', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'TipoExposicionYac.observaciones'
        db.alter_column('anarapp_tipoexposicionyac', 'observaciones', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'ManifestacionesAsociadas.descripcionCeramica'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionCeramica', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionOseo'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionOseo', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionMito'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionMito', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionCarbon'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionCarbon', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionCementerio'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionCementerio', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionMonticulo'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionMonticulo', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionLitica'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionLitica', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.descripcionConcha'
        db.alter_column('anarapp_manifestacionesasociadas', 'descripcionConcha', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'ManifestacionesAsociadas.otros'
        db.alter_column('anarapp_manifestacionesasociadas', 'otros', self.gf('django.db.models.fields.CharField')(max_length=1200))

        # Changing field 'OtrosValores.texto'
        db.alter_column('anarapp_otrosvalores', 'texto', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Croquis.urlImagen'
        db.alter_column('anarapp_croquis', 'urlImagen', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracDeLaPintura.anchoDe'
        db.alter_column('anarapp_caracdelapintura', 'anchoDe', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracDeLaPintura.anchoA'
        db.alter_column('anarapp_caracdelapintura', 'anchoA', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracDeLaPintura.anchoDeComp'
        db.alter_column('anarapp_caracdelapintura', 'anchoDeComp', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracDeLaPintura.otros'
        db.alter_column('anarapp_caracdelapintura', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracDeLaPintura.anchoAComp'
        db.alter_column('anarapp_caracdelapintura', 'anchoAComp', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'ObtencionInfo.nombre'
        db.alter_column('anarapp_obtencioninfo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ObtencionInfo.telefono'
        db.alter_column('anarapp_obtencioninfo', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'ObtencionInfo.twitter'
        db.alter_column('anarapp_obtencioninfo', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'ObtencionInfo.direccion'
        db.alter_column('anarapp_obtencioninfo', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'ObtencionInfo.telefonoCel'
        db.alter_column('anarapp_obtencioninfo', 'telefonoCel', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'ObtencionInfo.nombreFacebook'
        db.alter_column('anarapp_obtencioninfo', 'nombreFacebook', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'OrientacionYacimiento.orientacion'
        db.alter_column('anarapp_orientacionyacimiento', 'orientacion', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'OrientacionYacimiento.otros'
        db.alter_column('anarapp_orientacionyacimiento', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EsquemaPorCara.posicion'
        db.alter_column('anarapp_esquemaporcara', 'posicion', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EsquemaPorCara.numero'
        db.alter_column('anarapp_esquemaporcara', 'numero', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'EsquemaPorCara.textoCara'
        db.alter_column('anarapp_esquemaporcara', 'textoCara', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'ConstitucionYacimiento.otros'
        db.alter_column('anarapp_constitucionyacimiento', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'MaterialYacimiento.tipo'
        db.alter_column('anarapp_materialyacimiento', 'tipo', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'MaterialYacimiento.otros'
        db.alter_column('anarapp_materialyacimiento', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'TexturaSuelo.mixto'
        db.alter_column('anarapp_texturasuelo', 'mixto', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'HidrologiaYacimiento.distancia'
        db.alter_column('anarapp_hidrologiayacimiento', 'distancia', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'HidrologiaYacimiento.observaciones'
        db.alter_column('anarapp_hidrologiayacimiento', 'observaciones', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'HidrologiaYacimiento.nombre'
        db.alter_column('anarapp_hidrologiayacimiento', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'HidrologiaYacimiento.otros'
        db.alter_column('anarapp_hidrologiayacimiento', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoPetroglifo.anchoDe'
        db.alter_column('anarapp_caracsurcopetroglifo', 'anchoDe', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoPetroglifo.profundidadA'
        db.alter_column('anarapp_caracsurcopetroglifo', 'profundidadA', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoPetroglifo.anchoA'
        db.alter_column('anarapp_caracsurcopetroglifo', 'anchoA', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'CaracSurcoPetroglifo.produndidadDe'
        db.alter_column('anarapp_caracsurcopetroglifo', 'produndidadDe', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'FigurasPorTipo.cantidad'
        db.alter_column('anarapp_figurasportipo', 'cantidad', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'FigurasPorTipo.numero'
        db.alter_column('anarapp_figurasportipo', 'numero', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'FigurasPorTipo.descripcion'
        db.alter_column('anarapp_figurasportipo', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'TecnicaParaGeoglifo.tecnicas'
        db.alter_column('anarapp_tecnicaparageoglifo', 'tecnicas', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'TratFoto.tratamientoDigital'
        db.alter_column('anarapp_tratfoto', 'tratamientoDigital', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TratFoto.rellenoSurcos'
        db.alter_column('anarapp_tratfoto', 'rellenoSurcos', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TratFoto.otrosTratamientos'
        db.alter_column('anarapp_tratfoto', 'otrosTratamientos', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'TratFoto.limpiezaCon'
        db.alter_column('anarapp_tratfoto', 'limpiezaCon', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TratFoto.programaVersion'
        db.alter_column('anarapp_tratfoto', 'programaVersion', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Altitud.desarrollo'
        db.alter_column('anarapp_altitud', 'desarrollo', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Altitud.desnivel'
        db.alter_column('anarapp_altitud', 'desnivel', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Altitud.texto'
        db.alter_column('anarapp_altitud', 'texto', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Altitud.superficie'
        db.alter_column('anarapp_altitud', 'superficie', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Altitud.altura'
        db.alter_column('anarapp_altitud', 'altura', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'MatAudioVisual.formato'
        db.alter_column('anarapp_mataudiovisual', 'formato', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'MatAudioVisual.imagen'
        db.alter_column('anarapp_mataudiovisual', 'imagen', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'FaunaYacimiento.fauna'
        db.alter_column('anarapp_faunayacimiento', 'fauna', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Indicaciones.direcciones'
        db.alter_column('anarapp_indicaciones', 'direcciones', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Indicaciones.puntoDatum'
        db.alter_column('anarapp_indicaciones', 'puntoDatum', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'RepGrafPiedra.instituto'
        db.alter_column('anarapp_repgrafpiedra', 'instituto', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'RepGrafPiedra.persona'
        db.alter_column('anarapp_repgrafpiedra', 'persona', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'TecnicaParaMicroPetro.otros'
        db.alter_column('anarapp_tecnicaparamicropetro', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Video.autor'
        db.alter_column('anarapp_video', 'autor', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Video.formato'
        db.alter_column('anarapp_video', 'formato', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Video.institucion'
        db.alter_column('anarapp_video', 'institucion', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Video.titulo'
        db.alter_column('anarapp_video', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'TecnicaParaMonumentos.tecnicas'
        db.alter_column('anarapp_tecnicaparamonumentos', 'tecnicas', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'TecnicaParaMonumentos.otros'
        db.alter_column('anarapp_tecnicaparamonumentos', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.enterradoPa'
        db.alter_column('anarapp_estadoconseryac', 'enterradoPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.crecimientoVegPa'
        db.alter_column('anarapp_estadoconseryac', 'crecimientoVegPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.otros'
        db.alter_column('anarapp_estadoconseryac', 'otros', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.patinaPa'
        db.alter_column('anarapp_estadoconseryac', 'patinaPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.sumergidoPa'
        db.alter_column('anarapp_estadoconseryac', 'sumergidoPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.especificar'
        db.alter_column('anarapp_estadoconseryac', 'especificar', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.mas'
        db.alter_column('anarapp_estadoconseryac', 'mas', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.observaciones'
        db.alter_column('anarapp_estadoconseryac', 'observaciones', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.erosionPa'
        db.alter_column('anarapp_estadoconseryac', 'erosionPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.perdidoPa'
        db.alter_column('anarapp_estadoconseryac', 'perdidoPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.trasladadoPa'
        db.alter_column('anarapp_estadoconseryac', 'trasladadoPa', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'EstadoConserYac.destruidoPa'
        db.alter_column('anarapp_estadoconseryac', 'destruidoPa', self.gf('django.db.models.fields.CharField')(max_length=400))

    models = {
        'anarapp.altitud': {
            'Meta': {'object_name': 'Altitud'},
            'altura': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'desarrollo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'desnivel': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superficie': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'texto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Altitud'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.bibliografia': {
            'Meta': {'object_name': 'Bibliografia'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'codigo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'conDibujo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'titulo': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.bibpiedra': {
            'Meta': {'object_name': 'BibPiedra', '_ormbases': ['anarapp.Bibliografia']},
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'BibPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.bibyacimiento': {
            'Meta': {'object_name': 'BibYacimiento', '_ormbases': ['anarapp.Bibliografia']},
            'bibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Bibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'BibYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracdelapintura': {
            'Meta': {'object_name': 'CaracDeLaPintura'},
            'anchoA': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoAComp': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoDe': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoDeComp': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esImpresionDeManos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esImpresionDeManosPositivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaCompuesta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLineaSencilla': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaDactilar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTecnicaFibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tienesFigurasSuperpuestas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracDeLaPintura'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracdolmenart': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracDolmenArt'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracDolmenArt'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracmenhires': {
            'ConPetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'CaracMenhires'},
            'cantidadConPetroglifo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPinturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConPuntosAcoplados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadPiedrasVerticales': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conPinturas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conPuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distanciamiento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sonPiedrasVerticales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracMehnires'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracmonolitos': {
            'Meta': {'object_name': 'CaracMonolitos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidadConGrabados': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esPinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracMonolitos'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcoamoladores': {
            'Meta': {'object_name': 'CaracSurcoAmoladores'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoAmoladores'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcobateas': {
            'Meta': {'object_name': 'CaracSurcoBateas'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoBateas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcocupulas': {
            'Meta': {'object_name': 'CaracSurcoCupulas'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoCupulas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcomortero': {
            'Meta': {'object_name': 'CaracSurcoMortero'},
            'ancho': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoMortero'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopetroglifo': {
            'Meta': {'object_name': 'CaracSurcoPetroglifo'},
            'anchoA': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'anchoDe': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esAltoRelieve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAltoRelieveLineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAltoRelievePlanar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlinealPulida': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAreaInterlinealRebajada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelieve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelieveLineal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBajoRelievePlanar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBase': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBaseAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esBaseRedonda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoRebajado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoSuperpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produndidadDe': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidadA': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoPetroglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caracsurcopuntosacopl': {
            'Meta': {'object_name': 'CaracSurcoPuntosAcopl'},
            'diametro': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esPunteado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'profundidad': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'CaracSurcoPuntosAcopl'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.caratrabajada': {
            'Meta': {'object_name': 'CaraTrabajada'},
            'alto': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'ancho': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'numero': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'orientacion': ('django.db.models.fields.IntegerField', [], {}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'CaraTrabajada'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.conexionfiguras': {
            'Meta': {'object_name': 'ConexionFiguras'},
            'conexionFiguras': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConexionFiguras'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.considertemp': {
            'Meta': {'object_name': 'ConsiderTemp'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConsiderTemp'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.constitucionyacimiento': {
            'Meta': {'object_name': 'ConstitucionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nroPiedras': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasColocadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasGrabadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nroPiedrasPintadas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ConstitucionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.coordenadas': {
            'Meta': {'object_name': 'Coordenadas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'longitud': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'utmAdicional': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Coordenadas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.cronologiatentativa': {
            'Meta': {'object_name': 'CronologiaTentativa'},
            'autor': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'bibliografia': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'direccion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCrono1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono3': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono5': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCrono7': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'fecha': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'mail': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'pais': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tecnica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'telefono': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'twitter': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'CronologiaTentativa'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.croquis': {
            'Meta': {'object_name': 'Croquis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urlImagen': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Croquis'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.datum': {
            'Meta': {'object_name': 'Datum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoDatum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Datum'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.dimensionpiedra': {
            'Meta': {'object_name': 'DimensionPiedra'},
            'altoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'anchoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largoMaximo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'DimensionPiedra'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.escnatpiedra': {
            'Meta': {'object_name': 'EscNatPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.escredpiedra': {
            'Meta': {'object_name': 'EscRedPiedra', '_ormbases': ['anarapp.RepGrafPiedra']},
            'repgrafpiedra_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.RepGrafPiedra']", 'unique': 'True', 'primary_key': 'True'}),
            'tipoReproduccion': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.esquemaporcara': {
            'Meta': {'object_name': 'EsquemaPorCara'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'EsquemaPorCara'", 'to': "orm['anarapp.Piedra']"}),
            'posicion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'textoCara': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.estadoconseryac': {
            'Meta': {'object_name': 'EstadoConserYac'},
            'cincoAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'crecimientoVeg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crecimientoVegPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'cuatroAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruccionPotencial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destruido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'destruidoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'dosAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enBuenEstado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaHumanaLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalAguda': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enPorCausaNaturalLigera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enterrado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enterradoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'erosion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'erosionPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esDeTiempo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esInmediato': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPorCausaNatural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'especificar': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'estaDestruido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estadoModificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'observaciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'patina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patinaPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'perdido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perdidoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'porAsentamientoHumand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionExtModerada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionExtSevera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionParModerada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porErosionParSevera': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porExtraccionFamiliar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porExtraccionMayor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porNivelacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraCortoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraLargoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porObraMedianoPlazo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'porVandalismo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sumergido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sumergidoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'trasladado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trasladadoPa': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tresAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unAno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'EstadoConserYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.faunayacimiento': {
            'Meta': {'object_name': 'FaunaYacimiento'},
            'fauna': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'FaunaYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.figurasportipo': {
            'Meta': {'object_name': 'FigurasPorTipo'},
            'cantidad': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'descripcion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'esCantidadInexacta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FigurasPorTipo'", 'to': "orm['anarapp.Piedra']"}),
            'tipoFigura': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.florayacimiento': {
            'Meta': {'object_name': 'FloraYacimiento'},
            'flora': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'FloraYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.foto': {
            'Meta': {'object_name': 'Foto'},
            'esDeAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fotografo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'negativo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numCopiaAnar': ('django.db.models.fields.IntegerField', [], {}),
            'numFoto': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numMarcaNegativo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numReferencia': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numRollo': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'tipoFotografia': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotobibliografia': {
            'Meta': {'object_name': 'FotoBibliografia'},
            'descripcion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'esBlancoYNegro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDiapositiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDigital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esFotografia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esNegativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPapel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escolor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoMapa': ('django.db.models.fields.IntegerField', [], {})
        },
        'anarapp.fotobibpiedra': {
            'Meta': {'object_name': 'FotoBibPiedra', '_ormbases': ['anarapp.FotoBibliografia']},
            'fotobibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.FotoBibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotoBibPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.fotobibyac': {
            'Meta': {'object_name': 'FotoBibYac', '_ormbases': ['anarapp.FotoBibliografia']},
            'fotobibliografia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.FotoBibliografia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotoBibYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotografiayac': {
            'Meta': {'object_name': 'FotografiaYac'},
            'esAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSatelital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noEsAerea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urlImagen': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotografiaYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.fotopiedra': {
            'Meta': {'object_name': 'FotoPiedra', '_ormbases': ['anarapp.Foto']},
            'foto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Foto']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FotoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.hidrologiayacimiento': {
            'Meta': {'object_name': 'HidrologiaYacimiento'},
            'arroyo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'arroyoPerenne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distancia': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laguna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manantialIntermitente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'observaciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'rio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'HidrologiaYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.indicaciones': {
            'Meta': {'object_name': 'Indicaciones'},
            'direcciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntoDatum': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Indicaciones'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.llenadopiedra': {
            'Meta': {'object_name': 'LlenadoPiedra', '_ormbases': ['anarapp.LlenadoPor']},
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'LlenadoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.llenadopor': {
            'Meta': {'object_name': 'LlenadoPor'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'})
        },
        'anarapp.llenadoyac': {
            'Meta': {'object_name': 'LlenadoYac', '_ormbases': ['anarapp.LlenadoPor']},
            'llenadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.LlenadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'LlenadoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.localidadyacimiento': {
            'Meta': {'object_name': 'LocalidadYacimiento'},
            'esCentroNoPoblado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCentroPoblado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esIndigena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRural': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esUrbano': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreNoPoblado': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'nombrePoblado': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'LocalidadYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestaciones': {
            'Meta': {'object_name': 'Manifestaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Manifestaciones'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'tieneAmoladores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tieneCupulas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePetroglifo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePinturaRupestre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tienePuntosAcoplados': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.manifestacionesasociadas': {
            'Meta': {'object_name': 'ManifestacionesAsociadas'},
            'descripcionCarbon': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionCementerio': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionCeramica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionConcha': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionLitica': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionMito': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionMonticulo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'descripcionOseo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'esCarbon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCementerio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCeramica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esConcha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esLitica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonticulo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esOseo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'ManifestacionesAsociadas'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.manifestacionyacimiento': {
            'Meta': {'object_name': 'ManifestacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipoManifestacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ManifestacionYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.mataudiovisual': {
            'Meta': {'object_name': 'MatAudioVisual'},
            'formato': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'})
        },
        'anarapp.matavpiedra': {
            'Meta': {'object_name': 'MatAVPiedra', '_ormbases': ['anarapp.MatAudioVisual']},
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MatAVPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.matavyacimiento': {
            'Meta': {'object_name': 'MatAVYacimiento', '_ormbases': ['anarapp.MatAudioVisual']},
            'mataudiovisual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.MatAudioVisual']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MatAVYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.materialyacimiento': {
            'Meta': {'object_name': 'MaterialYacimiento'},
            'esCorteza': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esHueso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esIgnea': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMetamor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPiel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRoca': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSedimentaria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTierra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tipo': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'MaterialYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.multimedia': {
            'Meta': {'object_name': 'Multimedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnica': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.multimediapiedra': {
            'Meta': {'object_name': 'MultimediaPiedra', '_ormbases': ['anarapp.Multimedia']},
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MultimediaPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.multimediayac': {
            'Meta': {'object_name': 'MultimediaYac', '_ormbases': ['anarapp.Multimedia']},
            'multimedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Multimedia']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'MultimediaYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.notasyacimiento': {
            'Meta': {'object_name': 'NotasYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'NotasYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observaciones': {
            'Meta': {'object_name': 'Observaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.observacionesyac': {
            'Meta': {'object_name': 'ObservacionesYac', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObservacionesYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.observacpiedra': {
            'Meta': {'object_name': 'ObservacPiedra', '_ormbases': ['anarapp.Observaciones']},
            'observaciones_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Observaciones']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObservacPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.obtencioninfo': {
            'Meta': {'object_name': 'ObtencionInfo'},
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comunicacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direccion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'nombreFacebook': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'paginaWeb': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'prospeccion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefono': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'telefonoCel': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'twitter': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'verificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.obtinfopiedra': {
            'Meta': {'object_name': 'ObtInfoPiedra', '_ormbases': ['anarapp.ObtencionInfo']},
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObtInfoPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.obtinfoyac': {
            'Meta': {'object_name': 'ObtInfoYac', '_ormbases': ['anarapp.ObtencionInfo']},
            'obtencioninfo_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.ObtencionInfo']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ObtInfoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.orientacionyacimiento': {
            'Meta': {'object_name': 'OrientacionYacimiento'},
            'haciaCerro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaCielo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaCosta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaRio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haciaValle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientacion': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'OrientacionYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.otrosvalores': {
            'Meta': {'object_name': 'OtrosValores'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.otrosvalpiedra': {
            'Meta': {'object_name': 'OtrosValPiedra', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OtrosValPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.otrosvalyac': {
            'Meta': {'object_name': 'OtrosValYac', '_ormbases': ['anarapp.OtrosValores']},
            'otrosvalores_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.OtrosValores']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'OtrosValYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.paginaweb': {
            'Meta': {'object_name': 'PaginaWeb'},
            'direccionURL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anarapp.paginawebpiedra': {
            'Meta': {'object_name': 'PaginaWebPiedra', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PaginaWebPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.paginawebyac': {
            'Meta': {'object_name': 'PaginaWebYac', '_ormbases': ['anarapp.PaginaWeb']},
            'paginaweb_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.PaginaWeb']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PaginaWebYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.pelicula': {
            'Meta': {'object_name': 'Pelicula', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.peliculapiedra': {
            'Meta': {'object_name': 'PeliculaPiedra', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliculaPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.peliyacimiento': {
            'Meta': {'object_name': 'PeliYacimiento', '_ormbases': ['anarapp.Pelicula']},
            'pelicula_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Pelicula']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PeliYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.piedra': {
            'Meta': {'object_name': 'Piedra'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifiestacionAsociada': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'nombreFiguras': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numeroCaras': ('django.db.models.fields.IntegerField', [], {}),
            'numeroCarasTrajabadas': ('django.db.models.fields.IntegerField', [], {}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Piedra'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.plano': {
            'Meta': {'object_name': 'Plano'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numeroPlano': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Plano'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.repgrafpiedra': {
            'Meta': {'object_name': 'RepGrafPiedra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituto': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'numPiezas': ('django.db.models.fields.IntegerField', [], {}),
            'persona': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'RepGrafPiedra'", 'to': "orm['anarapp.Piedra']"})
        },
        'anarapp.supervisadopiedra': {
            'Meta': {'object_name': 'SupervisadoPiedra', '_ormbases': ['anarapp.SupervisadoPor']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SupervisadoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'supervisadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.SupervisadoPor']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.supervisadopor': {
            'Meta': {'object_name': 'SupervisadoPor'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'})
        },
        'anarapp.supervisadoyac': {
            'Meta': {'object_name': 'SupervisadoYac', '_ormbases': ['anarapp.SupervisadoPor']},
            'supervisadopor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.SupervisadoPor']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'SupervisadoYac'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparageoglifo': {
            'Meta': {'object_name': 'TecnicaParaGeoglifo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tecnicas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaGeoglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamicropetro': {
            'Meta': {'object_name': 'TecnicaParaMicroPetro'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaMicroPetro'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparamonumentos': {
            'Meta': {'object_name': 'TecnicaParaMonumentos'},
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMenhir': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMonolito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'tecnicas': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaMonumentos'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapetroglifo': {
            'Meta': {'object_name': 'TecnicaParaPetroglifo'},
            'esAbrasion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionArena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAbrasionPiedra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionDirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGrabadoPercusionIndirecta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaPetroglifo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tecnicaparapintura': {
            'Meta': {'object_name': 'TecnicaParaPintura'},
            'conDedo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fibra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'soplado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TecnicaParaPintura'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tenenciadetierra': {
            'Meta': {'object_name': 'TenenciaDeTierra'},
            'esABRAE': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esComunal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esEjido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esMunicipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPrivada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTenenciaOtros': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TenenciaDeTierra'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.texturasuelo': {
            'Meta': {'object_name': 'TexturaSuelo'},
            'esArcilloso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esArenoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esPedregoso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRocaMadre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mixto': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TexturaSuelo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoexposicionyac': {
            'Meta': {'object_name': 'TipoExposicionYac'},
            'expuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expuestoPeriodicamente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noExpuesto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'observaciones': ('anarapp.models.CharField', [], {'max_length': '65000', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TipoExposicionYac'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tipoyacimiento': {
            'Meta': {'object_name': 'TipoYacimiento'},
            'esAbrigo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCueva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esCuevadeRec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esDolmen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esParedRocosa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esRoca': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTerrenoPro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esTerrenoSup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TipoYacimiento'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.tratfoto': {
            'Meta': {'object_name': 'TratFoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limpiezaCon': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'otrosTratamientos': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'programaVersion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'rellenoSurcos': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'tratamientoDigital': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.tratfotopiedra': {
            'Meta': {'object_name': 'TratFotoPiedra', '_ormbases': ['anarapp.TratFoto']},
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'TratFotoPiedra'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'tratfoto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.TratFoto']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.ubicacioncaras': {
            'Meta': {'object_name': 'UbicacionCaras'},
            'altura': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'areasEspecificas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bocaPrincipal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'claraboya': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lagoInterior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'luminosidad': ('django.db.models.fields.IntegerField', [], {}),
            'otraSala': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piedra': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'UbicacionCaras'", 'unique': 'True', 'to': "orm['anarapp.Piedra']"}),
            'requiereAndamiaje': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'salaPrincipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'todaLaCaverna': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'anarapp.ubicacionyacimiento': {
            'Meta': {'object_name': 'UbicacionYacimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ubicacionManifestacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UbicacionYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.usoactsuelo': {
            'Meta': {'object_name': 'UsoActSuelo'},
            'esAgriRiesgo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esAgriTemp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esForestal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esGanadero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSueloTuristico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esSueloUrbano': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'UsoActSuelo'", 'unique': 'True', 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.video': {
            'Meta': {'object_name': 'Video'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'autor': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'formato': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'isFromAnar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numCopia': ('django.db.models.fields.IntegerField', [], {}),
            'numReferencia': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('anarapp.models.CharField', [], {'max_length': '65000'})
        },
        'anarapp.videopiedra': {
            'Meta': {'object_name': 'VideoPiedra', '_ormbases': ['anarapp.Video']},
            'piedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoPiedra'", 'to': "orm['anarapp.Piedra']"}),
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'})
        },
        'anarapp.videoyacimiento': {
            'Meta': {'object_name': 'VideoYacimiento', '_ormbases': ['anarapp.Video']},
            'video_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anarapp.Video']", 'unique': 'True', 'primary_key': 'True'}),
            'yacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'VideoYacimiento'", 'to': "orm['anarapp.Yacimiento']"})
        },
        'anarapp.yacimiento': {
            'Meta': {'object_name': 'Yacimiento'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'nombre': ('anarapp.models.CharField', [], {'max_length': '65000'}),
            'pais': ('anarapp.models.CharField', [], {'max_length': '65000'})
        }
    }

    complete_apps = ['anarapp']