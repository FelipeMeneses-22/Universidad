#Enunciado: Diseña un sistema para gestionar una biblioteca. Crea una clase Libro que contenga los atributos título, autor y número de páginas. La clase Ebook hereda de Libro y agrega el formato del libro (por ejemplo, "PDF", "EPUB"). Usa setters y getters para manipular los atributos. Implementa un menú que permita:

#Registrar libros.
#Registrar ebooks.
#Mostrar todos los libros y ebooks.
#Modificar el formato de un ebook registrado.
#Clases involucradas:

#Libro: título, autor, número de páginas.
#Ebook: hereda de Libro y añade formato.

# ----------------------------------------
# author : Juan Felipe Meneses Rodriguez
# Estudio: Semestre II / Ingenieria en sistemas
# Fecha creación : 18/10/2024
# ----------------------------------------

#------------clase base------------
class Libro:
    def __init__(self, titulo, autor, paginas) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
        
    def __str__(self) -> str:
        return f"Título: {self.getTitulo}, Autor: {self.getAutor}, Páginas: {self.getPaginas}"
        
# --------SETTERS Y GETTERS--------------

    @property
    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    @property
    def getAutor(self):
        return self.__autor

    def setAutor(self, autor):
        self.__autor = autor

    @property
    def getPaginas(self):
        return self.__paginas

    def setPaginas(self, paginas):
        self.__paginas = paginas


# -----------------clase que hereda---------------
class Ebook(Libro):
    def __init__(self, titulo, autor, paginas, formato) -> None:
        super().__init__(titulo, autor, paginas)
        self.__formato = formato

    def __str__(self):
        return f"{super().__str__()}, Formato: {self.__formato}"

    @property
    def getFormato(self):
        return self.__formato

    def setFormato(self, formato):
        self.__formato = formato


# -----clase de interacción---------

class SistemaBiblioteca:
    def __init__(self):
        self.listaLibros = []
        self.listaEbooks = []
    
    # Método para agregar libros a la lista
    def agregarLibro(self, libro):
        self.listaLibros.append(libro)
        print(f"El libro '{libro.getTitulo}' se agregó con éxito")
    
    def agregarEbook(self, ebook):
        self.listaEbooks.append(ebook)
        print(f"El ebook '{ebook.getTitulo}' se agregó con éxito")
    
    # Método para registrar un libro o ebook
    def registrarLibro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        paginas = input("Ingrese el número de páginas: ")
        es_ebook = input("¿Es un ebook? (s/n): ").lower()
        
        if es_ebook == "s":
            formato = input("Ingrese el formato del ebook (PDF, EPUB, etc.): ")
            nuevoLibro = Ebook(titulo, autor, paginas, formato)
            self.agregarEbook(nuevoLibro)
        else:
            nuevoLibro = Libro(titulo, autor, paginas)
            self.agregarLibro(nuevoLibro)
    
    # Mostrar los libros y ebooks registrados
    def mostrarLibros(self):
        if self.listaLibros:
            print("\nLibros registrados:")
            for libro in self.listaLibros:
                print(libro)
        else:
            print("\nNo hay libros registrados.")

    def mostrarEbooks(self):
        if self.listaEbooks:
            print("\nEbooks registrados:")
            for ebook in self.listaEbooks:
                print(ebook)
        else:
            print("\nNo hay ebooks registrados.")
    
    # Menú de interacción con el usuario
    def menu(self):
        while True:
            print("\n  Bienvenido al sistema de gestión de biblioteca \n \n\
                    1. Registrar Libro/Ebook \n\
                    2. Mostrar lista de Libros \n\
                    3. Mostrar lista de Ebooks \n\
                    4. Salir")
            
            opcion = int(input("\n Ingrese la opción que desea realizar: "))
            
            if opcion == 1:
                self.registrarLibro()
            
            elif opcion == 2:
                self.mostrarLibros()
            
            elif opcion == 3:
                self.mostrarEbooks()
            
            elif opcion == 4:
                print("Saliendo del menú.")
                break
                
            else:
                print("Opción incorrecta")


# ----------Inicializando el menú-----------------
sisBiblioteca = SistemaBiblioteca()
sisBiblioteca.menu()