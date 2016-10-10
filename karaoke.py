#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import sys
import urllib.request
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class karaokeLocal():

	def init(self, fichero):
		parser = make_parser()
		self.sHandler = SmallSMILHandler()
		parser.setContentHandler(self.sHandler)
		parser.parse(open(fichero))
		self.misDatos = self.sHandler.get_tags()

	def __str__(self):
		for elems in self.misDatos:
			etiq = elems['tag']  #cojo mi etiqueta tag para que sea lo primero que se imprime
			del elems['tag']	#borro tag de mi dicc para que no se repita al final
			text = (etiq +'\t')

			for atributos in elems:
				text = text + '\t' + atributos + '= "' + elems[atributos] + '"' + '\t'
			print(text)

	def to_json(self, fichero):
		fjson = open(fichero[:-4] + 'json', 'w')
		json.dump(self.misDatos, fjson)

	def do_local(self):
		for elems in self.misDatos:
			for atributos in elems:
				if elems[atributos].startswith('http://'): #si el valor de mi clave empieza por http...
					name = elems[atributos].split('/')[-1] #cogeme a partir de la ultima /
					urllib.request.urlretrieve(elems[atributos], name) #descarga del "archivo"
					elems[atributos] = name #quedate con logo.gif

if __name__ == "__main__":

	karaoke = karaokeLocal()

	try:
		fichero = sys.argv[1]
	except IndexError:
		sys.exit("Usage: python3 karaoke.py file.smil")
	
	karaoke.init(fichero)
	karaoke.__str__()
	karaoke.to_json(sys.argv[1])
	karaoke.do_local()
	karaoke.to_json('local')
	karaoke.__str__()



