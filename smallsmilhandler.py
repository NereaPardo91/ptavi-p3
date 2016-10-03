#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__ (self): 

        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
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
        self.etiquetas = []


    def startElement(self, name, attrs): 

        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('backgroundcolor',"")
            atrib = {'width' : self.width, 'height' : self.height, 'backgroundcolor' : self.backgroundcolor}
            atrib['tag'] = name
            self.etiquetas.append(atrib)
            #print(self.etiquetas)
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.right = attrs.get('right',"")
            self.left = attrs.get('left',"")
            atrib = {'id' : self.id, 'top' : self.top, 'bottom' : self.bottom, 'right' : self.right, 'left' : self.left}
            atrib['tag'] = name
            self.etiquetas.append(atrib)
            #print(self.etiquetas)
        elif name == 'img':
            self.i_src = attrs.get('src',"")
            self.i_region = attrs.get('region',"")
            self.i_begin = attrs.get('begin',"")
            self.i_dur = attrs.get('dur',"")
            atrib = {'src' : self.i_src, 'region' : self.i_region, 'begin' : self.i_begin, 'dur' : self.i_dur}
            atrib['tag'] = name
            self.etiquetas.append(atrib)
            #print(self.etiquetas)
        elif name == 'audio':
            self.a_src = attrs.get('src',"")
            self.a_begin = attrs.get('begin',"")
            self.a_dur = attrs.get('dur',"")
            atrib = {'src' : self.a_src, 'begin' : self.a_begin, 'dur' : self.a_dur}
            atrib['tag'] = name
            self.etiquetas.append(atrib)
            #print(self.etiquetas)
        elif name == 'textstream':
            self.t_src = attrs.get('src',"")
            self.t_region = attrs.get('region',"")          
            atrib = {'src' : self.t_src, 'region' : self.t_region}
            atrib['tag'] = name
            self.etiquetas.append(atrib)
            #print(self.etiquetas)


    def get_tags(self):
        return self.etiquetas


if __name__ == "__main__":

        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open('karaoke.smil'))
        misDatos = sHandler.get_tags()
        print(misDatos)



        
