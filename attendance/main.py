from pathlib import Path

DATA = Path(__file__).with_name("asistencia.txt")

# Recupera los nombres registrados.
def read_students():
    return DATA.read_text(encoding="utf-8").splitlines() if DATA.exists() else []


def main():
    while True:
        option = input("\n1. Ingresar estudiante\n2. Verificar estudiante\n3. Mostrar estudiantes\n4. Salir\nOpción: ").strip()
        if option == "1":
            student = input("Nombre del estudiante: ").strip()
            if not student:
                print("Ingresa un nombre válido.")
                continue
            with DATA.open("a", encoding="utf-8") as file:
                file.write(student + "\n")
            print(f"{student} fue agregado.")
        elif option == "2":
            # Compara nombres completos sin distinguir mayúsculas.
            student = input("Nombre a verificar: ").strip().casefold()
            found = bool(student) and any(name.strip().casefold() == student for name in read_students())
            print("Sí está presente." if found else "No está presente.")
        elif option == "3":
            print("\n".join(read_students()) or "No hay estudiantes registrados.")
        elif option == "4":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
