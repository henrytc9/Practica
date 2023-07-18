def main():
    # Primero consultamos los datos al usuario
    kilometros_recorridos = float(input("Ingrese la cantidad de kilómetros recorridos por la motocicleta: "))
    litros_combustible = float(input("Ingrese la cantidad de litros de combustible consumidos: "))

    # Luego calculamos el consumo de combustible en kilómetros por litro
    consumo_kilometros_litro = kilometros_recorridos / litros_combustible

    # Por último mostramos el resultado
    print(f"El consumo de combustible es de {consumo_kilometros_litro:.2f} kilómetros por litro.")

if __name__ == "__main__":
    main()