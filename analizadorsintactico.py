from msilib.schema import Error
from operator import index
from clases import *
from expresiones import *
from instrucciones import *


class analizadorSintactico():
    def __init__(self):
        self.listatokens = []
        self.listaerrores = []
        self.index = 0

    def prop3(self):
        if self.listatokens[self.index].tipo=="rpropiedades":
            pass
            #return insprop3(None, None)
        else:
            p2=self.prop2()
            p3=self.prop3()
            #return insprop3(p2, p3)

    def prop2(self):
        if self.listatokens[self.index].tipo=="identificador":
            self.index+=1
            if self.listatokens[self.index].tipo=="pto":
                self.index+=1
                if self.listatokens[self.index].tipo=="setColorLetra":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="digito":
                            numero = self.listatokens[self.index].lexema
                            self.index+=1
                            if self.listatokens[self.index].tipo=="coma":
                                self.index+=1
                                if self.listatokens[self.index].tipo=="digito":
                                    numero2 = self.listatokens[self.index].lexema
                                    self.index+=1
                                    if self.listatokens[self.index].tipo=="coma":
                                        self.index+=1
                                        if self.listatokens[self.index].tipo=="digito":
                                            numero3 = self.listatokens[self.index].lexema
                                            self.index+=1
                                            if self.listatokens[self.index].tipo=="parcierra":
                                                self.index+=1
                elif self.listatokens[self.index].tipo=="setColorFondo":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="digito":
                            numero = self.listatokens[self.index].lexema
                            self.index+=1
                            if self.listatokens[self.index].tipo=="coma":
                                self.index+=1
                                if self.listatokens[self.index].tipo=="digito":
                                    numero2 = self.listatokens[self.index].lexema
                                    self.index+=1
                                    if self.listatokens[self.index].tipo=="coma":
                                        self.index+=1
                                        if self.listatokens[self.index].tipo=="digito":
                                            numero3 = self.listatokens[self.index].lexema
                                            self.index+=1
                                            if self.listatokens[self.index].tipo=="parcierra":
                                                self.index+=1
                elif self.listatokens[self.index].tipo=="setAlineacion":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="rcentro":
                            pos = "c"
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                        elif self.listatokens[self.index].tipo=="rizquierdo":
                            pos = "i"
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                        elif self.listatokens[self.index].tipo=="rderecho":
                            pos = "d"
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                elif self.listatokens[self.index].tipo=="setTexto":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="cadena":
                            texto = self.listatokens[self.index].lexema
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                elif self.listatokens[self.index].tipo=="setMarcada":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="rtrue":
                            marc = True
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                        elif self.listatokens[self.index].tipo=="rfalse":
                            marc = False
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                elif self.listatokens[self.index].tipo=="setGrupo":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="identificador":
                            texto = self.listatokens[self.index].lexema
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                elif self.listatokens[self.index].tipo=="setAlto":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="parabre":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="digito":
                            texto = self.listatokens[self.index].lexema
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
                elif self.listatokens[self.index].tipo=="setAncho":
                    self.index+=1
                    if self.listatokens[self.index].tipo=="digito":
                        self.index+=1
                        if self.listatokens[self.index].tipo=="cadena":
                            texto = self.listatokens[self.index].lexema
                            self.index+=1
                            if self.listatokens[self.index].tipo=="parcierra":
                                self.index+=1
        lexema = self.listatokens[self.index].lexema
        linea = self.listatokens[self.index].linea
        columna = self.listatokens[self.index].columna
        self.listaerrores.append(error(lexema, "Error Sintactico, no se esperaba ese token", "Sintactico", linea, columna))
        self.index+=1
        return insError(linea)
                    

    def contpropiedades(self):
        prop2 = self.prop2()
        prop3 = self.prop3()
        #return insprop1(prop2, prop3)

    def Propiedades(self):
        if self.listatokens[self.index].tipo == "menorque":
            self.index+=1
            if self.listatokens[self.index].tipo == "exclamacion":
                self.index+=1
                if self.listatokens[self.index].tipo == "guion":
                    self.index+=1
                    if self.listatokens[self.index].tipo == "guion":
                        self.index+=1
                        if self.listatokens[self.index].tipo == "rpropiedades":
                            cont = self.contpropiedades()
                            if self.listatokens[self.index].tipo == "rpropiedades":
                                self.index+=1
                                if self.listatokens[self.index].tipo == "guion":
                                    self.index+=1
                                    if self.listatokens[self.index].tipo == "guion":
                                        self.index+=1
                                        if self.listatokens[self.index].tipo == "mayorque":
                                            self.index+=1
                                            return insPropiedades(cont)
        lexema = self.listatokens[self.index].lexema
        linea = self.listatokens[self.index].linea
        columna = self.listatokens[self.index].columna
        self.listaerrores.append(error(lexema, "Error Sintactico, no se esperaba ese token", "Sintactico", linea, columna))
        self.index+=1
        return insError(linea)

    def Controles(self):
        if self.listatokens[self.index].tipo == "menorque":
            self.index+=1
            if self.listatokens[self.index].tipo == "exclamacion":
                self.index+=1
                if self.listatokens[self.index].tipo == "guion":
                    self.index+=1
                    if self.listatokens[self.index].tipo == "guion":
                        self.index+=1
                        if self.listatokens[self.index].tipo == "rescontroles":
                            cont = self.contcontroles()
                            if self.listatokens[self.index].tipo == "rescontroles":
                                self.index+=1
                                if self.listatokens[self.index].tipo == "guion":
                                    self.index+=1
                                    if self.listatokens[self.index].tipo == "guion":
                                        self.index+=1
                                        if self.listatokens[self.index].tipo == "mayorque":
                                            self.index+=1
                                            return insControles(cont)
        lexema = self.listatokens[self.index].lexema
        linea = self.listatokens[self.index].linea
        columna = self.listatokens[self.index].columna
        self.listaerrores.append(error(lexema, "Error Sintactico, no se esperaba ese token", "Sintactico", linea, columna))
        self.index+=1
        return insError(linea)

    def Colocacion(self):
        if self.listatokens[self.index].tipo == "menorque":
            self.index+=1
            if self.listatokens[self.index].tipo == "exclamacion":
                self.index+=1
                if self.listatokens[self.index].tipo == "guion":
                    self.index+=1
                    if self.listatokens[self.index].tipo == "guion":
                        self.index+=1
                        if self.listatokens[self.index].tipo == "rcolocacion":
                            cont = self.contpropiedades()
                            if self.listatokens[self.index].tipo == "rcolocacion":
                                self.index+=1
                                if self.listatokens[self.index].tipo == "guion":
                                    self.index+=1
                                    if self.listatokens[self.index].tipo == "guion":
                                        self.index+=1
                                        if self.listatokens[self.index].tipo == "mayorque":
                                            self.index+=1
                                            return insColocacion(cont)
        lexema = self.listatokens[self.index].lexema
        linea = self.listatokens[self.index].linea
        columna = self.listatokens[self.index].columna
        self.listaerrores.append(error(lexema, "Error Sintactico, no se esperaba ese token", "Sintactico", linea, columna))
        self.index+=1
        return insError(linea)

    def Instruccion(self):
        if self.listatokens[self.index + 4].tipo == "rpropiedades":
            ins = self.Propiedades()
            return insInstruccion(ins)
        elif self.listatokens[self.index + 4].tipo == "rescontroles":
            ins = self.Controles()
            return insInstruccion(ins)
        elif self.listatokens[self.index + 4].tipo == "rcolocacion":
            ins = self.Colocacion()
            return insInstruccion(ins)

    def Instrucciones2(self):
        if self.listatokens[self.index].tipo == "<< EOF >>":
            print("Analisis Sintáctico realizado con éxito")
            return insInstrucciones2(None, None)
        else:
            ins = self.Instruccion()
            ins2 = None
            if self.index<len(self.listatokens):
                ins2 = self.Instrucciones2()
            return insInstrucciones2(ins, ins2)

    def Instrucciones(self):
        ins = self.Instruccion()
        ins2 = self.Instrucciones2()
        return insInstrucciones(ins, ins2)

    def Inicio(self):
        ins = self.Instrucciones()
        return insInicio(ins)

    def Analizar(self, listatokens, listaerrores):
        self.listatokens = listatokens
        self.listaerrores = listaerrores
        return self.Inicio()
