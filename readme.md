# Analizador de Gramáticas - Conjuntos PRIMEROS, SIGUIENTES y PREDICCIÓN

## Hecho por: William Alfonso, Samuel Leyton, Felipe Morales

## Descripción

Este proyecto implementa un analizador de gramaticas libres de contexto que calcula automáticamente los conjuntos **PRIMEROS**, **SIGUIENTES** y **PREDICCION** para una gramatica dada. Estos conjuntos son fundamentales en la construccion de analizadores sintacticos predictivos (parsers LL(1)).

## Funcionamiento del Programa

### Entrada
El programa recibe como entrada un archivo de texto que contiene las reglas de produccion de una gramatica en el siguiente formato:
```
A -> a d c
A -> c  
B -> D
```

### Componentes Principales

#### 1. **Lectura de Gramatica** (`leer_gramatica`)
- Lee las reglas de producción desde un archivo de texto
- Parsea cada linea separando la parte izquierda (no terminal) de la derecha (produccion)
- Maneja multiples alternativas separadas por el símbolo `|`
- Identifica automaticamente el símbolo inicial 
- Retorna un diccionario donde cada clave es un no terminal y el valor es una lista de producciones

#### 2. **Calculo de PRIMEROS** (`calcular_primeros`)
El conjunto PRIMEROS(X) contiene todos los simbolos terminales que pueden aparecer al inicio de las cadenas derivadas de X.

**Algoritmo:**
- **Inicializacion**: Los terminales se incluyen en su propio conjunto PRIMEROS
- **Iteración hasta convergencia**:
  - Para cada producción A → α:
    - Si α comienza con terminal: añadir ese terminal a PRIMEROS(A)
    - Si α comienza con no terminal B: añadir PRIMEROS(B) - {ε} a PRIMEROS(A)
    - Si todos los símbolos de α pueden derivar ε: añadir ε a PRIMEROS(A)

#### 3. **Calculo de SIGUIENTES** (`calcular_siguientes`)
El conjunto SIGUIENTES(A) contiene todos los terminales que pueden aparecer inmediatamente después del no terminal A en alguna forma sentencial.

**Algoritmo:**
- **Inicializacion**: Añadir $ al conjunto SIGUIENTES del símbolo inicial
- **Iteración hasta convergencia**:
  - Para cada producción A → αBβ (donde B es no terminal):
    - Añadir PRIMEROS(β) - {ε} a SIGUIENTES(B)
    - Si β puede derivar ε: añadir SIGUIENTES(A) a SIGUIENTES(B)
  - Para producciones A → αB: añadir SIGUIENTES(A) a SIGUIENTES(B)

#### 4. **Calculo de PREDICCIÓN** (`calcular_prediccion`)
El conjunto PREDICCIÓN de una producción A → α contiene todos los terminales que pueden aparecer al inicio de las cadenas derivadas cuando se aplica esta produccion.

**Algoritmo:**
- Para cada produccion A → α:
  - Si α no puede derivar ε: PRED(A → α) = PRIMEROS(α)
  - Si α puede derivar ε: PRED(A → α) = PRIMEROS(α) ∪ SIGUIENTES(A)

### Salida del Programa

El programa muestra:
1. **Gramática cargada**: Visualización de todas las producciones leídas
2. **Conjuntos PRIMEROS**: Para cada símbolo de la gramática
3. **Conjuntos SIGUIENTES**: Para cada no terminal
4. **Conjuntos PREDICCIÓN**: Para cada producción individual

### Ejemplo de Uso

```bash
python analizador.py gramatica1.txt
python analizador.py gramatica2.txt
```

### Ejemplos de Salida

#### Ejemplo 1: Gramática 1

**Contenido de gramatica1.txt:**
```
S -> A uno B C | S dos
A -> B C D | A tres | ε
B -> D cuatro C tres | ε
C -> cinco D B | ε
D -> seis | ε
```

