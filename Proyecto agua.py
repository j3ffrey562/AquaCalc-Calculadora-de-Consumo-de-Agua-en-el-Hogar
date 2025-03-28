def main():
    print("=== Calculadora de Consumo de Agua en el Hogar (Mensual) ===")
    
    # Solicitar el valor del agua (costo por m³)
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

    # Calcular el consumo total diario por persona
    consumo_por_persona = consumo_ducha + consumo_inodoro + consumo_lavadora + consumo_platos + consumo_otro

    # Calcular el consumo total diario en el hogar
    total_litros_diarios = consumo_por_persona * num_personas

    # Calcular el consumo mensual en litros (30 días) y convertir a m³
    total_litros_mensual = total_litros_diarios * 30
    total_m3_mensual = total_litros_mensual / 1000.0

    # Calcular el costo mensual del agua
    costo_mensual = total_m3_mensual * valor_agua

    # Mostrar resultados
    print("\n=== Resultados ===")
    print(f"Número de personas en el hogar: {num_personas}")
    print(f"Consumo total diario: {total_litros_diarios:.2f} litros ({total_litros_diarios / 1000:.2f} m³)")
    print(f"Consumo total mensual: {total_litros_mensual:.2f} litros ({total_m3_mensual:.2f} m³)")
    print(f"Costo mensual del agua: {costo_mensual:.2f}\n")

if __name__ == "__main__":
    main()
