import json


def caricaRisposte():
    try:
        with open("risposte.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  


def salvaRisposte(risposte):
    try:
        with open("risposte.json", "w") as file:
            json.dump(risposte, file, indent = 4)
    except Exception as e:
        print(f"Errore nel salvataggio delle risposte: {e}")
