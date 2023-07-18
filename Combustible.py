# Realizamos una funcion para limitar la mala digitacion de los valores como negativos o letras por el usuario
def obtener_numero_positivo(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Error: Por favor, ingrese un número positivo.")
            else:
                return numero
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def main():
    # Primero consultamos los datos al usuario
    kilometros_recorridos = obtener_numero_positivo("Ingrese la cantidad de kilómetros recorridos por la motocicleta: ")
    litros_combustible = obtener_numero_positivo("Ingrese la cantidad de litros de combustible consumidos: ")
    
    # Luego calculamos el consumo de combustible en kilómetros por litro
    consumo_kilometros_litro = kilometros_recorridos / litros_combustible

    # Por último mostramos el resultado
    print(f"El consumo de combustible es de {consumo_kilometros_litro:.2f} kilómetros por litro.")

if __name__ == "__main__":
    main()