#############
Guida ad ANPR
#############


L'Anagrafe Nazionale della Popolazione Residente (ANPR) è la banca dati
nazionale nella quale confluiranno progressivamente le anagrafi
comunali.

È istituita presso il Ministero dell'Interno ai sensi dell'articolo 62
del Dlgs n. 82/2005 (Codice dell'Amministrazione Digitale).

Il Decreto Ministeriale 194/2014 stabilisce i requisiti di sicurezza, le
funzionalità per la gestione degli adempimenti di natura anagrafica, le
modalità di integrazione con i diversi sistemi gestionali nonché i
servizi da fornire alle Pubbliche Amministrazioni ed Enti che erogano
pubblici servizi che, a tal fine, dovranno sottoscrivere accordi di
servizio con lo stesso Ministero.

ANPR non è solo una banca dati ma un sistema integrato che consente ai
Comuni di svolgere i servizi anagrafici, consultare o
estrarre dati, monitorare le attività ed effettuare statistiche.

L'ANPR consentirà di:

-  evitare duplicazioni di comunicazione con le Pubbliche
   Amministrazioni;
-  garantire maggiore certezza e qualità al dato anagrafico;
-  semplificare le operazioni di cambio di residenza, emigrazioni,
   immigrazioni, censimenti, e molto altro ancora.

.. contents:: Indice dei contenuti
   :local:

1. Come lavorare con ANPR
=========================


Per utilizzare l'ANPR è possibile scegliere tra due modalità:

-  tramite il sito web di ANPR (Web Application - WA o tramite WA
   integrata);
-  modificando il proprio sistema gestionale per farlo colloquiare con
   ANPR (Web Services - WS).

La prima modalità (WA e WA integrata), che permette al Comune di
svolgere le funzioni anagrafiche utilizzando il sito web dell'ANPR, è
completamente gratuita e consente comunque al Comune, nel caso se ne
ravveda la necessità, di mantenere allineata una banca dati locale per
l'espletamento di altre funzionalità (gestione tributi, elettorale,
etc.).

La WA contiene le funzionalità che consentono:

-  il subentro (trasmissione dei dati delle APR e AIRE locali,
   consultazione degli esiti del subentro, consultazione delle
   anomalie);  
-  le registrazioni anagrafiche (iscrizioni, mutazioni, cancellazioni);
    
-  l'emissione della carta di identità cartacea;  
-  le certificazioni anagrafiche;  
-  le consultazioni della base dati e l'invio delle richieste di
   estrazione di parte della base dati di ANPR, individuata sulla base
   di specifici criteri di ricerca.

A carico del Comune è la predisposizione del file di subentro che
contiene i dati delle proprie anagrafi.

Qualora il Comune abbia esigenza di aggiornare automaticamente le
proprie basi dati locali, necessarie per lo svolgimento dei propri
compiti istituzionali diversi da quelli di natura propriamente
anagrafica, utilizzerà i servizi che ANPR rende disponibili a questo
scopo. In particolare, la WA integrata prevede un servizio di notifica
che consente all'ente locale di effettuare l'integrazione e
l'allineamento delle basi dati eventualmente conservate localmente.

-  l'ANPR restituisce al Comune, mediante un servizio di notifica, i
   dati di ciascuna  registrazione anagrafica effettuata tramite WA dal
   Comune stesso;
-  il Software locale del Comune, che dovrà disporre di un servizio di
   ricezione delle notifiche, elabora le notifiche trasmesse da ANPR e
   le utilizza per allineare le basi dati locali.

`Consulta la documentazione tecnica -
pdf <https://www.anpr.interno.it/portale/documents/20182/26001/Sito+WEB+di+ANPR+e+specifiche+di+integrazione.pdf>`__

`Consulta l'elenco delle funzionalità disponibili -
xls <https://www.anpr.interno.it/portale/documents/20182/50186/Allegato+2+-+Elenco+funzioni+WEB19102017.xlsx/fa626e37-b3d3-4724-8c86-cc5b3efec217>`__ (aggiornato
al 19 ottobre 2017)

