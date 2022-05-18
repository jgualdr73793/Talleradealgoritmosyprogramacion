usuarios ={
    "iperurena":{
        "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    },
}
for c in range(1,4,1):
    User = input("Escriba su usuario: ")
    Pass = input("Escriba su password: ")
    if User in usuarios and Pass == usuarios[User]['password']:
        a=usuarios[User]["nombre"]
        b=usuarios[User]["apellido"]
        print(a)
        print(b)
        break
    if c==3:
        print("se acabaron los intentos")
        break
    else:
        print("intentelo denuevo")
    
    

            


