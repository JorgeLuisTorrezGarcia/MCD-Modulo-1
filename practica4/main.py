"""
Herramienta de gestión y consulta de inventario de autos.

Esta aplicación de consola permite al gerente de la empresa de alquiler
consultar información sobre los autos disponibles, precios y existencias.

Funcionalidades principales:
    - Consultar autos disponibles para alquilar
    - Obtener costo de alquiler de un auto específico
    - Verificar si un auto existe en el sistema
    - Obtener cantidad total de autos en la empresa
"""

# Nota: esta aplicación se puede ejecutar como módulo (`python -m src.main`)
# o directamente (`python src/main.py`). Para que ambas formas funcionen,
# intentamos primero import relativo (paquete) y luego absoluto (script).
# Cuando se ejecuta como script: python src/main.py
from src import obtener_autos_disponibles, obtener_costo_alquiler, auto_existe,obtener_cantidad_total_autos, autos_disponibles
    
#from src.auto_data import autos_disponibles


def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    """
    print("\n" + "=" * 60)
    print("SISTEMA DE CONSULTA DE AUTOS - GERENCIA DE ALQUILERES")
    print("=" * 60)
    print("1. Ver autos disponibles para alquilar")
    print("2. Consultar costo de alquiler de un auto")
    print("3. Verificar si un auto existe")
    print("4. Ver cantidad total de autos")
    print("5. Salir")
    print("=" * 60)


def ejecutar_aplicacion():
    """
    Ejecuta el ciclo principal de la aplicación de consola.

    Permite al usuario navegar entre diferentes opciones de consulta
    hasta que elija salir.
    """
    while True:
        mostrar_menu()
        opcion = input("\nIngrese una opción (1-5): ").strip()

        if opcion == "1":
            autos = obtener_autos_disponibles()
            print("\n--- AUTOS DISPONIBLES PARA ALQUILAR ---")
            for i, auto in enumerate(autos, 1):
                unidades = autos_disponibles[auto]
                print(f"{i}. {auto} - Unidades disponibles: {unidades}")

        elif opcion == "2":
            modelo = input("\nIngrese el nombre del modelo de auto: ").strip()
            costo = obtener_costo_alquiler(modelo)
            if costo is not None:
                print(f"\n>>> Costo de alquiler de {modelo}: ${costo} por día")
            else:
                print(f"\n>>> El auto '{modelo}' NO existe en el sistema.")

        elif opcion == "3":
            modelo = input(
                "\nIngrese el nombre del modelo de auto a verificar: "
            ).strip()
            existe = auto_existe(modelo)
            print(
                f"\n>>> El auto '{modelo}' {'SÍ existe' if existe else 'NO existe'} en el sistema."
            )

        elif opcion == "4":
            total = obtener_cantidad_total_autos()
            print(f"\n>>> La empresa tiene un total de {total} autos.")

        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break

        else:
            print("\n>>> Error: Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_aplicacion()
