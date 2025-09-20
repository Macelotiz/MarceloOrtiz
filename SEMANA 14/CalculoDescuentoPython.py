# CALCULO DE DESCUENTO EN COMPRAS

# 1. Creacion de la Función (Creamos la funcion para el descuento)
def calcular_descuento(monto_total, porcentaje_descuento=20):
    """
    Calcula el monto de descuento a aplicar sobre el total de una compra.

    Parámetros:
    monto_total (float): monto total de la compra
    porcentaje_descuento (float, opcional): porcentaje de descuento (por defecto 20%)

    Retorna:
    float: monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# 2. Llamadas a la función (Ingresamos los montos)
# Primera llamada: solo se pasa el monto total (se usa el 10% por defecto)
monto1 = 100
descuento1 = calcular_descuento(monto1)

# Segunda llamada: se pasa el monto total y un porcentaje personalizado (20%)
monto2 = 200
descuento2 = calcular_descuento(monto2, 20)

# 3. Salida de Resultados (Especificamos los resultados)
print("=== RESULTADOS ===")
print(f"Compra 1: Monto total = ${monto1}")
print(f"Descuento aplicado = ${descuento1}")
print(f"Monto final a pagar = ${monto1 - descuento1}\n")

print(f"Compra 2: Monto total = ${monto2}")
print(f"Descuento aplicado = ${descuento2}")
print(f"Monto final a pagar = ${monto2 - descuento2}")
