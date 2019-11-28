# Changelog

### Versione 5.6.9 (2019-11-28)

+ (Bug) Certificato storico di residenza - prima data iscrizione rettificata
    + In caso di rettifica della data di iscrizione sul certificato non viene riportatata la data aggiornata 
E' necessario quindi recuperare la data di iscrizione nel primo comune più aggiornata.

+ (Bug) Revoca matrimonio - non devono essere inseriti i dati  (issue: [https://github.com/italia/anpr/issues/1778](https://github.com/italia/anpr/issues/1778))
    + In caso di revoca dati matrimonio non devono essere inseriti gli estremi del matrimonio errato.
    
+ (Bug) Annullamento iscrizione bloccata dal coniuge (issue: [https://github.com/italia/anpr/issues/1766](https://github.com/italia/anpr/issues/1766))
    + Risolto il problema che impediva l'annullamento di un'iscrizione a seguito di iscrizione del coniuge e di ulteriori mutazioni sul coniuge.

### Versione 5.6.8 (2019-11-14)

+ (Bug) Errore upload forniture APR / AIRE in ambienti di test / presubentro (issue: [https://github.com/italia/anpr/issues/1762](https://github.com/italia/anpr/issues/1762))
    + Molto spesso l'upload delle forniture di subentro in ambiente di test / presubentro poteva non andare a buon fine.

+ (Bug) Assenza elemento formatoRichiesta nella elaborazione 4005 (issue: [https://github.com/italia/anpr/issues/1760](https://github.com/italia/anpr/issues/1760))
    + Nella elaborazione 4005 veniva impostato solo il tag formatoRisposta ma non quello formatoRichiesta.

### Versione 5.6.7 (2019-10-25)

+ (Bug) Fix [2003] Anomalia EN240 (issue: [https://github.com/italia/anpr/issues/1676](https://github.com/italia/anpr/issues/1676))
    + In alcuni casi la cancellazione non verificava correttamente l'elenco delle passate residenze.


### Versione 5.6.6 (2019-10-21)

+ (Requirement) Disabilitazione servizio subentro in ambiente di produzione (issue: [https://github.com/italia/anpr/issues/1289](https://github.com/italia/anpr/issues/1289))
    + Come annunciato il servizio S001 rimane abilitato solo fino all'ambiente di presubentro.
    
+ (Requirement) Servizio 3001 disabilitato in tutti gli ambienti eccetto produzione (issue: [https://github.com/italia/anpr/issues/1289](https://github.com/italia/anpr/issues/1289))
    + Il servizio 3001 è interrogabile ancora fino al 1 Dicembre 2019 solo in produzione.  
    
+ (Requirement) AN-74 Web - Risoluzione disallineamenti - gestione CF rifugiati
    + La funzionalità è resa disponibile per il collegamento tra CF numerici rifugiati e CF alfanumerici con stessi dati anagrafici.  
    

### Versione 5.6.5 (2019-10-17)

+ (Bug) Certificazione - Stampa frazione null (issue: [https://github.com/italia/anpr/issues/1675](https://github.com/italia/anpr/issues/1675))
    + In alcuni casi poteva essere stampata la dicitura "frazione : null" in modo erroneo.

### Versione 5.6.4 (2019-10-15)

+ (Requirement) Aggiunta parentesi al tipoProvinciaContea
    + Adesso il tipoProvinciaContea accetta anche le parentesi.

### Versione 5.6.3 (2019-10-12)

+ (Bug) Gestione esiti servizi 3003/4005 (issue: [https://github.com/italia/anpr/issues/1665](https://github.com/italia/anpr/issues/1665))
    + In alcuni casi i servizi 3003/4005 potevano portare ad un errore non gestito a causa di una non corretta gestione del meccanismo di verifica presenza idOperazioneComune ancora in stato di elaborazione.

### Versione 5.6.2 (2019-10-08)

+ (Bug) Port hotfix 5.5.6 su ramo 5.6

### Versione 5.5.6 (2019-10-08)

+ (Bug) EN493 in caso di modifica responsabile convivenza (issue: [https://github.com/italia/anpr/issues/1643](https://github.com/italia/anpr/issues/1643))
    + In caso di mutazione responsabile convivenza a volte si attivava impropriamente il controllo EN493.

+ (Bug) 1010 - associazione errato responsabile convivenza (issue: [https://github.com/italia/anpr/issues/1620](https://github.com/italia/anpr/issues/1620))
    + Risolto il bug per il servizio di iscrizione della convivenza.
    
+ (Bug) ws 1002: errata acquisizione dati unioneCivile  (issue: [https://github.com/italia/anpr/issues/1613](https://github.com/italia/anpr/issues/1613))
    + In presenza di sciogliemento unione poteva essere acquisito il luogo evento errato.
    
+ (Bug) 3002 - Nella ricerca per convivenza a volte veniva restituito erroneamente la voce "Responsabile assente"
    + Avveniva in caso venisse cercata una scheda famiglia esistente.  

### Versione 5.6.1 (2019-10-01)

+ (Bug) Port hotfix 5.5.5 su ramo 5.6

### Versione 5.5.5 (2019-10-01)

+ (Bug) WebApp - Validazione campo descrizione specie
    + L'applicazione web non accetta alcuni valori validi secondo gli xsd per il campo specie.

### Versione 5.6.0 (2019-09-26)

+ (Requirement) Richieste di allineamento dati trasmesse dai Consolati
    + Nell’applicazione WEB di ANPR è stata inserita una nuova funzionalità nella sezione “Utilità e notifiche” denominata “Richieste di allineamento dati trasmesse dai Consolati”. A partire da tale funzionalità il funzionario del Comune (sia subentrato che non subentrato) potrà ricercare le richieste di allineamento dati anagrafici. Solo il comune subentrato a fronte di ciascuna richiesta, potrà procedere all'allineamento dati tramite web app. Il comune non subentrato dovrà utilizzare il propio gestionale oppure l'AnagAire

### Versione 5.5.4 (2019-09-18)

+ (Bug) Malfunzionamento estrazione richiesta singola (issue: [https://github.com/italia/anpr/issues/1571](https://github.com/italia/anpr/issues/1571))
    + In caso di richiesta di estrazione singola 3003, non viene restituito il risultato ma un errore EN122.

+ (Bug) ANPRWEB campo annotazioni 6001 simbolo euro non ammesso (issue: [https://github.com/italia/anpr/issues/1580](https://github.com/italia/anpr/issues/1580))
    + Accettare l'inserimento del carattere € nei campi note nella richiesta di certificato dell'applicazione Web di ANPR.

+ (Bug) Subentro - Caricamento piano indirizzo (issue: [https://github.com/italia/anpr/issues/1339](https://github.com/italia/anpr/issues/1339))
    + Il piano è definito di 5 caratteri ma viene troncato a 3.

### Versione 5.5.3 (2019-08-08)

+ (Requirement) A001 e A002 controllare la presenza del tipo elettore

### Versione 5.5.2 (2019-07-24)

+ (Bug) Web - Validazione località estera
    + La web app non accettava le parentesi nella località estera di nascita.

+ (Bug) Web - Validazione IP con zero a sinistra
    + Il salvataggio dell'IP nell'area amministrazione non valida i numeri con degli zero a sinistra.
    
+ (Bug) Anomali Verifica esito operazione 4005 (issue: [https://github.com/italia/anpr/issues/1477](https://github.com/italia/anpr/issues/1477))
    + In alcuni casi il servizio di verifica esito richieste sincrone non restituiva il contenuto dell'elaborazione correttamente.
    
+ (Bug) A006 Errore valorizzazione idSchedaSoggettoComune stesso comune di riferimento AIRE (issue: [https://github.com/italia/anpr/issues/1475](https://github.com/italia/anpr/issues/1475))
    + A006  Errore valorizzazione idSchedaSoggettoComune in caso di cambio di residenza all'interno dello stesso comune di riferimento AIRE     

+ (Bug) Anomalia configurazione comuni fittizi ambiente free test (issue: [https://github.com/italia/anpr/issues/1479](https://github.com/italia/anpr/issues/1479))
    + Alcuni dei comuni fittizi 888* non erano configurati correttamente per poter effettuare il subentro di test.


### Versione 5.5.1 (2019-07-11)

+ (Requirement) WebApp - Modifiche segnalazione ambiente di accesso
    + Viene ora reso più evidente l'ambiente in cui l'utente ha effettuato l'accesso (test, presubentro, produzione). Inoltre in ambiente di produzione vengono forniti dei messaggi non bloccanti sullo stato del presubentro per il comune. (l'unica situazione bloccante continua ad essere, come sempre, l'assenza del comune dal piano di subentro.

+ (Bug) Anomalia verifica idOperazioneComune già utilizzata
    + Il servizio 4005 non verificava correttamente che n idOperazioneComune fosse già stato usato

+ (Bug) WebApp - Errore controllo estrazione id operazione comune da web app
    + In alcuni casi il servizio 4001 restituiva impropriamente il diagnostico EN148 da web app.

+ (Bug) WEB - Upload file subentro - Verifica consolato di residenza
    + Verifica al momento dell'upload del file AIRE dell'esistenza del consolato di residenza.
    
+ (Bug) Miglioramento sistema di gestione dell'anomalia EN527 (issue: [https://github.com/italia/anpr/issues/1447](https://github.com/italia/anpr/issues/1447))
    + A volte il sistema diagnostico EN527 non permetteva di reperire tutte le informazioni utili a risolvere il problema
    
    
### Versione 5.4.10 (2019-07-09)

+ (Bug) EN212 - Certificabilità convivenza
    + A volte il diagnostico EN212 poteva essere riportato erroneamente per le convivenze.

+ (Bug) Correzione generazione anomalie subentro duplicate (issue: [https://github.com/italia/anpr/issues/1422](https://github.com/italia/anpr/issues/1422))
    + In alcuni casi, per soggetti cancellati e re iscritti, potevano essere generate erroneamente troppe anomalie in fase di subentro.


### Versione 5.4.9 (2019-07-03)

+ (Bug) Verifica della denominazione traslitterata in caso di Comune di nascita con la lettera accentata (issue: [https://github.com/italia/anpr/issues/1415](https://github.com/italia/anpr/issues/1415))
    + Se il comune di nascita conteneva un accento invece di un apostrofo, l'iscrizione poteva fallire.


### Versione 5.5.0 (2019-07-01)

+ (Requirement) Limitazione richieste 4005 ad un periodo massimo di un mese (issue: [https://github.com/italia/anpr/issues/1410](https://github.com/italia/anpr/issues/1410))
    + Verrà introdotto un controllo che bloccherà le richieste per le quali il periodo di riferimento della richiesta abbia durata maggiore di 30 giorni.

+ (Bug) Rimozione colonna ID su tabella 045 del 7001 (issue: [https://github.com/italia/anpr/issues/1418](https://github.com/italia/anpr/issues/1418))
    + La colonna ID era stata erroneamente aggiunta alla tabella 045 scaricata da servizio 7001.
    

### Versione 5.4.8 (2019-06-28)

+ (Bug) Errore estrazione notifica N031 con richiesta singola 3003 (issue: [https://github.com/italia/anpr/issues/1412](https://github.com/italia/anpr/issues/1412))
    + L'estrazione delle richieste N031 produceva nessun risultato in caso di richiesta singola operazione.

+ (Bug) Errore richiesta 3003/3007 notifica N031 in caso di statolavorazione non congruente
    + in alcuni casi una richiesta con statoLavorazione non congruente poteva andare in errore.

+ (Bug) ws 6001 - certificati on line - esenzione diritti segreteria
    + Aggiornato  il servizio 6001: richiamato utilizzando il flag on line, deve tener conto della eventuale presenza tra i dati del comune di impostazione di esenzione diritti di segreteria per certificati on line

+ (Bug) ANPRWEB - campo "Esenzione diritti per certificati online" e campo "diritti di segreteria" (issue: [https://github.com/italia/anpr/issues/1411](https://github.com/italia/anpr/issues/1411))
    + Corretto il problema  nella pagina di Amministrazione: al Conferma il flag del campo in oggetto non veniva registrato in archivio.

+ (Requirement) Richiesta conferma upload forniture subentro in ambiente di produzione (issue: [https://github.com/italia/anpr/issues/1368](https://github.com/italia/anpr/issues/1368))
    + In previsione della modifica delle modalità di accesso in ambiente di presubentro, verrà richiesta conferma all'utente nel momento in cui esegue l'upload delle forniture APR e AIRE.


### Versione 5.4.7 (2019-06-13)

+ (Bug) Estrazione 4005 generazione notifiche N031 (issue: [https://github.com/italia/anpr/issues/1386](https://github.com/italia/anpr/issues/1386))
    + Quando non veniva specificata la tipologia di notifica richiesta poteva comparire nell'elenco anche notifiche generate per gli enti.


### Versione 5.4.6 (2019-06-11)

+ (Bug) Codice anomalia EN389 - gestione errore base dati (issue: [https://github.com/italia/anpr/issues/1378](https://github.com/italia/anpr/issues/1378))
    + Il servizio mostrava impropriamente l'eccezione della base dati. Ora il servizio viene mandato in errore in caso di anomalia base dati non gestita.

+ (Requirement) Web - Indicazione del formato in pixel dei loghi nell'area amministrativa comuni
    + Il logo dei certificati deve essere Altezza:70 pixel, Larghezza:70 pixel, quello web Altezza:56 pixel, Larghezza:40 pixel, entrambi in formato PNG, GIF o JPG


### Versione 5.4.5 (2019-06-05)

+ (Requirement) Pubblicazione WSDL su github (issue: [https://github.com/italia/anpr/issues/1374](https://github.com/italia/anpr/issues/1374))
    + I wsdl verranno pubblicati su github, nel ramo [master](https://github.com/italia/anpr/tree/master/wsdl) per produzione e [develop](https://github.com/italia/anpr/tree/develop/wsdl) per test/presubentro.


+ (Requirement) Webapp - Abilitazione consultazione per comuni non subentrati
    + Ora anche i comuni non subentrati sono abilitati alla consultazione da web application se hanno richiesto e ricevuto le smartcard.

+ (Requirement) Download risultato elaborazione export intero Comune (issue: [https://github.com/italia/anpr/issues/1357](https://github.com/italia/anpr/issues/1357))
    + Ora è possibile scaricare l'export anche da webapp di ANPR, dall'area download, ma per i soli profili che hanno anche accesso all'area amministrazione del comune (vale a dire chi ha potuto effettuare la richiesta di scarico).


### Versione 5.4.4 (2019-05-29)

+ (Requirement) Ampliamento dettaglio esiti errore ricerca soggetti cancellati per altri motivi (issue: [https://github.com/italia/anpr/issues/1349](https://github.com/italia/anpr/issues/1349))
    + I controlli effettuati dal servizio di mutazione scheda soggetto sono stati resi più dettagliati, come ad esempio il controllo inerente il comune di competenza sul soggetto.


+ (Bug) 3002 - data annullamento carta identità (issue: [https://github.com/italia/anpr/issues/1307](https://github.com/italia/anpr/issues/1307))
    + Risolve il problema del servizio di interrogazione relativo dell'assenza dei dati della carta di identità se annullata 


+ (Bug) Reiscrizione per ripristino posizione precedente (issue: [https://github.com/italia/anpr/issues/1292](https://github.com/italia/anpr/issues/1292))
    + Risolto problema verificato in caso di soggetto subentrato come residente e cancellato per ripristino posizione precedente: in caso di reiscrizione AIRE non era consentito reiscriverlo ad una data antecedente all'ultima data di decorrenza registrata

+ (Bug) Congruenza data origine famiglia / data appartenenza componenti
    + La data origine della famiglia convivenza veniva aggiornata impropriamente a fronte di una mutazione residenza dell'intera famiglia tra comuni diversi. 
    
+ (Bug) Rimosso aggiornamento data origine famiglia convivenza per 5001 mutazione 3
    + Per alcuni giorno il tipo mutazione 3 ha permesso di aggiornare la data origine famiglia convivenza, questo portava a volte a segnalare l'anomalia EF031. Per il momento non è più possibile aggiornare la data origine famiglia convivenza. 



### Versione 5.4.3 (2019-05-20)

+ (Bug) 3002 - Valore 99 specieConvivenza (issue: [https://github.com/italia/anpr/issues/1262](https://github.com/italia/anpr/issues/1262)[https://github.com/italia/anpr/issues/1335](https://github.com/italia/anpr/issues/1335))
    + Adesso, qualora sia stato inviato un valore non valido di specieConvivenza, questo non viene restituito dal servizio di interrogazione.

+ (Requirement) Iscrizione AIRE, validazione cap estero (issue: [https://github.com/italia/anpr/issues/1333](https://github.com/italia/anpr/issues/1333))
    + Adesso il punto viene accettato come valore del CAP estero.


### Versione 5.4.2 (2019-05-15)

+ (Bug) WS4005 - Verifica stato non controllo il tipo di operazione
    + La funzione di verifica stato non segnalava se viene richiesta la verifica su una operazione diversa da un 4005.

+ (Requirement) Recupero richieste 4005 non elaborate correttamente (issue: [https://github.com/italia/anpr/issues/1320](https://github.com/italia/anpr/issues/1320))
    + Gestione automatica recupero e monitoraggio delle richieste 4005 la cui elaborazione sia fallita.

+ (Bug) Annullamento cancellazione - soggetto competenza del comune (issue: [https://github.com/italia/anpr/issues/1311](https://github.com/italia/anpr/issues/1311))
    + Non veniva permessa l'annullamento della cancellazione di un soggetti il cui coniuge sia residente in altro comune.

+ (Bug) Stampa Visura - Stampa certificato: errore nella gestione dei diacritici (issue: [https://github.com/italia/anpr/issues/1304](https://github.com/italia/anpr/issues/1304))
    + Nella visura anagrafica il carattere Č non viene stampato e nei certificati non è accettato come carattere valido per l'xsd. Effettuare l'intervento anche sulla carte di identità e cartellini e su tutte le stampe riepilogative alla fine delle variazioni anagrafiche

+ (Requirement) Web - Filtro comune di residenza in certificazione
    + Nella ricerca dei soggetti per cui emettere certificati è stato aggiunta la possibilità di selezionare il comune di residenza.

+ (Bug) Mancato controllo di congruenza tra stati del procedimento ed l'operazione di apertura/chiusura
    + Nel caso in cui un procedimento/istruttoria viene chiuso dalla funzionalità 'Gestione procedimenti', non viene effettuato alcun controllo di congruenza sul motivo di chiusura utilizzato.

+ (Bug) Mancata visualizzazione della data di annullamento carta di identità (issue: [https://github.com/italia/anpr/issues/1100](https://github.com/italia/anpr/issues/1100))
    + Adeguamento dell'applicazione WEB per la visualizzazione del dato acquisito e già restituito dal servizio di interrogazione 3002.


### Versione 5.3.12 (2019-05-13)

+ (Bug) Errore elaborazione 4005 in caso di notifiche e dettaglio TUTTO (issue: [https://github.com/italia/anpr/issues/1313](https://github.com/italia/anpr/issues/1313))
    + A volte l'elaborazione delle richieste 4005 falliva in caso di notifiche per cui viene richiesto il livello dettaglio TUTTO. (In tale caso adesso per le notifiche viene generata solo la sezione del contenutoRisposta)


### Versione 5.4.1 (2019-05-06)

+ (Bug) Port hotfix 5.3.11 su ramo 5.4

### Versione 5.4.0 (2019-04-23)

+ (Requirement) Web - Scarico massivo comune per motivata richiesta
    + Nella sezione di amministrazione il sindaco, con la propria smart card, può richiedere uno scarico complessivo dei dati del comune per CAMBIO CASA SOFTWARE DI RIFERIMENTO o PERDITA DELLA BASE DATI LOCALE. Le richieste elaborate con successo potranno essere scaricate con il servizio 7002 usando l'id della richiesta come identificativo. (per questioni di sicurezza, questa funzione non sarà disponibile in ambiente di presubentro).

### Versione 5.3.11 (2019-05-06)

+ (Bug) AE03 mutazione dati anagrafici per collegamento CF - errore civicoFonte
    + Risolto il bug presente nell'operazione di collegamento CF, nel caso in cui il civicoFonte è impostato a zero, 

+ (Requirement) Certificato di stato di famiglia: introduzione forza certificato su errore EN222
    + E' necessario rendere warning il controllo CN222 nei certificati di stato di famiglia lì dove il comune vuole comunque stampare i certificati di stato di famiglia a prescindere dai legami parentela ecc.


+ (Bug) Mancata gestione del motivo fine matrimonio non censito (issue: [https://github.com/italia/anpr/issues/891](https://github.com/italia/anpr/issues/891))
    + Implementazione del controllo EN525 per la verifica di validità del motivo di fine matrimonio.

### Versione 5.3.10 (2019-04-30)

+ (Bug) AE03 mutazione dati anagrafici per collegamento CF - errore nell'impostazione località
    + Risolto il bug che generava errore nella funzione di collegamento CF (AEE97)

+ (Bug) Malfunzionamento gestione comune nascita non valido alla data
    + Risolto il malfunzionamento presente nel servizio di mutazione anagrafica (comune nascita) nel caso in cui si volesse modificare il comune di nascita da uno valido ad un non valido alla data di nascita.

### Versione 5.3.9 (2019-04-24)

+ (Bug) Errore estrazione notifica singola 3003 (issue: [https://github.com/italia/anpr/issues/1295](https://github.com/italia/anpr/issues/1295))
    + Le richieste singole di notifiche con il servizio 3003 non restituivano correttamente l'xml.

+ (Bug) Verifica controllo EN212 e EN222 certificabilità famiglia
    + Il controllo è stato temporaneamente disabilitato in quanto si attivava impropriamente in alcuni casi.

+ (Requirement) Servizio 4005 : Aggiunti controlli obbligatorietà
    + Ora viene verificato che in caso di richieste di elaborazione, siano valorizzati sempre le sezioni ricercaElenchiRichieste, statoLavorazione e almeno uno dei range periodoRiferimentoRichieste o identificativiANPR.

### Versione 5.4.0 (2019-04-23)

+ (Requirement) Web - Scarico massivo comune per motivata richiesta
    + Nella sezione di amministrazione del comune è possibile richiedere uno scarico complessivo dei dati del comune per CAMBIO CASA SOFTWARE DI RIFERIMENTO o PERDITA DELLA BASE DATI LOCALE. Le richieste elaborate con successo potranno essere scaricate con il servizio 7002 usando l'id della richiesta come identificativo. (per questioni di sicurezza, questa funzione non sarà disponibile in ambiente di presubentro).
    
### Versione 5.3.8 (2019-04-18)

+ (Bug) Permesso di soggiorno non consultabile nella data di inserimento (issue: [https://github.com/italia/anpr/issues/1269](https://github.com/italia/anpr/issues/1269))
    + Il permesso di soggiorno inserito con data decorrenza uguale a quella di sistema, era consultabile solo dal giorno seguente.

+ (Requirement) EN212 / EN222 - Revisione controllo famiglia certificabile
    + Evoluzione dei controlli sulla certificabilità della famiglia in base ai rapporti tra l'intestatario e gli altri componenti.

### Versione 5.3.7 (2019-04-16)

+ (Requirement) Stima data disponibilità elaborazioni 4005 (issue: [https://github.com/italia/anpr/issues/1277](https://github.com/italia/anpr/issues/1277))
    + La stima della data disponibilità è stata abbassata a 1 ora.

+ (Bug) Anomalia ricerca 3003/3007 per soggetto (issue: [https://github.com/italia/anpr/issues/1282](https://github.com/italia/anpr/issues/1282))
    + In alcuni casi la ricerca 3003/3007 poteva non generare la risposta correttamente.

+ (Bug) Elaborazione richieste 4005 in caso di dettaglio non impostato (issue: [https://github.com/italia/anpr/issues/1277](https://github.com/italia/anpr/issues/1277))
    + Se il dettaglio non era impostato nella richiesta, l'elaborazione poteva andava in errore invece di usare il dettaglio di default (RISPOSTA). Inoltre veniva valorizzato impropriamente anche il campo contenutoRichiesta.

### Versione 5.3.6 (2019-04-14)

+ (Requirement) Servizi di estrazione 3003/3007 – fine supporto della ricerca per procedimento (issue: [https://github.com/italia/anpr/issues/1279](https://github.com/italia/anpr/issues/1279))
    + Con la versione ANPR02, viene deprecata la funzionalità di ricerca elenchi 3007 e ricerca 3003 per procedimento, essendo in vigore la ricerca dei procedimenti tramite servizio 3004 più esaustiva.

+ (Requirement) Verifica congruenza statoLaborazione servizio 4005 (issue: [https://github.com/italia/anpr/issues/1275](https://github.com/italia/anpr/issues/1275))
    + Qualora siano specificati sia l'operazioneRichiesta che lo statoLavorazione ne verrà verificata la congruenza (per le notifiche vanno usati solo gli stati 7,8,9 - per le operazioni gli stati 1,2,3,6)

+ (Requirement) Retrocompatibilità 3003/3007 per notifica specifica e statoLavorazione non congruente (issue: [https://github.com/italia/anpr/issues/1275](https://github.com/italia/anpr/issues/1275)[https://github.com/italia/anpr/issues/1273](https://github.com/italia/anpr/issues/1273)
[https://github.com/italia/anpr/issues/1227](https://github.com/italia/anpr/issues/1227))
    + Qualora venga richiesta una notifica specifica (es. operazioneRichiesta N014, N015) e uno statoLaborazione 1 o 2 questo verrà considerato 9 (tutte le notifiche) come erroneamente avveniva per un bug. Questo comportamento verrà mantenuto solo per il periodo di supporto alla versione ANPR01.
    
+ (Bug) Certificato di stato civile coniugato in assenza di coniuge
    + Il certificato di stato civile per soggetto coniugato ma senza dati del matrimonio / coniuge in alcuni casi andava in errore invece di segnalare l'anomalia

### Versione 5.3.5 (2019-04-10)

+ (Requirement) Web - Ricerca per comune di residenza (issue: [https://github.com/italia/anpr/issues/1031](https://github.com/italia/anpr/issues/1031))
    + Implementazione del filtro per comune di residenza anche sull'applicazione web.

+ (Requirement) 3003/3007  - Aggiunta ricerca operazioni soggetto per id soggetto (issue: [https://github.com/italia/anpr/issues/1234](https://github.com/italia/anpr/issues/1234))
    + I servizio di ricerca identificativi (3007) e gestione richieste (3003) accettano anche l'idSchedaSoggettoANPR come parametro di ricerca nella ricerca per soggetto.

+ (Bug) Stato civile con codice 99 (issue: [https://github.com/italia/anpr/issues/1261](https://github.com/italia/anpr/issues/1261))
    + Il servizio di consultazione non restituisce più il codice stato civile 99
    
+ (Bug) WEB - malfunzionamento visualizzazione comune nascita coniuge non valido alla data nascita
    + Gestione dei comuni non validi alla data di nascita.

+ (Bug) Web - Validazione denominazioneConvivenza deve accettare numeri ordinali
    + La validazione della denominazione convivenza non accettava il carattere °

+ (Bug) Se il tipoRichiedente è 1 e gli estremi del documento del superano i 20 caratteri c'era un errore nella verifica del documento
    + Richiesta certificato con estremi del documento richiedente lunghi

+ (Bug) Hotfix Gestione Certificabilità famiglia
    + A volte i servizi 3002 e 6001 restituivano impropriamente le anomalie rispettivamente EN212, EN222.

### Versione 5.3.4 (2019-04-08)

+ (Bug) Anomalia download elaborazioni 4005 con servizio 7002 (issue: [https://github.com/italia/anpr/issues/1260](https://github.com/italia/anpr/issues/1260))
    + Ora il 7002 blocca con anomalia i tentativi di scaricare le elaborazioni 4005.

+ (Bug) Performance richieste notifiche 3003/3007/4005 (issue: [https://github.com/italia/anpr/issues/1236](https://github.com/italia/anpr/issues/1236))
    + E' stata fatta una correzione alla gestione delle interrogazioni 3003/3007/4005 che impattava negativamente sulle richieste di notifiche (venivano elaborati anche statiLavorazione diversi da 7/8/9)

### Versione 5.3.3 (2019-03-26)

+ (Bug) 3003 - Richiesta elenco notifiche non fruite (issue: [https://github.com/italia/anpr/issues/1227](https://github.com/italia/anpr/issues/1227))
    + Correzione gestione stato delle richieste elenco notifiche del servizio di gestione richieste.

### Versione 5.3.2 (2019-03-26)

+ (Bug) Correzione controllo EHR16 data finale periodo di riferimento (issue: [https://github.com/italia/anpr/issues/1219](https://github.com/italia/anpr/issues/1219))
    + Il controllo EHR16 per il servizio 4005 era molto restrittivo sull'orario di sistema e non formattava correttamente le date controllate.

+ (Bug) Web - Gestione preferenza certificati stampa frazione in produzione
    + La preferenza dei certificati stampa della frazione non era attiva in produzione.

+ (Bug) Errore estrazione 3003 in caso di assenza comune richiesta (issue: [https://github.com/italia/anpr/issues/1223](https://github.com/italia/anpr/issues/1223))
    + In alcuni casi in assenza del comune richiesta non veniva usato il comune mittente come predefinito.

+ (Requirement) Certificati - gestione interno1 ed espInterno1 a '0' per il comune di GENOVA
    + I campi interno1 ed espInterno1 vengono mostrati per  gli indirizzi relativi al comune di Genova anche quando il valore è '0'.

### Versione 5.3.1 (2019-03-20)

+ (Requirement) Aggiornamento tool validazione subentro (test comuni - Strumenti supporto)
    + Il comportamento del controllo EN009 su ambienti windows a volte è diverso dagli ambienti linux.  Viene ora offerta la possibilità di escludere tale controllo dalla validazione.

+ (Bug) Web - Decodifica colore in consultazione
    + Nella consultazione da applicazione web il colore del civico non veniva decodificato.

+ (Bug) Mancata presenza scioglimento in consultazione unione civile (issue: [https://github.com/italia/anpr/issues/1218](https://github.com/italia/anpr/issues/1218))
    + In caso di decesso, i dati dello scioglimento potevano essere mancanti quando incompleti.

+ (Bug) Anomalia ricerca elenco operazione per soggetto (issue: [https://github.com/italia/anpr/issues/1204](https://github.com/italia/anpr/issues/1204))
    + L'anomalia portava il servizio 3003 a non restituire risultati per la ricerca soggetto in alcuni casi. Nel web invece a volte non era possibile accedere al dettaglio xml delle operazioni nella consultazione soggetto.

### Versione 5.3.0 (2019-03-18)

+ (Requirement) Refactor servizio di consultazione/estrazione
    + I servizi 3003 e 3007 vengono spostati nella famiglia 4000. Il servizio 3005 nella famiglia 7000.

### Versione 5.2.7 (2019-03-18)

+ (Bug) Errore servizio mutazione in caso di duplicati
    + In alcuni casi il servizio poteva impedire la modifica di un soggetto in caso di due schede duplicate anche se tutte cancellate tranne una.

### Versione 5.2.6 (2019-03-11)

+ (Bug) Web - Controllo soggetto deceduto per certificato di morte
    + In caso di emissione certificato di morte, se la ricerca non era effettuata in modo puntuale l'emissione potrebbe essere bloccata.

+ (Requirement) Abilitazione feature Rettifica indirizzo per errore materiale o per integrazione
    + La rettifica indirizzo per errore materiale o per integrazione è stata abilitata anche in produzione.

### Versione 5.2.5 (2019-03-06)

+ (Bug) Web - Anomalia Intestatario convivenza con comune nascita non esistente alla data

+ (Bug) EC099 - Verifica denominazione sede consolato
    + Anche una differenza solo nella maiuscole / minuscole della sede del consolato (rispetto alla tabella di riferimento) portava alla segnalazione EC099 (consolato inesistente alla data).
    
+ (Bug) Controllo EC168 in assenza data formazione atto nascita (issue: [https://github.com/italia/anpr/issues/1187](https://github.com/italia/anpr/issues/1187))
    + In assenza della data formazione atto dell'atto di nascita, il controllo EC168 si poteva attivare anche su codistat validi se variati nel corso dell'anno dell'atto.

### Versione 5.2.4 (2019-03-01)

+ (Bug) Errore ultimo indirizzo di residenza riportato  su stampa certificato
    + In alcuni casi nei quali c'erano state più cancellazioni e reiscrizioni l'ultimo indirizzo riportato sul certificati non era corretto.

### Versione 5.2.3 (2019-02-27)

+ (Bug) Errore risposta 5014
    + E' stato corretto un errore di composizione della risposta 5014

### Versione 5.2.2 (2019-02-24)

+ (Bug) Port hotfix 5.1.7 su ramo 5.2

+ (Bug) Lista soggetti variati servizio 1014 (issue: [https://github.com/italia/anpr/issues/1165](https://github.com/italia/anpr/issues/1165))

+ (Requirement) Consultazione per comune di residenza e identificativo o codice fiscale (issue: [https://github.com/italia/anpr/issues/1159](https://github.com/italia/anpr/issues/1159)[https://github.com/italia/anpr/issues/1162](https://github.com/italia/anpr/issues/1162))
    + In caso di consultazione per comune di residenza (ricercaNazionale=0) era stato deciso inizialmente di restituire comunque il soggetto qualora i criteri di ricerca fossero per id soggetto anpr o codice fiscale. Adesso invece il filtro per comune di residenza verrà applicato sempre.


### Versione 5.1.7 (2019-02-24)

+ (Bug) Web - Ricerca procedimento amministrativo per protocollo comunale
    + La ricerca dei procedimenti da web accettava solo numeri per il protocollo comunale del provvedimento. Ora sono accettati lettere, numeri, spazi e '-'

### Versione 5.2.1 (2019-02-19)

+ (Bug) Port hotfix 5.1.6 su ramo 5.2

+ (Bug) Errore gestione risposta (ANPR02) per 1014 (issue: [https://github.com/italia/anpr/issues/1151](https://github.com/italia/anpr/issues/1151))
    + Per il servizio 1014 i dati controllo non sono obbligatori. 

+ (Requirement) Rettifica indirizzo per errore materiale o per integrazione
    + Utilizzo del codice mutazione 9  del servizio di mutazione famiglia/residenza  per comunicare la rettifica su un indirizzo per errore materiale.  Confermati dal Ministero i requisiti riportati  di seguito (cfr. e-mail della Dott.ssa Toscano 19.12.2018). Comunicata agli enti l’introduzione del nuovo codice mutazione per il ws 5001 (e-mail del 26.10.2018 ad AE, MCTC, INPS, ISTAT).   Attività previste:   -          ws 5001 : eliminazione del controllo sull’utilizzo del codice mutazione 9  per gli indirizzi in lingua italiana; inserimento  di un controllo sulla data decorrenza residenza: deve essere uguale a quella corrente, non può essere modificata  La  La nuova selezione va aggiunta anche sulla Web App.  n    N.b. --> cambiamo la descrizione del codice mutazione  9 sulla tabella  di decodifica                   "RETTIFICA/INTEGRAZIONE INDIRIZZO"  (già effettuato in SVILUPPO)

### Versione 5.1.6 (2019-02-19)

+ (Bug) Certificati - Richiesta dati storico di residenza soggetto AIRE diventato APR (issue: [https://github.com/italia/anpr/issues/1155](https://github.com/italia/anpr/issues/1155))
    + La richiesta dati storico residenza per i soggetti APR che sono stati AIRE nel passato poteva fallire.

+ (Bug) WEB: data nascita del coniuge può essere non congruente
    + Se la data di nascita del coniuge era stata inviata con una time zone non corretta poteva essere visualizzata una data diversa.

### Versione 5.1.5 (2019-02-13)

+ (Bug) Web - Validazione numero sentenza
    + L'applicazione web non accettava il carattere '-' nel numero sentenza.

+ (Bug) Malfunzionamento mutazione padre/madre in caso di rettifica cognome (case insensitive) (issue: [https://github.com/italia/anpr/issues/1102](https://github.com/italia/anpr/issues/1102))
    + In caso di mutazione padre/madre per rettifica cognome, non viene correttamente gestita la rettifica da maiuscolo a minuscolo e viceversa.

+ (Requirement) Gestione consolati cessati
    + L'intervento prevede il caricamento dei consolati cessati nelle tabelle di servizio e la loro gestione nei WS interessati e nelle corrispondenti funzioni della web app.

### Versione 5.2.0 (2019-02-13)

+ (Bug) Port hotfix 5.1.5 su ramo 5.2

+ (Requirement) Diagnostico in caso di scheda anagrafica individuale sintetica (issue: [https://github.com/italia/anpr/issues/1079](https://github.com/italia/anpr/issues/1079))
    + Nella consultazione individuale, qualora venga restituita la scheda sintetica, sarà presente anche il diagnostico EN528.

+ (Requirement) Diagnostico EN527 con informazioni sull'operazione effettuata
    + Alcuni servizi (in particolare i servizi di registrazione) restituiscono adesso un diagnostico per fornire informazioni utili sulle operazioni fallite.


+ (Requirement) Presentazione dettaglio soggetto nella consultazione della webapp (issue: [https://github.com/italia/anpr/issues/1031](https://github.com/italia/anpr/issues/1031)[https://github.com/italia/anpr/issues/1064](https://github.com/italia/anpr/issues/1064)[https://github.com/italia/anpr/issues/1079](https://github.com/italia/anpr/issues/1079))
    + A fronte del nuovo prospetto sintetico della consultazione, sarà possibile accedere anche al dettaglio completo.

+ (Requirement) Revisione risposte servizi di registrazione (solo ANPR02) (issue: [https://github.com/italia/anpr/issues/1079](https://github.com/italia/anpr/issues/1079))
    + Anche la risposta dei servizi di registrazione diventa sintetica. Vale a dire che invece di tutti i dati dei soggetti variati, vengono fornite solo la sintesi del risultato e gli eventuali dati generati da ANPR (idanpr, codice fiscale ecc).


### Versione 5.1.4 (2019-02-11)

+ (Bug) Errore associazione comune di emissione CIE
    + Alcune CIE non veniva visualizzate in consultazione per anomalia di associazione del comune di emissione.

### Versione 5.1.3 (2019-02-08)

+ (Bug) Gestione annullamenti parziali multipli su diversi soggetti ma stessa operazione (999) (issue: [https://github.com/italia/anpr/issues/1133](https://github.com/italia/anpr/issues/1133))
    + Non era possibile eseguire più annullamento parziali sulla stessa operazione anche quando riguardavano soggetti diversi.


+ (Bug) Gestione esito annullamenti in caso di operazione già annullata (999) (issue: [https://github.com/italia/anpr/issues/1133](https://github.com/italia/anpr/issues/1133))
    +  Ora viene restituito un diagnostico quando l'operazione è già stata annullata.


+ (Bug) Gestione esito annullamenti in caso di comune non competente (999) (issue: [https://github.com/italia/anpr/issues/1133](https://github.com/italia/anpr/issues/1133))
    +  Ora viene restituito un diagnostico quando il comune non è competente per l'annullamento.

### Versione 5.1.2 (2019-02-06)

+ (Requirement) Aggiungere scala esterna ai certificati di residenza (issue: [https://github.com/italia/anpr/issues/1115](https://github.com/italia/anpr/issues/1115))
    + Aggiungere se presente ai certificati di residenza (normale e storico) la scala esterna (scala est. + valore)

### Versione 5.0.2 (2019-02-06)

+ (Bug) WEB - Correzione validazione note indirizzo
    + Non veniva accettato il carattere due punti dall'applicazione web per il campo note indirizzo

### Versione 5.1.1 (2019-04-01)

+ (Bug) Malfunzionamento annullamento di un cambio residenza (5012) (issue: [https://github.com/italia/anpr/issues/1092](https://github.com/italia/anpr/issues/1092))
    + Sebbene la risposta del servizio sia positiva, di fatto non viene annullata l'operazione.

+ (Bug) [2003] malfunzionamento controllo di conformità evento (EN344) (issue: [https://github.com/italia/anpr/issues/1097](https://github.com/italia/anpr/issues/1097))
    + Rimozione controllo EN344 in caso di cancellazione per ripristino posizione anagrafica.

### Versione 5.1.0 (2019-01-17)

+ (Requirement) Superamento vincoli annullamento (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + E' stato reso possibile effettuare annullamenti per ripristino posizione anagrafica anche se la mutazione di residenza non è l’ultima operazione effettuata sul soggetto (ma non vi siano altre mutazioni di residenza) Sono stati eliminati i vincoli sugli annullamenti impediti da operazioni su soggetti collegati (es. coniugi o legami parentela)

+ (Requirement) Sezione famiglia risposta 3002 (solo ANPR02) (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Solo nella interrogazione per famiglia/convivenza con codDestintario ANPR02 viene restituito un blocco esplicito opzionale della famiglia.

+ (Requirement) Avvisi nella risposta del 3002 (solo ANPR02) (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Solo in caso di chamata con codDestintario ANPR02 viene aggiunta una sezione di anomalie anche in caso di risposta OK del servizio 3002.

+ (Requirement) Scarico massivo dei dati di un comune (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Consente di scaricare i dati di un comune da ANPR al solo scopo di utilizzarli nel caso di cambio gestionale comunale. Tale soluzione provvisoria prevede la generazione di una fornitura di tutti i soggetti di un Comune sotto forma di file compresso, che verrà consegnato al Comune tramite PEC.  

+ (Requirement) Web - Amministrazione gestione ip (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Nel menù Amministrazione - gestione dati comune aggiunta la possibilità di inserire, dismettere, riabilitare uno o più indirizzi IP da far abilitare per l'utilizzo dei servizi ANPR

+ (Requirement) Estensione del servizio revoca dato (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Estensione del servizio revoca dato per i seguenti dati: - Matrimonio / Convivenza / Unione civile - Permesso di soggiorno - Carta di identità - Atto di nascita

+ (Requirement) Inibizione invio validazione file AIRE con precedenti regole (issue: [https://github.com/italia/anpr/issues/1060](https://github.com/italia/anpr/issues/1060))
    + Viene da adesso accettata solo la nuova validazione del tracciato AIRE per evitare di acquisire dati non congruenti con le regole di validazione XSD.


### Versione 5.0.1 (2019-01-16)

+ (Requirement) Aggiunta sezione datiCancellazione alla risposta sintetica del servizio 3002 (issue: [https://github.com/italia/anpr/issues/1031](https://github.com/italia/anpr/issues/1031)[https://github.com/italia/anpr/issues/1064](https://github.com/italia/anpr/issues/1064))
    + Quando il servizio 3002 restituisce la nuova risposta sintetica (versione 5.0, codDestintario ANPR02) è stata aggiunta la sezione dei datiCancellazione alle sezioni già restituite (generalita, legame, residenza, famiglia).

+ (Requirement) Gestione risposta completa 3002 in caso di ricerca per famiglia o codice fiscale (issue: [https://github.com/italia/anpr/issues/1031](https://github.com/italia/anpr/issues/1031)[https://github.com/italia/anpr/issues/1064](https://github.com/italia/anpr/issues/1064))
    + Nel caso in cui tra i parametri di ricerca sia indicata una ricerca codice fiscale o per famiglia (ma non per convivenza) non viene restituita la nuova risposta sintetica ma quella completa della versione 4.X


### Versione 5.0.0 (2019-01-10)
 
+ (Requirement) Abilitazione codDestintario ANPR02 (issue: [https://github.com/italia/anpr/issues/1031](https://github.com/italia/anpr/issues/1031)) [La versione 5.0.0 sostituisce le 4.2.0 / 4.2.1]
    + Le funzionalità specifiche della major version 5.0 vengono attivate indicando il codDestintario ANPR02, che comporterà :  
Dettaglio risposte del 3002 ridotte se la ricerca produce più di un soggetto nel risultato
Se non indicata espressamente la ricerca nazionale, la ricerca è limitata ai soggetti residenti nel comune che sta eseguendo l'interrogazione.
 
+ (Requirement) 3003 - Gestione richieste - rimozione N031 dal risultato in caso di interrogazione per data (issue: [https://github.com/italia/anpr/issues/1037](https://github.com/italia/anpr/issues/1037))
    + La notifica N031 è stata rimossa dal risultato della gestione richieste nel caso di interrogazione per data.
 
+ (Bug) Port hotfix 4.1.23 / 4.1.24 / 4.1.25 su ramo 5.0
 
+ (Requirement) ws 6001:  nuovi certificati per bilinguismo (lingua tedesca)
    + Aggiunta di due nuovi certificati per il bilinguismo - lingua tedesca:  a) stato libero (codice identificativo tipo certificato 17); b) stato civile (codice identificativo tipo certificato 11)
 
+ (Requirement) Ottimizzazione risposta servizio consultazione 3002
    + In conseguenza della decisione di permettere l'accesso al servizio 3002 anche per i comuni non subentrati e nell'ambito dell'ottimizzazione delle prestazioni rese necessarie dall'aumento del carico si è reso necessario modificare il comportamento del servizio di consultazione soggetto / famiglia / convivenza.
Con riferimento alle sezioni della risposta de servizio 3002, vedi [tabella decodifica 16](https://www.anpr.interno.it/portale/tabelle-di-riferimento), qualora la ricerca trovi più di un soggetto, verrà restituita solo la sezione generalità (senza tenere conto delle eventuali altre sezioni indicate, compresa la scheda individuale completa). Le ricerche che si traducono in un solo soggetto continuano a comportarsi come prima.



### Versione 4.1.25 (2019-01-08)

+ (Bug) Web - Validazione note permesso soggiorno
    + Deve accettare anche il doppio apice


### Versione 4.1.24 (2019-01-04)

+ (Bug) Accettazione numeri in nome e cognomi (issue: [https://github.com/italia/anpr/issues/1036](https://github.com/italia/anpr/issues/1036))
    + Il tipo dato alfabeticoNomiCognomi accettava erroneamente anche i numeri.

+ (Bug) Errore gestione mutazione famiglia convivenza - cambio residenza con patente e autoveicoli (issue: [https://github.com/italia/anpr/issues/1033](https://github.com/italia/anpr/issues/1033))
    + E' stato corretto un bug nella gestione del cambio residenza famiglia con patente e autoveicoli.

+ (Bug) Web - Etichette criteri ricerca consultazione soggetto / famiglia
    + Nella consultazione da webapp veniva usata la stessa etichetta per la i criteri ricerca dell' identificato soggetto attribuito da ANPR e identificativo famiglia attribuito da ANPR.

+ (Bug) Web - Validazione campo autorità sentenza
    + Il campo autorità della sentenza deve accettare anche lo slash


### Versione 4.1.23 (2018-12-27)

+ (Bug) Correzione controllo EHR78
    + Il controllo EHR78 non si attivava per le richieste 3003/3007 in caso di date uguali (la data iniziale deve essere sempre strettamente minore della finale).

+ (Bug) Errore nella gestione della risposta 5001 in caso di dati sporchi
    + In alcuni casi il servizio 5001 poteva andare in errore se in subentro non era stata inviata correttamente la residenza.
    

### Versione 4.1.22 (2018-12-19)

+ (Bug) A006 - verifica presenza cittadinanza italiana (issue: [https://github.com/italia/anpr/issues/982](https://github.com/italia/anpr/issues/982))
    + In caso di mutazione AIRE (tipo = 1 da residente ad AIRE), se la cittadinanza italiana non è presente nella richiesta si effettua una verifica che sia già presente nel DB e in caso contrario viene inserita di default come già fanno A001 e A002.

+ (Bug) Errore archiviazione convivenza
    + Malfunzionamento del servizio di archiviazione famiglia convivenza quando la lunghezza delle noteArchiviazione supera i 30 caratteri.


+ (Bug) Ripristino indirizzo post subentro: errore impostazione data decorrenza residenza per 5001 codice 6 
    + WS 5001: la mutazione di residenza per ripristino della posizione post-subentro non impostava la nuova data di decorrenza della residenza per il/i soggetti interessati.

### Versione 4.1.21 (2018-12-13)

+ (Bug) Errore salvataggio mutazione residenza (issue: [https://github.com/italia/anpr/issues/1001](https://github.com/italia/anpr/issues/1001))
    + Il cambio di residenza poteva andare in errore in caso di numeri soggetti e contestuale trasmissione dei dati su patente e autoveicoli.

### Versione 4.1.20 (2018-12-10)

+ (Bug) Web - Errore encoding in validazione in file subentro AIRE  (issue: [https://github.com/italia/anpr/issues/995](https://github.com/italia/anpr/issues/995))
    + Nella validazione eseguita in fase di upload è stato necessario correggere l'encoding del file AIRE per evitare di segnalare come errori anche dei record validi.

+ (Bug) Controllo EC083 in assenza data formazione atto matrimonio (issue: [https://github.com/italia/anpr/issues/981](https://github.com/italia/anpr/issues/981))
    + In assenza della data formazione atto del matrimonio, il controllo EC083 si poteva attivare anche su codistat validi se variati nel corso dell'anno dell'atto.

### Versione 4.1.19 (2018-12-07)

+ (Bug) Abilitazione elenchi ausilio ambiente di produzione (issue: [https://github.com/italia/anpr/issues/985](https://github.com/italia/anpr/issues/985))
    + La funzione consultazione e estrazione - Elenchi di ausilio non era stata attivata in ambiente di produzione.

### Versione 4.1.18 (2018-12-05)

+ (Bug) Errore cancellazione altri motivi
    + Per il servizio 2003 non era stato trattato un correttamente un esito.

+ (Requirement) Estensione idSchedaSoggettoANPR da 15 a 16 cifre
    + Il dominio utile per l'id scheda soggetto ANPR è stato esteso da 15 a 16 cifre.

+ (Requirement) Ordinamento richiesta cancellazione subentro
    + Negli ambienti di presubentro / test comuni è possibile richiedere la cancellazione dei dati della simulazione di subentro. L'elenco delle richieste precedentemente inserite viene ora ordinato per data inserimento.

+ (Bug) Upload tracciato AIRE con le nuove regole di validazione ANPR01
    + L'upload del tracciato AIRE è stato adeguato alle nuove regole di validazione già presenti negli XSD. Inoltre nella denominazione toponimo estero verranno accettati anche i due punti e nel presso le parentesi.
 Fino al 31 Dicembre 2018 sarà consentito l'upload del tracciato AIRE anche senza questo adeguamento.


### Versione 4.1.17 (2018-11-30)

+ (Bug) Certificato stato civile per soggetto unito civilmente
    + In alcuni casi il certificato di stato civile per soggetti uniti civilmente non veniva emesso

+ (Bug) Consultazione convivenza senza residenza
    + La consultazione di convivenze inserite da subentro senza residenza generava un errore

+ (Bug) Mutazione convivenza senza residenza
    + All'atto di un 5001 per una residenza senza convivenza poteva generarsi un errore 999

+ (Requirement) Correzione denominazione comune di VENARIA REALE
    + Su segnalazione del comune di Venaria Reale, è stato verificato che il comune, sin dalla sua istituzione, ha avuto questa denominazione. L’archivio storico dei comuni utilizzato da ANPR riportava la situazione seguente:  DATAISTITUZIONE|DATACESSAZIONE|CODISTAT|CODCATASTALE|DENOMINAZIONE_IT<br/> 17/03/1861     |19/11/1987    |001292  |L727        |VENARIA<br/> 20/11/1987     |31/12/9999    |001292  |L727        |VENARIA REALE<br/> Si procederà, pertanto, a modifica la denominazione Venaria con quella ufficiale, desumibile dagli atti forniti dal comune interessato. Tale variazione, già disponibile in ambiente di test-comuni e pre-subentro, sarà apportata anche in ambiente di produzione a partire dal prossimo 12 dicembre. 


### Versione 4.1.16 (2018-11-27)

+ (Bug) Certificato contestuale di residenza e residenza in convivenza - Stringa errata
    + Su alcuni certificati aire può comparire la dicitura errata.

+ (Bug) Verifica congruenza dati comune di nascita (issue: [https://github.com/italia/anpr/issues/949](https://github.com/italia/anpr/issues/949))
    + In alcuni casi il controllo sulla congruenza del luogo di nascita era errato producendo un esito EN185 in fase di re iscrizione del soggetto.

### Versione 4.1.15 (2018-11-22)

+ (Bug) Web - Errore chiusura procedimento
    + L'identificativo del procedimento a volte veniva convertito in modo anomalo.

+ (Bug) Web - Validazione nome / cognome allineata ai servizi
    + Consentita la presenza di spazi precedenti o successivi al carattere trattino ('-') .

+ (Bug) Estensione a 20 della lunghezza del tipoIsolato
    + Il campo tipoIsolato è stato adeguato a 20 caratteri nelle specifiche XSD come già previsto nella [documentazione](https://www.anpr.interno.it/portale/documentazione-tecnica) 

+ (Bug) 5008 tipo muatazione 4 - Permesso di soggiorno
    + Nel servizio di mutazione tutti i dati, per il tipo mutazione 4 Permesso di soggiorno, viene attivato il controllo bloccante CN368 se inserito per un cittadino italiano.

+ (Requirement) Subentro: controllo dell'indirizzo principale
    + In assenza, nell'indirizzo principale, della descrizione della specie o in alternativa del codiceSpecie, viene restituita un'anomalia non bloccante CN524. 

### Versione 4.1.14 (2018-11-15)

+ (Bug) 1010 Istituzione convivenza - Errori ES008 (issue: [https://github.com/italia/anpr/issues/932](https://github.com/italia/anpr/issues/932))
    + Nell'istituzione della Convivenza,  viene rimosso il controllo ES008 che verifica l'uguaglianza tra la data decorrenza dell'operazione  e la data di nascita del responsabile della convivenza

+ (Bug) 6001 richiesta dati, noteIndirizzo vuote (issue: [https://github.com/italia/anpr/issues/924](https://github.com/italia/anpr/issues/924))
    + Quando il campo noteIndirizzo non contiene valori significativi non viene più restituito dal servizio 6001 come già avviene per il servizio 3002.

+ (Bug) Correzione encoding wsdl da distribuire per i comuni (issue: [https://github.com/italia/anpr/issues/807](https://github.com/italia/anpr/issues/807))
    + L'encoding dell tipoDato.xsd non era sempre corretto per gli ultimi diacritici aggiunti.

+ (Bug) Web - Blocco mutazione tutti i dati per validazione data scadenza permesso di soggiorno
    + Alcune date formalmente valide non impedivano (come il 31/12/8999) bloccavano la possibilità di eseguire una mutazione tutti i dati da web.


+ (Requirement) Estensione caratteri amessi per alcuni tipi XSD (slash e cancelletto) (issue: [https://github.com/italia/anpr/issues/902](https://github.com/italia/anpr/issues/902)[https://github.com/italia/anpr/issues/907](https://github.com/italia/anpr/issues/907))
    + Verranno accettati il carattere "/" per l'elemento descrizioneLocalita del tipo Località e il carattere "#" per gli elementi denominazione e numeroCivico del tipoToponimoEstero.

+ (Bug) Ricerca di convivenza senza responsabile nè soggetti restituisce EN122
    + Solo l'applicazione web adesso restituisce un soggetto fittizio con cognome e nome "RESPONSABILE CONVIVENZA ASSENTE" al fine di poter restituire gli altri dati sulla convivenza.


### Versione 4.1.13 (2018-11-08)

+ (Bug) Certificati bug testo normativo sigillo digitale (issue: [https://github.com/italia/anpr/issues/915](https://github.com/italia/anpr/issues/915))
    + Nei certificati in ambiente di produzione per emissione=2 appare il testo normativo previsto per il sigillo digitale che non è ancora previsto.

+ (Requirement) Possibilità di upload file subentro solo con nuove regole in tutti gli ambienti (issue: [https://github.com/italia/anpr/issues/819](https://github.com/italia/anpr/issues/819))
    + In nessun ambiente (in particolare anche produzione) sarà possibile l'upload delle forniture del subentro con le regole precedenti.

+ (Bug) Carattere euro nell'annotazione certificato (issue: [https://github.com/italia/anpr/issues/807](https://github.com/italia/anpr/issues/807))
    + Nelle righe di annotazione dei certificati viene ora accettato anche il carattere euro.

+ (Bug) Web - Ricerca per codice fiscale con omocodia specie 4+
    + Ora la validazione dell'applicazione web per il codice fiscale è allineata a quella dei servizi [lunghezza minima (11), massima (16) e valori che siano lettere minuscole, maiuscole, numeri]


+ (Bug) Controllo presenza dati unione per certificato stato civile
    + In alcuni casi veniva emesso il certificato di unione civile anche in mancanza dei dati.


+ (Requirement) Nuova gestione annullamento carta identità
    + Sul sito web è stata inserita la possibilità di revocare o annullare una carta di identità emessa dal sito web di ANPR o acquisita tramite i servizi di registrazione

### Versione 4.1.12 (2018-11-05)

+ (Bug) stampa "colore" sui certificati (issue: [https://github.com/italia/anpr/issues/892](https://github.com/italia/anpr/issues/892))
    + Errata decodifica del COLORE nei certificati di residenza.


### Versione 4.1.11 (2018-10-26)

+ (Bug) 3002 - consultazione carta identità
    + Aggiunto elemento dataAnnullamento al tipoCartaIdentita.

+ (Bug) 3002 - Filtro ricerca per soggetto AIRE e per  tipo scheda (famiglia/convivenza) (issue: [https://github.com/italia/anpr/issues/871](https://github.com/italia/anpr/issues/871))
    + La consultazione ignorava i criteri di ricerca: soggetto AIRE e tipo scheda (famiglia/convivenza)


### Versione 4.1.10 (2018-10-25)

+ (Bug) Certificato AIRE - Stringa errata
    + Su alcuni certificati aire può comparire la dicitura errata 'sez_cum_stato_famiglia_header_senza_ind_m'

+ (Requirement) Estensione delle restrizioni XSD per versione ANPR01 (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617)[https://github.com/italia/anpr/issues/819](https://github.com/italia/anpr/issues/819))
    + In vista del fatto che dopo il 5 novembre sarà saranno rese obsolete le versioni degli XSD inferiori alla 4.0.0 (codDestintario = ANPR00), viene pubblicata un'ultima revisione degli XSD per minimizzare l'impatto sui valori già acquisiti.

### Versione 4.1.9 (2018-10-24)

+ (Bug) Certificato di stato civile per unito civilmente
    + Nel caso in cui un soggetto presenta stato civile unito civilmente (codice 6), non viene emesso il certificato di stato civile sebbene siano presenti tutti i dati relativi all'unione civile stipulata dal soggetto; l'errore sollevato è EN404

### Versione 4.1.8 (2018-10-22)

+ (Bug) Gestione controllo accessi - Errore gestione operazione 2009 (issue: [https://github.com/italia/anpr/issues/876](https://github.com/italia/anpr/issues/876))
    + Non implementata correttamente la gestione accessi del servizio di archiviazione convivenza.

+ (Bug) Errore rettifica 101 per soggetto riconciliato tra due subentri
    + La rettifica in oggetto viene bloccata anche quando andrebbe permessa nel caso venga eseguita su un soggetto riconciliato tra due subentri di comuni diversi.

+ (Bug) Gestione controllo accessi - Errore nella ricerca per più generalità soggetto (issue: [https://github.com/italia/anpr/issues/876](https://github.com/italia/anpr/issues/876))
    + Non era implementata correttamente la gestione accessi quando presenti più soggetti.

+ (Bug) Gestione controllo accessi - Errore nella ricerca della famiglia per identificativo comunale (issue: [https://github.com/italia/anpr/issues/876](https://github.com/italia/anpr/issues/876)[https://github.com/italia/anpr/issues/877](https://github.com/italia/anpr/issues/877))
    + A volte viene restituito l'errore di mancata autorizzazione (EN493) quando una famiglia viene ricercata per id comunale e non per id ANPR.

+ (Requirement) Filtro per comune di residenza servizio interrogazione 3002 (issue: [https://github.com/italia/anpr/issues/565](https://github.com/italia/anpr/issues/565)[https://github.com/italia/anpr/issues/576](https://github.com/italia/anpr/issues/576))
    + Permette di filtrare per comune di residenza il servizio 3002


### Versione 4.1.7 (2018-10-19)

+ (Requirement) Web - Strumenti di supporto test comuni - esempio validatore XSD (issue: [https://github.com/italia/anpr/issues/819](https://github.com/italia/anpr/issues/819))
    + Aggiunto download di un tool di validazione dei file xsd dall'area strumenti di supporto in test comuni.

### Versione 4.1.6 (2018-10-18)

+ (Bug) Controllo certificati cumulativi AIRE
    + Permetteva alcune combinazioni di certificate non ammessi per i soggetti AIRE.

+ (Bug) Web - Errore cancellazione altri motivi su intestatario famiglia
    + La richiesta per il servizio non veniva preparata correttamente e portava ad un errore EN489

+ (Bug) Intestazione comune esiti subentro
    + Nel report esiti del subentro per alcuni comuni, quando il codice istat è variato nel tempo, l'intestazione poteva essere errata.

### Versione 4.1.5 (2018-10-16)

+ (Bug) Gestione controllo accessi - Incongruenze nei dati del soggetto (issue: [https://github.com/italia/anpr/issues/876](https://github.com/italia/anpr/issues/876))
    + In caso di dati incongruenti su uno o più soggetti non era gestito correttamente il risultato.

### Versione 4.1.4 (2018-10-15)

+ (Bug) Gestione controllo accessi - mutazione residenza (issue: [https://github.com/italia/anpr/issues/876](https://github.com/italia/anpr/issues/876)[https://github.com/italia/anpr/issues/877](https://github.com/italia/anpr/issues/877))
    + Il controllo accessi del servizio 5005 non valutava correttamente i permessi nel caso di famiglia nuova.

+ (Bug) Adattamento restrizioni diacritici xsd (issue: [https://github.com/italia/anpr/issues/861](https://github.com/italia/anpr/issues/861))
    + Alcuni dei diacritici da considerare validi non erano inclusi nelle restrizioni degli XSD.

### Versione 4.1.3 (2018-10-14)

+ (Bug) Web - Eliminazione dati - Errore creazione richiesta
    + L'applicazione web generava alcune richieste per il servizio 5013 non corrette.

+ (Bug) Web - Errore formattazione data nascita 28 maggio 1978
    + L'applicazione dell'ora legale non segue regole precise fino ad una certa data (http://toi.inrim.it/it/ienitlt.html). L'applicazione web non formattava bene l'orario per alcuni periodi.

+ (Requirement) Modifiche regole upload file APR per subentro
    + In produzione e presubentro è possibile usare sia le regole ANPR00 che le regole ANPR01. In test comuni e free test solo le nuove regole ANPR01.

+ (Bug) Verifica soggetto con procedimento aperto: escludere i soggetti eliminati (issue: [https://github.com/italia/anpr/issues/511](https://github.com/italia/anpr/issues/511))
    + Eliminare il blocco della certificazione in presenza di un procedimento aperto nel caso in cui sia stata eliminata l'associazione del cittadino dal procedimento. 

+ (Requirement) idOperazioneComune nella testata come alfanumerico (issue: [https://github.com/italia/anpr/issues/596](https://github.com/italia/anpr/issues/596)[https://github.com/italia/anpr/issues/814](https://github.com/italia/anpr/issues/814))
    + L'id operazione comune passa da numerico ad alfanumerico

### Versione 4.1.2 (2018-10-05)

+ (Bug) Assenza nome e cognome ufficiale anagrafe certificati
    + Il nome e cognome dell'ufficiale di anagrafe non era correttamente riportato.

+ (Bug) Web Stampa scheda individuale (issue: [https://github.com/italia/anpr/issues/856](https://github.com/italia/anpr/issues/856))
    + Errore decodifica legami nella convivenza.

+ (Bug) Web Iscrizione per altri motivi
    + Correzione assenza motivo iscrizione : Ripristino posizione anagrafica

+ (Requirement) 3002- implementazione ricerca "senzaNome" - "senzaCognome"
    + Implementare la consultazione scheda individuale del ws 3002 utilizzando come parametri di ricerca anche  i campi "senzaNome"  o "senzaCognome". 

+ (Bug) Elenco operazioni soggetto: errore reperimento alcune tipologie di rettifica 5014 (issue: [https://github.com/italia/anpr/issues/725](https://github.com/italia/anpr/issues/725))
    + L'elenco delle operazioni comunicate da ANPR per un cittadino non riporta  alcune tipologie di rettifica effettuate con il ws 5014

### Versione 4.1.1 (2018-09-30)

+ (Requirement) Fine validità major version con codDestinatario ANPR00 (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617)[https://github.com/italia/anpr/issues/775](https://github.com/italia/anpr/issues/775)[https://github.com/italia/anpr/issues/819](https://github.com/italia/anpr/issues/819))
    + Implementazione meccanismo per gestione fine validità versioni depcrecate.

### Versione 4.1.0 (2018-09-12)

+ (Requirement) WB 24 Bilinguismo
    + L'intervento prevede la gestione delle informazioni relative agli indirizzi in altre lingue al fine di produrre i certificati per i paesi ove vige il bilinguismo. 

+ (Requirement) WB 30 Stampa scheda dati individuale
    + I comuni hanno segnalato la necessità di poter stampare i dati parziali di una persona presente in Anpr. Oltre alla visura completa, già disponibile, viene richiesto quindi di produrre una stampa delle schede individuali limitata ai dati di interesse specifico. Gli interventi riguardano solo il sito web di Anpr e sono descritti nel documento MI-04-AN-13. 

### Versione 4.0.27 (2018-09-28)

+ (Bug) Web - Validazione numero sentenza mutazione tutti i dati
    + Le regole di validazione del campo numero sentenza non erano allineate nell'applicazione web.

### Versione 4.0.26 (2018-09-13)

+ (Bug) Restrizioni XSD per ANPR01 (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617))
    + Corrette regole validazione xsd per alcuni tipoQuesturaRilascio, tipoDenominazioneToponimoTranslitterato e tipoDescrizioneLocalitaTranslitterata

### Versione 4.0.25 (2018-09-11)

+ (Bug) Web - Caricamento provincia littoria / latina
    + L'applicazione web, in alcuni menu a tendina, presentava il comune di Littori al posto di Latina.


+ (Bug) procedura di elaborazione prospetto riepilogativo mensile:  ricalcolo valori aggregati
    + Revisione elaborazione dati del prospetto riepilogativo mensile, con particolare riferimento al calcolo della popolazione residente al 1 del mese che sarà ricalcolato partendo dai dati presenti sul DB  e non dal saldo del prospetto precedente.  


### Versione 4.0.24 (2018-09-07)

+ (Bug) Validazione web denominazione comune
    + Errore nella validazione del nome comune nell'applicazione web.

+ (Bug) Il tipo dato xsd siglaProvincia deve accettare solo valori di lunghezza 2
    + Venivano accettati valori anche di un carattere perl a sigla provincia.

+ (Bug) Controllo presenza codice specie se specie fonte vale 1
    + Modificato il controllo ES023 per verificare sempre la presenza del codice specie quando specie fonte è 1.

### Versione 4.0.23 (2018-09-04)

+ (Bug) WA: selezione comune per creazione richiesta elenchi e prospetti
    + Creazione richiesta xml per elenchi e prospetti: la ricerca non può essere pilotata solo con il codice ISTAT di un  comune perchè potrebbe lo stesso codice può essere appartenuto ad altro comune cessato. 

+ (Bug) ws 3007: gestione della casistica di assenza di notifiche nel periodo di riferimento  (issue: [https://github.com/italia/anpr/issues/758](https://github.com/italia/anpr/issues/758))
    + WS 3007 -  richiesta elenco notifiche riferite ad un determinato arco temporale: in assenza di occorrenze di interesse restituisce le altre tipologie di eventi comunicati nel periodo

### Versione 4.0.22 (2018-08-30)

+ (Bug) Data decorrenza responsabile convivenza
    + Corregge un errore nella impostazione della data di decorrenza del legame per il responsabile.

+ (Bug) web - errore Iscrizione altri motivi AIRE
    + Si verificava un errore se impostato il campo "trascritto" dell'atto di nascita senza compilare nessun altro dato dell'atto.

+ (Bug) Correzione automatica specieFonte = 0
    + A tutti gli effetti, qualsiasi valore di specieFonte diverso da 1 viene trattato come 2.

### Versione 4.0.21 (2018-08-24)

+ (Requirement) Modifica messaggio pec presubentro / testcomuni

### Versione 4.0.20 (2018-08-03)

+ (Bug) Malfunzionamento controllo CN352 per servizio 5012
    + In caso di annullamento di mutazione residenza 5001, il controllo CN352 non deve scattare se il tipo mutazione è 4 oppure 5 (patenti / autoveicoli)

### Versione 4.0.19 (2018-07-26)

+ (Bug) 5001 tipoMutazione 2 congruenza tipo scheda famiglia e datiControllo
    + 5001 tipoMutazione 2 verificata la congruenza tipo scheda famiglia e datiControllo

+ (Bug) Malfunzionamento risoluzione convivenza / scioglimento unione (issue: [https://github.com/italia/anpr/issues/774](https://github.com/italia/anpr/issues/774))
    + Risoluzione convivenza / scioglimento unione civile: fix per malfunzionamento sui dati di stipula.

+ (Bug) Malfunzionamento integrazione dati coniuge
    + Mutazione matrimonio/legame: correzione malfunzionamento per integrazione dei dati del coniuge non ANPR 

+ (Bug) Mutazione altri recapiti (issue: [https://github.com/italia/anpr/issues/769](https://github.com/italia/anpr/issues/769))
    + Corretto il malunzionamento nella mutazione altri recapiti

+ (Bug) Controllo correttezza CF
    + Nelle pagine di ricerca per CF e risoluzione disallineamenti viene restituito un errore in caso di CF con doppia omocodia es BLDMMD88A0MZ34A deve essere rimosso tale controllo


+ (Bug) WEB Gestione matrimoni pregressi
    + in caso di Mutazione scheda, se nei Dati Controllo viene selezionato: Cessazione matrimonio o vedovanza reso editabile il tag matrimonio; Risoluzione Convivenza reso editabile il tag convivenza;
 Scioglimento Unione reso editabile il tag unione civile.



+ (Bug) Inseriti controlli tipo residenza su iscrizione Convivenza
    + Verificato che la residenza nel 1010 (iscrizione convivenza) può essere solo italiana

### Versione 4.0.18 (2018-07-20)

+ (Bug) Errore elenco notifiche web
    + Aggiornata la visualizzazione delle notifiche al Comune interrogabili via Web (le notifiche non venivano mostrate correttamente)

### Versione 4.0.17 (2018-07-16)

+ (Bug) Annullamento mutazione dati decesso
    + Se su un soggetto viene fatta una mutazione 22 (dati decesso) dopo la morte non era più possibile annullare nessuna delle due operazioni.

### Versione 4.0.16 (2018-07-11)

+ (Bug) Malfunzionamento WEB in iscrizione altri motivi famiglia esistente - toponimo
    + Il 3002 non riporta tutte le informazioni sul toponimo presenti sul DB dando origine ad errore bloccante ES024 in caso di iscrizione n famiglia esistente (quando nell'indirizzo sul DB è valorizzato sia cod toponimo che toponimo fonte)

### Versione 4.0.15 (2018-07-09)

+ (Bug) Restrizioni versione applicativo (issue: [https://github.com/italia/anpr/issues/696](https://github.com/italia/anpr/issues/696))
    + Il campo versione applicativo ora accetta gli stessi valori del campo fornitoreApplicativo

+ (Bug) Parentesi accettate per tipoRigaAnnotazione (issue: [https://github.com/italia/anpr/issues/754](https://github.com/italia/anpr/issues/754))
    + Il pattern accettato per il campo tipoRigaAnnotazione passa da ([0-9À-ža-zA-Z\- &apos;/.,])* a ([0-9À-ža-zA-Z\- &apos;/.,()])*.

+ (Bug) Modifica visualizzazione monitoraggio operazioni
    + Corretto il reperimento del valore riportato nella colonna "Data di elaborazione dell'operazione"


+ (Bug) Regole validazione file aire subentro
    + La data di iscrizione AIRE diventa abbligatoria nel file AIRE.

### Versione 4.0.14 (2018-07-03)

+ (Bug) Web - Validazione denominazione convivenza
    + La denominazione della convivenza nel web non usava le stesse regole di validazione dei servizi.

+ (Bug) Gestione encoding diacritici certificati (issue: [https://github.com/italia/anpr/issues/744](https://github.com/italia/anpr/issues/744))
    + Alcuni diacritici non venivano trattati correttamente nel PDF dei certificati (6001)

+ (Bug) Web - residenti temporanei: gestione soggetti cancellati da ANPR 
    +  Sito web di ANPR -  residenti temporanei: gestione soggetti cancellati da ANPR

### Versione 4.0.13 (2018-06-20)

+ (Bug) Errore generazione messaggio controllo ES077
    + Corretto un errore nella generazione del testo dell'anomalia ES077

+ (Bug) Consultazione scheda soggetto
    + Ora è possibile inserire anche identificativi scheda comunale alfanumerici.

+ (Bug) Escludere CC030 e CC031 dal WS 6001
    + Da una email del 18/06/2018 del Comune di Novellara subentrato è emersa la necessità di escludere i controlli sullo stato di nascita dall'emissione dei certificati. I controlli sul comune di nascita risultano già esclusi

+ (Bug) 6001 - tipoRichiesta 2 (richiesta dati) corretta decodifica del campo tipoIndirizzo 10 ed 11  (issue: [https://github.com/italia/anpr/issues/721](https://github.com/italia/anpr/issues/721))
    + Servizio di certificazione: tipo richiesta 2 (richiesta dati) correttiva sulla decodifica del tipo di indirizzo 10 (revisione onomastica) ed 11 (rettifica indirizzo post accertamenti) 

### Versione 4.0.12 (2018-06-18)

+ (Bug) Implementato blocco mutazione composizione scheda in assenza dell'elenco soggetti
    + In precedenza le mutazione di composizione scheda famiglia convivenza erano permesse anche senza variare nessun soggetto.

+ (Bug) Gestione matrimoni/legami pregressi
    + Nella mutazione tutti i dati TipoMutazione = 13/14/17/19 è possibile inserire un matrimonio pregresso già chiuso per vedovanza o cessazione, inviando le informazioni complete. Vengono effettuati controlli di congruenza delle date di inizio e fine in modo tale che non vi sia sovrapposizione con matrimoni/legami esistenti

### Versione 4.0.11 (2018-06-15)

+ (Bug) Errato blocco generazione certificato di stato civile
    + E' stato rimosso un blocco che impediva in alcuni casi di generare il certificato di stato civile

### Versione 4.0.10 (2018-06-12)

+ (Bug) sito web ANPR: errata gestione tipo indrizzi 10 ed 11
    + Mancata  visualizzazione del TAB residenza se l'origine dell'indirizzo è una revisione dell'onomastica comunale o una rettifica post accertamenti, nei servizi di mutazione ed iscrizione.

### Versione 4.0.9 (2018-06-11)

+ (Bug) Blocco upload file subentro
    + Il modulo di upload dei file del subentro ora blocca l'invio se il comune non è inserito correttamente nel piano dei subentri. (in precedenza il messaggio aveva solo valore di avviso).

+ (Bug) Modifica controllo di congruenza date in inserimento matrimonio/legame e convivenza (issue: [https://github.com/italia/anpr/issues/705](https://github.com/italia/anpr/issues/705))
    + Modifica controllo di congruenza date per consentire la chiusura di una convivenza di fatto nella stessa data della stipula di un matrimonio/legame

### Versione 4.0.8 (2018-06-07)

+ (Bug) Bug controllo certificati APR su stato civile Divorziato (issue: [https://github.com/italia/anpr/issues/692](https://github.com/italia/anpr/issues/692))
    + E' necessario permettere la produzione di certificato non solo se ci sia l'atto di annullamento ma in alternativa la sentenza di fine matrimonio.

+ (Bug) WS 5008 - controllo comune di nascita
    + Nel WS 5008 il controllo di validità comune di nascita CN332 deve scattare solo se sono cambiati i dati anagrafici. Per verificare se è variato il luogo di nascita utilizzare denominazione e provincia

### Versione 4.0.7 (2018-06-05)

+ (Bug) Verifica dati soggetto per mutazione
    + Nei servizi di mutazione, c'era un errore nella gestione dei dati del soggetto ricercato quando i dati non sono congruenti (es. viene passato un cognome relativo ad un identificativo soggetto diverso).

+ (Bug) Verifica senza giorno / senza anno in caso di mutazione dati anagrafici
    + La data di nascita non veniva sempre confrontata correttamente in caso di senza giorno / senza giorno mese.

### Versione 4.0.6 (2018-05-28)

+ (Bug) Modifica regex elemento piano dell'indirizzo (issue: [https://github.com/italia/anpr/issues/676](https://github.com/italia/anpr/issues/676))
    + Estensione valori ammessi per elemento piano. Ora viene accettato anche il trattino.

+ (Bug) Integrazione versioni 3.7.2 / 3.7.3 su versione 4.0.6

### Versione 4.0.5 (2018-05-21)

+ (Bug) Controllo tipo emissione / tipo richiesta 6001
    + Verifica valori ammessi per emissione e tipoRichiesta nei dati controllo dell'operazione 6001.

+ (Bug) Modifica regex luogoEccezionale (issue: [https://github.com/italia/anpr/issues/676](https://github.com/italia/anpr/issues/676))
    + Estensione valori ammessi per elemento luogoEccezionale che si accetta ora gli stessi valori di localitaEstera.

+ (Bug) Integrazione versioni 3.7.0 / 3.7.1 su versione 4.0.5
    + Vengono riportati gli interventi presenti nella version 3.7.0/3.7.1 dell'applicazione anche nella versione 4.0.5

+ (Bug) Correzione integrazione gestione duplicati 6001

+ (Bug) Modifica regex tipo email xsd (issue: [https://github.com/italia/anpr/issues/670](https://github.com/italia/anpr/issues/670))
    + Correzione della regex del tipoEmail con la rimozione della negazione iniziale.

### Versione 4.0.4 (2018-05-17)

+ (Bug) Estensione hotfix 3.6.9 sulla versione 4.0.4

### Versione 4.0.3 (2018-05-10)

+ (Bug) Estensione hotfix 3.6.8 sulla versione 4.0.3

### Versione 4.0.2 (2018-05-07)

+ (Bug) Estensione hotfix 3.6.7 sulla versione 4.0.2

### Versione 4.0.1 (2018-05-04)

+ (Bug) Estensione hotfix 3.6.6 sulla versione 4.0.1

### Versione 4.0.0 (2018-04-30)

+ (Requirement) Revisione valori ammessi da subentro e servizi (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617))
    + Viene resa più rigorosa la verifica dei campi a testo libero. Tale restrizione è applicata solo indicando la versione ANPR01 nel tag codDestinatario della richiesta

+ (Requirement) WB 5 - Gestione cod destinatario per versione (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617))
    + Nel campo codDestinatario viene indicata la versione dei tracciati XSD: ANPR00 è la versione di partenza (fino alla release 3.x) ANPR01 dalla release 4.0

+ (Requirement) WB 29 - Mutazione dati del decesso (issue: [https://github.com/italia/anpr/issues/510](https://github.com/italia/anpr/issues/510))
    + Nuova mutazione con codice  22 per il servizio 5008.

+ (Requirement) WB 25 Rettifica indirizzo post accertamenti  (issue: [https://github.com/italia/anpr/issues/508](https://github.com/italia/anpr/issues/508))
    + ws 5001: gestione del nuovo codice mutazione 8 che identifica una rettifica indirizzo  emersa in fase di accertamenti  legati ad una richiesta di cambio residenza. 

+ (Requirement) WB 13 - Gestione duplicati (post subentro) (issue: [https://github.com/italia/anpr/issues/401](https://github.com/italia/anpr/issues/401))
    + Gestione delle posizione duplicate: produzione di liste di soggetti duplicati in ANPR al momento del subentro. Inserimento di controlli bloccanti nei servizi di registrazione che impediscano la coesistenza di due schede differenti per lo stesso soggetto

### Versione 3.7.3 (2018-05-28)

+ (Bug) Correzione esito servizio di rettifica (issue: [https://github.com/italia/anpr/issues/690](https://github.com/italia/anpr/issues/690))
    + Il servizio restituiva un esito positivo mentre avrebbe dovuto restituire un errore ES127.


### Versione 3.7.2 (2018-05-23)

+ (Bug) Webapp Validazione numero sentenza
    + L'applicazione web bloccava il carattere slash nel numero sentenza.

### Versione 3.7.1 (2018-05-23)

+ (Bug) Gestione autorità sentenza (issue: [https://github.com/italia/anpr/issues/680](https://github.com/italia/anpr/issues/680))
    + Nel campo autorità della sentenza sono ora ammesse le parentesi tonde

+ (Bug) Comune residenza sindaco
    + In Amministrazione nella funzione di Gestione dati del comune, nella ricerca dati del sindaco è stato modificato il controllo sul comune di nascita quando sono presenti caratteri speciali .

### Versione 3.7.0 (2018-05-18)

+ (Requirement) WB 14.1 GESTIONE DATA DECORRENZA LEGAME E RETTIFICA ALTRE DATE
    + L'intervento include: la gestione data decorrenza legame nei servizi subentro (S001) di registrazione (ws 1001, 1002, 5001, 5005, A001, A002, A006, 2001, 2003) e consultazione (ws 3002)  oltre che da web In particolare nel tracciato di subentro e nel tracciato del servizio 3002 è stata aggiunta  la data di decorrenza legame la rettifica delle seguenti date da ws 5014 e da web: Data ultimo aggiornamento scheda Data di iscrizione nel comune Data di ingresso nella famiglia

+ (Requirement) WB 15 Inserimento Comune o Stato Estero di Provenienza in A002
    + L'intervento prevede l'indicazione del comune o dello stato estero di provenienza nel servizio di iscrizione AIRE sia per il WS A002 che nella funzione accessibile da Web Nel tracciato del servizio A002 è stato aggiunto l'oggetto non obbligatorio relativo alla "Provenienza"

+ (Requirement) Semplificazione protocollo di sicurezza per inoltro notifiche verso gli endpoint dei Comuni
    + Eliminazione della Mutual Authentication che costringeva ad esporre un endpoint del Comune con il relativo certificato Server. Utilizzo del protocollo TLS sbilanciato, per permettere l'esposizione dell'endpoint con un certificato emesso da una CA pubblica. La riservatezza delle informazioni è garantita dalla crittografia del contenuto della notifica con la chiave pubblica del certificato assegnato ad ogni Comune (CO-9999).


+ (Requirement) WB 10 Integrazione  ws 5008 per completamento dati da subentro di un soggetto AIRE (cod. mutazione = 21)
    + Per la gestione del completamento dati da subentro di un soggetto AIRE si introduce nel ws 5008 “Mutazione tutti i dati”  e nella funzionalità web il  nuovo codice mutazione 21  (Dati integrativi AIRE). Il tracciato del servizio rimane immutato