**Salida del programa:**
```
Gramática cargada de: gramatica1.txt
S -> ['A uno B C', 'S dos']
A -> ['B C D', 'A tres', 'ε']
B -> ['D cuatro C tres', 'ε']
C -> ['cinco D B', 'ε']
D -> ['seis', 'ε']

--- PRIMEROS ---
PRIMEROS(uno) = {'uno'}
PRIMEROS(dos) = {'dos'}
PRIMEROS(tres) = {'tres'}
PRIMEROS(cuatro) = {'cuatro'}
PRIMEROS(cinco) = {'cinco'}
PRIMEROS(seis) = {'seis'}
PRIMEROS(S) = {'cuatro', 'tres', 'uno', 'cinco', 'seis'}
PRIMEROS(A) = {'cuatro', 'ε', 'tres', 'cinco', 'seis'}
PRIMEROS(B) = {'cuatro', 'seis', 'ε'}
PRIMEROS(D) = {'seis', 'ε'}
PRIMEROS(C) = {'cinco', 'ε'}

--- SIGUIENTES ---
SIGUIENTES(S) = {'dos', '$'}
SIGUIENTES(A) = {'tres', 'uno'}
SIGUIENTES(B) = {'dos', 'tres', 'uno', '$', 'cinco', 'seis'}
SIGUIENTES(C) = {'tres', 'uno', 'dos', '$', 'seis'}
SIGUIENTES(D) = {'dos', 'cuatro', 'tres', 'uno', '$', 'seis'}

--- PREDICCIÓN ---
PRED(S -> A uno B C) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
PRED(S -> S dos) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
PRED(A -> B C D) = {'tres', 'uno', 'cinco', 'cuatro', 'seis'}
PRED(A -> A tres) = {'tres', 'cinco', 'cuatro', 'seis'}
PRED(A -> ε) = {'tres', 'uno'}
PRED(B -> D cuatro C tres) = {'cuatro', 'seis'}
PRED(B -> ε) = {'tres', 'uno', 'dos', '$', 'cinco', 'seis'}
PRED(C -> cinco D B) = {'cinco'}
PRED(C -> ε) = {'tres', 'uno', 'dos', '$', 'seis'}
PRED(D -> seis) = {'seis'}
PRED(D -> ε) = {'tres', 'uno', 'dos', '$', 'cuatro', 'seis'}
```

#### Ejemplo 2: Gramática 2

**Contenido de gramatica2.txt:**
```
S -> A B uno
A -> dos B | ε
B -> C D | tres | ε
C -> cuatro A B | cinco
D -> seis | ε
```

**Salida del programa:**
```
Gramática cargada de: gramatica2.txt
S -> ['A B uno']
A -> ['dos B', 'ε']
B -> ['C D', 'tres', 'ε']
C -> ['cuatro A B', 'cinco']
D -> ['seis', 'ε']

--- PRIMEROS ---
PRIMEROS(uno) = {'uno'}
PRIMEROS(dos) = {'dos'}
PRIMEROS(tres) = {'tres'}
PRIMEROS(cuatro) = {'cuatro'}
PRIMEROS(cinco) = {'cinco'}
PRIMEROS(seis) = {'seis'}
PRIMEROS(S) = {'tres', 'cinco', 'cuatro', 'dos', 'uno'}
PRIMEROS(A) = {'dos', 'ε'}
PRIMEROS(B) = {'cinco', 'tres', 'cuatro', 'ε'}
PRIMEROS(C) = {'cinco', 'cuatro'}
PRIMEROS(D) = {'seis', 'ε'}

--- SIGUIENTES ---
SIGUIENTES(S) = {'$'}
SIGUIENTES(A) = {'cinco', 'cuatro', 'tres', 'seis', 'uno'}
SIGUIENTES(B) = {'cinco', 'cuatro', 'tres', 'seis', 'uno'}
SIGUIENTES(C) = {'cinco', 'cuatro', 'tres', 'seis', 'uno'}
SIGUIENTES(D) = {'cinco', 'cuatro', 'tres', 'seis', 'uno'}

--- PREDICCIÓN ---
PRED(S -> A B uno) = {'cinco', 'tres', 'cuatro', 'uno', 'dos'}
PRED(A -> dos B) = {'dos'}
PRED(A -> ε) = {'seis', 'cinco', 'cuatro', 'tres', 'uno'}
PRED(B -> C D) = {'cinco', 'cuatro'}
PRED(B -> tres) = {'tres'}
PRED(B -> ε) = {'seis', 'cinco', 'cuatro', 'tres', 'uno'}
PRED(C -> cuatro A B) = {'cuatro'}
PRED(C -> cinco) = {'cinco'}
PRED(D -> seis) = {'seis'}
PRED(D -> ε) = {'seis', 'cinco', 'cuatro', 'tres', 'uno'}
```

