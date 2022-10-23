from expresiones import *

textsalidahtml = ""
textsalidacss = ""

def Salidahtml():
    global textsalidahtml
    return textsalidahtml 

def Salidacss():
    global textsalidacss
    return textsalidacss

class insError():
    def __init__(self, linea):
        self.linea = linea
    
    def ejecutar(self, entorno):
        pass

class insInicio():
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
    
    def ejecutar(self, entorno):
        self.instrucciones.ejecutar(entorno)

class insInstrucciones():
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)
        self.instrucciones2.ejecutar(entorno)

class insInstruccion():
    def __init__(self, instruccion):
        self.instruccion = instruccion
    
    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

class insInstrucciones2():
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
        if self.instrucciones2:
            self.instrucciones2.ejecutar(entorno)

class insPropiedades():
    def __init__(self, propiedades):
        self.propiedades = propiedades
    
    def ejecutar(self, entorno):
        self.propiedades.ejecutar(entorno)

class insControles():
    def __init__(self, controles):
        self.controles = controles
    
    def ejecutar(self, entorno):
        self.controles.ejecutar(entorno)

class insColocacion():
    def __init__(self, colocacion):
        self.colocacion = colocacion
    
    def ejecutar(self, entorno):
        self.colocacion.ejecutar(entorno)