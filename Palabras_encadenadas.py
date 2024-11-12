def jugar_palabras_encadenadas():  
    print("🎉 ¡Bienvenido al juego de Palabras Encadenadas! 🎉")
    print("Instrucciones:")
    print("🔹 Ingresa una palabra que comience con la última letra de la palabra anterior.")
    print("🔹 No puedes repetir palabras ya usadas.")
    print("🔹 ¡Veamos cuántas palabras puedes encadenar! 💪")
    print("=" * 50)
    
    nombre_jugador = input("🖊️  Ingresa tu nombre: ")  # Pide el nombre del jugador

    while True:
        palabra_anterior = ""
        palabras_usadas = set()
        puntaje = 0

        while True:
            if palabra_anterior: # verifica si hay palabra anterior
                letra_inicial = palabra_anterior[-1] # si hay, toma la última letra
                print("=" * 50)
                print(f"👉 Tu palabra debe comenzar con '{letra_inicial}'.")
            else:
                letra_inicial = '' # si no hay, queda vacía

            palabra_actual = input("💬 Ingresa una palabra: ").lower()  # Pide al usuario la palabra

            if palabra_actual in palabras_usadas: # verifica que la palabra no se haya usado
                print("="*50)
                print("🚫 Ya usaste esa palabra. Fin del juego.")
                break

            if palabra_anterior and palabra_actual[0] != letra_inicial: # verifica que la primera letra coincida
                print("="*50)
                print(f"🚫 La palabra no comienza con la letra '{letra_inicial}'.")
                break
            
            palabras_usadas.add(palabra_actual) # agrega la palabra al conjunto de palabras usadas
            puntaje += 1 
            palabra_anterior = palabra_actual
            print(f"✅ ¡Correcto! Tu puntaje actual es: {puntaje}")
            
            if puntaje == 10: # El juego termina si el puntaje alcanza 10
                print("🎉 ¡Felicidades! Has alcanzado las 10 palabras encadenadas.")
                break

        print(f"🎊 ¡Juego terminado! Tu puntaje final es: {puntaje} 🎊")
        print("="*50)

        # Guardar el nombre del jugador y el puntaje en un archivo
        with open("puntajes.txt", "a") as archivo:  # Abre el archivo en modo adjuntar
            archivo.write(f"Nombre: {nombre_jugador}, Puntaje: {puntaje}\n")  # Guarda nombre y puntaje

        print("📄 Puntaje guardado en 'puntajes.txt'.")  # Notifica al usuario que el puntaje fue guardado
        
        seguir_jugando = input("¿Quieres jugar de nuevo? Ingresa 1 para continuar o 0 para salir: ").lower()
            
        print("="*50)
        
        # Si el jugador no quiere seguir, termina el bucle
        if seguir_jugando == '0' or seguir_jugando == 'no':
            print("¡Hasta pronto!")  
            break  
