def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt!")
    except IsADirectoryError:
        print("El archivo config.txt es un directorio!")
    except (BlockingIOError, TimeoutError):
        print("El sistema está saturado, no es posible abrir el archivo config.txt")
if __name__ == '__main__':
    main()