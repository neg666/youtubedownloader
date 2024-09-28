import subprocess
import sys
import os

# Función para verificar e instalar dependencias
def verificar_instalar_dependencias():
    # Lista de dependencias necesarias
    dependencias = ["yt-dlp"]  # Cambia a "youtube-dl" si prefieres usar esa librería

    for paquete in dependencias:
        try:
            __import__(paquete)  # Intenta importar el paquete
        except ImportError:
            print(f"{paquete} no está instalada. Procediendo a instalarla...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
            print(f"Instalación de {paquete} completada.")
    
    print("Todas las dependencias están satisfechas.")

# Mostrar el logo de YouTube en formato ASCII
def mostrar_logo():
    print("██╗   ██╗ ██████╗ ██╗   ██╗████████╗ ██████╗ ██╗   ██╗███████╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔═══██╗██║   ██║██╔════╝")
    print(" ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██║   ██║█████╗  ")
    print("  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██║   ██║██╔══╝  ")
    print("   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗")
    print("   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝")
    print("                      YouTube Video Downloader                ")
    print("-------------------------------------------------------------\n")

# Función que muestra el menú
def menu():
    print("---- Descargador de Videos de YouTube ----")
    print("1. Descargar video en máxima calidad")
    print("2. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

# Función para descargar el video usando yt-dlp
def descargar_video(link):
    try:
        carpeta_descargas = os.path.expanduser("~/Videos")  # Puedes cambiar la ruta de descarga aquí
        comando = ["yt-dlp", "-f", "best", "-o", f"{carpeta_descargas}/%(title)s.%(ext)s", link]
        subprocess.run(comando)
        print(f"Descarga completada! El archivo se guardó en {carpeta_descargas}")
    except Exception as e:
        print(f"Error: {e}")

# Función principal del script
def main():
    verificar_instalar_dependencias()  # Verificar e instalar dependencias antes de ejecutar el resto
    mostrar_logo()  # Mostrar el logo al inicio del programa
    while True:
        opcion = menu()
        if opcion == "1":
            link = input("Ingresa el link del video de YouTube: ")
            descargar_video(link)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()

