def mostrar_menu():
    print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (burbuja)")
    print("9. Ordenar cursos por nombre (inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")

def leer_opcion ():
    while True:
        valor = input("Seleccione una opcion: ").strip #eliminar los espacios en blanco
        if valor =="":
            print("Debe eligir una opcion")
            continue
        try:
            return int(valor)
        except ValueError:
           print("opcion invalida. Ingrese un numero")
def registrar_curso():
    nombre= input("Ingrese el nombre del curso: ") .strip() #Limpia el texto que el usuario escribió, quitando espacios vacíos al principio y al final.
    if nombre == "":#Aquí el programa verifica si el usuario no escribió nada (es decir, si nombre está vacío)
        print ("El nombre esta vacio.")
        return
    try: #esto nos ayuda para ver si el usuario escribe un error como letras o numeros
        nota = float (input("Ingrese la nota del curso (0-100): "))
        if 0 <= nota <= 100:# revisa que el dato ingresado este dentro del rango requerido
            cursos.append({"Nombre":nombre,"nota": nota})
            print("Curso registrado con exito.")
        else:
            print("La nota debe de estar entre 0 y 100.")
    except ValueError:# notiica al usuario que tuvo error y envia el mensaje
        print("Error:La nota debe ser numerica.")
        # mostrar todos los cursos

def mostrar_cursos(): # muestra todos los cursos guardados en la lista
    if not cursos: # verifica si la lista esta vacia 
        print("No hay cursos registrados.")
        return
    print("\nCursos registrados:")
    for i, c in enumerate(cursos, start=1):# el for sirve para recurrer la lista de cursos uno por uno
        # i es el numero de cursos y c es el curso en si mismo y start inicia la numeracion del 1 y no del cero
        print(f"{i}. {c['nombre']} - Nota: {c['nota']}")     
        # 3. Calcular promedio
def calcular_promedio():
    if not cursos:# si la lista esta vacia 
        print("No hay cursos registrados.")
        return
    promedio = sum(c["nota"] for c in cursos) / len(cursos) # es un mini bucle que toma solo la parte numerica de las notas en el curso
    print(f"Promedio general: {promedio:.2f}")   # fstring es una forma de escribir texto con variables
    #2f es que monstrara dos decimales ejemplo 8.22222 mostrara 8.22
    # 4. Contar aprobados/reprobados
def contar_aprobados_reprobados():#contar cuántos cursos tienen nota mayor o igual a 60
    if not cursos:
        print("No hay cursos registrados.")
        return
    aprobados = sum(1 for c in cursos if c["nota"] >= 60) #aqui se va sumando los cursos aprovados sum los suma los cursos mayor a 60
    reprobados = len(cursos) - aprobados#len cursos se calculo cuantos cursos fueron aprobados 
    #Si le restamos los aprobados, nos da los reprobados.
    print(f"Aprobados: {aprobados}, Reprobados: {reprobados}")# la f permite escribir varibles dentro del texto y llmarlas
    # 5. Buscar curso (lineal)
def buscar_curso_lineal():
    if not cursos:
        print("No hay cursos registrados.")
        return
    nombre = input("Ingrese el nombre del curso a buscar: ").strip().lower() # el .strip elimina los espacios del principio y del fin 
    #.lower covierte todo a miniscula por lo que Mate y mate es igual 
    for curso in cursos:# recorre todos los cursos guardado en la lista 
        if curso["nombre"].lower() == nombre:#curso["nombre"].lower() en esto se hace la comoparacion entre el nombre escrito antes con el nuevo que se ingreso a buscar
            print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']}")# busca el resultado nombre mas la nota
            return
    print("Curso no encontrado.")
# 6. Actualizar curso
def actualizar_curso():
    if not cursos:#busca si la lista esta vacia
        print("No hay cursos registrados.")
        return
    nombre = input("Ingrese el nombre del curso a actualizar: ").strip().lower()#se ingrese el nombre y .strip borra espacios y lower compara nombres entre mayuscula y miniscula
    for curso in cursos:
        if curso["nombre"].lower() == nombre:
            try:#
                nueva_nota = float(input("Ingrese la nueva nota: "))#aqui el usuario ingresa la nueva nota el float para si desea ingresar decimal
                if 0 <= nueva_nota <= 100:# evalua si la nota esta entre 0 y 100
                    historial.append(f"Se actualizó: {curso['nombre']} - Nota anterior: {curso['nota']} → Nueva nota: {nueva_nota}")#control de los cambios realizados.
                    curso["nota"] = nueva_nota# reemplaza la nota anitgua por la nueva
                    print(" Nota actualizada con éxito.")
                else:
                    print("La nota debe estar entre 0 y 100.")
                return
            except ValueError:# si el usuario escribe un numero en letras dice que el valor a ingresar debe de ser numerico
                print("Error: la nota debe ser numérica.")
                return
    print("Curso no encontrado.")
    # 7. Eliminar curso
