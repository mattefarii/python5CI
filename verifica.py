class Articolo:
    def __init__(self, codice, fornitore, marca,prezzo, quantita):
    #1 Implementa il costruttore
        self.codice = codice
        self.fornitore = fornitore
        self.marca = marca
        self.prezzo = prezzo
        self.quantita = quantita

    def scheda_articolo(self):
    #2 Ritorna una stringa contenente gli attributi dell'articolo
        return f"""
                codice: {self.codice}
                fornitore: {self.fornitore}
                marca: {self.marca}
                prezzo: {self.prezzo}
                quantità: {self.quantita}
                """

    def modifica_scheda(self):
    #3 Permette di modificare gli attributi dell'articolo
        scelta=int(input("Cosa vuoi modificare? 1.codice, 2.fornitore, 3.marca, 4.prezzo, 5.quantità: "))
        if (scelta == 1):
            self.codice = int(input("Inserisci il codice: "))
        elif (scelta == 2):
            self.fornitore = input("Inserisci il fornitore: ")
        elif (scelta == 3):
            self.marca = input("Inserisci la marca: ")
        elif (scelta == 4):
            self.prezzo = int(input("Inserisci il prezzo: "))
        elif (scelta == 5):
            self.quantita = int(input("Inserisci la quantità: "))



class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      #4 Implementa il costruttore
      super().__init__(codice, fornitore, marca, prezzo, quantita)
      self.pollici = pollici
      self.tipo = tipo

    def scheda_articolo(self): 
      #5 Ritorna una stringa contenente gli attributi del televisore 
      return f"""
                codice: {self.codice}
                fornitore: {self.fornitore}
                marca: {self.marca}
                prezzo: {self.prezzo}
                quantità: {self.quantita}
                pollici: {self.pollici}
                tipo: {self.tipo}
                """
    
class Frigorifero(Articolo):
    def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    #6 Implementa il costruttore
        super().__init__(codice, fornitore, marca, prezzo, quantita)
        self.dimensioni = dimensioni
        self.modello = modello

    def scheda_articolo(self):
    #7 Ritorna una stringa contenente gli attributi del frigorifero
        return f"""
                codice: {self.codice}
                fornitore: {self.fornitore}
                marca: {self.marca}
                prezzo: {self.prezzo}
                quantità: {self.quantita}
                pollici: {self.dimensioni}
                tipo: {self.modello}
                """


t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())

t1.modifica_scheda()
print(t1.scheda_articolo())

class Ordine(): #finita 9:48
  def __init__(self,codice,data, piva,indirizzo):
    #8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo


    self.ordini = []
    


  def aggiungi_articolo(self,articolo): #controllato alle 9:36
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
      if (articolo not in self.ordini):
        self.ordini.append(articolo)
        print("articolo aggiunto correttamente")
      else:
         print("articolo già presente")
        
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"
      if (articolo not in self.ordini):
        self.ordini.append(articolo)
        print("articolo aggiunto correttamente")
      else:
         print("articolo non presente")

    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno
  
  def rimuovi_articolo(self,articolo): #controllato alle 9:36
    #10 Implementa il metodo
    if isinstance(articolo,Televisore):
        if (articolo in self.ordini):
            self.ordini.remove(articolo)
            print("articolo rimosso correttamente")

    elif isinstance(articolo,Frigorifero):
        if (articolo in self.ordini):
            self.ordini.remove(articolo)
            print("articolo rimosso correttamente")


  def importo_ordine(self): #controllato alle 9:36
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita) 
    totale_articoli = 0
    importo_televisore = 0
    importo_frigorifero = 0

    for articolo in self.ordini:
      totale_articoli += 1
      if isinstance (articolo, Televisore):
        importo_televisore += articolo.prezzo
      

    for articolo in self.ordini:
      totale_articoli += 1
      if isinstance (articolo, Televisore):
        importo_frigorifero += articolo.prezzo
      

    return f"""
            totale articoli: {totale_articoli}
            """
            #importo televisori: {importo_televisore * articolo.quantita} 
            #importo frigoriferi: {importo_frigorifero * articolo.quantita}

  def dettaglio_ordine(self): #controllato alle 9:36
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente 
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...
    importi_televisori = 0
    importi_frigoriferi = 0
    importo_totale = 0


    for articolo in self.ordini:
        if isinstance (articolo, Televisore):
            importi_televisori += articolo.prezzo * articolo.quantita
            print (f"""
                articolo: televisore
                importo: {importi_televisori}
                {articolo.scheda_articolo()}
                """)
        for articolo in self.ordini:
            if isinstance (articolo, Frigorifero):
                importi_frigoriferi += articolo.prezzo * articolo.quantita
                print (f"""
                    articolo: frigorifero
                    importo: {importi_frigoriferi}
                    {articolo.scheda_articolo()}
                    """)

      
    importo_totale = importi_televisori
    importo_totale += importi_frigoriferi



    return([importi_televisori, importi_frigoriferi, importo_totale])


t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)

#13 Risposta al Punto 1 : Per un ordine: il numero di articoli presenti e
# l'importo totale senza distinguere il tipo di articolo

ordine1.importo_ordine()

#14 Risposta punto 2.   Per un ordine: il dettaglio degli articoli, l'importo totale, 
# l'importo dei televisori e l'importo dei frigoriferi.
importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")



class Ordini(): #controllato 9:55
  def __init__(self,nome_negozio,codice_negozio):
    #16 Implementa il costruttore
    self.nome_negozio = nome_negozio
    self.codice_negozio =codice_negozio

    self.ordine = []

  def aggiungi_ordine(self,ordine):
    #17 Implementa il metodo
    if isinstance (ordine, Ordine):
      if (ordine not in self.ordine):
        self.ordine.append(ordine)
      else:
        print("ordine già presente")

  def rimuovi_ordine(self,ordine):
    #18 Implementa il metodo
    if isinstance (ordine, Ordine):
            if (ordine in self.ordine):
                self.ordine.remove(ordine)
            else:
                print("ordine non trovato")

  def totale_ordini(self):
    #19 Implementa il metodo
    #...
     tot = 0
     totT = 0
     totF = 0
    

     for ordine in self.ordine:
        importi = ordine.dettaglio_ordine()
        totT+= importi [0]
        totF += importi [1]
        tot = totT + totF


     return ([totT, totF, tot])


ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

# 20 Riposta punto 3: Per tutti gli ordini del negozio mostra 
# il dettaglio degli articoli, l'importo totale, 
# l'importo dei televisori e l'importo dei frigoriferi.
importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")