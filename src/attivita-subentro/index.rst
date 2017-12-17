Stima dei tempi per il subentro di un Comune
============================================

.. WARNING::
	Il documento è da ritenersi in versione beta.

L’esperienza dei Comuni subentrati, che hanno eseguito sulla piattaforma 1.7 milioni di operazioni anagrafiche nell'ultimo anno, dimostra che **è possibile passare ad ANPR** .
Le informazioni raccolte da ANPR, relativamente alle anomalie riscontrate sulle schede soggetto inoltrate da parte dei Comuni, permettono di individuare le attività che i Comuni realizzano e l'effort necessario per permettere il **completamento del subentro in circa 2 mesi**.


Attività per il subentro
^^^^^^^^^^^^^^^^^^^^^^^^

Gli obiettivi del subentro sono:

- **Migrazione dei dati dalle APR / AIRE locali ad ANPR.** I dati presenti nelle APR / AIRE locali sono trasferiti al sistema ANPR, favorendo l’allineamento dei codici fiscali associati ai soggetti così come attribuiti dall’Agenzia delle Entrate.
- **Integrazione degli APR locali con il sistema ANPR.** I Comuni che decidono di utilizzare le APR locali si assicurano che al momento della migrazione dei dati i propri sistemi siano integrati tramite i web services esposti dal sistema ANPR al fine di garantire l'immediata registrazione degli eventi anagrafici relativi ai cittadini residenti nel proprio territorio in ANPR.

L'esperienza che dei Comuni subentrati forniscono indicazioni sulle attività che i Comuni devono realizzare per raggiungere gli obiettivi del subentro, insieme alle loro software house, e che sono:

- **Aggiornamento del software** delle APR locali per l'integrazione con il sistema ANPR attraverso i web services esposti da quest'ultimo.
- **Predisposizione delle procedure di ETL** (estrazione, trasformazione e caricamento) per la predisposizione dei file di subentro da inoltrare al sistema ANPR.
- **Bonifica delle anomalie**, ove necessario dei dati anagrafici, segnalate dal sistema ANPR a valle dell'elaborazione del file di subentro inoltrato dal Comune.

.. Important::
	I *35 Comuni che sono subentrati* in ANPR e i *951 che sono in fase di pre-subentro* hanno coinvolto la quasi totalità delle software house interessate.
	Abbiamo analizzato tutti i dati relativi ai pre subentri dei comuni  ed estratto i seguenti risultati:

.. Note::
	**983 Comuni hanno esperienza di ANPR** pari al 12,32% dei Comuni italiani

	*948 Comuni sono in pre-subentro* pari al 11,88% dei Comuni italiani

	*35 Comuni sono subentrati* pari al 0,44% dei Comuni italiani

	**7.617.298 Schede soggetto sono state trattate da ANPR** pari al 12,57% della popolazione italiana

	*860.843 Cittadini subentrati** pari al 1,42% della popolazione italiana


	\* *Dati raccolti al 16/12/2017 dal sistema ANPR*


L'insieme di task che i Comuni devono realizzare per dare seguito alla **bonifica** dei dati anagrafici per cui sia riscontrata un'anomalia è sintetizzato nella seguente figura.

.. image:: image/IMAGE001_presubentro.png


Gestione delle anomalie
^^^^^^^^^^^^^^^^^^^^^^^

Le anomalie tracciate da ANPR sono suddivisibili in due macro-categorie, nel dettaglio:

- **89 Anomalie sui dati anagrafici**, la cui correzione vedrà direttamente coinvolto gli ufficiali anagrafici nel dare seguito alle necessarie istruttorie per constatare la corretto valorizzazione dei dati anagrafici stessi;
- **30 Anomalie sui file di subentro**, che riguardano la formazione dei file per il trasferimento dall’APR locale all’ANPR e, per la loro natura, vedano direttamente interessati i tecnici informatici che predispongono i file.

Nel dettaglio le 119 anomalie tracciate da ANPR nella fase di pre-subentro e subentro sono:

