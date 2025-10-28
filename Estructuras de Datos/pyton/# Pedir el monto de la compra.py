# Pedir el monto de la compra
monto = float(input("Ingresa el monto de la compra: "))

# Calcular el precio final con o sin descuento
if monto > 500:
    descuento = monto * 0.10
    total = monto - descuento
    print(f"Se aplicó un 10% de descuento. Total a pagar: ${total:.2f}")
else:
    print(f"No hay descuento. Total a pagar: ${monto:.2f}")
