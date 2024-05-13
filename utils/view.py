from tkinter import *
import tkintermapview
from models.data_source import users
import requests
from bs4 import BeautifulSoup

#settings
users=[]
class User:
    def __init__(self, name, surname, posts, location): #init metoda magiczna, powoduje przy tworzeniu obiektu są przypisane wartsoci
        self.name = name
        self.surname = surname
        self.posts = posts
        self.location = location
        self.wspolrzedne = User.wspolrzedne(self) #Self odwolujemy się do uzytkownika ktory jest w tym miejscu - self jest kontekstowy który odwoluje się do danych

    def wspolrzedne(self) -> list: #wywolanie/przypisuje funkcji przez self, metoda wspolrzedne oddaje/zwraca liste ->
        url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        responsse = requests.get(url)
        responsse_html = BeautifulSoup(responsse.text, 'html.parser')
        return [
            float(responsse_html.select('.latitude')[1].text.replace(",", ".")),
            float(responsse_html.select('.longitude')[1].text.replace(",", "."))
        ]


def lista_uzytkownikow():
    listbox_lista_obiektow.delete(0, END) #wyswietla obiekty
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{user.name} {user.surname} {user.posts} {user.location}')
        user.marker = map_widget.set_marker(user.wspolrzedne[0], user.wspolrzedne[1], text=f"{user.name}") #f-string

def dodaj_uzytkownika():
    imie= enter_imie.get()
    nazwisko= enter_nazwisko.get()
    posty= enter_posty.get()
    lokalizacja= enter_lokalizacja.get()
    print(imie, nazwisko)
    users.append(User(imie, nazwisko, posty, lokalizacja))

    lista_uzytkownikow()

    enter_imie.delete(0, END)
    enter_nazwisko.delete(0, END)
    enter_posty.delete(0, END)
    enter_lokalizacja.delete(0, END)

    enter_imie.focus()

def usun_uzytkownika():
    i=listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users.pop(i)
    lista_uzytkownikow()
def pokaz_szczegoly_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    imie = users[i].name
    nazwisko = users[i].surname
    posty = users[i].posts
    lokalizacja = users[i].location
    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    label_posty_szczegoly_obiektu_wartosc.config(text=posty)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=lokalizacja)
    map_widget.set_position(users[i].wspolrzedne[0], users[i].wspolrzedne[1])
    map_widget.set_zoom(12) #przyblizenie do lokalizacji

def edytuj_uzytkownika():
    i = listbox_lista_obiektow.index(ACTIVE)
    enter_imie.insert(0, users[i].name)
    enter_nazwisko.insert(0, users[i].surname)
    enter_posty.insert(0, users[i].posts)
    enter_lokalizacja.insert(0, users[i].location)

    button_dodaj_uzytkownika.config(text = "Zapisz zmiany", command= lambda: aktualizauj_uzytkownika(i))
def aktualizauj_uzytkownika(i):
    users[i].name = enter_imie.get()
    users[i].surname = enter_nazwisko.get()
    users[i].posts = enter_posty.get()
    users[i].location = enter_lokalizacja.get()
    lista_uzytkownikow()
    button_dodaj_uzytkownika.config(text='Dodaj uzytkownika', command=dodaj_uzytkownika)
    enter_imie.delete(0, END)
    enter_nazwisko.delete(0, END)
    enter_posty.delete(0, END)
    enter_lokalizacja.delete(0, END)
    enter_imie.focus()



#GUI
root = Tk()
root.title("MapBook")
root.geometry("1200x900")

# ramki do porządkowania struktury
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=100)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=50, pady=20)

# lista obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista obiektów: ")
listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=50)
button_pokaz_szczegoly = Button(ramka_lista_obiektow, text="Pokaz szczegoly", command=pokaz_szczegoly_uzytkownika)
button_usun_obiekt = Button(ramka_lista_obiektow, text="Usun obiekt", command=usun_uzytkownika)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj obiekt", command=edytuj_uzytkownika)

label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=3)

# formularz
label_formularz = Label(ramka_formularz, text="Formularz")
label_imie = Label(ramka_formularz, text="Imie")
label_nazwisko = Label(ramka_formularz, text="Nazwisko")
label_posty = Label(ramka_formularz, text='Liczba postów')
label_lokalizacja = Label(ramka_formularz, text='Lokalizacja')

enter_imie = Entry(ramka_formularz)
enter_nazwisko = Entry(ramka_formularz)
enter_posty = Entry(ramka_formularz)
enter_lokalizacja = Entry(ramka_formularz)

label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_posty.grid(row=3, column=0, sticky=W)
label_lokalizacja.grid(row=4, column=0, sticky=W)

enter_imie.grid(row=1, column=2)
enter_nazwisko.grid(row=2, column=2)
enter_posty.grid(row=3, column=2)
enter_lokalizacja.grid(row=4, column=2)

button_dodaj_uzytkownika=Button(ramka_formularz,text='Dodaj uzytkownika', command=dodaj_uzytkownika)
button_dodaj_uzytkownika.grid(row=5, column=2, columnspan=2)

#szczegoly uzytkownika
label_szczegoly_uzytkownika = Label(ramka_szczegoly_obiektu,text='Szczegóły użytkownika: ')
label_imie_szczegoly_obiektu= Label(ramka_szczegoly_obiektu,text='Imie')
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Nazwisko')
label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Liczba postów')
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Lokalizacja')

label_imie_szczegoly_obiektu_wartosc= Label(ramka_szczegoly_obiektu,text='...', width=10)
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='...', width=10)
label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='...', width=10)
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='...', width=10)

label_szczegoly_uzytkownika.grid(row=0, column=0, sticky=W)
label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_posty_szczegoly_obiektu.grid(row=1, column=4)
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)


map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width = 900, height = 500)
map_widget.set_position(52.21, 21.0)
map_widget.set_zoom(8)
#marker_WAT = map_widget.set_marker(52.254144, 20.900888, text="WAT")

map_widget.grid(row = 2, column = 0, columnspan = 8)



root.mainloop()