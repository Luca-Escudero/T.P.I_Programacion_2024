# Importa las funciones de cada juego
from Palabras_encadenadas import jugar_palabras_encadenadas
from Carrera_de_palabras import jugar_carrera_palabras
from geo_capital import jugar_geo_capital

def mostrar_menu():
    print("\n" + "=" * 30)
    print("🎉 ¡Bienvenidos! 🎉")
    print("=" * 30)
    print("Selecciona tu juego:")
    print("1️⃣  Palabras Encadenadas")
    print("2️⃣  Carrera de Palabras")
    print("3️⃣  Geo Capital")
    print("0️⃣  Salir")
    print("=" * 30)

def seleccionar_juego():
    while True:
        mostrar_menu()
        opcion = input("\nIngresa el número de tu elección (0-3): ")
        
        if opcion == "1":
            print("\n🟢 Iniciando Palabras Encadenadas...\n" + "=" * 30)
            jugar_palabras_encadenadas()
        elif opcion == "2":
            print("\n🟢 Iniciando Carrera de Palabras...\n" + "=" * 30)
            jugar_carrera_palabras()
        elif opcion == "3":
            print("\n🟢 Iniciando Adivina la Capital...\n" + "=" * 30)
            jugar_geo_capital()
        elif opcion == "0":
            print("\n👋 ¡Gracias por jugar! Hasta luego.\n" + "=" * 30)
            break
        else:
            print("🚫 Opción no válida. Intente nuevamente.\n" + "=" * 30)

# Ejecuta el menú principal solo si el archivo es ejecutado directamente
if __name__ == "__main__":
    seleccionar_juego()
