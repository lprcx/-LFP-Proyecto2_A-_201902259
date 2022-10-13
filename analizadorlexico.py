from clases import *


class analizadorlexico():
    def __init__(self):
        self.listatokens = []
        self.listaerrores = []

    def analizar(self, texto):
        self.listatokens = []
        self.listaerrores = []

        indice = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = "qo"

        while indice < len(texto):
            caracter = texto[indice]
            if estado == "qo":
                if caracter == "<":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "menorque", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == ">":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "mayorque", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == "!":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "exclamacion", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == "-":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "guion", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == "(":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "parabre", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == ")":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "parcierra", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == ";":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "ptocoma", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == ".":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "pto", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == ",":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "coma", linea, columna))
                    buffer = ""
                    estado = "qo"
                elif caracter == "\n":
                    columna=1
                    linea+=1
                elif caracter == "\t":
                    columna+=1
                elif caracter == " ":
                    columna=1
                elif caracter.isdigit():
                    buffer = caracter
                    columna+=1
                    estado = "q1"
                elif caracter.isalpha()and(not caracter.isdigit()):
                    buffer = caracter
                    columna += 1
                    estado = "q2"
                elif caracter == '"':
                    buffer = caracter
                    columna+=1
                    estado = "q3"
                elif caracter == "/":
                    buffer=caracter
                    columna+=1
                    estado = "q4"
                else:
                    self.listaerrores.append(error(caracter, caracter+" no es reconocido como token", "Error Lexico", linea, columna))
                    buffer = ""
                    columna+=1
            elif estado == "q1":
                if caracter.isdigit():
                    buffer+=caracter
                    columna+=1
                    estado = "q1"
                else:
                    self.listatokens.append(token(buffer, "digito", linea, columna))
                    buffer = ""
                    indice-=1
                    estado = "qo"
            elif estado == "q2":
                if caracter.isalpha() or caracter=="_":
                    buffer+=caracter
                    columna+=1
                    estado = "q2"
                else:
                    if buffer == "Controles":
                        self.listatokens.append(token(buffer, "rescontroles", linea, columna))
                    elif buffer == "propiedades":
                        self.listatokens.append(token(buffer, "rpropiedades", linea, columna))
                    elif buffer == "Colocacion":
                        self.listatokens.append(token(buffer, "rcolocacion", linea, columna))
                    elif buffer == "Etiqueta":
                        self.listatokens.append(token(buffer, "retiqueta", linea, columna))
                    elif buffer == "Boton":
                        self.listatokens.append(token(buffer, "rboton", linea, columna))
                    elif buffer == "Check":
                        self.listatokens.append(token(buffer, "rcheck", linea, columna))
                    elif buffer == "RadioBoton":
                        self.listatokens.append(token(buffer, "radboton", linea, columna))
                    elif buffer == "Texto":
                        self.listatokens.append(token(buffer, "rtexto", linea, columna))
                    elif buffer == "AreaTexto":
                        self.listatokens.append(token(buffer, "artexto", linea, columna))
                    elif buffer == "Clave":
                        self.listatokens.append(token(buffer, "rclave", linea, columna))
                    elif buffer == "Contenedor":
                        self.listatokens.append(token(buffer, "rcontenedor", linea, columna))
                    elif buffer == "setTexto":
                        self.listatokens.append(token(buffer, "settext", linea, columna))
                    elif buffer == "setAlineacion":
                        self.listatokens.append(token(buffer, "setal", linea, columna))
                    elif buffer == "setColorFondo":
                        self.listatokens.append(token(buffer, "setcolfon", linea, columna))
                    elif buffer == "setMarcada":
                        self.listatokens.append(token(buffer, "setmarc", linea, columna))
                    elif buffer == "setColorLetra":
                        self.listatokens.append(token(buffer, "setcolet", linea, columna))
                    elif buffer == "setGrupo":
                        self.listatokens.append(token(buffer, "setgrup", linea, columna))
                    elif buffer == "setAncho":
                        self.listatokens.append(token(buffer, "sancho", linea, columna))
                    elif buffer == "setAlto":
                        self.listatokens.append(token(buffer, "salto", linea, columna))
                    elif buffer == "Centro":
                        self.listatokens.append(token(buffer, "rcentro", linea, columna))
                    elif buffer == "Izquierdo":
                        self.listatokens.append(token(buffer, "rizquierdo", linea, columna))
                    elif buffer == "Derecho":
                        self.listatokens.append(token(buffer, "rderecho", linea, columna))
                    elif buffer == "setPosicion":
                        self.listatokens.append(token(buffer, "setpos", linea, columna))
                    elif buffer == "add":
                        self.listatokens.append(token(buffer, "radd", linea, columna))
                    elif buffer == "this":
                        self.listatokens.append(token(buffer, "rthis", linea, columna))
                    else:
                        self.listatokens.append(token(buffer, "identificador", linea, columna))
                    buffer = ""
                    estado = "qo"
                    indice-=1
            elif estado == "q3":
                if caracter != '"':
                    buffer+=caracter
                    columna+=1
                    estado = "q3"
                elif caracter == "\n":
                    columna = 1
                    linea+=1
                    estado = "q3"
                elif caracter=='"':
                    buffer+=caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "cadena", linea, columna))
                    buffer = ""
                    estado = "qo"
            elif estado == "q4":
                if caracter == "/":
                    buffer+=caracter
                    columna+=1
                    estado = "q5"
                elif caracter == "*":
                    buffer+=caracter
                    columna+=1
                    estado = "q6"
                else:
                    buffer+=caracter
                    columna+=1
                    self.listaerrores.append(error(buffer, buffer+" no reconocido como token", "Error Lexico", linea, columna))
                    buffer = ""
                    estado = "qo"
            elif estado == "q5":
                if caracter == "\n":
                    self.listatokens.append(token(buffer, "comentario simple", linea, columna))
                    buffer = ""
                    indice-=1
                    estado = "qo"
                else:
                    buffer+=caracter
                    columna+=1
                    estado = "q5"
            elif estado == "q6":
                if caracter == "*":
                    buffer+=caracter
                    columna+=1
                    if texto[indice+1] == "/":
                        buffer+=texto[indice+1]
                        columna+=1
                        self.listatokens.append(token(buffer, "comentario multilinea", linea, columna))
                        buffer=""
                        estado = "qo"
                        indice +=1
                    else:
                        buffer+=caracter
                        columna+=1
                        estado = "q6"
                elif caracter == "\n":
                    buffer+=caracter
                    columna = 1
                    linea+=1
                    estado = "q6"
                else:
                    buffer+=caracter
                    columna+=1
                    estado = "q6"
            indice+=1
        self.listatokens.append(token("", "<<EOF>>", linea, columna))