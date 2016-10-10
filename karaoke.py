#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def to_json(misDatos, fichero):
	fjson = open(fichero[:-4] + 'json', 'w')
	json.dump(misDatos, fjson)

if __name__ == "__main__":

	parser = make_parser()
	sHandler = SmallSMILHandler()
	parser.setContentHandler(sHandler)

	try:
		fichero = sys.argv[1]

	except IndexError:
		sys.exit("Usage: python3 karaoke.py file.smil")

	parser.parse(open(fichero))
	misDatos = sHandler.get_tags()

	for elems in misDatos:

		etiq = elems['tag']  #cojo mi etiqueta tag para que sea lo primero que se imprime
		del elems['tag']	#borro tag de mi dicc para que no se repita al final
		text = (etiq +'\t')

		for atributos in elems:
			text = text + '\t' + atributos + '= "' + elems[atributos] + '"' + '\t'
		print(text)


	to_json(misDatos, fichero)

	 