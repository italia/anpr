Stima dei tempi per il subentro di un Comune
============================================

.. WARNING::
	Il documento è da ritenersi in versione beta.

L’esperienza dei Comuni subentrati, che hanno eseguito sulla piattaforma 1.7 milioni di operazioni anagrafiche nell’ultimo anno, dimostra che **è possibile passare ad ANPR**. 
Le informazioni raccolte da ANPR, relativamente alle anomalie riscontrate sulle schede individuali soggetto, che sono di fatto tutte le informazioni anagrafiche del cittadino, permettono di individuare le attività che i Comuni realizzano e l’effort necessario per permettere il **completamento del subentro in circa 2 mesi**.
	

Attività per il subentro
^^^^^^^^^^^^^^^^^^^^^^^^

Gli obiettivi del subentro sono:

- **Migrazione dei dati dalle APR / AIRE locali ad ANPR.** I dati presenti nelle APR / AIRE locali sono trasferiti al sistema ANPR, favorendo l’allineamento dei codici fiscali associati ai soggetti così come attribuiti dall’Agenzia delle Entrate.
- **Integrazione degli APR locali con il sistema ANPR.** I Comuni che decidono di utilizzare le APR locali si assicurano che, al momento della migrazione dei dati, i propri sistemi siano integrati tramite i web services esposti dal sistema ANPR al fine di garantire l’immediata registrazione degli eventi anagrafici relativi ai cittadini residenti nel proprio territorio in ANPR.

L’esperienza  dei Comuni subentrati fornisce indicazioni sulle attività che gli altri Comuni, insieme alle loro software house, devono realizzare per raggiungere gli obiettivi del subentro:

- **Aggiornamento del software** delle APR locali per l’integrazione con il sistema ANPR attraverso i web services esposti da quest’ultimo (questo passo non è necessario nel caso di subentro in modalità webapp e si può assumere come già completato nel caso in cui il fornitore sia lo stesso usato da un altro Comune già subentrato).
- **Predisposizione delle procedure di ETL** (estrazione, trasformazione e caricamento) per la predisposizione dei file di subentro da inoltrare al sistema ANPR.
- **Bonifica delle anomalie**, ove necessario, dei dati anagrafici, segnalate dal sistema ANPR a valle dell’elaborazione del file di subentro inoltrato dal Comune.


L’insieme di task che i Comuni realizzano per dare seguito alla bonifica dei dati anagrafici per cui sia riscontrata un’anomalia è sintetizzato nella seguente figura.

.. image:: image/IMAGE001_presubentro.png

.. Note::
	**Il nostro campione**
	
	Abbiamo reperito tutti i dati disponibili al 16 Dicembre, rispetto ai quali sappiamo che:
	
	* 948 Comuni sono in pre-subentro pari al 11,88% dei Comuni italiani
	* 35 Comuni sono subentrati pari al 0,44% dei Comuni italiani
	* 860.843 Cittadini subentrati pari all'1,42% della popolazione italiana
	* 7.617.298 schede individualisoggetto, quindi informazioni anagrafiche di altrettanti cittadini, sono state esaminate complessivamente da ANPR
	
	L’analisi quindi si basa su un campione di posizioni anagrafiche rappresentativo pari al 12,57% della popolazione italiana.
	
	I *35 Comuni che sono subentrati* in ANPR e i *951 che sono in fase di pre-subentro* hanno coinvolto la quasi totalità delle software house interessate.


Gestione delle anomalie
^^^^^^^^^^^^^^^^^^^^^^^

Le anomalie tracciate da ANPR sono suddivisibili in due macro-categorie, nel dettaglio:

- **89 tipi di anomalia sui dati anagrafici**, la cui correzione vedrà direttamente coinvolto gli ufficiali anagrafici nel dare seguito alle necessarie istruttorie per constatare la corretto valorizzazione dei dati anagrafici stessi;
- **30 tipi di anomalia sui file di subentro**, che riguardano la formazione dei file per il trasferimento dall’APR locale all’ANPR e, per la loro natura, vedano direttamente interessati i tecnici informatici che predispongono i file.

Nel dettaglio i 119 tipi di anomalia tracciati da ANPR nella fase di pre-subentro e subentro sono:

