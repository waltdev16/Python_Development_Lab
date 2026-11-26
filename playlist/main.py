from pathlib import Path

DATA = Path(__file__).with_name("playlist.txt")

# Lee las canciones guardadas.
def read_songs():
    return DATA.read_text(encoding="utf-8").splitlines() if DATA.exists() else []

# Guarda y muestra las canciones con numeración actualizada.
def save_songs(songs):
    DATA.write_text("".join(song + "\n" for song in songs), encoding="utf-8")


def show_songs(songs):
    if not songs:
        print("Tu playlist está vacía.")
    for number, song in enumerate(songs, 1):
        print(f"{number}. {song}")


def main():
    while True:
        option = input("\n1. Mostrar playlist\n2. Agregar canción\n3. Eliminar canción\n4. Salir\nOpción: ").strip()
        songs = read_songs()
        if option == "1":
            show_songs(songs)
        elif option == "2":
            song = input("Canción (o salir): ").strip()
            if song and song.lower() != "salir":
                songs.append(song)
                save_songs(songs)
            elif not song:
                print("Ingresa una canción válida.")
        elif option == "3":
            show_songs(songs)
            if not songs:
                continue
            try:
                number = int(input("Número de canción: "))
                if not 1 <= number <= len(songs):
                    raise ValueError
                print(f"Canción eliminada: {songs.pop(number - 1)}")
                save_songs(songs)
            except ValueError:
                print("Número inválido.")
        elif option == "4":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
