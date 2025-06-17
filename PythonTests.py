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