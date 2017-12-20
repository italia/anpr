Procedura 000 - Verifica AT
===========================

.. WARNING::
	Il documento è da ritenersi in versione beta.
   
In quanto segue si riporta la procedura suggerita ai Comuni per dare seguito alla verfica della presenza di un soggetto nell'Anagrafe Tributaria al fine di riscontrare il Codice Fiscale ad esso attribuito.

Precondizione
^^^^^^^^^^^^^
Per dare seguito alla presente procedura è necessario che l'ufficiale d'anagrafe disponga:

- accesso al sistema gestionale del Comune (APR o AIRE locale) con diritti di lettura e aggiornamento delle schede soggetto;
- accesso al sistema *SIATEL v2.0 - PuntoFisco* reso disponibile dall'Agenzia delle Entrate. 

Diagramma della procedura
^^^^^^^^^^^^^^^^^^^^^^^^^
La seguente figura sintetizza la procedura per la gestione delle anomalie.

.. image:: image/IMAGE_000.png

Si evidenzia che le condizioni di uscita dalla procedura, le circonferenza in rosso, indicano:

- **SÌ**, è stato possibile riscontrare il soggetto nell'Anagrafe Tributaria con dati corrispondenti;
- **NO**, non è stato possibile riscontrare il soggetto nell'Anagrafe Tributaria con dati corrispondenti.

Descrizione azione
^^^^^^^^^^^^^^^^^^
In quanto segue si riporta una descrizione delle azioni previsti per la presente procedura.

AZIONE 000_001 - RICERCA SOGGETTO IN AT
---------------------------------------
L'ufficiale d'anagrafe, tramite il sistema *SIATEL v2.0 - PuntoFisco* reso disponibile dall'Agenzia delle entrate, ricerca il soggetto nell'Anagrafe Tributaria. A tale proposito si ricorda che il sistema *SIATEL v2.0 - PuntoFisco* permette la ricerca di un soggetto per:

- Codice fiscale
- Dati anagrafici completi
- Cognome, Casella senza cognome, Nome, Casella senza nome, Sesso, Data di Nascita, Casella senza giorno, Casella senza giorno e mese
- Cognome, Casella senza cognome, Nome, Casella senza nome, -----, Data di Nascita, Casella senza giorno, Casella senza giorno e mese
- Cognome, Casella senza cognome, Nome, Casella senza nome, Sesso, ---------------, Intervallo Anni
- Cognome, Casella senza cognome, Nome, Casella senza nome, Sesso, ---------------, ---------------, Comune e Prov. di Nascita
- Cognome, Casella senza cognome, Nome, Casella senza nome, -----, ---------------, ---------------, Comune e Prov. di Nascita
- Cognome, Casella senza cognome, ----, Casella senza nome, Sesso, Data di Nascita, Casella senza giorno, Casella senza giorno e mese, ---------------, Comune e Prov. di Nascita 
- -------, Nome, Casella senza nome, Sesso, Data di Nascita, Casella senza giorno, Casella senza giorno e mese, ---------------, Comune e Prov. di Nascita 

Si raccomanda di effettuare ricerche sfruttando i diversi criteri disponibili per verificare "al di là di ogni ragionevole dubbio" che la persona sia effettivamente sprovvista di codice fiscale, per evitare di creare posizioni riferite allo stesso soggetto, registrato più volte negli archivi dell'Agenzia delle Entrate con dati anagrafici diversi.

AZIONE 000_002 – ISTRUTTORIA
----------------------------
Nel ricordare che l'obiettivo ultimo del subentro è quello di assicurare che i dati presenti nelle APR locali siano trasferiti al sistema ANPR e nel contempo si assicuri l'allineamento dei codici fiscali associati ai soggetti così come attribuiti dall'Agenzia delle Entrate, si evidenzia che in caso di disallineamento tra il codice fiscale registrato dall'APR e quello attribuito dall'Agenzia delle Entrate o dei dati anagrafici del comune rispetto a quelli dell'Agenzia, l'ufficiale di anagrafe deve dare seguito ai necessari accertamenti al fine di verificare che i dati registrati nell'APR o nell'AIRE locali corrispondano alle informazioni registrate sugli Atti dello stato civile. Nel caso in cui la correzione dei dati anagrafici in possesso dell'Agenzia delle Entrate determini la necessità di mutare il codice fiscale attribuito al cittadino, si suggerisce che l'ufficiale d'anagrafe, per sanare la circostanza rilevata, convochi il cittadino indicandogli le seguenti possibilità:

- applicazione dell'`articolo 36 - Indicazioni sul nome <http://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2000-10-03;396~art36>`_ del DPR 396 del 3 novembre 2000 "Regolamento per la revisione e la semplificazione dell'ordinamento dello stato civile";
- applicazione dell'`articolo 89 - Modificazioni del nome o del cognome <http://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2000-10-03;396~art89>`_ del DPR 396 del 3 novembre 2000 "Regolamento per la revisione e la semplificazione dell'ordinamento dello stato civile";
- invito al cittadino a rivolgersi all'Agenzia delle Entrate per una nuova assegnazione di codice fiscale.

AZIONE 000_003 – AGGIORNAMENTO DATI ANAGRAFICI
----------------------------------------------
L'ufficiale d'anagrafe dà seguito agli aggiornamenti dei dati anagrafici sull'APR locale, anche in considerazione delle volontà espresse dal cittadino.  
