import tkinter as tk
from tkinter import messagebox

jautajumi = [
    {
        "jautajums": "Kura atslēgvārda Python valodā izmanto, lai veidotu nosacījuma pārbaudi?",
        "opcijas": ["switch", "when", "if", "select"],
        "atbilde": 2
    },
    {
        "jautajums": "Kāds ir pareizs veids, kā veidot if-else konstrukciju?",
        "opcijas": ["if x > 5 then:", "if x > 5:", "if (x > 5) then", "x > 5 if:"],
        "atbilde": 1
    },
    {
        "jautajums": "Kā Python valodā pieraksta vairākus nosacījumus vienlaikus?",
        "opcijas": ["if x > 0 & x < 10:", "if x > 0 and x < 10:", "if (x > 0, x < 10):", "if x > 0; x < 10:"],
        "atbilde": 1
    },
    {
        "jautajums": "Kāda būs rezultāta vērtība: `if 0:`",
        "opcijas": ["Izpildās", "Kļūda", "Neizpildās", "Bezgalīgs cikls"],
        "atbilde": 2
    },
    {
        "jautajums": "Kura no šīm nav loģiska salīdzinājuma operācija Python valodā?",
        "opcijas": ["==", "!=", "<>", ">="],
        "atbilde": 2
    },
    {
        "jautajums": "Kā Python valodā pieraksta 'ja ne' nosacījumu?",
        "opcijas": ["unless", "not", "no", "!"],
        "atbilde": 1
    },
    {
        "jautajums": "Kāda būs šī koda izvade? `if True: print('Yes') else: print('No')`",
        "opcijas": ["Yes", "No", "Kļūda", "Nekas netiek izvadīts"],
        "atbilde": 0
    },
    {
        "jautajums": "Kāds ir pareizs veids, kā pārbaudīt, vai `a` ir vienāds ar `b`?",
        "opcijas": ["if a = b:", "if a == b:", "if a === b:", "if a equal b:"],
        "atbilde": 1
    },
    {
        "jautajums": "Kā nosacījuma konstrukcijā pievieno papildu pārbaudi?",
        "opcijas": ["elseif", "elif", "else if", "also if"],
        "atbilde": 1
    },
    {
        "jautajums": "Ko nozīmē `pass` if bloka iekšpusē?",
        "opcijas": ["Pāriet uz nākamo if", "Ignorēt nosacījumu", "Neizpildīt neko", "Izvadīt kļūdu"],
        "atbilde": 2
    },
]
def sakt_testu():
    sakt_logs.destroy()
    root.deiconify()
    radit_jautajums()

def iziet_program():
    sakt_logs.destroy()

root = tk.Tk()
root.title("Tests: Sazarojuma konstrukcijas Python valodā")
root.geometry("650x450")
root.configure(bg="#e6ccff")

sakt_logs = tk.Toplevel()
sakt_logs.title("Sveicināts testā!")
sakt_logs.geometry("400x200")
sakt_logs.configure(bg="#e6ccff")

sakuma_label = tk.Label(sakt_logs, text="Vai vēlies sākt testu?", font=("Arial", 14), bg="#e6ccff", fg="#4b0082")
sakuma_label.pack(pady=30)

sakt_Button = tk.Button(sakt_logs, text="Sākt testu", font=("Arial", 12), bg="lightgreen", command=sakt_testu)
sakt_Button.pack(pady=5)

iziet_Button = tk.Button(sakt_logs, text="Iziet", font=("Arial", 12), bg="lightcoral", command=iziet_program)
iziet_Button.pack(pady=5)

