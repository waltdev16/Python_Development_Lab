from pathlib import Path

DATA = Path(__file__).with_name("tareas.txt")

# Agrega una tarea al archivo local.
def add_task():
    task = input("Ingresa tarea a guardar: ").strip()
    if not task:
        print("La tarea no puede estar vacía.")
        return
    with DATA.open("a", encoding="utf-8") as file:
        file.write(task + "\n")

# Muestra las tareas registradas.
def show_tasks():
    tasks = DATA.read_text(encoding="utf-8") if DATA.exists() else ""
    print(tasks or "No hay tareas registradas.")


def main():
    while True:
        option = input("\n1. Ingresar tarea\n2. Ver tareas\n3. Salir\nOpción: ").strip()
        if option == "1":
            add_task()
        elif option == "2":
            show_tasks()
        elif option == "3":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
