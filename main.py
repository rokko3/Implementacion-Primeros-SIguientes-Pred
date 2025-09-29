import sys
reglas={}
prueba={'a':['a','b']}
primeros={}


def primeros(clave: str):
    if 'ε' in reglas.get(str):
        pass

    for produccion in reglas.get(str):


        if produccion==ε:
            pass

        pass        
    return

def siguientes():
    return

def prediccion():
    return


def main():
    
    if len(sys.argv) != 2:
        print("Hace falta uno o mas archivos ")
        return
    

    nombre_archivo = sys.argv[1]

    
    

    try:
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()
            
                
            for linea in lineas:
                    
                if "->" in linea:
                    parte_izquierda, parte_derecha = linea.split("->")
                    parte_izquierda = parte_izquierda.strip()
                    alternativas=[alt.strip() for alt in parte_derecha.split("|")]
                        
                    for alt in alternativas:
                        for p in alt.split():
                            if p!="":
                                reglas.setdefault(parte_izquierda, []).append(p)
                Exception("Las reglas tienen que estar definidas mediante ->")

        
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        
if __name__ == "__main__":

    main()
    for no_terminal in reglas.keys():

        primeros.setdefault(no_terminal,[]).append(no_terminal)

    print(reglas)
    print(prueba)
    print(prueba.get('a'))