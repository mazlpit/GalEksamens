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
        "opcijas": ["if x > 5 tad:", "if x > 5:", "if (x > 5) tad", "x > 5 if:"],
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

pasreizejais_jautajums = 0
lietotaja_atbildes = []
# Funkcija testu restartēšanai
def restartet_testu():
    global pasreizejais_jautajums, lietotaja_atbildes
    pasreizejais_jautajums = 0
    lietotaja_atbildes = []
    restartet_Button.pack_forget()
    nakamais_Button.config(state="normal")
    apstadinat_Button.config(state="normal")
    radit_jautajums()
# Funkcija, kas rāda pašreizējo jautājumu un opcijas
def radit_jautajums():
    jautajums_label.config(text=jautajumi[pasreizejais_jautajums]["jautajums"])
    izveleta_opcija.set(-1)
    for i in range(4):
        opcijas[i].config(text=jautajumi[pasreizejais_jautajums]["opcijas"][i])

def nakamais_jautajums():
    global pasreizejais_jautajums
    izveleta = izveleta_opcija.get()
    if izveleta == -1:
        # Ja nav izvēlēta atbilde, parāda brīdinājuma ziņojumu
        messagebox.showwarning("Uzmanību", "Lūdzu, izvēlies atbildi!")
        return
    lietotaja_atbildes.append(izveleta)# Pievieno lietotāja atbildi
    pasreizejais_jautajums += 1 # Pāriet uz nākamo jautājumu
    if pasreizejais_jautajums == len(jautajumi):
        radit_rezultatus()
    else:
        radit_jautajums()
# Funkcija, kas apstādina testu un rāda rezultātus
def apstadinat_testu():
    global pasreizejais_jautajums
    izveleta = izveleta_opcija.get()
    if izveleta != -1:
        lietotaja_atbildes.append(izveleta)
    radit_rezultatus()
# Funkcija, kas rāda rezultātus un nepareizās atbildes
def radit_rezultatus():
    pareizie = 0
    nepareizie_jautajumi = []
    # Pārbauda lietotāja atbildes un skaita pareizās
    for i in range(len(lietotaja_atbildes)):
        if lietotaja_atbildes[i] == jautajumi[i]["atbilde"]:
            pareizie += 1
        else:
            nepareizie_jautajumi.append((jautajumi[i]["jautajums"], jautajumi[i]["opcijas"][jautajumi[i]["atbilde"]]))
            # Ja atbilde ir nepareiza, pievieno jautājumu un pareizo atbildi
    rezultatus_text = f"Tu atbildēji pareizi uz {pareizie} no {len(lietotaja_atbildes)} jautājumiem.\n\n"
    if nepareizie_jautajumi:
        rezultatus_text += "Nepareizie jautājumi un pareizās atbildes:\n"
        for q_text, pareizie_ans in nepareizie_jautajumi:
            rezultatus_text += f"- {q_text}\n  Pareizā atbilde: {pareizie_ans}\n"

    messagebox.showinfo("Rezultāts", rezultatus_text)
    nakamais_Button.config(state="disabled")
    apstadinat_Button.config(state="disabled")
    restartet_Button.pack(pady=10)
# Funkcija, kas sāk testu no jauna pēc tam, kad tas ir pabeigts
def sakt_testu():
    sakt_logs.destroy()
    root.deiconify()
    radit_jautajums()
# Funkcija, kas aizver programmu
def iziet_program():
    sakt_logs.destroy()
# Galvenais logs
root = tk.Tk()
root.title("Tests: Sazarojuma konstrukcijas Python valodā")
root.geometry("650x450")
root.configure(bg="#e6ccff")
root.withdraw()  # Paslēpj galveno logu, līdz tests sākas
# Sakma logs
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
# Galvenais logs, kurā tiks rādīti jautājumi un atbildes
jautajums_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600, justify="left", bg="#e6ccff", fg="#4b0082")
jautajums_label.pack(pady=20)

izveleta_opcija = tk.IntVar()
opcijas = []
for i in range(4):
    rb = tk.Radiobutton(
        root, text="", variable=izveleta_opcija, value=i, font=("Arial", 12),
        bg="#e6ccff", fg="#000000", selectcolor="#d9b3ff", activebackground="#e6ccff"
    )
    rb.pack(anchor="w", padx=50)
    opcijas.append(rb)

    nakamais_Button = tk.Button(root, text="Nākamais", command=nakamais_jautajums, font=("Arial", 12), bg="lightblue")
nakamais_Button.pack(pady=10)

apstadinat_Button = tk.Button(root, text="Beigt testu", command=apstadinat_testu, font=("Arial", 12), bg="orange")
apstadinat_Button.pack(pady=5)

restartet_Button = tk.Button(root, text="Sākt no jauna", command=restartet_testu, font=("Arial", 12), bg="lightgreen")

root.mainloop()