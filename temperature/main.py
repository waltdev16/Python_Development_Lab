from datetime import date
from pathlib import Path
import math

DATA = Path(__file__).with_name("temperaturas.txt")

# Valida la temperatura y la fecha antes de guardar.
def add_temperature():
    try:
        temperature = float(input("Temperatura (°): "))
        if not math.isfinite(temperature):
            raise ValueError
        day = int(input("Día: "))
        month = int(input("Mes: "))
        year = int(input("Año: "))
        recorded_date = date(year, month, day)
    except ValueError:
        print("Temperatura o fecha inválida.")
        return
    with DATA.open("a", encoding="utf-8") as file:
        file.write(f"{recorded_date.isoformat()}: {temperature:g}°\n")


def main():
    while True:
        option = input("\n1. Agregar temperatura\n2. Mostrar temperaturas\n3. Salir\nOpción: ").strip()
        if option == "1":
            add_temperature()
        elif option == "2":
            print(DATA.read_text(encoding="utf-8") if DATA.exists() else "No hay registros.")
        elif option == "3":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
