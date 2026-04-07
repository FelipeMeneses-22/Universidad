class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)

    # MÍNIMO
    def minimo(self):
        if self.raiz is None:
            return None

        actual = self.raiz
        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual.valor

    # MÁXIMO
    def maximo(self):
        if self.raiz is None:
            return None

        actual = self.raiz
        while actual.derecha is not None:
            actual = actual.derecha

        return actual.valor

    # TOP N (mayores puntajes)
    def top_n(self, n):
        resultado = []

        def reverse_inorder(nodo):
            if nodo is None or len(resultado) >= n:
                return

            # derecha → raíz → izquierda
            reverse_inorder(nodo.derecha)

            if len(resultado) < n:
                resultado.append(nodo.valor)

            reverse_inorder(nodo.izquierda)

        reverse_inorder(self.raiz)
        return resultado


# EJECUCIÓN (FUERA DE LA CLASE — MUY IMPORTANTE)
if __name__ == "__main__":
    torneo = BST()

    puntos = [3200, 4100, 1800, 5000, 2700, 3900, 4800]

    for p in puntos:
        torneo.insertar(p)

    print("Mínimo:", torneo.minimo())   # 1800
    print("Máximo:", torneo.maximo())   # 5000
    print("Top 3:", torneo.top_n(3))    # [5000, 4800, 4100]