La seconda modalità (WS) consente al Comune di continuare a lavorare con
il proprio sistema gestionale opportunamente modificato per integrare i
WS che consentono l'aggiornamento di ANPR in tempo reale.

Per utilizzare questa modalità è dunque necessario che il Comune
modifichi il software anagrafico per integrarlo con ANPR. Si fa presente
che, anche utilizzando questa modalità, le certificazioni che si
rilasciano ai cittadini sono esclusivamente quelle prodotte da ANPR (in
particolare i certificati sono validi soltanto se muniti del QR-CODE che
ne consente la verifica on-line).

Il Comune in tal caso opera attraverso il proprio sistema gestionale
modificato.

I WS previsti, da integrare nei sistemi gestionali, consentono:

-  il subentro (trasmissione dei dati delle APR e AIRE);
-  le registrazioni anagrafiche (iscrizioni, mutazioni, cancellazioni);
-  la consultazione dei dati registrati in ANPR per emettere la carta di
   identità cartacea e comunicare ad ANPR gli estremi del documento;
-  le certificazioni anagrafiche;
-  le consultazioni della base dati e l'invio delle richieste di
   estrazione di parte della base dati di ANPR, individuata sulla base
   di specifici criteri di ricerca

L'aggiornamento delle basi dati locali è eseguito dal sistema gestionale
che:

-  riceve l'esito della registrazione anagrafica effettuata da ANPR;
-  riporta localmente le variazioni.

`Consulta la documentazione tecnica -
pdf <https://www.anpr.interno.it/portale/documents/20182/26001/MI-14-AN-01+SPECIFICHE+DI+INTERFACCIA+WS_16_05_2017.pdf/4448b5f1-0e54-410b-a468-2cac69050129>`__

`Consulta l'elenco dei WS disponibili -
xls <https://www.anpr.interno.it/portale/documents/20182/26001/Utilizzo+WS+ANPR+27072016.xlsx>`__

Sono ammesse, ovviamente, modalità miste: il Comune potrà scegliere di
operare utilizzando il proprio sistema gestionale, riservandosi di
effettuare alcune operazioni utilizzando la Web Application (ad es. il
Comune potrà rilasciare certificati ai propri cittadini tramite il
proprio sistema gestionale e certificati ai cittadini residenti in altri
Comuni utilizzando la WA).

2. Come iniziare
================


La prima operazione da fare per poter utilizzare ANPR è la "compilazione
della scheda di monitoraggio".

La compilazione di tale scheda consente al Ministero dell'Interno di
predisporre il c.d. "Piano di subentro" e assegnare a ogni Comune la
data a partire dalla quale potrà iniziare a svolgere i passi
propedeutici all'utilizzo effettivo di ANPR illustrati di seguito.

Solo dopo aver compilato la scheda di monitoraggio il Comune che non ha
partecipato alla fase di sperimentazione, riceverà via PEC un messaggio
che conterrà:

-  la data per l'avvio dei test;
-  le credenziali per l'accesso al sistema di test;
-  la URL del sistema di test.

Dopo aver ricevuto tale messaggio sarà necessario effettuare le seguenti
attività:

-  test;
-  pre-subentro;
-  censimento degli utenti;
-  subentro.

 

 

3. Test
=======


ANPR prevede un ambiente di test che i Comuni possono utilizzare per:

-  verificare il software sviluppato dal Comune per l'estrazione dei
   dati dall'anagrafe comunale e il loro invio ad ANPR (test del
   subentro);
-  apprendere le modalità di funzionamento della Web Application (WA e
   WA integrata);
-  verificare il funzionamento del proprio sistema gestionale integrato
   con i servizi di ANPR (WS);
-  verificare l'allineamento delle proprie basi dati locali di servizio
   (WA integrata e WS).

Durante la fase di test , si dovrà inviare una parte dei dati registrati
nella base dati comunale: tali dati popoleranno l'ANPR, facilitando in
questo modo le successive fasi di apprendimento e test delle restanti
funzionalità.

