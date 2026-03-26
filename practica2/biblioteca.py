# INTEGRANTES:
# Andrea Arana Ore
# Oscar Andrés Delgadillo Alvarado
# Jorge Luis Torrez Garcia
# Gabriela Xiomara Gallardo Flores
# José Luis Romero
class Item:
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio

    def display_info(self):
        print("Título: {self.titulo}")
        print("Año: {self.anio}")


class Libro(Item):
    def __init__(self, titulo, anio, autor):
        super().__init__(titulo, anio)
        self.autor = autor

    def display_info(self):
        print("--------LIBROS--------")
        print(f"Título: {self.titulo}")
        print(f"Año: {self.anio}")
        print(f"Autor: {self.autor}")


class Revista(Item):
    def __init__(self, titulo, anio, numero):
        super().__init__(titulo, anio)
        self.numero = numero

    def display_info(self):
        print("--------REVISTAS--------")
        print(f"Título: {self.titulo}")
        print(f"Año: {self.anio}")
        print(f"Número de Revista: {self.numero}")


def main():
    libreria = []
    while True:

        print("Librería")
        print("1. Añadir un libro")
        print("2. Añadir una Revista")
        print("3. Mostrar todos los productos")
        print("4. Salir")

        opcion = input("Elija una opción ")

        if opcion == "1":
            titulo = input("Inserte el título del libro: ")
            anio = input("Inserte el año del libro: ")
            autor = input("Inserte el autor del libro: ")

            libro = Libro(titulo, anio, autor)
            libreria.append(libro)
            print("Libro añadido correctamente")

        elif opcion == "2":
            titulo = input("Inserte el título de la revista: ")
            anio = input("Inserte el año de la revista: ")
            numero = input("Inserte el número de la revista: ")

            revista = Revista(titulo, anio, numero)
            libreria.append(revista)
            print("Revista añadida correctamente")

        elif opcion == "3":
            print("Productos:")
            for item in libreria:
                item.display_info()
        else:
            print("Opción no válida")
            break


if __name__ == "__main__":
    main()
