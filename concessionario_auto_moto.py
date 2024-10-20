#vendite giornaliere = lista di auto e moto

class Veicolo:
  def __init__(self, codice, marca, modello, prezzo, annoRevisione):
    #1 Implementa il costruttore
    self.codice = codice
    self.marca = marca
    self.modello = modello
    self.prezzo = prezzo
    self.annoRevisione = annoRevisione


  def scheda_veicolo(self):
    #2 Ritorna una stringa contenente gli attributi del veicolo
    return "codice: ",self.codice, "marca: ", self.marca, "modello: ",self.modello, "prezzo: ",self.prezzo, "anno di revisione: ",self.annoRevisione


  def modifica_scheda(self):
    #3 Permette di modificare gli attributi del veicolo
    self.codice = int(input("inserisci il codice: "))
    self.marca = input("inserisci la marca: ")
    self.modello = input("inserisci il modello: ")
    self.prezzo = int(input("inserisci il prezzo: "))
    self.annoRevisione = int(input("inserisci l'anno di revisione: "))
    


class Automobile(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,lunghezza,larghezza):
        super().__init__(codice, marca, modello, prezzo, annoRevisione)
      #4 Implementa il costruttore
        self.lunghezza = lunghezza
        self.larghezza = larghezza



    def scheda_veicolo(self):
      #5 Ritorna una stringa contenente gli attributi dell'automobile
      return f"""
        Codice: {self.codice}
        Marca: {self.marca}
        Modello: {self.modello}
        Prezzo: {self.prezzo} €
        Anno di revisione: {self.annoRevisione}
        Lunghezza: {self.lunghezza}
        Larghezza: {self.larghezza} 
        """


 

class Motociclo(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,tipo,potenza):
        super().__init__(codice, marca, modello, prezzo, annoRevisione)
    #6 Implementa il costruttore
        self.tipo = tipo
        self.potenza = potenza


    def scheda_veicolo(self):
    #7 Ritorna una stringa contenente gli attributi del motociclo
        return f"""
            Codice: {self.codice}
            Marca: {self.marca}
            Modello: {self.modello}
            Prezzo: {self.prezzo} €
            Anno di revisione: {self.annoRevisione}
            Tipo: {self.tipo}
            Potenza: {self.potenza} CV
        """




class Vendita():
  def __init__(self,codice,data, codiceVenditore):
    #8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.codiceVenditore = codiceVenditore

    self.veicoli = []
    self.lista_auto = []
    self.lista_moto = []



  def aggiungi_veicolo(self,veicolo):
    if isinstance(veicolo,Automobile):
        tipo_veicolo="automobile"
        self.veicoli.append(veicolo)
            

    elif isinstance(veicolo,Motociclo):
        tipo_veicolo="motociclo"
        self.veicoli.append(veicolo)
        
    
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno


  def rimuovi_veicolo(self,veicolo):
    #10 Implementa il metodo
    if veicolo in self.veicoli:
       self.veicoli.remove(veicolo)
       print("veicolo rimosso correttamente")
    else:
       print("veicolo non trovato")




  def importo_vendita(self):
    #11 Stampa il numero di veicoli e l'importo totale della vendita giornaliera
    totale_veicoli = 0
    importo_totale = 0

    for veicolo in self.veicoli:
        totale_veicoli += 1
        importo_totale += veicolo.prezzo

    print(f"Numero di veicoli venduti: {totale_veicoli}")
    print(f"Importo totale della vendita: {importo_totale} €")

    if isinstance(veicolo,Automobile):
       self.lista_auto.append(veicolo)
    elif isinstance(veicolo, Motociclo):
       self.lista_moto.append(veicolo)

  def dettaglio_vendita(self):
    #12 Stampa il dettaglio della vendita e restituisce una lista contenente
    # [somma importi automobili, somma importi motocicli, somma importi totali, provvigione ]
    # e il totale della provvigione spettante al venditore sapendo che:
    # per automobili la provvigione spettante è il 3% del prezzo di vendita
    # per motocicli la provvigione spettante è il 2% del prezzo di vendita
    #...
    importi_auto = 0
    importi_moto = 0
    totale_importi = 0
    provvigione = 0

    for veicolo in self.veicoli:
        if isinstance(veicolo, Automobile):
            importi_auto += veicolo.prezzo
            provvigione += veicolo.prezzo * 0.03

    for veicolo in self.veicoli:
        if isinstance(veicolo, Motociclo):
            importi_moto += veicolo.prezzo
            provvigione += veicolo.prezzo * 0.02

    totale_importi += importi_auto
    totale_importi += importi_moto
    
    return([importi_auto, importi_moto, totale_importi, provvigione])
  

class Vendite():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome = nome_negozio
    self.codice = codice_negozio
    
    self.vendite = []

  def aggiungi_vendita(self,vendita):
    #17 Implementa il metodo
    if isinstance(vendita,Vendita):
        self.vendite.append(vendita)


  def rimuovi_vendita(self,vendita):
    #18 Implementa il metodo
        if isinstance(vendita,Vendita):
            self.vendite.remove(vendita)

  def totale_vendite(self):
    #19 Implementa il metodo
    #...
    totA = 0  
    totM = 0  
    tot = 0   

    for vendita in self.vendite:
        for veicolo in vendita.veicoli:
            if isinstance(veicolo, Automobile):
                totA += veicolo.prezzo
            elif isinstance(veicolo, Motociclo):
                totM += veicolo.prezzo
        tot = totA + totM  

    return [totA, totM, tot]  


a1 = Automobile(1,"Audi","Audi Q3",25000,2015,4.5,1.85)
print(a1.scheda_veicolo())

print("modifica scheda del veicolo:")
a1.modifica_scheda()
print(a1.scheda_veicolo())

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

vendite_negozio=Vendite("Concessionaria Magenta ",1)
vendite_negozio.aggiungi_vendita(vendita1)
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