def eliminar_curso(): #aqui es una funcion para eliminar cursos de la lista
    if not cursos:# verifica si la lista esta vacia
        print("No hay cursos registrados.")#da el mensaje que no hay cursos 
        return
    nombre = input("Ingrese el curso a eliminar: ").strip().lower()# se ingrese el curso a eliminar .strip borra los espacios y lower hace que sean iguales
    for curso in cursos:
        if curso["nombre"].lower() == nombre:
            confirmacion = input(f"¿Está seguro que desea eliminar '{curso['nombre']}'? (s/n): ").lower()
            #aqui pregunta al usuario si esta seguro de eliminar y da el nombre del curso si escribe s se guarda y n no
            if confirmacion == "s": #verifica la respuesta del usuario que guardamos en la varible de confirmacion
                historial.append(f"Se eliminó: {curso['nombre']} - Nota: {curso['nota']}")# lo elimina en el registro que se lleva en el historial
                cursos.remove(curso)
                print(" Curso eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    print("Curso no encontrado.")
# 8. Ordenar por nota (burbuja)
def ordenar_por_nota():
    n = len(cursos) # en la varible n se guarda el total de curso de la lista 
    #Esto es importante porque necesitaremos saber cuántas veces repetir los pasos para comparar cada curso con los demás.
    for i in range(n):#el bucle sirve para repetir el proceso de comparacion 
        for j in range(0, n - i - 1): # este otro bucle sirve para comparar los elementos que ya estan ordenados 
            if cursos[j]["nota"] < cursos[j + 1]["nota"]:# esta condicion compara la nota actual con la siguiente nota
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j] #Aquí se realiza el intercambio de posiciones entre los dos cursos
    print("\nCursos ordenados por nota (de mayor a menor):")
    mostrar_cursos()
    # 9. Ordenar por nombre (inserción)
def ordenar_por_nombre():
    for i in range(1, len(cursos)):# este es un bucle recorre los cursos desde el segundo elemento ya que el insercion parte de la idea de que el primer el elemento ya esta ordenado
        actual = cursos[i]#Guarda el curso actual (el que queremos colocar en su posición correcta) dentro de la variable actual
        j = i - 1#Sirve para comparar el curso que estamos ordenando (actual) con los que ya están antes de él
        while j >= 0 and cursos[j]["nombre"].lower() > actual["nombre"].lower():
        #Este bucle while compara los nombres de los cursos uno por uno hacia atrás
       #asegura que no se salga del rango de la lista lo de j


            cursos[j + 1] = cursos[j]#Mueve el curso anterior una posición hacia adelante para hacer espacio al curso que queremos insertar
            j -= 1
        cursos[j + 1] = actual#Cuando encuentra la posición correcta, coloca ahí el curso que estaba guardado en actual.
     #Así, el curso queda insertado en su orden alfabético correcto
    print("\nCursos ordenados alfabéticamente:")
    mostrar_cursos()

# 10. Buscar curso (binaria)
def buscar_curso_binario():
    if not cursos:
        print("No hay cursos registrados.")
        return
    ordenar_por_nombre()
    nombre = input("Ingrese el nombre del curso a buscar: ").strip().lower()#Aquí el usuario escribe el nombre del curso que quiere buscar
    izquierda, derecha = 0, len(cursos) - 1
    while izquierda <= derecha:#Estas dos variables marcan los límites de la búsqueda
        medio = (izquierda + derecha) // 2#Este bucle se repite mientras los límites no se crucen, es decir, mientras aún haya elementos por revisar
        if cursos[medio]["nombre"].lower() == nombre:
            print(f"Curso encontrado: {cursos[medio]['nombre']} - Nota: {cursos[medio]['nota']}")
            return
        elif cursos[medio]["nombre"].lower() < nombre:#Si el nombre del curso en el medio está antes alfabéticamente que el que buscamos,
#significa que el curso está a la derecha del medio
            izquierda = medio + 1
        else:
            derecha = medio - 1 # no, el curso está a la izquierda, y se reduce el rango:
    print("Curso no encontrado (búsqueda binaria).")
    # 11. Cola de revisión
def simular_cola_revision():
    cola = []#Se crea una lista vacía llamada cola, que se usará para guardar los cursos que el usuario vaya escribiendo
    print("Ingrese cursos para revisión ('fin' para terminar):")
    while True:#Crea un bucle infinito que se repetirá hasta que el usuario escriba “fin”
        curso = input("> ").strip() #Aquí el programa le pide al usuario que escriba el nombre del curso.
        if curso.lower() == "fin":# verifica si el usuario escribio fin sin importar las mayusculas o minusculas
            break
        cola.append(curso)#Si el usuario no escribió “fin”, el curso se agrega al final de la cola
    print("\nProcesando solicitudes:")
    while cola:#Este bucle se ejecuta mientras la cola tenga elementos
        actual = cola.pop(0)#.pop extrae el primer elemento de la lista, o sea, el primer curso que entró
        print(f"Revisando: {actual}")#Muestra el nombre del curso que se está revisando
        # 12. Mostrar historial (pila)
def mostrar_historial():
    if not historial:
        print("No hay cambios registrados.")
        return
    print("\nHistorial de cambios recientes:")#Si la pila sí tiene datos, se muestra un encabezado indicando que el usuario está por ver los últimos cambios
    for i, h in enumerate(reversed(historial), start=1):#Muestra los elementos al revés, porque una pila funciona con el principiO
        #LIFO, o sea que el último cambio realizado es el primero que se muestra.
        print(f"{i}. {h}")#Numera automáticamente cada elemento que se imprime, empezando desde 1
        # 13. Control principal
def ejecutar_opcion(opcion):
    if opcion == 1: registrar_curso()
    elif opcion == 2: mostrar_cursos()
    elif opcion == 3: calcular_promedio()
    elif opcion == 4: contar_aprobados_reprobados()
    elif opcion == 5: buscar_curso_lineal()
    elif opcion == 6: actualizar_curso()
    elif opcion == 7: eliminar_curso()
    elif opcion == 8: ordenar_por_nota()
    elif opcion == 9: ordenar_por_nombre()
    elif opcion == 10: buscar_curso_binario()
    elif opcion == 11: simular_cola_revision()
    elif opcion == 12: mostrar_historial()
    elif opcion == 13:
        print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
        return False
    else:
        print("Opción no válida.")
    return True