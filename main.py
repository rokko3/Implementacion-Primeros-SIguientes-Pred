import sys
reglas={}
primeros={}


def hallar_primeros(clave: str):
    produccion=reglas.get(clave,[])
    
    for produce in produccion:
        if produce=='ε':
            primeros[clave].append('ε')
        else:
            pass
            


     
    return

def hallar_siguientes():
    return

def hallar_prediccion():
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
                        produccion=[p for p in alt.split() if p!=""]
                        reglas.setdefault(parte_izquierda, []).append(produccion)
                else:
                    raise Exception("Las reglas tienen que estar definidas mediante ->")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        
if __name__ == "__main__":

    main()
    for no_terminal in reglas.keys():


        primeros[no_terminal]=[]

    print(reglas)
    print(primeros.keys())