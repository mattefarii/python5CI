class Veicolo:
  def __init__(self, codice, marca, modello, prezzo, annoRevisione):
    self.codice = codice
    self.marca = marca
    self.modello = modello
    self.prezzo = prezzo
    self.annoRevisione = annoRevisione

    self.veicoli = []



  def scheda_veicolo(self):
    #2 Ritorna una stringa contenente gli attributi del veicolo
    return "codice: ", self.codice, "marca: ", self.marca, "modello: ", self.modello, "prezzo: ", self.prezzo, "anno di revisione: ", self.annoRevisione


  def modifica_scheda(self):
    #3 Permette di modificare gli attributi del veicolo
    for veicolo in self.veicoli:
       if veicolo == self.veicoli[veicolo]:
        codice = int(input("Inserisci il nuovo codice del veicolo:"))
        marca = input("Inserisci la nuova marca del veicolo:")
        modello = input("Inserisci il nuovo modello del veicolo:")
        prezzo = int(input("Inserisci il nuovo prezzo del veicolo:"))
        annoRevisione = int(input("Inserisci il nuovo anno di revisione del veicolo:"))
        self.veicoli[veicolo].append(codice, marca, modello, prezzo, annoRevisione)

class Automobile(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,lunghezza,larghezza):
      self.codice = codice
      self.marca = marca
      self.modello = modello
      self.prezzo = prezzo
      self.annoRevisione = annoRevisione
      self.lunghezza = lunghezza
      self.larghezza = larghezza
      


    def scheda_veicolo(self):
      #5 Ritorna una stringa contenente gli attributi dell'automobile
      return "codice: ", self.codice, "marca: ", self.marca, "modello: ", self.modello, "prezzo: ", self.prezzo, "anno di revisione: ",self.annoRevisione, "lunghezza: ", self.lunghezza, "larghezza: ", self.larghezza

class Motoveicolo(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,tipo,potenza):
    #6 Implementa il costruttore
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.annoRevisione = annoRevisione
        self.tipo = tipo
        self.potenza = potenza


    def scheda_veicolo(self):
    #7 Ritorna una stringa contenente gli attributi del motociclo
        return "codice: ", self.codice, "marca: ", self.marca, "modello: ", self.modello, "prezzo: ", self.prezzo, "anno di revisione: ",self.annoRevisione, "tipo: ", self.tipo, "potenza: ", self.potenza
    

class Vendita():
  def __init__(self,codice,data, codiceVenditore):
    #8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.codiceVenditore = codiceVenditore

    self.automobili = []
    self.motocicli = []


  def aggiungi_veicolo(self,veicolo):
    if isinstance(veicolo,Automobile):
      self.automobili.append(veicolo)
    
    elif isinstance(veicolo,Motoveicolo):
      self.motocicli.append(veicolo)
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno
    


  def rimuovi_veicolo(self,veicolo):
    #10 Implementa il metodo
    if isinstance(veicolo,Automobile):
      self.automobili.remove(veicolo)
    
    elif isinstance(veicolo,Motoveicolo):
      self.motocicli.remove(veicolo)

    
    def importo_vendita(self, importo_vendita):
    #11 Stampa il numero di veicoli e l'importo totale della vendita giornaliera 
        totale_automobili = len(self.automobili)
        totale_motocicli = len(self.motocicli)
        totale_automobili = 0
        
        totale = 0

        for veicolo in self.veicoli:
            totale += veicolo.prezzo

        return totale
    


  def dettaglio_vendita(self):
    #12 Stampa il dettaglio della vendita e restituisce una lista contenente
    # [somma importi automobili, somma importi motocicli, somma importi totali, provvigione ]
    # e il totale della provvigione spettante al venditore sapendo che:
    # per automobili la provvigione spettante è il 3% del prezzo di vendita
    # per motocicli la provvigione spettante è il 2% del prezzo di vendita
    #...





    return([sommaA,sommaM,sommaA+sommaM,provvigione])


