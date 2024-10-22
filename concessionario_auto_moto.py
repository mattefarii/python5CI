class Veicolo:
  def __init__(self, codice, marca, modello,prezzo, annoRevisione):
    #1 Implementa il costruttore
    self.codice = codice
    self.marca = marca
    self.modello = modello
    self.prezzo = prezzo
    self.annoRevisione = annoRevisione



  def scheda_veicolo(self):
    #2 Ritorna una stringa contenente gli attributi del veicolo
    return f"""
            codice: {self.codice}
            marca: {self.marca}
            modello: {self.modello}
            prezzo: {self.prezzo}
            anno di revisione: {self.annoRevisione}
            """
            


  def modifica_scheda(self):
    #3 Permette di modificare gli attributi del veicolo
    scelta = int(input("Cosa vuoi modificare? 1.codice, 2.marca, 3.modello, 4.prezzo, 5.anno di revisione: "))
    if (scelta == 1):
      self.codice = int(input("Inserisci codice: "))
    elif (scelta == 2):
      self.marca = input("Inserisci la marca: ")
    elif (scelta == 3):
      self.modello = input("Inserisci il modello: ")
    elif (scelta == 4):
        self.prezzo = int(input("Inserisci il prezzo: "))
    elif (scelta == 5):
      self.annoRevisione = int(input("Inserisci l'anno di revisione: "))
    

class Automobile(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,lunghezza,larghezza):
      #4 Implementa il costruttore
      super().__init__(codice, marca, modello, prezzo, annoRevisione)
      self.lunghezza = lunghezza
      self.larghezza = larghezza


    def scheda_veicolo(self):
      #5 Ritorna una stringa contenente gli attributi dell'automobile
      return f"""
            codice: {self.codice}
            marca: {self.marca}
            modello: {self.modello}
            prezzo: {self.prezzo}
            anno di revisione: {self.annoRevisione}
            lunghezza: {self.lunghezza}
            larghezza: {self.larghezza}
            """



class Motociclo(Veicolo):
  def __init__(self, codice, marca, modello,prezzo, annoRevisione,tipo,potenza):
    #6 Implementa il costruttore
    super().__init__(codice, marca, modello, prezzo, annoRevisione)
    self.tipo = tipo
    self.potenza = potenza



  def scheda_veicolo(self):
    #7 Ritorna una stringa contenente gli attributi del motociclo
    return f"""
            codice: {self.codice}
            marca: {self.marca}
            modello: {self.modello}
            prezzo: {self.prezzo}
            anno di revisione: {self.annoRevisione}
            tipo: {self.tipo}
            potenza: {self.potenza}
            """

a1 = Automobile(1,"Audi","Audi Q3",25000,2015,4.5,1.85)
print(a1.scheda_veicolo())

a1.modifica_scheda()
print(a1.scheda_veicolo())


class Vendita():
  def __init__(self,codice,data, codiceVenditore):
    #8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.codiceVenditore = codiceVenditore

    self.veicoli = []
    self.automobili = []
    self.motocicli = []



  def aggiungi_veicolo(self,veicolo):
    if isinstance(veicolo,Automobile):
        tipo_veicolo="automobile"
        if (veicolo not in self.automobili):
            self.automobili.append(veicolo)
        else:
            print("Automobile già presente")

    elif isinstance(veicolo,Motociclo):
        tipo_veicolo="motociclo"
        if (veicolo not in self.motocicli):
            self.motocicli.append(veicolo)
        else:
            print("Motociclo già presente")
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno


  def rimuovi_veicolo(self,veicolo):
    #10 Implementa il metodo
    if veicolo in self.veicoli:
       self.veicoli.remove(veicolo)
       print("Veicolo rimosso correttamente")
    else:
       print("Veicolo non trovato")




  def importo_vendita(self,veicolo):
    #11 Stampa il numero di veicoli e l'importo totale della vendita giornaliera
    tot_veicoli = 0
    importo_totale = 0
    for veicolo in self.veicoli:
        tot_veicoli += 1
        importo_totale += veicolo.prezzo

    print(f"Numero di veicoli venduti: {tot_veicoli}")
    print(f"Importo totale della vendita: {importo_totale} €")
       


  def dettaglio_vendita(self):
    #12 Stampa il dettaglio della vendita e restituisce una lista contenente
    # [somma importi automobili, somma importi motocicli, somma importi totali, provvigione ]
    # e il totale della provvigione spettante al venditore sapendo che:
    # per automobili la provvigione spettante è il 3% del prezzo di vendita
    # per motocicli la provvigione spettante è il 2% del prezzo di vendita
    #...
    somma_importi_auto = 0
    somma_importi_moto = 0
    somma_importi_totali = 0
    provvigione = 0

    for veicolo in self.automobili:
       somma_importi_auto += veicolo.prezzo
    
    for veicolo in self.motocicli:
       somma_importi_moto += veicolo.prezzo

    somma_importi_totali = somma_importi_auto
    somma_importi_totali += somma_importi_moto

    for veicolo in self.automobili:
        provvigione += veicolo.prezzo * 0.03

    for veicolo in self.motocicli:
        provvigione += veicolo.prezzo * 0.02

       

    return f"""
            somma_importi_auto: {somma_importi_auto}
            somma_importi_moto: {somma_importi_moto}
            somma_importi_totali: {somma_importi_totali}
            provvigione: {provvigione}
            """



