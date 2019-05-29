[Torna all'indice](../index.md)

# Nota rilascio versione 5.X (ANPR02) #

Autore : mttfranci, Date: 2019-05-29, Versione : 001

Abstract : Al fine in particolare di migliorare le performance dei servizi ANPR, e' stato predisposto un set di aggiornamenti che si attiveranno a partire dalla versione 5 (ANPR02).


**1) Ottimizzazione risposta servizio consultazione 3002 in ambiente di produzione**  
  
*Issue di riferimento : [1031](https://github.com/italia/anpr/issues/1031)*    
Nella versione 5 vengono inclusde alcune modifiche al comportamento del servizio 3002 :   

1.1) Scheda sintetica  
Se viene restituito più di un soggetto, indipendentemente dalle sezioni richieste, ne verranno restituite al massimo un sotto insieme :
generalita, famiglia, legame, residenza, dati cancellazione
Eccezione : Se viene interrogata una famiglia (tipo scheda 3), la scheda sara' completa per tutti i soggetti (non vale per le convivenze, tipo scheda 4)

1.2) Ricerca per comune di residenza
Se non viene specificata espressamente la ricerca nazionale, i soggetti verranno ricercati solo nel comune di residenza (se non specificato nel comune mittente).

1.3) Sezioni aggiuntive
E' ora disponibile una sezione generale per le anomalie anche quando la risposta abbia avuto esito positivo (ad esempio con un avviso se la scheda restituita e' sintetica).
Se viene effettuata una ricerca per famiglia/convivenza viene anche restituita espressamente la sezione della famiglia oltre a comparire nei singoli soggetti.



**2) Revisione risposte servizi di registrazione**  
  
*Issue di riferimento : [1079](https://github.com/italia/anpr/issues/1079)*     

Con riferimento alla sezione tipoDatiSoggettiRisposta, restituito nel blocco della RispostaComune dei servizi di registrazione (famiglie 1000, 2000, 5000, A000),
Non verranno più restituite tutte le sezioni, ma solo le sezioni che contengono dei dati generati dal sistema ANPR.
Tutte le altre sezioni non verranno restituite.


**3) L'operazione 4005 sostituisce in modalita' asincrona le richieste multiple dei servizi 3003/3007**  
  
*Issue di riferimento : [1161](https://github.com/italia/anpr/issues/1161)*     

Il servizio di [richieste asincrone (4005)](../4000/nota_4005_richieste_asincrone.md) sostituisce la modalit&agrave; 'elenchi richieste' dei servizi di gestione richieste (3003) e indetificativi ANPR (3007). Il nuovo servizio prevede due modalit&agrave;. Con la prima (Elaborazione) viene inserita una richiesta di elaborazione, mentre la seconda (verifica stato) permette di verificare se la richiesta &egrave; e pronta e scaricarla.

