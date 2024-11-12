import random

# Diccionario de países y sus capitales
paises_capitales = {
    "España": "Madrid", "Francia": "París", "Italia": "Roma", "Alemania": "Berlín",
    "Portugal": "Lisboa", "Inglaterra": "Londres", "China": "Pekín", "Japón": "Tokio",
    "Brasil": "Brasilia", "Argentina": "Buenos Aires", "México": "Ciudad de México", 
    "Colombia": "Bogotá", "Perú": "Lima", "Chile": "Santiago", "Uruguay": "Montevideo",
    "Ecuador": "Quito", "Bolivia": "La Paz", "Venezuela": "Caracas", "Paraguay": "Asunción",
    "Cuba": "La Habana", "Canadá": "Ottawa", "Egipto": "El Cairo", "Australia": "Canberra",
    "Rusia": "Moscú", "India": "Nueva Delhi", "Sudáfrica": "Pretoria", "Indonesia": "Yakarta", 
    "Suecia": "Estocolmo", "Grecia": "Atenas", "Turquía": "Ankara", "Pakistán": "Islamabad",
    "Nigeria": "Abuya", "Corea del Sur": "Seúl", "Arabia Saudita": "Riad", "Bangladesh": "Daca",
    "Filipinas": "Manila", "Irán": "Teherán", "Irak": "Bagdad", "Tailandia": "Bangkok",
    "Kenia": "Nairobi", "Qatar": "Doha",
    "Polonia": "Varsovia", "Bélgica": "Bruselas", "Finlandia": "Helsinki", "Suiza": "Berna",
    "Noruega": "Oslo", "Dinamarca": "Copenhague", "Países Bajos": "Ámsterdam", "Hungría": "Budapest",
}

# Función para mensaje de bienvenida
def mensaje_bienvenida():
    print("--- ¡Bienvenido al juego de seleccionar la capital correcta! --- ")
    print("Selecciona la capital correcta de cada país aleatorio. \n")

def generar_opciones(correcta):
    opciones = random.sample([capital for capital in paises_capitales.values() if capital != correcta], 3)  # Selecciona 3 capitales aleatorias
    opciones.append(correcta)  # Añade la capital correcta a las opciones
    random.shuffle(opciones)  # Mezcla las opciones
    return opciones  # Devuelve las opciones

def jugar_geo_capital():
    mensaje_bienvenida()  # Muestra el mensaje de bienvenida
    puntos = 0  # Inicia el contador desde 0

    preguntas = random.sample(list(paises_capitales.items()), 8)  # Elige 8 países aleatorios

    for pais, capital_correcta in preguntas:  # Itera sobre los países y capitales
        opciones = generar_opciones(capital_correcta)  # Obtiene las opciones

        print(f"¿Cuál es la capital de {pais}?")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        respuesta = input("Elige la opción correcta (1-4): ")
        while not respuesta.isdigit() or int(respuesta) not in range(1, 5):  # Verifica si la respuesta es válida
            print("No es una respuesta válida. Debe ser un número entre el 1 y el 4.")
            respuesta = input("Inserte la opción que es (1-4): ")

        respuesta = int(respuesta)  # Convierte la respuesta a entero
        if opciones[respuesta - 1] == capital_correcta:  # Verifica si la respuesta es correcta
            print("¡Correcto! +1 punto \n")
            puntos += 1
        else:
            print(f"Incorrecto. La capital correcta era {capital_correcta}.\n")

    print(f"Puntaje final: {puntos}/8")
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").strip().lower()
    if jugar_de_nuevo == "si":
        jugar_geo_capital()  # Si el usuario quiere jugar de nuevo, se llama a la función jugar
    else:
        print("----- ¡Gracias por jugar! ¡Adiós! -----")

