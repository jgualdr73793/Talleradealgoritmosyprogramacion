#entradas
total_de_la_compra=int(input("ingrese el precio del producto "))
#caja negra
descuento=(total_de_la_compra*15)/100
valor_total_a_pagar=total_de_la_compra-descuento
#salidas
print("el valor a pagar por el producto con el descuento es: ", valor_total_a_pagar)