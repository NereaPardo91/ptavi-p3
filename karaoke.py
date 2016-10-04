#!/usr/bin/python3
# -*- coding: utf-8 -*-
import smallsmilhandler
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class Karaoke(smallsmilhandler.SmallSMILHandler):

	def __init__ (self, fichero): 

		parser = make_parser()
		kHandler = smallsmilhandler.SmallSMILHandler()
		parser.setContentHandler(kHandler)
		parser.parse(open(fichero))
		self.misDatos = kHandler.get_tags()


if __name__ == "__main__":

	try:
		fichero = sys.argv[1]

	except IndexError:
		sys.exit("Usage: python3 karaoke.py file.smil")
    
   