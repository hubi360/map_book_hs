def read_friends(users: list) -> None:
    print("Informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

def add_user(lista: list) -> list:  # wezmie liste i potem odd liste
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_psotow = int(input("Podaj liczbe postow uzytkownika: "))
    nazwa_miejscowosci = input("Podaj nazwe miejscowosci: ")
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_psotow, 'location': nazwa_miejscowosci}
    lista.append(new_user)

def search_user(users: list)->str:
    imie = input("Podaj imie: ")
    for user in users:
        if user["name"] == imie:
            print(user)
            return user
def remove_user(users: list):
    imie = input("Podaj imie: ")
    for user in users:
        if user["name"] == imie:
            users.remove(user)

def update_user(users: list):
    imie = input("Wporowadz imie użytkownika, którego dane chcesz zmienić: ")
    for user in users:
        if user["name"] == imie:
            user["name"] = input("Podaj nowe imie: ")
            user["surname"] = input("Podaj nowe nazwisko: ")
            user["posts"] = int(input("Podaj nową liczbę postów: "))
            print(users)


