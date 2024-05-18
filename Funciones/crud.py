


animales=["perro","gato","leon","jirafa"]

running = True

while running:

    print("mi zoologico \n") 
    print("opciones")
    opciones= int(input("Ingresa una opcion: \n1. Agregar \n2. Mostrar \n3. Eliminar por indice\n4. Eliminar por nombre \n5. Salir \n"))

    if opciones == 1:
        animal=input("Ingresa animal ")
        animales.append(animal)

    if opciones == 2:
        print(animales)

    if opciones == 3:
            eliminar_index=int(input("Ingrese el indice"))
            animales.pop(eliminar_index)

    if opciones == 4:
         eliminar_palabra= input("Ingresa el animal a eliminar: ")
         animales.remove(eliminar_palabra)

    if opciones == 5:
         
         running = False

    print("\n")
