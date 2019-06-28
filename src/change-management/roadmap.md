# Prossime versioni


### Versione 5.5-RC (2019-07-01)

+ (Requirement) Limitazione richieste 4005 ad un periodo massimo di un mese (issue: [https://github.com/italia/anpr/issues/1410](https://github.com/italia/anpr/issues/1410))
    + Verrà introdotto un controllo che bloccherà le richieste per le quali il periodo di riferimento della richiesta abbia durata maggiore di 30 giorni.

+ (Requirement) Verifica obbligatorietà numero permesso di soggiorno da XSD (issue: [https://github.com/italia/anpr/issues/1413](https://github.com/italia/anpr/issues/1413))
    + Adesso l'xsd verifica che il numero del permesso di soggiorno sia impostato.
    

### Versione 6.0-RC (2019-07-15)

+ (Requirement) Fine supporto servizio richiesta paternità maternità 3001
    + Con il rilascio della versione ANPR03 di ANPR, questo servizio sarà supportato solo per i 3 mesi di supporto alla precedente versione.

+ (Requirement) Fine supporto servizio di invio forniture subentro S001
    + Con il rilascio della versione ANPR03 di ANPR, l'acquisizione delle forniture di subentro potrà avvenire esclusivamente da webapp.


# Roadmap

+ (Feature) Scarico massivo dati ANPR  per motivata richiesta
    + L'intervento prevede l'automazione delle richieste di scarico massivo per motivata richiesta. Sono previsti i seguenti macroprocessi:   -       gestione della richiesta di scarico massivo per giustificato motivo; -       realizzazione di una procedura batch di estrazione massiva con innesco da richiesta approvata (cfr req 55986);  -       nuova tipologia di notifica di fine elaborazione per la comunicazione dell’unico o degli “n” identificativi di file prodotti. 

+ (Requirement) Accesso tramite CIE/CNS/SPID
    + Accesso all'applicazione InterrogazioneCittadino, per la consultazione dei propri dati, con CNS,CIE e credenziali SPID.

