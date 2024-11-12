def jugar_carrera_palabras():
    letras_disponibles = ['t', 'r','a', 'b', 'a', 'j', 'o']

    palabras_disponibles = ["raja", "raba", "rabo", "rajo",
                            "rata", "rato", "roja", "roba","atajo",
                            "ajo", "abajo", "aorta", "abra", "atrajo",
                            "ata", "ato", "aro", "ara","trabajo", "traba","tora","tara"
                            "tajo", "trajo", "trabo", "toba","bajo", "barato", "bar", "bajar",
                            "barajo", "boa", "bota", "baja", "bata", "bato","otra",
                            "jota", "jara"]

    def palabra_valida(palabra_ingresada,palabras_disponibles):
        return palabra_ingresada in palabras_disponibles

    copia_palabras_disponibles = palabras_disponibles.copy()
    def juego ():
        palabras_correctas = 0
        palabras_acertadas = []
        print('¡bienvenido/a a la carrera de palabras!')
        print (f"letras disponibles para formar la mayor cantidad de palabras posibles {',' .join(letras_disponibles)}")
        while True:
            palabra_ingresada = input('ingrese una palabra o salir para finalizar el juego: ').lower()
            #si ingresa salir finaliza el juego
            if palabra_ingresada == "salir":
                break
            elif palabra_ingresada in palabras_acertadas:
                print ('palabra repetida')
                print (f"letras disponibles   {','.join(letras_disponibles)}")
            #para verificar si la palabra ingresada es valida o invalida
            elif palabra_ingresada in copia_palabras_disponibles:
                palabras_correctas += 1 
                print ('palabra correcta',palabras_correctas)
                print (f"letras disponibles   {','.join(letras_disponibles)}")
                
                #si la palabra que se ingresa es correcta agregar a la lista de palabras acertadas
                palabras_acertadas.append(palabra_ingresada)
                # si la palabra ingresada es correcta, para que no se pueda repetir y la tome como valida, la removemos de la copia_palabras_disponibles.
                copia_palabras_disponibles.remove(palabra_ingresada)

            else:
                print('palabra incorrecta')
                print (f"letras disponibles   {','.join(letras_disponibles)}")
        print(f'usted acertó', palabras_correctas,'/', len(palabras_disponibles) )
        print (f"sus palabras acertadas fueron las siguientes:",','.join(palabras_acertadas))

    def jugar_nuevamente():#funcion que pregunta al ususario si desea jugar 
        while True:
            jugar_de_nuevo = input('¿Desea jugar nuevamente? si/no: ').lower()
            if jugar_de_nuevo == 'si':
                juego()
            elif jugar_de_nuevo == 'no':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            else:
                print("Por favor, responde con 'si' o 'no'.")
                
    juego()#para ejecutar el juego
    jugar_nuevamente()#para volver a ejecutar el juego