- **1 anomalia ERRORE** sui dati anagrafici (ES092 - Soggetto senza scheda famiglia/convivenza associata);
- **30 anomalie ERRORE** sui file di subentro (ad esempio: EN012 - Totale schede soggetto dichiarato per l'intera fornitura incongruente con quello calcolato);
- **88 anomalie WARNING** sui dati anagrafici (ad esempio: EC030 - Stato estero di nascita inesistente sulla tabella di riferimento).

.. Important::
	*Le uniche anomalie che impediscono ad comune di subentrare sono quelle classificate come ERRORE.*

	Vi è un'**unica anomalia sui dati anagrafici che impedisce ad un comune di subentrare in ANPR**, determinata dal *Regolamento anagrafico della popolazione residente* (DPR 223/1989), e viene segnalata nel caso in cui sia presente una persona senza scheda famiglia/convivenza associata.

Relativamente al task **valutazione anomalie** in cui il Comune analizza le anomalie segnalate da ANPR, si ricorda che i Comuni possono decidere di dare seguito alla bonifica dei dati, fatto salve le anomalie ERRORE, sia ex-ante che ex-post il subentro. *Il sistema ANPR assicura ai Comuni il controllo delle anomalie a valle del subentro impedendo la generazione di certificati con dati per cui è tracciata un'anomalia*.

Sulla base dei dati raccolti al 16/12/2017 dal sistema ANPR si rilevano i seguenti tassi:


- **schede anagrafiche con anomalie che impediscono il subentro è 0,01%**;
- **schede anagrafiche con aanomalie che si suggerisce di corregere prima del subentro è 0,53%**;
- schede anagrafiche con anomalia nel CF è pari al 1,36%.
- schede anagrafiche con altre anomalie è pari al 8,73%;

.. Note::
	**7.617.298 Schede soggetto trattate da ANPR**

	**768.929 Totale anomalie riscontrate**, di cui:

	- **381 anomalie ERRORE**
	- **40.729 anomalie WARNING che si suggerisce di "rimuovere prima del subentro"**

	ed inoltre:

	- *103.905 anomalie legate al codice fiscale*
	- *665.024 altre anomalie*


	\* *Dati raccolti al 16/12/2017 dal sistema ANPR*


Stima del tempo necessario al subentro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il tempo necessario al subentro del Comune dipende dalla:

1. capacità di **coinvolgere la software house alle attività** da realizzarsi, in merito si evidenzia che le software house hanno e stanno maturando esperienza nell'iterazione con ANPR;
2. **qualità dei dati anagrafici attualmente presenti nelle APR locali**, le schede anagrafiche fin qui inoltrate ad ANPR evidenziano un tasso di anomalie di circa il 10% pienamente accettabile;
3. realizzazione delle **attività una tantum da realizzarsi per il subentro**, quali censimento degli operatori e delle postazioni e successiva richiesta delle smart-card che richiedono un tempo di produzione ed invio di 20gg;
4. attività di **bonifica delle anomalie riscontrate**, attraverso cui si provvede alla bonifica delle posizioni critiche rimandando le altre, cosi come l'attuale "modus operandi" dei Comuni, al riscontro con il cittadino interessato.

Relativamente al precedente punto 4 avendo ipotizzato:

- una capacità di risoluzione delle anomalie riscontrate di allineamento pari a 20 per giornata uomo
- che il Comuni sia interessato a risolvere prima del subentro le sole anomalie segnalate da ANPR come ERRORE o WARNING che si suggerisce di "rimuovere prima del subentro", pari allo 0,53% della popolazione;

sono state elaborate le stime riportate nella seguente tabella:

+--------------------+------------+------------+----------------------------------+-------------+
| Popolazione Comune | % Anomalie | # Anomalie | # Anomalie risolte per gg uomo   | # gg uomo   |
+--------------------+------------+------------+----------------------------------+-------------+
|            200.000 |      0,53% |      1.080 |                             20,0 |          54 |
+--------------------+------------+------------+----------------------------------+-------------+
|            100.000 |      0,53% |        540 |                             20,0 |          10 |
+--------------------+------------+------------+----------------------------------+-------------+
|             50.000 |      0,53% |        270 |                             20,0 |          27 |
+--------------------+------------+------------+----------------------------------+-------------+
|             10.000 |      0,53% |         54 |                             20,0 |           3 |
+--------------------+------------+------------+----------------------------------+-------------+
|              5.000 |      0,53% |         27 |                             20,0 |           2 |
+--------------------+------------+------------+----------------------------------+-------------+
