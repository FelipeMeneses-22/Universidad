# ------------clase base Cliente------------
class Cliente:
    def __init__(self, nombre, identificacion) -> None:
        self.__nombre = nombre
        self.__identificacion = identificacion

    def __str__(self) -> str:
        return f"Nombre: {self.getNombre}, ID: {self.getIdentificacion}"

# --------SETTERS Y GETTERS--------------
    @property
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    @property
    def getIdentificacion(self):
        return self.__identificacion

    def setIdentificacion(self, identificacion):
        self.__identificacion = identificacion

# -----------------clase que hereda ClienteVIP---------------
class ClienteVIP(Cliente):
    def __init__(self, nombre, identificacion, nivelVIP) -> None:
        super().__init__(nombre, identificacion)
        self.__nivelVIP = nivelVIP

    def __str__(self):
        return f"{super().__str__()}, Nivel VIP: {self.getNivelVIP}"

    @property
    def getNivelVIP(self):
        return self.__nivelVIP

    def setNivelVIP(self, nivelVIP):
        self.__nivelVIP = nivelVIP

# ------------------clase Pelicula------------------
class Pelicula:
    def __init__(self, titulo, duracion, genero) -> None:
        self.__titulo = titulo
        self.__duracion = duracion
        self.__genero = genero

    def __str__(self) -> str:
        return f"Título: {self.getTitulo}, Duración: {self.getDuracion} min, Género: {self.getGenero}"

# --------SETTERS Y GETTERS--------------
    @property
    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    @property
    def getDuracion(self):
        return self.__duracion

    def setDuracion(self, duracion):
        self.__duracion = duracion

    @property
    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

# ------------------clase Tiquete------------------
class Tiquete:
    def __init__(self, cliente, pelicula) -> None:
        self.__cliente = cliente
        self.__pelicula = pelicula

    def __str__(self) -> str:
        return f"Cliente: {self.__cliente.getNombre}, Película: {self.__pelicula.getTitulo}"

# -----clase de interacción---------
class SistemaCine:
    def __init__(self):
        self.listaClientes = []
        self.listaClientesVIP = []
        self.listaPeliculas = []
        self.listaTiquetes = []

    # Métodos para agregar clientes, clientes VIP y películas
    def agregarCliente(self, cliente):
        self.listaClientes.append(cliente)
        print(f"El cliente '{cliente.getNombre}' se agregó con éxito")

    def agregarClienteVIP(self, clienteVIP):
        self.listaClientesVIP.append(clienteVIP)
        print(f"El cliente VIP '{clienteVIP.getNombre}' se agregó con éxito")

    def agregarPelicula(self, pelicula):
        self.listaPeliculas.append(pelicula)
        print(f"La película '{pelicula.getTitulo}' se agregó con éxito")

    # Método para registrar clientes, clientes VIP y películas
    def registrarCliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        identificacion = input("Ingrese el número de identificación del cliente: ")
        es_vip = input("¿Es un cliente VIP? (s/n): ").lower()

        if es_vip == "s":
            nivel_vip = input("Ingrese el nivel VIP del cliente: ")
            nuevoCliente = ClienteVIP(nombre, identificacion, nivel_vip)
            self.agregarClienteVIP(nuevoCliente)
        else:
            nuevoCliente = Cliente(nombre, identificacion)
            self.agregarCliente(nuevoCliente)

    def registrarPelicula(self):
        titulo = input("Ingrese el título de la película: ")
        duracion = input("Ingrese la duración de la película (min): ")
        genero = input("Ingrese el género de la película: ")
        nuevaPelicula = Pelicula(titulo, duracion, genero)
        self.agregarPelicula(nuevaPelicula)

    # Método para vender tiquetes asociando un cliente a una película
    def venderTiquete(self):
        if not self.listaClientes and not self.listaClientesVIP:
            print("No hay clientes registrados.")
            return
        if not self.listaPeliculas:
            print("No hay películas registradas.")
            return

        print("\nClientes disponibles:")
        for i, cliente in enumerate(self.listaClientes + self.listaClientesVIP, 1):
            print(f"{i}. {cliente}")

        cliente_idx = int(input("\nSeleccione el cliente (número): ")) - 1
        cliente = (self.listaClientes + self.listaClientesVIP)[cliente_idx]

        print("\nPelículas disponibles:")
        for idx, pelicula in enumerate(self.listaPeliculas, 1):
            print(f"{idx}. {pelicula}")

        pelicula_idx = int(input("\nSeleccione la película (número): ")) - 1
        pelicula = self.listaPeliculas[pelicula_idx]

        nuevoTiquete = Tiquete(cliente, pelicula)
        self.listaTiquetes.append(nuevoTiquete)
        print(f"Tiquete vendido a {cliente.getNombre} para la película {pelicula.getTitulo}")

    # Métodos para mostrar clientes, películas y tiquetes
    def mostrarClientes(self):
        if self.listaClientes:
            print("\nClientes registrados:")
            for cliente in self.listaClientes:
                print(cliente)
        else:
            print("\nNo hay clientes registrados.")

    def mostrarClientesVIP(self):
        if self.listaClientesVIP:
            print("\nClientes VIP registrados:")
            for clienteVIP in self.listaClientesVIP:
                print(clienteVIP)
        else:
            print("\nNo hay clientes VIP registrados.")

    def mostrarPeliculas(self):
        if self.listaPeliculas:
            print("\nPelículas registradas:")
            for pelicula in self.listaPeliculas:
                print(pelicula)
        else:
            print("\nNo hay películas registradas.")

    def mostrarTiquetes(self):
        if self.listaTiquetes:
            print("\nTiquetes vendidos:")
            for tiquete in self.listaTiquetes:
                print(tiquete)
        else:
            print("\nNo hay tiquetes vendidos.")

    # Menú de interacción con el usuario
    def menu(self):
        while True:
            print("\n  Bienvenido al sistema de gestión de cine \n \n\
                    1. Registrar Cliente/Cliente VIP \n\
                    2. Registrar Película \n\
                    3. Vender Tiquete \n\
                    4. Mostrar lista de Clientes \n\
                    5. Mostrar lista de Clientes VIP \n\
                    6. Mostrar lista de Películas \n\
                    7. Mostrar Tiquetes vendidos \n\
                    8. Salir")
            
            opcion = int(input("\n Ingrese la opción que desea realizar: "))
            
            if opcion == 1:
                self.registrarCliente()
            
            elif opcion == 2:
                self.registrarPelicula()

            elif opcion == 3:
                self.venderTiquete()

            elif opcion == 4:
                self.mostrarClientes()
            
            elif opcion == 5:
                self.mostrarClientesVIP()

            elif opcion == 6:
                self.mostrarPeliculas()

            elif opcion == 7:
                self.mostrarTiquetes()
            
            elif opcion == 8:
                print("Saliendo del menú.")
                break
                
            else:
                print("Opción incorrecta")


# ----------Inicializando el menú-----------------
sisCine = SistemaCine()
sisCine.menu()