#entradas
T=int(input("ingrese la temperatura en farenheit "))
#caja negra y salidas
if T>85:
    print("el deporte apropiado de parcticar a esa temperatura es natación ")
if 70<T<=85:
    print("el deporte apropiado de parcticar a esa temperatura es tenis")
if 32<T<=70:
    print("el deporte apropiado de parcticar a esa temperatura es golf ")
if 10<T<=32:
    print("el deporte apropiado de parcticar a esa temperatura es esqui ")
if T<=10:
    print("el deporte apropiado de parcticar a esa temperatura es marcha ")
