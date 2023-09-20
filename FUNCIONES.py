# Importar librerias
"""Estas son las funciones que cumplen con los requisitos para ejecutar el programa solicitado
en ellas tenemos list comprehencion, anonimas, y funcion de orden superios aqui solo estan las funciones """

import pickle 
import time
# esta es la función que hace el llamado de las demas funciones para que se ejecute el sistema deseado
def main_menu ():
    
    base_datos = base_de_datos()
    
    cantidad_estudiantes = len(base_datos["nombres"])                  # Esta parte se encarga de mostrar las primeras 
    if cantidad_estudiantes > 0:                                       # palabras del sistema
        print("cargando datos....\n")
        time.sleep(3)
        print("....Base cargada\n")

        print (f"Hola se acaba de cargar una base de datos con {cantidad_estudiantes} Estudiantes")
        time.sleep(3)

    else:
        print("No se encontró una base de datos anterior. Comenzando con una base de datos vacia\n")
        time.sleep(3)

    ''' muestra el menú al usuario y lo deja ingresar cualquier opcion del menú'''
    
    while True: #ciclo inicializado en verdadero
        print('~' * 50)
        print('~' * 50)
        opcion_valida= validar_opciones(1,6,"Menú: \n 1. Registrar estudiante\n 2. Consultar estudiantes de una carrera\n 3. Calcular promedio general\n 4. Validar estudiantes destacados\n 5. Salir\n Seleccione una opción: ") #valida que las opciones digitadas por el usuario sean de la 1 a la 5
 
        if opcion_valida == 1:
            
            register_stu()                        #Esta funcion llama las funcoines necesarias para reg-estu
        
        if opcion_valida == 2:
            
            find_carrer (carrers())               #Hace el llamado de las funciones para mostrar los est. de una ing.
        
        if opcion_valida == 3:
            
            media()                                #Notas -promedio 
        
        if opcion_valida == 4:
            
            destacados()                           #Estudiantes superior  o igual a 4.0 
        
        if opcion_valida == 5:
            
            print("Programa finalizado, hasta pronto") #imprime el mensaje y finaliza el programa
            
            break

def numero_entero(numero):                              
    
        ''' valida que la opcion digitada por el usuario sea un número entero.
        recibe la opción digitada por el usuario y retorna un número entero'''
    
        try:
            
            entero= int(numero)         #valida que la opción ingresada sea un número entero
            return entero               #retorna un número entero
        
        except ValueError: 
            print("~" * 50 + "\nDebe ingresar un número entero\n" + "~" * 50) #si el número no es entero, imprime el mensaje
        
    
def validar_opciones(inicio,fin,men):
    
    ''' valida que la opcion digitada por el usuario esté entre la opción 1 y 5.
        recibe la opción digitada por el usuario y retorna la opción'''
    while (True):
        opciones = input(men)
        try:
            opcion= numero_entero(opciones)
            
            if opcion in range(inicio,fin):       #verifica que la opción esté entre 1 y 5
                return opcion                     #retorna la variable opción
            else:
                raise ValueError(f"Opción no válida, recuerde que debe ser entre {inicio} y {fin-1}\n") #si la opción no está entre 1 y 5 imprime el mensaje
                
        except ValueError as mensaje:
            print(mensaje)                        #si la opción no está entre 1 y 5 imprime el mensaje


def base_de_datos():
    try:
        with open('bases_de_datos.pkl', 'rb') as archivo:
            base_datos = pickle.load(archivo)                 #Carga la base de datos en .PKL
            return base_datos
    except FileNotFoundError: 
        base_datos = {"nombres" : [],
                      "edad":[],
                      "carrera":[],
                      "promedio":[] }
        return base_datos

#*************************************************************************************************
# funcion para pedir nombre recibe una sola palabra.parametros solo el mensaje como quieras pedir el nombre
#retorna nombre

def solo_alfabetico(mensaje):     #Evita que se ingrese un dato diferente a un entero.
    while(True):
        dato = input(mensaje) 
        if dato.isalpha():        #Condición que solo sean caracteres alfabeticos
            return dato    
            break 
        else:
            print('\nPor favor ingrese un nombre valido...\n')
#*************************************************************************************************
# funcion ingresa nota no tiene parametros