L'ambiente di test è destinato prevalentemente ai fornitori dei SW
anagrafici comunali prima del rilascio della nuova versione al comune
per l'avvio dei test di pre-subentro.Per l'accesso all'ambiente di test
si utilizza un certificato di postazione e una user-id e password che
saranno trasmesse via PEC ai Comuni successivamente alla compilazione
della scheda di monitoraggio, con almeno due mesi di anticipo rispetto
alla data indicata dal comune per l'avvio dei test.

I link attuali rimangono

-  `Predisposizione e invio del file APR e AIRE preliminari
   all'esecuzione dei test (aggiornato al 19 ottobre 2017) -
   pdf <https://www.anpr.interno.it/portale/documents/20182/50186/Invio+file+di+Subentro.pdf/2f51abd2-bffc-4417-8f49-9dcaa49a3f99>`__
-  `Piano di test -
   pdf <https://www.anpr.interno.it/portale/documents/20182/23925/Piano+di+test.pdf/b79e113d-2da9-4f0c-9f13-a01ef2961bcb>`__
   (aggiornato il 27/02/2017, aggiunti test
   su unioni civili e convivente)
-  `Errori segnalati da ANPR -
   xls <https://www.anpr.interno.it/portale/documents/20182/26001/errori_anpr+16112017.xlsx/30e1fdcf-f97e-4f0c-99d3-e571aa021158>`__
   (aggiornato al 16 novembre 2017)
-  `Errori segnalati dall'Agenzia delle Entrate -
   xls <https://www.anpr.interno.it/portale/documents/20182/26001/errori_ae_11_05_2017.xlsx/eb45d775-21f1-4436-9a86-b8ab0169aee6>`__  a
   fronte delle richieste di attribuzione del codice fiscale e di
   verifica dei dati anagrafici, inoltrate dal Comune tramite WA o WS.

 

4. Pre-subentro
===============


È la fase immediatamente successiva a quella di test, che viene
utilizzata per rilevare, preliminarmente al subentro, la presenza di
eventuali criticità nella base dati.

Per poter eseguire questa fase è necessario aver predisposto il file di
subentro.

Si utilizza in questa fase un ambiente diverso da quello di test, che
consente di simulare il subentro e la successiva fase di esercizio.

La fase di pre-subentro consta di due attività principali:

**1\. Simulazione del subentro**

Questa attività, obbligatoria per tutti i Comuni, prevede:

-  l'invio da parte del Comune del file contenente i dati dell'APR e
   dell'AIRE locali;
-  l'elaborazione e controllo da parte di ANPR completa dei dati
   trasmessi;
-  l'applicazione degli indicatori di qualità concordati con ISTAT,
   sentito il Garante per la protezione dei dati personali, pubblicati
   nel portale
   `www.anpr.interno.it <https://www.anpr.interno.it/portale/documentazione>`__;
-  la validazione del codice fiscale con l'Agenzia delle Entrate;
-  la restituzione degli esiti al Comune (elenchi relativi alle anomalie
   riscontrate che saranno resi disponibili nell'area "Subentro e
   anomalie” della WA, in ambiente di pre-subentro).
   
In particolare, la validazione del codice fiscale consiste nel
verificare se il codice fiscale e i dati che concorrono alla sua
formazione (cognome e nome; sesso; luogo e data di nascita), coincidono
con quelli registrati dall'Agenzia delle Entrate.

Durante il pre-subentro, i Comuni che riceveranno le segnalazioni di
eventuali anomalie dovranno verificarle con attenzione, rimuoverle
utilizzando le proprie applicazioni quando dipendono da cause imputabili
al comune e, successivamente, effettuare un nuovo invio dei dati.

Le anomalie che non dipendono dal comune saranno gestite a livello
centrale. 

Per l'accesso all'ambiente di pre-subentro si utilizzano al momento le
stesse credenziali già distribuite per la l'accesso all'ambiente di test
e lo stesso certificato di postazione.

