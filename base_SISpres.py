#Programa genreador de presupuestos 
#Autor: Sergio Ismael Sosa
#Fecha: 2024-06-01      
#Definimos una función para calcular el presupuesto
def calcular_presupuesto(costo_materiales, costo_mano_obra, costo_gastos_generales):
    # Calculamos el costo total sumando los costos individuales
    costo_total = costo_materiales + costo_mano_obra + costo_gastos_generales
    return costo_total                      
#Solicitamos al usuario que ingrese los costos
costo_materiales = float(input("Ingrese el costo de los materiales: "))         
costo_mano_obra = float(input("Ingrese el costo de la mano de obra: "))
costo_gastos_generales = float(input("Ingrese el costo de los gastos generales: "))         
#Calculamos el presupuesto total utilizando la función definida
presupuesto_total = calcular_presupuesto(costo_materiales, costo_mano_obra, costo_gastos_generales)
#Mostramos el resultado al usuario      
print(f"El presupuesto total es: {presupuesto_total:.2f}")  

                                                                                                                            