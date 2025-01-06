import tkinter as tk
import threading 
from risposte_json import salvaRisposte, caricaRisposte


risposteP = caricaRisposte()

def creaRisposta(messaggio):
    messaggio = messaggio.lower().strip()

    if 'ciao' in messaggio or 'salve' in messaggio or 'buon giorno' in messaggio or 'buona notte' in messaggio or 'hey' in messaggio:
     return'Ciao come stai'
    
    elif 'tutto bene' in messaggio or 'non sto bene' in messaggio or 'me la cavo' in messaggio or 'cosi cosi'in messaggio or 'tutto a posto' in messaggio or "tutto bene grazie" in messaggio or 'bene grazie'in messaggio:
     return 'ah,mi fa piacere'
   
    elif 'arrivederci' in messaggio or 'addio' in messaggio or 'non ci rivedremo mai piu'in messaggio or 'e stato bello conoscerti'in messaggio:
      return 'ok,a presto rivederci'
    
    elif 'mi manchi' in messaggio or 'ti voglio bene' in messaggio:
      return 'anche tu mi manchi,ti voglio bene'
    
    elif 'che ce' in messaggio or 'come mai' in messaggio:
      return 'dimmi,hai qualche dubbio'
    
    elif 'dai'in messaggio or 'diamine' in messaggio:
      return 'tranquillo,ce le puoi fare'
    
    elif 'che ne dici' in messaggio or 'che ne pensi'in messaggio:
      return 'boh,sentiamo anche la sua opinione'
    
    elif 'scusa ma non ho capito cosa intendi' in messaggio or 'in che senso'in messaggio:
      return 'non preocuparti ora ti spiego'
    
    elif 'non mi lamento' in messaggio or 'non posso lamentarmi'in messaggio:
      return 'beh,anche se lo facessi non cambierebbe niente'
    
    elif 'ci vediamo' in messaggio:
      return 'okok fammi uno squillo mi raccomando'
    
    elif 'scusa il disturbo' in messaggio:
      return 'non preocuparti'
    
    elif 'devo andare'in messaggio:
      return 'va bene, ci vediamo'
    
    elif 'sto arrivando' in messaggio:
      return ' ok,mandami un messaggio quando sei arrivato'
    
    elif 'non ho niente da dire' in messaggio or 'non ti preocupare 'in messaggio:
      return 'ok'
    
    elif 'bella partita' in messaggio or 'hai visto la partita ieri'in messaggio:
     return ' si,e stata molto combattuta'

    elif 'come stai' in messaggio:
      return 'sto molto bene'
    
    elif 'niente di che' in messaggio:
      return 'Ah,ok'
    
    elif 'mi fa piacere' in messaggio:
      return 'sono contento di sentirti'

    elif 'sono stato in ' in messaggio or 'ho passato le feste a' in messaggio or 'ho visitato' in messaggio:
      return 'mi fa davvero piacere sentirtelo dire,io invece non ho fatto niente di che'
    
    elif 'ah ok'in messaggio or 'interessante'in messaggio:
      return 'arrivederci'

    elif 'che fai' in messaggio or 'cosa vorresti fare domani' in messaggio:
      return 'domani scendo e mi faccio un giro,vuoi venire'

    elif 'come hai passato le feste'in messaggio or 'ti sei divertito durante le feste'in messaggio:
      return 'si,sono stato molto bene'

    elif 'pensvavo di andare a'in messaggio or 'ti piacerebbe se domani andiamo in' in messaggio or'ti piacerebbe venire con me'in messaggio:
      return 'si,certo'

    elif 'domani devi lavorare'in messaggio or 'domani lavori' in messaggio or 'domani sei impegnato'in messaggio:
      return 'purtroppo si'

    elif 'ciao,ci vediamo'in messaggio:
      return 'a presto'

    elif 'ti va di' in messaggio or 'dopo'in messaggio:
      return 'ok,va bene'

    if messaggio in risposteP:
      
      return risposteP[messaggio]
    else:
      return "mi ero distratto puoi ripetere"

def salvaRisposta(chatBox,messaggio):
  
  chatBox.config(state = tk.NORMAL)
  chatBox.insert(tk.END,f"{messaggio}\n\n")
  chatBox.config(state = tk.DISABLED)
  chatBox.yview(tk.END)

def inputUser(messaggio,chatBox):
    risposta = creaRisposta(messaggio)

    chatBox.config(state = tk.NORMAL) 
    chatBox.insert(tk.END,f"User {messaggio}\n\n")
    chatBox.insert(tk.END,f"answer {risposta}\n\n")
    chatBox.config(state = tk.DISABLED)
    chatBox.yview(tk.END)

    if risposta == "mi ero distratto puoi ripetere":
      apriFinestra(messaggio,chatBox)
      

def apriFinestra(messaggio,chatBox):
  finestra = tk.Toplevel()
  finestra.title("Inserisci la tua risposta")
  finestra.geometry("400x200")

  risposta = tk.Entry(finestra,width = 40)
  risposta.pack(pady = 20)

  sB_sB = tk.Button(finestra,text = "salva la risposta",command = lambda: salvaFinestra(risposta.get(),chatBox,messaggio,finestra))
  sB_sB.pack(pady = 10)


def salvaFinestra(messaggio,chatBox,risposte,finestra):
  if risposte:
   risposteP[risposte] = messaggio
   salvaRisposte(risposteP) 
  
  finestra.destroy()
  salvaRisposta(chatBox,messaggio)

def defineGUI(callBack):
    root = tk.Tk()
    root.title("<<<CHAT>>>")
    root.geometry("500x500")
    root.resizable(False, False)

    chatBox = tk.Text(root, state=tk.DISABLED, height=20, width=50, wrap=tk.WORD, font=("Arial", 14), bg="#E5DDD5", fg="black", padx=10, pady=10)
    chatBox.pack(padx=10, pady=10)

    enFrame = tk.Frame(root, bg="#D3D3D3", bd=0)
    enFrame.pack(padx=10, pady=10)

    ris = tk.Entry(enFrame, width=40, font=("Arial", 14), bd=0, relief="flat", bg="#D3D3D3", fg="black")
    ris.pack(padx=10, pady=5)
 

    def message():
        msm = ris.get()
        if msm:
            chatBox.config(state = tk.NORMAL)
            chatBox.config(state = tk.DISABLED)
            chatBox.yview(tk.END)

            
            threading.Thread(target=callBack, args=(msm, chatBox)).start()
            ris.delete(0, tk.END)  

    sendButton = tk.Button(root, text="INVIA", font=("Arial", 14), command = message, bg="#25D366", fg="green", relief = tk.RAISED)
    sendButton.pack(pady=10)

    root.mainloop()
    


defineGUI(inputUser)