Per suggerimenti relativi al trattamento delle anomalie, consultare:

`Buone pratiche per le attività di
pre-subentro <https://anpr.readthedocs.io/en/latest/subentro/index.html>`__

 

**2\. Test di integrazione**

È una fase fortemente consigliata per i Comuni che utilizzano la
modalità WS e consiste nella esecuzione di uno specifico piano di test
che sarà fornito per la valutazione del corretto funzionamento del
sistema gestionale.

`Predisposizione e invio del file di pre-subentro (Apertura nuova
finestra) -
pdf <https://www.anpr.interno.it/portale/documents/20182/50186/Invio+file+di+Subentro.pdf/2f51abd2-bffc-4417-8f49-9dcaa49a3f99>`__
(aggiornato al 19 ottobre 2017)

`Piano dei test di integrazione (Apertura nuova finestra) -
pdf <https://www.anpr.interno.it/portale/documents/20182/23925/Piano+dei+test+di+integrazione_1.pdf>`__

5. Censimento degli utenti e delle postazioni
=============================================
 
Il DPCM 194/2014 prevede specifici requisiti di sicurezza per l'accesso
ad ANPR, consentito esclusivamente mediante postazioni certificate e,
quindi, munite di un certificato di postazione distribuito dal Ministero
dell'Interno; gli operatori comunali, inoltre, devono essere
riconosciuti e appositamente autorizzati e, per l'accesso in modalità
WA e WA integrata, titolari di una smart card, distribuita dal Ministero
dell'Interno unitamente al lettore.

Tutti i comuni, pertanto, dovranno censire:

-  gli utenti autorizzati all'accesso ad ANPR, specificando quelli che
   opereranno in modalità WA;
-  le postazioni che opereranno su ANPR.

Completato il censimento, i comuni riceveranno:

-  le Smart Card che saranno distribuite tramite la Prefettura
   competente;
-  i certificati di postazione che saranno acquisiti attraverso la WA.
-  i lettori che saranno recapitati direttamente al Comune;

Possono procedere con le operazioni di censimento i comuni prossimi al
subentro, già in possesso delle credenziali di accesso agli ambienti di
test e di pre-subentro, seguendo le istruzioni contenute nella `Guida
operativa per il censimento degli utenti e delle postazioni e delle
successive attività di consegna delle smart card -
pdf <https://www.anpr.interno.it/portale/documents/20182/209632/Guida+operativa+censimento+utenti+e+postazioni.pdf/bb0b9be5-b861-4cbb-8791-cc339b8c7d4b>`__.
(aggiornato al 11 maggio 2017)

Consulta anche:

 

-  `Guida rapida per il censimento degli utenti e delle postazioni per i
   Comuni -
   pdf <https://www.anpr.interno.it/portale/documents/20182/236150/Censimento+utenti+e+postazioni+-+guida+rapida+per+i+comuni.pdf/52bdcd74-1b04-4a25-b2b1-55922395a598>`__
-  `Guida rapida per il censimento degli utenti e delle postazioni per
   le Prefetture -
   pdf <https://www.anpr.interno.it/portale/documents/20182/236150/Censimento+utenti+e+postazioni+-+guida+rapida+per+le+Prefetture.pdf/c0422267-41db-4830-b178-fb7980f439f0>`__

6. Subentro 
===========

Superata con esito positivo la fase di pre-subentro, i Comuni potranno
procedere con le operazioni di subentro, che consistono nella ripetizione
in ambiente di subentro dell'invio dei file contenenti i dati
registrati nella propria APR e AIRE.

Sono necessarie le seguenti modifiche:

