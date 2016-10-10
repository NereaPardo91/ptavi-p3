#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


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
	salida = ""

	for elems in misDatos:
		etiq = elems['tag']
		salida = (etiq+'\t')
		for atributos in elems:
			salida = salida+atributos+"="+elems[atributos]+'\t'
		print(salida)



		


	



   