#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):


	def __init__ (self): 
    
        self.width = ""
        self.heigh = ""
        self.background-color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.right = ""
        self.left = ""
        self.i_src = ""
        self.i_region = ""
        self.i_begin = ""
        self.i_dur = ""
        self.a_src = ""
        self.a_begin = ""
        self.a_dur = ""
        self.t_src = ""
        self.t_region = ""


    def startElement(self, name, attrs): 

        if name == 'root-layout':   
            self.width = attrs.get('width',"")
            self.heigh = attrs.get('heigh',"")
            self.background-color = attrs.get('background-color',"")
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.right = attrs.get('right',"")
            self.left = attrs.get('left',"")
        elif name == 'img':
            self.i_src = attrs.get('src',"")
            self.i_region = attrs.get('region',"")
            self.i_begin = attrs.get('begin',"")
            self.i_dur = attrs.get('dur',"")
        elif name == 'audio':
            self.a_src = attrs.get('src',"")
            self.a_begin = attrs.get('begin',"")
            self.a_dur = attrs.get('dur',"")
        elif name == 'textstream':
            self.t_src = attrs.get('src',"")
            self.t_region = attrs.get('region',"")

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))




        
