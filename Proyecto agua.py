def main():
    print("=== Calculadora de Consumo de Agua en el Hogar ===")
    
    # Solicitar el valor del agua (costo por m^3)
    try:
        valor_agua = float(input("Ingrese el valor del agua (por m³): "))
    except ValueError:
        print("Error: debe ingresar un valor numérico para el costo del agua.")
        return

    # Solicitar el número de personas en el hogar
    try:
        num_personas = int(input("Ingrese el número de personas en el hogar: "))
    except ValueError:
        print("Error: debe ingresar un número entero para la cantidad de personas.")
        return

    print("\nIngrese el consumo diario en litros para cada actividad por persona:")
    
    try:
        consumo_ducha = float(input("  - Consumo en duchas: "))
        consumo_inodoro = float(input("  - Consumo en inodoros (descargas): "))
        consumo_lavadora = float(input("  - Consumo en lavadora: "))
        consumo_platos = float(input("  - Consumo al lavar platos: "))
        consumo_otro = float(input("  - Otros consumos: "))
    except ValueError:
        print("Error: debe ingresar valores numéricos para los consumos.")
        return

    # Calcular el consumo total diario en litros (multiplicado por la cantidad de personas)
    consumo_por_persona = consumo_ducha + consumo_inodoro + consumo_lavadora + consumo_platos + consumo_otro
    total_litros = consumo_por_persona * num_personas
    total_m3 = total_litros / 1000.0

    # Calcular el costo diario del agua
    costo_diario = total_m3 * valor_agua

    # Mostrar resultados
    print("\n=== Resultados ===")
    print(f"Número de personas en el hogar: {num_personas}")
    print(f"Consumo total diario: {total_litros:.2f} litros (equivalente a {total_m3:.2f} m³)")
    print(f"Costo diario del agua: {costo_diario:.2f}\n")

if __name__ == "__main__":
    main()
