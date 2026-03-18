class Libro:
    def __init__(self,titulo,autor,anioPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion

    def descripcion(self):
        return (f"Hola este libro {self.titulo} es muy feo por que el autor '{self.autor}' no sabe escribir desde que publico el libro en el año {self.anioPublicacion}  ")

libro = Libro(autor="Felipe Meneses",titulo="'Detras del ultimo no hay nadie'", anioPublicacion=2002 )

print(libro.descripcion())