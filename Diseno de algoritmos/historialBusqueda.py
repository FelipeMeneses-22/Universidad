def retroceder(historial, pasos):
    if pasos == 0:
        print("Se completaron los pasos.")
        return historial

    if not historial:
        print("Historial vacío.")
        return historial

    pagina = historial.pop()
    print(f"Retrocediendo desde: {pagina}")

    if pagina == "Error 404":
        print("Se encontró un Error 404. Deteniendo proceso.")
        return historial

    return retroceder(historial, pasos - 1)


# 🔹 Generar 100 páginas automáticamente
historial = [f"pagina_{i}.com" for i in range(1, 101)]

# Insertar un Error 404 en una posición intermedia
historial[70] = "Error 404"   # posición 71 aprox

# Ver últimas páginas antes de ejecutar
print("Últimas 5 páginas antes:")
print(historial[-5:])

# Ejecutar retroceso
resultado = retroceder(historial, 50)

print("\nÚltimas 5 páginas después:")
print(resultado[-5:])