a2 = Automobile(2,"Peugeot","Peugeot 2008",18000,2014,4.2,1.75)
m1 = Motociclo(3,"Gilera","Gilera Runner 50",3500,2016,"Scooter",1200)
m2 = Motociclo(4,"Honda","SW-T 400 – 2013",4500,2012,"Super Sport",1000)


vendita1=Vendita(1,"01/04/2022",'123')
vendita1.aggiungi_veicolo(a1)
vendita1.aggiungi_veicolo(a2)
vendita1.aggiungi_veicolo(m1)
vendita1.aggiungi_veicolo(m2)


vendita1.rimuovi_veicolo(m2)
vendita1.rimuovi_veicolo(m2)


#13 Risposta al Punto 1 : Per una vendita: 'importo totale senza distinguere il tipo di veicolo
vendita1.importo_vendita()


#14 Risposta punto 2.   Per una ogni vendita: l'importo totale,
# l'importo delle automobili, l'importo dei motocicli e il totale della provvigione.
importi=vendita1.dettaglio_vendita()
print("--------------------------")
print(f"\nImporto Automobili= {importi[0]}")
print(f"\nImporto Motocicli= {importi[1]}")
print(f"\nImporto Totale= {importi[2]}")
print(f"\nImporto Provvigione= {importi[3]}")


class Vendite():
  def __init__(self,nome_negozio,codice_negozio):
    #16 Implementa il costruttore
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio

    self.vendita = []
    

  def aggiungi_vendita(self,vendita):
    #17 Implementa il metodo
    if isinstance(vendita,Vendita):
        if (vendita not in self.vendite):
            self.vendite.append(vendita)
        else:
            print("Vendita già presente")


  def rimuovi_vendita(self,vendita):
    #18 Implementa il metodo
    if vendita in self.vendite:
       self.vendite.remove(vendita)
       print("Vendita rimossa correttamente")
    else:
       print("Vendita non trovato")

  def totale_vendite(self):
    #19 Implementa il metodo
    #...
    totale_vendite = 0
    totale_vendite_auto = 0
    totale_vendite_moto = 0

    for vendita in self.vendita:
       totale_vendite += 1

    importi = vendita.dettaglio_vendita()
    totale_vendite_auto += importi [0]
    totale_vendite_moto += importi [1]



    return ([totale_vendite_auto,totale_vendite_moto,totale_vendite])


vendite_negozio=Vendite("Concessionaria Magenta ",1)
vendite_negozio.aggiungi_vendita(vendita1)
vendite_negozio.rimuovi_vendita(vendita1)
vendite_negozio.rimuovi_vendita(vendita1)

vendite_negozio.aggiungi_vendita(vendita1)

a3 = Automobile(5,"Renault","Renault Clio",12000,2020,3.2,1.55)

m3 =  Motociclo(6,"Honda","SW-T 500",5500,2021,"Sport",1200)
vendita2=Vendita(2,"2/04/2022",'234')
vendita2.aggiungi_veicolo(a3)
vendita2.aggiungi_veicolo(m3)

vendite_negozio.aggiungi_vendita(vendita2)

# 20 Riposta punto 3: Per tutti le vendite della concessionaria mostra
# il dettaglio dei veicoli, l'importo totale,
# l'importo delle automobili e l'importo dei motocicli.
importiTotali=vendite_negozio.totale_vendite()
print("--------------------------")
print(f"\nImporto totale automobili= {importiTotali[0]}")
print(f"\nImporto totale motocilci= {importiTotali[1]}")
print(f"\nImporto totale di tutte le vendite= {importiTotali[2]}")
