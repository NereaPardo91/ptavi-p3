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

	for elem in misDatos:
		print(elem)

		


	



   