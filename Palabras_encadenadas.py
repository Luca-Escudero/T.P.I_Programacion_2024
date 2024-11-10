print("Bienvenido al juego de Palabras Encadenadas")

while True:
    palabra_anterior = ""
    palabras_usadas = set()
    puntaje = 0

    while True:
        if palabra_anterior: #verifica si hay palabra anterior
            letra_inicial = palabra_anterior[-1] #si hay toma la ultima letra
            print(f"Tu palabra debe comenzar con '{letra_inicial}'.")
        else:
            letra_inicial = '' #si no hay queda vacia

        palabra_actual = input("Ingresa una palabra: ").lower() # pide al usuario la palabra

        if palabra_actual in palabras_usadas: #verifica que la palabra no se haya usado
            print("Ya usaste esa palabra. Fin del juego.")
            break

        if palabra_anterior and palabra_actual[0] != letra_inicial: #verif. que la ult letra sea igual 
            print(f"La palabra no comienza con la letra '{letra_inicial}'.")
            break
        
        palabras_usadas.add(palabra_actual) # agrega la palabra al conjuntoi de palbras usadas
        puntaje += 1 
        palabra_anterior = palabra_actual
        print(f"¡Correcto! Tu puntaje actual es: {puntaje}")
        
        if puntaje == 10: # El juego termina si el puntaje alcanza 10
            print("¡Felicidades! Has alcanzado las 10 palabras encadenadas.")
            break

    print(f"¡Juego terminado! Tu puntaje final es: {puntaje}")
    print("="*50)

    seguir_jugando = input("¿Quieres jugar de nuevo? Ingresa 1 para continuar o 0 para salir: ").lower()
        
    print("="*50)
    
    # Si el jugador no quiere seguir, termina el bucle
    if seguir_jugando == '0' or seguir_jugando == 'no':
        print("¡Hasta pronto!")  
        break  
   