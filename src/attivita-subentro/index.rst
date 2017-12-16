Le attività per il subentro di un Comune
========================================

.. WARNING::
	Il documento è da ritenersi in versione beta.
	
L’esperienza dei Comuni subentrati dimostra che è possibile passare ad ANPR, anzi che ANPR funziona e che sia ora di fare il passaggio dato che non abbia più senso aspettare, né aspettare che qualcuno lo faccia per voi.

Gli obiettivi del subentro sono:

- **Migrazione dei dati dalle APR / AIRE locali ad ANPR.** I dati presenti nelle APR / AIRE locali sono trasferiti al sistema ANPR, favororendo l’allineamento dei codici fiscali associati ai soggetti così come attribuiti dall’Agenzia delle Entrate.
- **Integrazione degli APR locali con il sistema ANPR.** I Comuni che decidono di utilizzare le APR locali si assicurano che al momento della migrazione dei dati i propri sistemi siano integrati tramite i web services esposti dal sistema ANPR al fine di garantire l'immediata registrazione degli eventi anagrafici relativi ai cittadini residenti nel proprio territorio in ANPR.

L'esperienza dei Comuni subentrati forniscono indicazioni sulle attività che i Comuni devono realizzare per raggiungere gli obiettivi del subentro. 

L'esperienza realizzata dai Comuni subentrati in ANPR si evidenzia che le attività che i Comuni realizzano, insieme alle loro software house, sono:

- **Aggiornamento del software** delle APR locali per l'integrazione con il sistema ANPR attraverso i web services esposti da quest'ultimo.
- **Predisposizione delle procedure di ETL** (estrazione, trasformazione e caricamento) per la predisposizione dei file di subentro da inoltrare al sistema ANPR.
- **Bonifica delle anomalie**, ove necessario dei dati anagrafici, segnalate dal sistema ANPR a valle dell'elaborazione del file di subentro inoltrato dal Comune.
	
.. Important:
	I 35 Comuni che sono subentrati in ANPR e i 951 che sono in fase di pre-subentro ha coinvolto la quasi totalità delle software house interessate.
	L'esperienza maturata dalla software house permette ai Comuni di concentrano sull'azione di **bonifica**.

La anomalie tracciate da ANPR sono suddivisibili in due macro-categorie, nel dettaglio:
- 89 Anomalie sui dati anagrafici, la cui correzione vedrà direttamente coinvolto gli ufficiali anagrafici nel dare seguito alle necessarie istruttorie per constatare la corretto valorizzazione dei dati anagrafici stessi
- 30 Anomalie sui file di subentro, che riguardano la formazione dei file per il trasferimento dall’APR locale all’ANPR e, per la loro natura, vedano direttamente interessati i tecnici informatici che predispongono i file

Nel dettaglio ANPR per il subentro evidenzia 119 anomalie, di cui:

- 1 anomalia ERRORE sui dati anagrafici (ES092 - Soggetto senza scheda famiglia/convivenza associata)
- 30 anomalie ERRORE sui file di subentro (ad esempio: EN012 - Totale schede soggetto dichiarato per l'intera fornitura incongruente con quello calcolato)
- 88 anomalie WARNING sui dati anagrafici (ad esempio: EC030 - Stato estero di nascita inesistente sulla tabella di riferimento)

.. Important:
	Le uniche anomalie che impediscono ad comune di subentrare sono quelle classificate come ERRORE. L'**unica anomalia sui dati anagrafici che impedisce ad un comune di subentrare in ANPR**, determinata dal *Regolamento anagrafico della popolazione residente* (DPR 223/1989), è viene segnalata nel caso un cui sia presente una persona senza scheda famiglia/convivenza associata.
	


	