+------------------+------------------------+------------------------------------------------+-------------+
| Fase             | Attività               | Ambiente/Modalità                              | In carico a |
+==================+========================+================================================+=============+
| Pianificazione e | Contattare il proprio  | Aggiornamento                                  | Fornitore   |
| cronoprogramma   | fornitore del sw       | `dashboard <https://dashboard.anpr.it/>`__ (*) | del         |
|                  | anagrafico per         |                                                | comune      |
|                  | definire la data       |                                                |             |
+------------------+------------------------+------------------------------------------------+-------------+
|                  | Spedizioni lettori a   | In caso di mancata consegna,                   | Sogei       |
|                  | comune                 | avvertire Sogei                                |             |
|                  +------------------------+------------------------------------------------+-------------+
| Predisposizione  | Censimento utenti e    |                                                |             |
| ambiente         | comunicazione          | Area riservata CNSD                            | Comune      |
|                  | numero postazioni      |                                                |             |
|                  +------------------------+------------------------------------------------+-------------+
|                  | Personalizzazione e    | --                                             | Sogei       |
|                  | spedizione smart card  |                                                |             |
+------------------+------------------------+------------------------------------------------+-------------+
| Configurazione   | Postazioni, parametri, | Esercizio                                      | Comune      |
| comune           | ecc.                   |                                                |             |
+------------------+------------------------+------------------------------------------------+-------------+


(*) I fornitori che non ancora possiedono le credenziali di accesso alla
dashboard, dovranno richiederle tramite e-mail alla casella
segnalazioni-anpr@teamdigitale.governo.it

 

La configurazione del comune consiste in particolare nelle seguenti
attività, da effettuarsi in ambiente di esercizio:

 

-  Acquisizione e installazione certificati di postazione
-  Accesso alla WA da parte di un utente autorizzato per inserire

   -  Logo
   -  Estremi dell'autorizzazione all'assolvimento dell'imposta di bollo
      in modo virtuale
   -  Eventuale esenzione dal pagamento dei diritti di segreteria per
      tutti i certificati
   -  INDIRIZZI IP DA ABILITARE

 

Nella data prestabilita per il subentro, il comune chiude gli sportelli
al pubblico, assicurandosi che nessun dipendente stia operando sull'APR
ed effettua lo scarico e l'invio dei dati (APR e AIRE), con le stesse
modalità in precedenza utilizzate in ambiente di pre-subentro.

ANPR provvederà a elaborare nuovamente i dati, ripetendo i controlli
già descritti per la fase di pre-subentro e restituendone gli esiti al
Comune, che riceverà via PEC una comunicazione che:

-  conferma l'avvenuto subentro
-  notifica il mancato subentro. Il Comune, in tal caso, dovrà procedere
   alla rimozione degli errori/anomalie segnalate da ANPR; il Ministero
   dell'Interno comunicherà la data prevista entro la quale il Comune
   dovrà procedere a un nuovo invio del file

 

In caso di esito positivo del subentro, gli adempimenti anagrafici
dovranno essere effettuati dai Comuni mediante l'utilizzo dell'ANPR.

Da questo momento in poi, gli adempimenti anagrafici dovranno essere
effettuati dai Comuni mediante l'utilizzo dell'ANPR, sulla base della
modalità prescelta.

Contestualmente, si effettuerà in automatico la revoca del certificato
di sicurezza attualmente utilizzato per l'invio delle comunicazioni
INA-SAIA e l'aggiornamento dell'AIRE centrale che saranno “dismesse” con
il subentro di ANPR:

 

-  le comunicazioni alle PA/ENTI che avranno sottoscritto un accordo con
   il Ministero dell'Interno saranno effettuate automaticamente da ANPR;
-  l'elenco unico sarà predisposto sulla base del contenuto di ANPR.

 

Rimane la facoltà per i Comuni di consentire l'accesso ai propri dati
anagrafici, attraverso la sottoscrizione di apposite convenzioni, così
come previsto dal DPCM n. 194/2014 (art. 5, comma 4).

7. Cosa cambia per i comuni dopo il subentro
============================================


A questo
`link <https://anpr.readthedocs.io/en/latest/comuni/index.html>`__ sono
disponibili ulteriori documenti utili ai comuni per comprendere meglio i
cambiamenti e i vantaggi di ANPR, in particolare dopo il subentro.

