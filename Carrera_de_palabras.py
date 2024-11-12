def jugar_carrera_palabras():
    import time
    letras_disponibles = ['r', 't','b', 'a', 'j', 'o', 'a']

    palabras_disponibles = ["raja", "raba", "rabo", "rajo",
                            "rata", "rato", "roja", "roba","atajo",
                            "ajo", "abajo", "aorta", "abra", "atrajo",
                            "ata", "ato", "aro", "ara","trabajo", "traba","tora","tara"
                            "tajo", "trajo", "trabo", "toba","bajo", "barato", "bar", "bajar",
                            "barajo", "boa", "bota", "baja", "bata", "bato","otra",
                            "jota", "jara"]#diccionaio de palabras correctas



    def juego ():
        copia_palabras_disponibles = palabras_disponibles.copy()#creamos una copia del diciconario para poder modificarlo
        palabras_correctas = 0
        palabras_acertadas = []
        inicio = time.time()
        print('¡Bienvenido/a a la carrera de palabras!\n')
        print (f"Intente formar la mayor cantidad de palabras con las siguientes letras {'-' .join(letras_disponibles)}")
        while True:
            palabra_ingresada = input('\nIngrese una palabra o salir para finalizar el juego: ').lower()
            
            if palabra_ingresada == "salir":#si ingresa salir finaliza el juego
                break
            elif palabra_ingresada in palabras_acertadas:#para verificar si la palabra ingresada es valida o invalida
                print ('\nPalabra repetida')
                print (f"Letras disponibles   {'-'.join(letras_disponibles)}")
            
            elif palabra_ingresada in copia_palabras_disponibles:#si ingresa una palabra correcta agregar a lista palabras acertadas.
                palabras_correctas += 1 
                print ('\nPalabra correcta',palabras_correctas)
                print (f"Letras disponibles   {'-'.join(letras_disponibles)}")
                
                palabras_acertadas.append(palabra_ingresada)
                copia_palabras_disponibles.remove(palabra_ingresada)
                # si la palabra ingresada es correcta, para que no se pueda repetir y la tome como valida,
                # la removemos de la copia_palabras_disponibles.

            else:
                print('\nPalabra incorrecta')
                print (f"\nLetras disponibles   {','.join(letras_disponibles)}")
        fin =time.time()
        tiempo_total = round(fin-inicio,2)
        print ("_"*144)#multiplico el ("_")
        print(f'\nUsted acertó', palabras_correctas,'/', len(palabras_disponibles) )
        print (f"Sus palabras acertadas fueron las siguientes:",' - '.join(palabras_acertadas))
        print (f"tiempo total: {tiempo_total} segundos")
        print ("_"*144)

    def jugar_nuevamente():#funcion para preguntar al usuario si desea jugar nuevamente o no.
        while True:
            jugar_de_nuevo = input('\n¿Desea jugar nuevamente? si/no: ').lower()
            if jugar_de_nuevo == 'si':
                juego()
            elif jugar_de_nuevo == 'no':
                print("\nGracias por jugar. ¡Hasta la próxima!\n")
                break
            else:
                print("\nPor favor, responde con SI o NO.")

    juego()#para ejecutar eljuego
    jugar_nuevamente()#para ejecutar nuevamente el juego