def num_note ():
    while True:
        try:
            numero = float(input("por favor ingresa la nota del estudiante de 0.0 a 5.0: "))
            
            if numero >= 0.0 and numero <= 5.0:   # rango de la nota
                return numero
                break
            
            else:
                 print("~" * 50)
                 print("El rango es de 0 a 5")
                 print("~" * 50)
        
        except ValueError:
                print("~" * 50)
                print("\nPor favor ingrese un dato valido\n")
                print("~" * 50)
        
        except TypeError:                                        
             print("~" * 50)
             print ("\npor favor la nota debe de estar en un rango de 0.0 a 5.0:\n")
             print("~" * 50)
#*************************************************************************************************                
#funcion para pedir carrera no tiene parametros retorna el string de la carrera

def carrers ():
    while True:
        print("~" * 50)
        carreras=("Ingeniería de Productividad y Calidad.","Ingeniería Agropecuaria.","Ingeniería civil.",
                  "Ingeniería en Seguridad y Salud en el Trabajo.","Ingeniería en Automatización y Control.","Ingeniería Informatica.") # tuplas
        
        opcion_valida= validar_opciones(1,7,f"Selecione el programa: \n\n1. {carreras[0]}.\n2. {carreras[1]}\n3. {carreras[2]}\n4. {carreras[3]}\n5. {carreras[4]}\n6. {carreras[5]} \n")
        if opcion_valida == 1:
            return carreras[0]            #retorna el dato que hay en el indice de la tuplas
        elif opcion_valida == 2:
            return carreras[1]                                  
        elif opcion_valida == 3:
            return carreras[2]
        elif opcion_valida == 4:
            return carreras[3]
        elif opcion_valida == 5:
            return carreras[4]
        elif opcion_valida == 6:
            return carreras[5]

#*************************************************************************************************    
#Funcion registar estudiantes sin parametros. pero usa todas las funciones del scrip funciones_snake.py
#Retorna un diccionario con los datos del ultimo estudiante agregado
def register_stu():
    
    base_datos = base_de_datos()
    
    base_datos["nombres"].append(solo_alfabetico("Por favor ingrese el nombre del estudiante: "))  
    
    base_datos["edad"].append(validar_opciones(8,101,"Ingrese la edad del estudiante: "))

    base_datos["carrera"].append(carrers())

    base_datos["promedio"].append(num_note())
    
    #Abrir un archivo binario en modo escritura
    with open('bases_de_datos.pkl', 'wb') as archivo:       
        pickle.dump(base_datos, archivo)                    #Enviamos los datos al archivo
        
#*************************************************************************************************
#funcion para buscar los estudiantes de un acarrera
def find_carrer (ingenieria):

    base_datos = base_de_datos()
    for i in range (len(base_datos["carrera"])):                         #Longitud de base de datos
       
        if ingenieria in base_datos.get("carrera"):                      #.get nos devuelve el valor que tiene ese key en la lista

            indices = [indice for indice,ing in enumerate(base_datos["carrera"] )   if ing == ingenieria  ] # list comprehencion retorna el indice del dato que se cumple
            students_in = [base_datos["nombres"][i]   for i in indices]   #Retorna el nombre del dato que se cumple
            cant_estud=len(students_in)
            
            print("Los estudiantes son:\n")
            for i in range(cant_estud):
                print(f"--{students_in[i]}")                               #Imprime los estudientes de una carrera previamente selecionada
        else:
            print('~' * 50)
            print(f"{ingenieria}\n{'*' * 6}No se encontró en la lista")
        time.sleep(2)
        break
#*************************************************************************************************
#funcoin promedio general
def media():
    base_datos = base_de_datos()
    media = sum(base_datos["promedio"])/len(base_datos["promedio"])
    print('~' * 50)
    print(f"La media en El Politecnico Colombiano\nJaime Isaza Cadavid es: {round(media,1)}")
    time.sleep(2)
#*************************************************************************************************
def destacados():
    base_datos = base_de_datos()
    indices = [indice for indice,nota in enumerate(base_datos["promedio"] )   if nota >= 4  ] #Retorna indice
    notas = [nota for indice,nota in enumerate(base_datos["promedio"] )   if nota >= 4  ]     #Retorna nota
    students_in = [base_datos["nombres"][i]   for i in indices]
    programa = [base_datos["carrera"][i]   for i in indices]
    cant_estud=len(students_in)
    for i in range (cant_estud):
         print(f"Nombre: {students_in[i]}     Nota:{notas[i]}     Programa:{programa[i]}\n")
    time.sleep(3)
#*************************************************************************************************

if __name__ == '__main__':       #Entry point sirve para que se ejecute las pruebas de las funciones
                                 #solo en el lugar donde esta la instrucion y no donde son llamadas 

    main_menu()
            
            
