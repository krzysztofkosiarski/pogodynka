#import potrzebnych bibliotek
import tkinter as tk
from requests import get
from json import loads

#tworzenie okna aplikacji
frame = tk.Tk()
frame.title('Pomiar temperatury - Źródłem pochodzenia danych jest Instytut Meteorologii i Gospodarki Wodnej – Państwowy Instytut Badawczy')

#tworzenie pola textowego z tytułem
label = tk.Label(frame, text='Wpisz miasto', width=20)
label.pack()

#tworzenie pola na wpisanie miasta
entry = tk.Entry(0, width=30)
entry.pack()

#tworzenie pola wyniku pomiaru
text = tk.Text(0, width=70, height=5)
text.pack()

#funkcja pobierająca dane z imgw
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    city = entry.get()
    city = city.capitalize()
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura'] #selekcja informacji z api
    ]
    for row in loads(response.text):
        if row['stacja'] in city:
            a = row['stacja']
            b = row['temperatura']
            c = row['godzina_pomiaru']
            q = (f'Temperatura w mieście {a} o godzinie {c} wynosiła {b} \n')
            text.insert('1.0', q)

#funkcja czyszcząca pola na wynik pomiaru
def delete_text():
    text.delete('1.0', tk.END)

#tworzenie przycisku sprawdzenia
button = tk.Button(frame, text='Sprawdź', padx=50, command=main)
button.pack()

#tworzenie przycisku czyszczenia okna
button_2 = tk.Button(frame, text='Wyczyść', padx=50, command=delete_text)
button_2.pack()

frame.mainloop()