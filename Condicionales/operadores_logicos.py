



print("Hola soy el portero de la discoteca\n")

edad= int(input("Dime tu edad: "))
hora= int(input("Son las: <Ingresa la hora> "))
adulto_contigo = input("Vienes acompanado de un adulto: ")



if (edad >= 18 or adulto_contigo== "si") and hora>8:
    print("Puedes pasar ")

elif (edad<18 or adulto_contigo == "no") and hora>8:
    print("Eres muy pequeño, ven con un adulto")

else:
    print("Todavia no son mas de las 8")