- **1 tipo anomalia ERRORE** sui dati anagrafici (ES092 - Soggetto senza scheda famiglia/convivenza associata);
- **30 tipi di anomalie ERRORE** sui file di subentro (ad esempio: EN012 - Totale schede soggetto dichiarato per l'intera fornitura incongruente con quello calcolato);
- **88 tipi di anomalie WARNING** sui dati anagrafici (ad esempio: EC030 - Stato estero di nascita inesistente sulla tabella di riferimento).

.. Important::
	*Le uniche anomalie che impediscono ad comune di subentrare sono quelle classificate come ERRORE.*
	
	*Le anomalie di tipo ERRORE sul file di subentro implicano un difetto nel software usato dal Comune e devono quindi essere risolte dal fornitore del software.   Si può assumere che, se il fornitore è lo stesso usato da un altro Comune che è già subentrato, l'incidenza di queste anomalia sarà zero in quanto il software sarà già stato verificato e corretto nel subentro precedente.*
	
	Vi è un'**unica anomalia sui dati anagrafici che impedisce ad un comune di subentrare in ANPR**, determinata dal *Regolamento anagrafico della popolazione residente (DPR 223/1989)*, e viene segnalata nel caso in cui sia presente una persona senza scheda famiglia/convivenza associata. Questa tipologia di errore va risolta dal personale Comunale e si può ripresentare in corrispondenza di ogni subentro, per tutti i Comuni gestiti da uno stesso fornitore.

Relativamente all’attività di **valutazione anomalie** in cui il Comune analizza le anomalie segnalate da ANPR, si ricorda che i Comuni possono decidere di dare seguito alla bonifica dei dati, fatto salve le anomalie ERRORE, sia *prima* che *dopo* il subentro. *Il sistema ANPR assicura ai Comuni il controllo delle anomalie a valle del subentro impedendo la generazione di certificati con dati per cui è tracciata un’anomalia.* A seguito della valutazione del risultato indicante le anomalie, il Comune organizza la bonifica dei dati sulla base delle risorse disponibili (forze lavoro ed economiche), individuando le anomalie da risolvere prima del subentro e quelle da realizzarsi successivamente al subentro stesso.

Sulla base dei dati raccolti al 16/12/2017 dal sistema ANPR si rilevano i seguenti tassi:

- **schede anagrafiche con anomalie riscontrate che impediscono il subentro e che quindi vanno corrette: 0,01%**;
- **schede anagrafiche con anomalie riscontrate che si suggerisce di correggere prima del subentro: 0,53%**;
- schede anagrafiche con anomalie nel CF: 1,36%.
- schede anagrafiche con altre anomalie: 8,73%;

.. Note::
	**I numeri delle anomalie in dettaglio**
	
	**7.617.298 Schede individuali trattate da ANPR**

	**768.929 Totale anomalie riscontrate**, di cui:

	- **381 anomalie ERRORE**
	- **40.729 anomalie WARNING che si suggerisce di “rimuovere prima del subentro”"**

	ed inoltre:

	- *103.905 anomalie legate al codice fiscale*
	- *665.024 altre anomalie*

Stima del tempo necessario al subentro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il tempo necessario al subentro del Comune dipende dalla:

1. capacità di **coinvolgere la software house del Comune nelle attività da realizzarsi, e disponibilità della software house a fare una prova di subentro**. Il caso in cui la stessa software house abbia già completato con successo un subentro con un altro Comune rende probabilmente non necessario questo passo;
2. **qualità dei dati anagrafici attualmente presenti nelle APR locali**, le schede anagrafiche fin qui inoltrate ad ANPR evidenziano un tasso di anomalie complessivo di circa il 10%;
3. realizzazione delle **attività una tantum da realizzarsi per il subentro**, quali censimento degli operatori e delle postazioni e successiva richiesta delle smart-card che richiedono un tempo di produzione ed invio di 20 gg, che si può svolgere in parallelo alle altre attività;
4. attività di **bonifica delle anomalie riscontrate**, nella quale si dà priorità, effettuandola prima del subentro, alla bonifica delle posizioni critiche rimandando le altre ad un momento successivo.

Relativamente al precedente punto 4 si assume che il Comune si organizza per risolvere prima del subentro le sole anomalie segnalate da ANPR come ERRORE e i WARNING accompagnati dalla dizione  “rimuovere prima del subentro”: complessivamente queste anomalie sono , pari allo 0,54% della popolazion;

Sono state elaborate le stime (teoriche) riportate nella seguente tabella:

+--------------------+------------+------------+----------------------------------+-------------+
| Popolazione Comune | % Anomalie | # Anomalie | # Anomalie risolte per gg uomo   | # gg uomo   |
+--------------------+------------+------------+----------------------------------+-------------+
|            200.000 |      0,54% |      1.080 |                                7 |         154 |
+--------------------+------------+------------+----------------------------------+-------------+
|            100.000 |      0,54% |        540 |                                7 |          77 |
+--------------------+------------+------------+----------------------------------+-------------+
|             50.000 |      0,54% |        270 |                                7 |          39 |
+--------------------+------------+------------+----------------------------------+-------------+
|             10.000 |      0,54% |         54 |                                7 |           8 |
+--------------------+------------+------------+----------------------------------+-------------+
|              5.000 |      0,54% |         27 |                                7 |           4 |
+--------------------+------------+------------+----------------------------------+-------------+

Il dettaglio dei tempi
^^^^^^^^^^^^^^^^^^^^^^

In conclusione gli step necessari al comune per il subentro:

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+
| Attività                                                                                   | Attività per il Comune                                                                          | Effort per il Comune (gg)  | Tempo (gg)                                 |             
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+
| Prova di subentro. La sw house fa una prova di subentro ed indica le anomalie da risolvere | Contattare la propria sw house                                                                  | 0                          | 1                                          |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+
| Censimento e produzione delle smart card                                                   | Censimento  degli operatori comunali sul sito del Ministero                                     | 1                          | 20                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+  
| Bonifica dei dati prima del subentro                                                       | Gli operatori anagrafici correggono le anomalie secondo una pianificazione desunta dall’’effort | 0-60                       | Dipendente dal numero di risorse impiegate |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+
| Ritiro e configurazione smart card                                                         |                                                                                                 | 1                          | 1                                          |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+
| Subentro                                                                                   | Chiusura delle attività di sportello ed invio del file presso ANPR e acquisizione dei risultati | 1                          | 1                                          |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------+


Conclusioni 
^^^^^^^^^^^

Dall’analisi dei dati si evince che i comuni, soprattutto quelli fino a 10.000 abitanti (oltre l’80% dei Comuni italiani), hanno un tempo stimato di risoluzione delle anomalie anagrafiche bloccanti  inferiore ai 10 giorni. Si precisa che le stime sono state realizzate assumendo che le risorse siano assegnate completamente alla bonifica dei dati; pertanto, l’organizzazione del singolo comune dovrà tenere conto della effettiva disponibilità delle risorse. Comunque è oltremodo realistico prevedere che, anche nei casi peggiori, il completamento della bonifica delle anomalie bloccanti è di gran lunga inferiore ai 2 mesi.

In considerazione che per il subentro vanno considerati anche i  tempi tecnici di produzione e distribuzione delle smart card, che può essere avviata già dal primo giorno, é di circa 15-20 giorni, si ritiene **ragionevole indicare una stima conservativa di 2 mesi come tempo medio dei comuni** per effettuare tutte le operazioni necessarie ad un subentro.

**Nel caso il comune avviasse la richiesta delle smart card in anticipo rispetto alle date previste di subentro in tempi potrebbero essere ulteriormente ridotti.**

Al fine di facilitare l’organizzazione delle attività dei comuni per la bonifica dei dati anagrafici, si ricorda che il **completamento del subentro agevola le amministrazioni nella azione di correzione delle anomalie, in considerazione che ANPR offre una integrazione privilegiata con l’anagrafe tributaria**, l’adozione di tabelle di decodifica riconosciute a livello nazionale e non da meno una riduzione delle esigenze dell’impegno di risorse per soddisfare il debito informativo dei comuni verso istituzioni centrali, quali: INPS, ISTAT, MCTC, ed altri.


Ulteriori ottimizzazioni possibili
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

E’ utile ricordare che le operazioni di pre subentro e subentro possono essere fatte in modalità remota attraverso una chiamata alle relative API (Web Service). In questo scenario al comune sarebbe richiesto, oltre alla bonifica dei dati, di fatto solo l’attivazione delle smart card.

