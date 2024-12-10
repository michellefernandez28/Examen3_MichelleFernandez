## hacer un programa para registrar a estudiantes en una sección X, ademas tengo que pedir contraseñas
##voy a poner el cosito para que se limpie porque no me gusta ver la terminal llena
import os
os.system("cls")


datos_ingreso = ["abc" , 123]
intentos_ingreso = 1

#abro bucle para pedir la contraseña
for intento_ingreso in range(1,4):
    usuario_solicitado = input("Ingrese el nombre de usuario:__")
    contraseña_solicitada = input("Ingrese la contraseña:___")
    if usuario_solicitado != datos_ingreso[0] or contraseña_solicitada != datos_ingreso[1]:
        print("Lo sentimos, datos de ingreso incorrecto, intentelo de nuevo")


#aqui hago las funciones que son las que me van a dejar agregar la informacion y guardarla
#creo que primero deberia hacer una que tenga solo las secciones y otra que pueda meter dentro de cada una para agregar los datos del estudiante


def inscripcion_estudiante ():
    nombre_estudiente = input("Ingrese el nombre de la persona estudiante, sin los apellidos:__").title() #el title es para que me ponga las iniciales en mayuscula y se vea lindo
    apellido_estudiante = input("Ingrese los apellidos de la persona estudiante:___").title()
    cedula_estudiante = int(input("Digite el número de cédula sin espacio ni guiones:____"))

def grupo_seccion():
    print("Seleccione uno de los siguientes grupos para hacer la inscripción")
    print("1. Sección 7-4")
    print("2. Sección 8-6")
    print("3. Seccion 9-1")
    print("4. Sección 10-7")
    print("5. Sección 11-6")
    grupo_seleccionado = input("Digite el grupo que sea completar:___")
    if grupo_seleccionado == "1":
        inscripcion_estudiante()
    elif grupo_seleccionado == "2":
        inscripcion_estudiante()
    elif grupo_seleccionado == "3":
        inscripcion_estudiante()
    elif grupo_seleccionado == "4":
        inscripcion_estudiante()
    elif grupo_seleccionado == "5":
        inscripcion_estudiante()
        
def consulta_seccion():
    while True:
        print("")       
    
    
    
    
    
    


def menu_inscripciones():
    while True:
        print("___BIENVENIDO AL MENÚ PRINCIPAL___")
        print("1. Inscripción de estudiantes")
        print("2. Consulta por sección")
        print("3. Salir")
        seleccion = input("Seleccione una de las opciones anteriores:___")
        if seleccion == "1":
            grupo_seccion()#tengo que que hacer primero las funciones
        elif seleccion == "2": #porque me da error si antes he usado eso igual?
            
        elif seleccion == "3":
            break
        