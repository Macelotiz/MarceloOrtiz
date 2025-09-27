# -------------------------------
# Tarea: Trabajando con Diccionarios en Python
# -------------------------------

# 1) Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Marcelo Ortiz",   # Nombre ficticio
    "edad": 36,                 # Edad ficticia
    "ciudad": "Guayaquil",         # Ciudad inicial
    "profesion": None           # Profesión inicialmente vacía
}

# 2) Acceder al valor de "ciudad" y modificarlo
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Quito"   # Nueva ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])

# 3) Agregar o modificar la clave "profesion"
informacion_personal["profesion"] = "Ingeniero"

# 4) Verificar si la clave "telefono" existe; si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593002244889"   # Número ficticio

# 5) Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# 6) Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
