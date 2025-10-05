# Tarea: Trabajo con Archivos de Texto en Python

# 1. Escritura de Archivo de Texto
# Creamos un archivo llamado "my_notes.txt" en modo escritura ("w").

archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando write().
archivo.write("Nota 1: Hoy ha sido el mejor día de mi vida mañana será mucho mejor.\n")
archivo.write("Nota 2: El éxito es la suma de pequeños esfuerzos repetidos día tras día.\n")
archivo.write("Nota 3: La tecnolgía es la herramienta, tu mente la solución.\n")

# Cerramos el archivo después de escribir.
archivo.close()


# 2. Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ("r").
archivo = open("my_notes.txt", "r")

# Leemos línea por línea usando readline().
# readline() devuelve una línea completa cada vez que se llama.
print("Contenido del archivo my_notes.txt:\n")

linea = archivo.readline()  # Leemos la primera línea
while linea != "":  # Mientras no lleguemos al final del archivo
    print(linea.strip())  # Mostramos la línea sin saltos extra
    linea = archivo.readline()  # Leemos la siguiente línea

# 3. Cierre de Archivos
archivo.close()  # Siempre cerramos el archivo después de leerlo
