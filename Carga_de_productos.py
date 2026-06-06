IVA = 0.21
GANANCIA = 0.17

productos = []

cantidad_productos = int(input("¿Cuántos productos desea ingresar?: "))

for i in range(cantidad_productos):

    print(f"\nProducto {i + 1}")

    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    costo_unitario = float(input("Costo unitario: "))

    costo_total = cantidad * costo_unitario

    ganancia = round (costo_total * GANANCIA,2)

    precio_sin_iva = round(costo_total + ganancia,2)

    iva = round(precio_sin_iva * IVA,2)

    precio_final = round(precio_sin_iva + iva,2)

    producto = {
        "descripcion": descripcion,
        "cantidad": cantidad,
        "costo_unitario": costo_unitario,
        "costo_total": costo_total,
        "ganancia": ganancia,
        "precio_final": precio_final
    }

    productos.append(producto)

print("\nRESUMEN\n")

for producto in productos:

    print("\n----------------")

    print("Producto:", producto["descripcion"])

    print("Cantidad:", producto["cantidad"])

    print("Costo Total:", producto["costo_total"])

    print("Ganancia:", producto["ganancia"])

    print("Precio Final:", producto["precio_final"])

total_presupuesto = 0

for producto in productos:
    total_presupuesto += producto["precio_final"]

print("\nTOTAL PRESUPUESTO")
print(total_presupuesto)

from openpyxl import Workbook

libro = Workbook()

hoja = libro.active

hoja.title = "Inventario"

hoja.append(["Producto", "Cantidad"])

for producto in productos:

    hoja.append([
        producto["descripcion"],
        producto["cantidad"]
    ])

libro.save("inventario.xlsx")

print("\nArchivo Excel generado correctamente")