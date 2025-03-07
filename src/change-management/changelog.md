# Changelog

## Versione 9.1.4 (2025-03-07)

+ (Bug) Modifica xsd notifiche di stato civile
    + Aggiunto riferimento evento collegato per trascrizioni.

## Versione 9.1.3 (2025-03-05)

+ (Requirement) WebApp: nuova sezione elettorale download file
    + Pubblicata una nuova linea di menu nella sezione "Liste Elettorali" per lo scarico delle anomalie del campo elettore

## Versione 9.1.2 (2025-02-25)

+ (Requirement) ANNCSU: Controllo indirizzo (issue: [https://github.com/italia/anpr/issues/4827](https://github.com/italia/anpr/issues/4827))
    + Nel corso dell'inizio della prossima settimana sarà attivato un controllo sull'indirizzo inserito in un cambio di residenza o in una iscrizione per il quale l'indirizzo stesso sarà validato con l'archivio ANNCSU e, in caso di incogruenza, sarà restituito un warning di tipo CN558.

## Versione 9.1.1 (2025-02-11)

+ (Bug) 6001: internal server error per rilascio certificati  (issue: [https://github.com/italia/anpr/issues/4811](https://github.com/italia/anpr/issues/4811))
    + E' stato corretto un errore che mandava in errore la generazione dei certificati da WebService.

## Versione 9.1.0 (2025-02-10)

+ (Requirement) ANPR / ws P000 / wsdl - Visualizzazione identificativo ANNCSU  
    + Web Service P000 - Operazione P002 - Nella sezione Indirizzo di una dichiarazione di cambio residenza (tipologia 2) e in una richiesta di trasferimento dall'estero in Italia (tiplogia 4) inviate dall'area autenticata di ANPR sarà restituito in output il campo prognazacc proveniente dal sistema ANNCSU. (questa modifica si ripercuote anche sull'anteprima pratiche della webapp)

+ (Requirement) Notifiche ANSC: Inseriti nuovi campi nel tracciato per le trascrizioni  
    + Inseriti nuovi campi nel tracciato delle notifiche verso ANPR: cognomeAggiunto, nomeAggiunto e il tipo di modifica oggetto della trascrizione.

+ (Requirement) Reindirizzamento accesso anpr anagrafico smart card 
    + Il predente link di accesso ridirige al nuovo SPID/CIE/CNS/Smartcard <https://dait.interno.gov.it/servizi-demografici/circolari/circolare-dait-n76-del-19-settembre-2024>

+ (Bug) 6001: emissione online cf assente  va in errore
    + Correzione di un bug della certificazione che casu un errore in alcuni casi particolari.

## Versione 9.0.11 (2025-02-03)

+ (Bug) Controlli sull'atto unione civile
    + Risolto bug che impediva la notifica di una unione civile con scioglimento.

## Versione 9.0.10 (2025-01-30)

+ (Bug) Verifica id comunale convivenza
    + Inserito un controllo che non permette l'iscrizione di una convivenza con lo stesso id comunale.

## Versione 9.0.9 (2025-01-27)

+ (Bug) Controlli framework non gestiscono il nuovo attoeventoanpr
    + Risolto un bug che permetteva l'inserimento in un atto ansc di date incongruenti

## Versione 9.0.8 (2025-01-24)

+ (Bug) [SC]: Notifiche ANSC da ANPR, non coerenti con la richiesta (issue: [https://github.com/italia/anpr/issues/3883](https://github.com/italia/anpr/issues/3883))
    + Anche quando viene richiesto un tipo di registro specifico (es. NA01 per la nascita) venivano restituite tutte le notifiche (come se si fosse scelto NA00). vedi <https://github.com/italia/ansc/issues/1258>

+ (Bug) Verifica QRCode possibile solo nel periodo di validità
    + La verifica del QRCode dei certificati è ora limitata al solo periodo di validità degli stessi.

## Versione 9.0.7 (2025-01-16)

+ (Bug) Errori in comunicazione con ANPR (issue: [https://github.com/italia/anpr/issues/4769](https://github.com/italia/anpr/issues/4769))
    + Risolti problemi di comunicazione con il sistema ANPR 16/01/2025

+ (Bug) Anomalia verifica QRCode certificato
    + Risolta verifica QR code certificati ANPR

## Versione 9.0.6 (2025-01-14)

+ (Bug) 1000, 2000, A000 e 5000 non validano id ansc
    + Applicati dei controlli di validità più stringenti quando viene inserito l'id ANSC

## Versione 9.0.5 (2024-12-11)

+ (Requirement) ANNCSU: verifica odonimo in ANPR
    + In caso di nuova iscrizione o cambio residenza sarà fatta una verifica dell'indirizzo con l'archivio ANNCSU. In caso di incongruenza sarà restituito un warning

## Versione 9.0.4 (2024-12-02)

+ (Bug) Consultazione liste elettorali: non viene visualizzato lo stato di nascita
    + Risolto bug che non visualizzava lo stato estero di nascita per la consultazione elettorale
    
+ (Requirement) 5008: impedire modifiche alle liste elettorali
    + Sarà impedito l'inserimento dei dati elettorali con Mutazione tutti i dati dato il subentro elettorale di tutti i comuni in ANPR

## Versione 9.0.3 (2024-11-28)

+ (Requirement) Aggiornamento XSD notifiche stato civile (issue: [https://github.com/italia/anpr/issues/3883](https://github.com/italia/anpr/issues/3883))
    + Aggiunti dati trascrizione e dati lingua, gli intestatari ora possono essere più di 2.
	
+ (Requirement) Fine tuning prestazionale
    + Riviste alcune funzionalità per far fronte al carico crescente del sistema ANPR.

+ (Bug) A002 e 1002: in reiscrizione viene controllata la validita del luogo di nascita
	+ Risolto bug che verificava la conformità del comune di nascita anche in caso di nuova iscrizione di un soggetto esistente

## Versione 8.5.2 (2024-11-25)

+ (Requirement) WebApp: disabilitazione invio richiesta contributo al subentro elettorale
    + Non è più possibile inviare richieste di contributo per il subentro elettorale

## Versione 8.5.1 (2024-09-31)

+ (Bug) A002: controllo 339 controlla congruenza codcatastale comune nascita con codice fiscale
    + Per Iscrizione aire altri motivi non verrà più effettuato il controllo di congruenza tra codice catastale del comune nascita  e codice fiscale in caso di reiscrizione

## Versione 9.0.2 (2024-10-29)

+ (Bug) web: pannelli di monitoraggio ministero
    + Aggiornata la home del profilo Ministero e tolte informazioni non più accessibili

## Versione 9.0.1 (2024-10-21)

+ (Requirement) Liste elettorali: scarico massivo
    + Nella sezione "Liste elettorali" sarà possibile richiedere lo scarico dei dati elettorali del proprio comune con profilo ufficiale elettorale

+ (Requirement) Scarico comuni: download personalizzato
    + Possibilità di scegliere le sezioni dati da includere nello scarico massivo comune

## Versione 9.0.0 (2024-09-30)

+ (Requirement) Gestione poligamie
    + Servizi di gestione delle poligamie [disponibile solo in test comuni, verra' data comunicazione della disponibilità in produzione.]

## Versione 8.5.0 (2024-09-23)

+ (Requirement) WebApp: Accesso comune spid/cie/cns Anagrafe/Elettorale/Stato civile
    + Come da comunicazione <https://dait.interno.gov.it/servizi-demografici/circolari/circolare-dait-n76-del-19-settembre-2024>

## Versione 8.4.8 (2024-09-17)

+ (Bug) 6001: non certificabilita anagrafica impedisce di emettere il certificato elettorale
    + Risolto bug che riguardava la richiesta di un certificato elettorale. Veniva restituito un errore di non certificabilita quando il soggetto non era certificabile anagraficamente ma lo era elettoralmente

## Versione 8.4.7 (2024-07-12)

+ (Requirement) WebApp: Disabilitata Richiesta di contributo per l'adesione allo stato civile - modifica etichetta
    + In attesa delle nuove linee guida per la richiesta di contributo, la funzione viene disabilitata.

## Versione 8.4.6 (2024-07-05)

+ (Bug) 7001 : Scarico tabelle 61 (tipo categoria) e 62 (tipo componente) - valori errati (issue: [https://github.com/italia/anpr/issues/4575](https://github.com/italia/anpr/issues/4575))
    + Ora il servizio restituisce anche le tabelle con id 61 e 62

## Fine supporto versione ANPR precedenti alla 8 (2024-07-01)

+ (Requirement) Fine supporto versione ANPR precedenti alla 8 (issue: [https://github.com/italia/anpr/issues/4360](https://github.com/italia/anpr/issues/4360))
    + Da oggi i cod destintario inferiori ad ANPR05 non verranno più accettati.

## Versione 8.4.5 (2024-06-12)

+ (Bug) 3002: desclocalitaprov visualizzata in presenza di idcomuneprov
    + Risolto il bug che restituiva la descrizione localita di provenienza anche in caso di comune di provenienza

+ (Requirement) WebApp: Gestire ritorno ae 27 e 28 per omocodice
    + Sarà permesso l'annullamento di un omocodia precedentemente richiesta

## Versione 8.4.4 (2024-06-04)

+ (Bug) 1000: reiscrizione con nome città di castello
    + Risolto un bug che riguardava la reiscrizione di un soggetto avente nel comune di nascita un carattere diacritico.

## Versione 8.4.3 (2024-05-30)

+ (Bug) WebApp: timeout in consultazione convivenza
    + Migliorate le perfomance della risposta delle consultazione delle convivenze, che in alcuni casi poteva portare a dei timeout.

## Versione 8.4.2 (2024-05-22)

+ (Bug) webapp: rifugiati con cf numerico nati in italia
    + Risolto bug collegamento cf tra numerico e alfanumerico nel caso in cui il cittadino è uno stranierio nato in Italia

## Versione 8.4.1 (2024-05-07)

+ (Requirement) Iscrizioni: inserire warning in caso di cognome o nome con pattern NN o N.N
    + Nei servizi 1001,1002,A001,A002,5008, se verrano forniti i dati di paternità o maternità con il campo cognome/nome uguale a NN o nn (con o senza punteggiatura), sarà restituito il controllo warning EN566

+ (Requirement) Aggiunta residenza soggetto a notifiche di stato civile
    + Aggiunte nelle notifiche da ANSC verso ANPR le informazioni relative alla cittadinanza e alla residenza sia dell’intestatario dell’atto (non per l’atto di nascita) che dei genitori in caso di atti di nascita.
    
+ (Requirement) 6001 emissione online: impedire che venga richiesto certificato per un componente terzo
    + Servizio di certificazione 6001 con emissione online: non sarà possibile richiedere un certificato per un componente terzo non presente nella famiglia.
    
+ (Requirement) 6001: errori su certificato in tedesco
    + Nel testo tedesco del certificato la denominazione del comune viene indicata adesso in lingua tedesca.

## Versione 8.4.0 (2024-04-15)

+ (Requirement) Iscrizione liste elettorali da portale cittadini.
    + Gestione della nuova pratica di iscrizione alle liste elettorali proveniente dal portale per i cittadini. (Webapp e P000)

## Versione 8.3.6 (2024-04-07)

+ (Requirement) Webapp: Identificativo unico nazionale usabile nella consultazione Agenzia Entrate
    + Gestione identificativo unico nazionale nella consultazione agenzia entrate.

## Versione 8.3.5 (2024-03-26)

+ (Bug) webapp: bug elettorale sulla cancellazione sezione
    + Risolto un bug sull'applicazione web anpr che, alla cancellazione di una sezione, restituiva pagina bianca.

## Versione 8.3.4 (2024-03-11)

+ (Bug) 6001: iscrizione liste senza declinazione del sesso per iscritta
    + Certificato di iscrizione nelle liste elettorale: sarà declinato il sesso del termine iscritto/a presente nel body del certificato. (Risolve bug reltivo alla certificazione anagrafica per i cancellati da ANPR)

## Versione 8.3.3 (2024-03-05)

+ (Requirement) Certificati elettorali
    + Servizi per i comuni: nei certificati elettorali non compare più l'atto di nascita

## Versione 8.3.2 (2024-02-29)

+ (Bug) 5010: non permette di inserire un lista aggiunta ue dopo una generale
    + adesso permette di inserire un lista aggiunta ue a seguito di una cancellazione di una lista generale

## Versione 8.3.1 (2024-02-13)

+ (Requirement) 4003: impedire inserimento nuove richieste in presenza di un altra da elaborare
    + Non sarà più possibile inserire una richiesta 4003 se ne è presente un'altra in attesa di elaborazione

+ (Bug) WEBAPP: valorizza circoscrizione camera e senato anche quando il flag è N
    + Risolto bug che non permetteva la mutazione dei dati elettorali quando si impostavano i flag camara e senato a N

## Versione 8.3.0 (2024-02-05)

+ (Requirement) Pratiche di iscrizione SDG da area riservata (issue: [https://github.com/italia/anpr/issues/4384](https://github.com/italia/anpr/issues/4384))
    + WEBAPP - gestione delle dichiarazioni di trasferimento cittadino EU inviate da Portale ANPR attraverso la webapp di ANPR, funzionalità Utilità e notifiche - Dichiarazioni di trasferimento in italia trasmesse dai cittadini ue. Web Service P000 - gestione dichiarazioni di trasferimento cittadino EU inviate da Portale ANPR attraverso le operazioni wsP001, wsP002, wsP003 della famiglia di wsP000 - Nuova tipologia di richiesta con identificativo 4.

+ (Bug) 5010: bloccare se motivo cancellazione 9 e manca lista generale

+ (Bug) WEBAPP: lista generale erroneamente quando presente lista aggiunta ue

+ (Bug) WS1000 - Presenza elemento attoEventoANPR vuoto
    + In presenza di elemento XML empty <attoEventoANPR/> il servizio falliva. (da notare che in questi casi sarebbe preferibile non inviare per niente l'elemento)


## Versione 8.2.6 (2024-01-29)

+ (Bug) WEBAPP: decesso - mutazione tutti i dati - non vengono riportati i dati dell'atto inserito durante la cancellazione (issue: [https://github.com/italia/anpr/issues/4161](https://github.com/italia/anpr/issues/4161))
    + Effettuando una mutazione tutti i dati, dati di decesso: non vengono riportati i dati dell’atto inserito durante la cancellazione.

+ (Requirement) Richiesta di contributo per l'adesione allo stato civile - modifica etichetta
    + Modificare l'etichetta visualizzata nella schermata dell'immagine in allegato da "Gestione Comunale" in "Gestionale Comunale".

+ (Requirement) WEB : gestione da parte dei comuni dei certificati per la firma delle notifiche
    + I comuni potranno 1. Inserire – aggiornare – abilitare – disabilitare l’endpoint cui chiedono gli vengano inviate le notifiche, 2 - Scegliere con quale certificato, tra quelli che l’applicazione mostrerà come disponibili, gli vengano firmate le notifiche.

+ (Requirement) Notifiche da AppIO del cambio di stato delle richieste di cambio di residenza e di rettifica dati inserite dai cittadini nell'Area Riservata del sito ANPR
    + Da oggi 29 Gennaio, i cittadini riceveranno le notifiche di lavorazione e cambio di stato della richiesta, oltre che per mezzo del canale mail anche da AppIO a meno di non eseguire esplicito opt-out (disabilitazione) del relativo servizio di notifica presente nella sezione Servizi di AppIO.


## Versione 8.2.5 (2023-12-20)

+ (Requirement) Performance tuning notifiche stato civile per anagrafe
    + Coda a priorità per le notifiche da ANSC verso ANPR, con tempo stimato della richiesta entro 15 minuti (la notifica viene inclusa nella risposta solo se è stata prodotta già).

## Versione 8.2.4 (2023-12-18)

+ (Bug) Bug: Allineamento template richiesta contributo Stato Civile
    + Il documento da firmare per richiedere il contributo per l'adesione allo stato civile digitale è stato aggiornato.

+ (Requirement) Accesso contributo stato civile
    + Ora i permessi richiesti per accedere alla richiesta contributo per l'adesione allo Stato Civile digitale sono gli stesso necessari per il contributo al subentro delle liste elettorali

## Versione 8.2.3 (2023-12-14)

+ (Bug) Bug: scambiato lista warning con lista errori nel servizio 2012
    + Bug nella operation 2012 che restituiva errore EN562 come warning anzichè come bloccante

## Versione 8.2.2 (2023-12-05)

+ (Requirement) Liste Elettorali: gestione sezioni
    + E' stata implementata la gestione della consultazione e cancellazione delle sezioni.

## Versione 8.2.1 (2023-12-04)

+ (Bug) Liste: in consultazione non viene visualizzata la lista senza sezione
    + WebApp: sarà possibile visualizzare un elettore ad N senza una sezione associata.

## Versione 8.2.0 (2023-11-28)

+ (Requirement) Richiesta di contributo per l'adesione allo stato civile.
    + Nell'applicazione web di ANPR è disponibile per i sindaci la funzione per effettuare la richiesta di contributi per l'adesione all' Archivio Nazionale informatizzato dei registri dello Stato Civile. (Amministrazione - RICHIESTA CONTRIBUTO PER L’ADESIONE AL SISTEMA ANSC). [La richiesta può essere inviata solo dopo l'adesione formale e la registrazione del primo evento di stato civile]

+ (Requirement) XSD ed Esempi discordanze anagrafiche
    + Oltre alla predisposizione eventi digitali stato civile sono disponibili anche le segnalazioni di discordanze anagrafiche tra Stato civile e Anagrafe.

## Versione 8.1.9 (2023-11-21)

+ (Requirement) Aggiornamento notifiche di stato civile
    + Adeguamento alla versione [1.19.0](https://github.com/italia/ansc/tree/v1.19.0) di ANSC.

+ (Requirement) Contributi al subentro elettorale - IBAN
    + Ora è sempre possibile indicare l'IBAN per ricevere il contributo.

## Versione 8.1.8 (2023-10-23)

+ (Requirement) Mev elettorale certificati e consultazione
    + Inserite traduzioni in sloveno e tedesco per la sezione di firma dei certificati elettorali. Gestione del caso di elettore N senza l'associazione della lista.

## Versione 8.1.7 (2023-10-17)

+ (Bug) WS4005 - Esclusione P00X da risultati richiesta asincrone 4005
    + Ora i serrvizi P000 non vengono più restituiti negli elenchi generati tramite il servziio 4005. 

## Versione 8.1.6 (2023-10-13)

+ (Requirement) Webapp - disabilitazione del salvataggio nella richiesta di contributo elettorale
    + Nel caso in cui non venga modificato alcun dato nella form del contributo al subentro elettorale, alla pressione del tasto "salva" non verrà generato un nuovo documento da firmare digitalmente.

## Versione 8.1.5 (2023-10-03)

+ (Requirement) Webapp : Notifiche ANSC
    + Visualizzazione delle predisposizione anagrafiche dello stato civile.

+ (Requirement) Webapp: gestione documenti storici e visualizzazione operazioni elettorali
    + Nella sezione documenti storici presente nella pagina carta d'identita saranno visualizzabili, oltre ai documenti cartacei storici, anche i documenti elettronici cie storici
    
+ (Requirement) WS6001 : liste elettorali: mev sui certificati
    + Sarà possibile firmare con il nome di un incaricato o a nome del vice sindaco i certificati di godimento dei diritti politici o il certificato di iscrizione nelle liste elettorali (impostare il flag tipoFirmaElettorale a 1 nei dati controllo) 

## Versione 8.1.4 (2023-09-22)

+ (Bug) Scarico massivo comune adattato ad ANPR05
    + Lo scarico massivo comune non era ancora stato adattato alle ultime versioni di ANPR.

+ (Requirement) Contributo subentro liste elettorali - modifica testi prima schermata.
    + Chiarificati i test della prima schermata della richiesta contributo subentro liste elettorali.

## Versione 8.1.3 (2023-08-31)

+ (Bug) WebApp: ricerca soggettoa aire con lista aggiunta 
    + Andava in errore la ricerca di un aire con una lista generale aggiunta

+ (Requirement) 1002,A002: bloccare inserimento liste in caso di lista generale inserita
    + Non sarà permesso inserire con 1002 e A002 la sezione listaElettorale relativamente a soggetti a cui sono stati inseriti i nuovi dati elettorali da altro comune (a meno di una cancellazione elettorale)

## Versione 8.1.2 (2023-08-22)

+ (Bug) 5010: mutazione listareg bloccata se manca lista generale
    + Sarà possibile inserire una lista generale aggiunta prima dell'inserimento di una lista generale. 

+ (Bug)  WebApp: errore ricerca convivenza
    + Era presente un errore nella ricerca delle convivenze da webapp.
   
## Versione 8.1.1 (2023-08-10)

+ (Requirement) Contributi al subentro delle liste elettorali visualizzazione campo note rifiuto richiesta 
    + Nel riepilogo di una richiesta in presenza di note valorizzate mostrarle a video nela box riepilogativo dei dati della richiesta (box nell'immagine in allegato). 

## Versione 8.1.0 (2023-08-03)

+ (Requirement) Richiesta contributo adesione liste elettorali 
    + Nuova funzionalità disponibile nella web app di ANPR alla voce Amministrazione->Richiesta Contributo Integrazione Liste Elettorali in ANPR. La funzionalità deve essere utilizzabile solo dal profilo del Sindaco. 

+ (Requirement) Aggiornato tracciato XSD per le notifiche delle predisposizioni anagrafiche (issue: [https://github.com/italia/anpr/issues/3587](https://github.com/italia/anpr/issues/3883))
    + Revisione tracciato predisposizioni anagrafiche di Stato Civile (ANSC)

## Versione 8.0.1 (2023-06-14)

+ (Requirement) Elettorale: certificati elettorali sloveno, scarico massivo e riepiloghi
    + Integrazione funzionalità liste elettorali 

## Versione 8.0.0 (2023-05-05)

+ (Requirement) Identificativo Unico Nazionale (DECRETO 3 marzo 2023)
    + Viene reso disponibile il nuovo ID ANPR, come previsto dal decreto [ID ANPR, DECRETO 3 marzo 2023](https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2023-04-18&atto.codiceRedazionale=23A02326&elenco30giorni=false)
  
+ (Requirement) Notifiche eventi di stato civile
    + Sono rese disponibili le notifiche relative agli eventi (atti) provenienti dal nuovo Archivio Nazionale informatizzato dei registri dello Stato Civile (ANSC), nei casi in cui sia prevista la registrazione anagrafica.

+ (Requirement) Limite ricerca operazioni e notifiche a 180 giorni
    + Con la major versione 8 (ANPR05) la ricerca delle operazioni e delle notifiche dai servizi come il 4005 viene limitata agli ultimi 180 giorni. Sarà ancora possibile ricercare periodi precedenti indicando le versioni di anpr 7 o inferiore (fino ad ANPR04). Dal 15 Gennaio 2024 anche la web app imporrà tale limitazione (ad esempio sull'accesso alle notifiche o i dettagli delle operazioni dei soggetti).
    
+ (Requirement) Adeguamento Web App ANPR per gestione nuovo identificativo ATTI digitali 
    + Per i servizi di ANPR di Iscrizione, Iscrizione AIRE (per nascita e altri motivi), mutazione, Cancellazione per decesso, Consultazione, Emissione carta identità, sono state adeguate le sezioni ATTO.
    

### Versione 7.1.1 (2023-03-07)

+ (Bug) webapp: upload liste elettorali con refresh pagina e certificati
    + Controllo della presenza della data decorrenza su ws 5010 e 5011. Vietato l'upload massivo di due liste elettorali. Per i certificati elettorali, in caso di elettore a N, lo stesso non viene prodotto.

### Versione 7.1.0 (2023-02-27)

+ (Requirement) Domicilio Digitale Webapp e ws P000
    + Gestione Domicilio Digitale: Il servizio è attualmente in sperimentazione per un numero ristretto di utenti il cui domicilio digitale viene trasmesso da INAD a ANPR
Per tali utenti le comunicazioni relative alle pratiche di richiesta di rettifica e dichiarazioni di residenza vengono trasmesse al domicilio digitale. In caso di richiesta di un certificato, gli stessi utenti possono scegliere di riceverlo al domicilio digitale eletto su INAD.
ws P000 viene inserita l’informazione del domicilio digitale tra i <recapiti> associati alla pratica identificato con idTipologiaRecapito=5


### Versione 7.0.4 (2023-02-08)

+ (Bug) ws 5008: tipo mutazione 20  
    + Il ws 5008 tipo mutazione 20 deve essere utilizzato per "completare" l'iscrizione del cittadino inviando ulteriori dati afferenti allo stesso; non deve in alcun modo modificare i dati anagrafici del cittadino. 

### Versione 7.0.3 (2023-02-02)

+ (Requirement) Liste elettorali: mev dec_collegi, bilinguismo e scarico
    + Gestione Bilinguismo: nella mutazione sezione è possibile inserire l'indirizzo e la denominazione della sezione in altra lingua e consultarlo con il servizio di consultazione 3002.
+ (Bug) Aggiornamento Web Service P000 - Gestione richieste dei cittadini da Portale ANPR (issue: [https://github.com/italia/anpr/issues/3587](https://github.com/italia/anpr/issues/3587) [https://github.com/italia/anpr/issues/3603](https://github.com/italia/anpr/issues/3603) [https://github.com/italia/anpr/issues/3608](https://github.com/italia/anpr/issues/3608) [https://github.com/italia/anpr/issues/3620](https://github.com/italia/anpr/issues/3620))
    + Viene inserita l’informazione soggettoAIRE (Y/N) per P002 e aggiornato formato del campo note per P003. (vedi in particolare issue #3731)
   
### Versione 7.0.2 (2023-01-22)

+ (Requirement) Web App Consultazione AE per dati anagrafici
    + La consultazione AE permette ora anche l'interrogazione per dati anagrafici. Sono sempre obbligatori COGNOME, NOME e SESSO oltre a uno tra data di nascita e range di anni di nascita.
+ (Bug) Web App produzione: atti di stato civile non visibili (issue: [https://github.com/italia/anpr/issues/3760](https://github.com/italia/anpr/issues/3760) [https://github.com/italia/anpr/issues/3753](https://github.com/italia/anpr/issues/3753))
    + Gli atti di stato civile dalla web app non era più visualizzabili.

### Versione 7.0.1 (2022-12-22)

+ (Requirement) Integrazione patch 6.0.5 su ramo 7.0 (issue: [https://github.com/italia/anpr/issues/3705](https://github.com/italia/anpr/issues/3705))
    + Le hotfix attualmente presenti in produzione sono state riportate anche sulla versione 7.0 di ANPR.

### Versione 6.0.5 (2022-12-20)

+ (Requirement) 5008: tipo mutazione 5 liste: bloccare in caso di primo caricamento
    + Per i soggetti per i quali sono stati inseriti i nuovi dati delle liste elettorali verrà inibito il 5008 per la mutazione delle stesse.

### Versione 6.0.4 (2022-12-12)

+ (Bug) Liste elettorari: ricerca soggetto cancellato
    + Mutazione liste elettorali: è stata aggiunta la possibilità di aggiornare la lista elettorale anche per un soggetto cancellato

### Versione 7.0.0 (2022-11-30)

+ (Requirement) Rilascio atto ANSC per ANPR (issue: [https://github.com/italia/anpr/issues/3625](https://github.com/italia/anpr/issues/3625))
    + Il nuovo tipo verrà trattato se viene indicato il codDestintario ANPR04

### Versione 6.0.3 (2022-11-30)

+ (Requirement) Aggiunti controlli al servizio 5010 - liste elettorali

### Versione 6.0.2 (2022-09-20)

+ (Bug) 1001: traslitterazione frazione verso ae
    + Nel 1001 in alcuni casi c'era una errata tralitterazione della frazione nell'invio dei dati ad Agenzia entrate.

### Versione 6.0.1 (2022-09-03)

+ (Bug) 2011: risposta con datiiscrizioneaire senza che il soggetto sia aire
    + A volte il 2011 poteva restituire i dati iscrizione aire anche per soggetti non aire.

### Versione 6.0.0 (2022-09-01)

+ (Requirement) Rilascio liste elettorali
    + Le liste elettorali sono richiamabili con il codice destintario ANPR03

### Versione 5.15.8 (2022-05-17)

+ (Bug) Web: Riabilitazione campo residenza e conteggi ricerca richieste cittadini (issue: [https://github.com/italia/anpr/issues/3366](https://github.com/italia/anpr/issues/3366))
    + Il campo residenza deell'elenco richieste cittadini e i conteggi delle richieste inviate sono stati ripristinati. Contestualmente è stato rimosso il campo email del cittadino, sempre dall'elenco.

### Versione 5.15.7 (2022-05-10)

+ (Requirement) Web: rimozione campo residenza ricerca richieste cittadini (issue: [https://github.com/italia/anpr/issues/3366](https://github.com/italia/anpr/issues/3366))
    + Al fine di migliorare le prestazione delal ricerca, il campo residenza viene rimosso dal risultato sintetico delle richieste dei cittadini.  (2022-05-12)

+ (Bug) Web: performance Export (issue: [https://github.com/italia/anpr/issues/3366](https://github.com/italia/anpr/issues/3366))CSV richieste cittadino (issue: [https://github.com/italia/anpr/issues/3366](https://github.com/italia/anpr/issues/3366))
    + L'esport CSV delle richieste del cittadino poteva portare a dei timeout, specialmente per i comuni più popolosi. (2022-05-11)

+ (Requirement) Web: Disabilitata ricerca iniziale richieste cittadini (issue: [https://github.com/italia/anpr/issues/3366](https://github.com/italia/anpr/issues/3366))
    + Al fine di limitare il carico sul sistema è stato per ora inibilita la ricerca iniziale di default delle richieste dei cittadini (va effettuata esplicitamente). 

+ (Requirement) Web: Disabilitazione contatori richieste cittadini (issue: [https://github.com/italia/anpr/issues/3366](https://github.com/italia/anpr/issues/3366))
    + Al fine di limitare il carico sul sistema è stato per ora rimossa la dashboard con i contatori delle richieste dei cittadini sulla home page. 

### Versione 5.15.6 (2022-04-29)

+ (Bug) Web: Allineamento codice fiscale da 11 cifre in Entrate
    + Non era consentito il collegamento tra CF numerico e alfanumerico in caso di cittadino nato in Italia

### Versione 5.15.5 (2022-04-05)

+ (Bug) Visualizzazione componenti, versione PDF dichiarazioni cambio residenza
    + In alcuni casi la versione PDF non mostra i componenti aggiuntivi della richiesta.

+ (Bug) Invio pec notifica richieste portale cittadini
    + A volte le notifiche di cambio stato di rettifiche e cambio residenza non veniva inviate quando era stata indicata una PEC.

+ (Requirement) Notifiche - Gestione rinnovo certificati CO-9999
    + gestione sostituzione certificati Comunali CO-9999 che sono in scadenza con CO-9998, per crittografia notifiche verso endpoint Comunali.

### Versione 5.15.4 (2022-03-08)

+ (Bug) [ws P002] Dettagli Richieste - Allegati: Formato File (issue: [https://github.com/italia/anpr/issues/3200](https://github.com/italia/anpr/issues/3200))
    + Correzione gestione formato file dei P002

### Versione 5.15.3 (2022-02-16)

+ (Bug) Email / PEC notifica richieste cittadino superiore ai 50 caratteri
    + Nella sezione amministrazione, gestione dati comune, della web app, non era possibile indicare Email / PEC di noficia richieste dei cittadini con lunghezza superiore ai 50 caratteri.

### Versione 5.15.2 (2022-02-11)

+ (Bug) Errore visualizzazione riepilogo dichiarazione cambio residenza web app
    + Nella web app, il riepilogo delle dichiarazini di residenza non mostrava correttamente i dati dei cittadini che si spostano insieme al richiedente (nella versione html, la versione pdf era funzionante).

### Versione 5.15.1 (2022-01-27)

+ (Bug) controllo EN248
    + Risolto il bug per cui il controllo EN248 scattava anche se il CF indicato nella mutazione non era più utilizzato 

### Versione 5.15.0 (2021-12-29)

+ (Requirement) Web Service P000 - gestione dichiarazioni cambio residenza dei cittadini da Portale ANPR

### Versione 5.14.1 (2021-11-22)

+ (Requirement) 4005 - Integrazione patch 5.13.15 su ramo 5.14

### Versione 5.13.13 (2021-11-09)

+ (Bug) 4005 - Esclusione operazioni 6001 dal risultato (issue: [https://github.com/italia/anpr/issues/2905](https://github.com/italia/anpr/issues/2905))
    + Ora il servizio 4005 non restituisce più le operazioni di certificazione 6001 quando invocato senza filtro per operazione.

### Versione 5.13.12 (2021-10-17)

+ (Bug) [italia/anpr] [6001] anomalia in certificazione soggetti residenti (issue: [https://github.com/italia/anpr/issues/2858](https://github.com/italia/anpr/issues/2858))
    + In alcuni casi particolari poteva venire mostrato uno dei precedenti comuni di residenza del soggetto come responsabile dei dati del cittadino (in particolare se sul comune in questione era attiva la personalizzazione del nome).

### Versione 5.13.11 (2021-09-27)

+ (Bug) WEB - Diacritici sommario richiesta cittadini PDF (issue: [https://github.com/italia/anpr/issues/2828](https://github.com/italia/anpr/issues/2828))
    + Nel PDF di sommari delle richieste dei cittadini, alcuni diacritici potevano non essere visualizzati correttamente.

### Versione 5.14.0 (2021-09-24)

+ (Requirement) Web Service P000 - gestione richieste dei cittadini da Portale ANPR (issue: [https://github.com/italia/anpr/issues/2765](https://github.com/italia/anpr/issues/2765))
    + Cooperazione applicativa con i gestionali comunali per automatizzare la consultazione / cambiamento stati delle richieste inviata dai cittadini

### Versione 5.13.10 (2021-09-16)

+ (Bug) WEB - web: certificati prima in doppia lingua e poi monolingua (issue: [https://github.com/italia/anpr/issues/2814](https://github.com/italia/anpr/issues/2814))
    + Nella produzione del certificato prima bilingue e poi monolingua (tramite la funzione altro certificato) il sistema produceva erroneamente un errore che è stato risolto

+ (Requirement) Certificati in sloveno: sistemare la formattazione
    + Corretta la formattazione del certificato bilingue italiano sloveno relativamente alla sezione indirizzo

### Versione 5.13.9 (2021-09-06)

+ (Requirement) Certificati in sloveno: traduzione del bollo errata
    + E' stato corretto una traduzione relativa al bollo in lingua slovena che ci era stato tradotta erroneamente e modificata la generazione del certificato storico di residenza per casistiche particolari (soggetto presente in ANPR, emigrato in un altro comune, per il quale non è stata fatta una mutazione residenza ma bensi' una cancellazione e una successiva iscrizione).

### Versione 5.13.8 (2021-08-11)

+ (Bug) WEB - Cambio residenza soggetto con parentesi nel luogo eccezionale di nascita
    + La web app di anpr bloccava un cambio residenza in caso di soggetto con luogo eccezionale di nascita con parentesi.

### Versione 5.13.7 (2021-07-08)

+ (Bug) 6001 - certificati in tedesco 
    + E' stato corretto l'errore nella stampa dei certificati in lingua tedesca: la frazione nella colonna tedesca viene riportata in tale lingua

+ (Requirement) Estremi autorizzazione in lingua straniera
    + E' stata aggiunta in stampa e sulla funzione di gestione dati del comune la dicitura relativa agli Estremi dell'autorizzazione rilasciata dall'Agenzia delle Entrate per la riscossione del bollo in modo virtuale,  in duplice lingua

### Versione 5.13.6 (2021-06-28)

+ (Requirement) Visualizzazione richieste cittadino sulla home page
    + In caso non sia ancora pervenuta nessuan richiesta di rettifica da parte dei cittadini, l'applicazione ora veicola tale informazione con un messaggio.

### Versione 5.13.5 (2021-05-26)

+ (Bug) La consultazione potrebbe restituire un codistat comune nascita non congruente
    + In alcuni casi il codistat restituito dalla consultazione non era congruente rispetto alla data di nascita.

### Versione 5.13.4 (2021-05-08)

+ (Requirement) WEB -Flusso gestione richieste cittadini - Nuovo stato irricevibile
    + In caso di richiesta irricevibile l'ufficiale d'anagrafe può ora respingere immediatamente le richieste dei cittadini (per ora attiva solo per i comuni che partecipano alla sperimentazione delle richieste rettifiche dati)

### Versione 5.13.3 (2021-05-04)

+ (Requirement) WEB - Amministrazione comune : Notifica richieste inviate dal cittadino
    + Funzione di trasmissione delle notifiche via PEC e/o PEL delle richieste di rettifica trasmesse dai cittadini, disponibile ai comuni nell’Area Amministrazione.

+ (Bug) WEB - Anomalia salvataggio area amministrazione comune (issue: [https://github.com/italia/anpr/issues/2642](https://github.com/italia/anpr/issues/2642) [https://github.com/italia/anpr/issues/2643](https://github.com/italia/anpr/issues/2643))
    + L'applicazione web di ANPR, andava in errore al momento di salvare le preferenze nell'area Amministrazione - Gestione Dati Comune.

### Versione 5.13.2 (2021-04-26)

+ (Bug) 4001 - Anomalia specie in forniture elenchi cittadini (issue: [https://github.com/italia/anpr/issues/2626](https://github.com/italia/anpr/issues/2626))
    + In caso di specieFonte=1 la specie poteva non essere valorizzata nella risposta del 4001 scaricata dal 7002.

### Versione 5.13.1 (2021-04-22)

+ (Bug) 6001 - Errore Certificato storico di residenza
    + In alcuni casi veniva le residenze storiche potevano essere sbagliate.

### Versione 5.12.12 (2021-04-02)

+ (Bug) WEB - Anomalia richieste consolati per comuni non subentrati
    + Correzione anomalia delle richieste allineamento trasmesse dai consoloati per comuni non subentrati

### Versione 5.12.11 (2021-03-26)

+ (Bug) 6001 certificati on line (issue: [https://github.com/italia/anpr/issues/2545](https://github.com/italia/anpr/issues/2545))
    + Corretto l'errore per cui, impostando nella sezione Amministrazione ->Parametri utilizzati per l'emissione dei certificati online
Spunta su Attiva responsabile certificazione online e impostando nel campo Titolo responsabile certificazione online: L'Ufficiale d'Anagrafe
in stampa viene riportato LUfficale dAnagrafe.

+ (Bug) 6001 - Errore certificato in presenza di isolato
    + In alcuni caso il certificato di residenza poteva andare in errore qualora fosse presente la sezione "isolato".

### Versione 5.12.10 (2021-03-15)

+ (Bug) Visura cittadino - visualizzazione date
    + In alcuni casi le date veniva visualizzate in modo non corretto.

### Versione 5.13.0 (2021-03-01)

+ (Requirement) WEB - RICHIESTE DI RETTIFICA DATI TRASMESSE DAI CITTADINI
    + Nella sezione "utilità e notifiche" sarà disponibile la funziona per gestiore il flusso delle richieste rettifica trasmesse dai cittadini. [non sarà presente in ambiente di presubentro]

### Versione 5.12.9 (2021-02-17)

+ (Requirement) Web: Stampa carta identità cartacea da web app e generazione NRIS con tutti i dati della carta

### Versione 5.12.8 (2021-02-10)

+ (Bug) WEB - Errore Abilitazione ip per utilizzo servizi
    + Le richieste di abilitazione di nuovi IP poteva fallire. (gli ip non abilitati vanno inseriti nuovamente).

### Versione 5.12.7 (2021-02-05)

+ (Bug) WS 5008: corretto l'errore di rettifica dei dati del divorzio con presenza di successiva convivenza (issue: [https://github.com/italia/anpr/issues/2470](https://github.com/italia/anpr/issues/2470) )

### Versione 5.12.6 (2021-01-25)

+ (Requirement) Servizi 4000 Verifica valori tabella di decodifica (issue: [https://github.com/italia/anpr/issues/2447](https://github.com/italia/anpr/issues/2440) [https://github.com/italia/anpr/issues/2440](https://github.com/italia/anpr/issues/2443) [https://github.com/italia/anpr/issues/2447](https://github.com/italia/anpr/issues/2447) [https://github.com/italia/anpr/issues/2448](https://github.com/italia/anpr/issues/2440) )
    + Le operazioni del servizio 4000 non gestivano correttamente alcuni controlli (EC021 / EC025)

### Versione 5.12.5 (2021-01-19)

+ (Requirement) Modifica messaggio diagnostico EN493 (issue: [https://github.com/italia/anpr/issues/1433](https://github.com/italia/anpr/issues/1433) [https://github.com/italia/anpr/issues/1574](https://github.com/italia/anpr/issues/1574) [https://github.com/italia/anpr/issues/2422](https://github.com/italia/anpr/issues/2422) )
    + Il diagnostico EN493 passa da a "L'utente non dispone dei privilegi per eseguire l' operazione @"  "La ricerca non produce risultati o l'utente non dispone dei privilegi per eseguire l' operazione @ sul soggetto/famiglia".

+ (Bug) Prospetto statistico annuale ISTAT: incongruenze su totali ad inizio anno ed iscritti con provenienza da altri comuni
    + Prospetto annuale: rilevate incongruenze sui cittadini ad inizio anno e sulla voce "iscritti con provenienza da altri comuni". 

+ (Bug) WEB - Cambio residenza soggetto proveniente da comune bilingue
    + Per un cambio residenza in ANPR da comune bilingue a comune non bilingue, si attivava il controllo EN504.

### Versione 5.12.4 (2021-01-12)

+ (Requirement) Eliminazione controllo EN222 sul tipo certificato 12 - stato famiglia
    + Il certificato di stato di famiglia viene emesso anche in  caso di incongruenza dei legami di parentela in quanto questi non vengono riportati sul certificato stesso. E' stato quindi eliminato il controllo EN222

### Versione 5.12.3 (2020-12-15)

+ (Bug) 6001 - errore emissione certificato soggetto senza cognome [EN148] (issue: [https://github.com/italia/anpr/issues/2384](https://github.com/italia/anpr/issues/2384))
    + Risolto il bug per cui non era possibile emettere un certificato da Web App per un soggetto senza nom o senza cognome.

+ (Bug) 5008 web: errore in caso di presenza contratto di convivenza
    + In alcuni casi la modifica di un soggetto poteva andare in errore se era presente un contratto di convivenza
   
+ (Bug) WEB - Fix gestione risorse per performance del sistema ANPR (issue: [https://github.com/italia/anpr/issues/2388](https://github.com/italia/anpr/issues/2388))
    + Un errato utilizzo delle risorse dell'applicazione web di ANPR portava ad un utilizzo eccessivo delle risorse, con conseguente decadimento delle prestazioni.

+ (Bug) Anomalia generazione richieste 4001
    + In alcuni casi le richieste 4001 non venivano elaborate correttamente.

### Versione 5.12.2 (2020-12-10)

+ (Requirement) Modifica Data Validità Cittadinanza ITALIA per AIRE da WEB (issue: [https://github.com/italia/anpr/issues/2370](https://github.com/italia/anpr/issues/2370))
    + E' necessario consentire di far modificare la data decorrenza ITALIA per gli AIRE da web eliminando con il bottoncino rosso e poi reinserendo ITALIA con la nuova data. Questo è già possibile per le altre cittadinanze.

+ (Requirement) Preferenze Stampa : Possibilità di personalizzare voce "Comune di ..." relativa alla comune di residenza del soggetto (issue: [https://github.com/italia/anpr/issues/2353](https://github.com/italia/anpr/issues/2353))
    + La funzione si trova si trova nell'area amministrazione - Parametri utilizzati per l'emissione dei certificati (se non impostata nei certificati verrà riportata la dicitura standard "Comune di ..")

### Versione 5.12.1 (2020-12-10)

+ (Requirement) Preferenze Stampa : Possibilità di personalizzare l'intestazione "Comune di ..." relativa al comune di emissione del certificato (issue: [https://github.com/italia/anpr/issues/2353](https://github.com/italia/anpr/issues/2353))
    + La funzione si trova si trova nell'area amministrazione - Parametri utilizzati per l'emissione dei certificati (se non impostata nei certificati verrà riparata la dicitura standard "Comune di ..")
    
### Versione 5.12.0 (2020-12-10)

+ (Requirement) Preferenza Stampa : responsabile comunale emissione certificati online (issue: [https://github.com/italia/anpr/issues/2353](https://github.com/italia/anpr/issues/2353))
    + E' possibile indicare una dicitura diversa rispetto al sindaco quando vengo emessi certificati online. In tal caso il nome e il cognome vengono ricavati automaticamente dall'utente usato per le invocazioni.

### Versione 5.11.11 (2020-11-27)

+ (Bug) Anomalia generazione richiesta 4005 [EN148] (issue: [https://github.com/italia/anpr/issues/2359](https://github.com/italia/anpr/issues/2359))
    + Una anomolia nell'elaborazione delle richieste poteva portare ad un errore EN148 anche quando la richiesta è effettivamente generabile.

### Versione 5.11.10 (2020-11-18)

+ (Bug) Servizi ANPR - Gestione atto di nascita inferiore a 4 cifre
    + Per il servizio 5008 è stato aggiunto il attivato il controllo EHR69 che verifica non vengano inseriti anni atto non validi, come 0008.

+ (Bug) Web - Stampa Visura anagrafica - anomalia decodifica legame di parentela soggetti AIRE (issue: [https://github.com/italia/anpr/issues/2331](https://github.com/italia/anpr/issues/2331))
    + Corretta stampa Visura anagrafica da Web ANPR che riportava una relazione parentela errata per soggetti AIRE.

### Versione 5.11.9 (2020-11-06)

+ (Bug) WS 5008 Attribuzione omocodia
    + E' stato corretto l'errore che consentiva di modificare il codice fiscale impostando il campo gestioneCF = 2 richiesta omocodice. Tale operazione è prevista solo in assenza di codice fiscale

+ (Bug) WEB UPLOAD CONTRATTO CONVIVENZA
    + E' stato corretto l'errore che non consentiva di acquisire il file relativo al contratto di convivenza dall'applicazione Web di ANPR
    
+ (Bug) Modifica controllo EN447
    + E' stato necessario modificare il controllo "la data di decorrenza non è congruente con la data di ingresso in famiglia del soggetto  EN 447" nel caso in cui non cambia l'intestatario (es. il marito) ma si vuole cambiare il legame di uno dei componenti la famiglia (es. da convivente a moglie) ad una data antecedente la data di ingresso dei componenti rimanenti (es. i figli)

### Versione 5.11.8 (2020-10-28)

+ (Requirement) 5014- attivazione diagnostico EN527 per rettifica dati
    + In precedenza il servizio 5014 non forniva infomrazioni diagnostiche da comunicare all'assistenza ANPR in caso di problemi.

### Versione 5.11.7 (2020-10-20)

+ (Bug) WS6001 - CN542 - Errore 99 in assenza del legame di parentela
    + Quando non presente il legame di parentela, in alcune situazione il servizio poteva andare in errore

+ (Bug) Visura anagrafica - Formattazione date permesso di soggiorno (issue: [https://github.com/italia/anpr/issues/2275](https://github.com/italia/anpr/issues/2275))
    + Le date della sezione permesso di soggiorno non vengono formattate correttamente.

### Versione 5.11.6 (2020-09-25)

+ (Bug) WEB - Anomalia controllo diacritici sulla scelta sindaco in amministrazione comune
    + A volte il controllo della ricerca sindaco poteva fallire in presenza di diacritici.

+ (Requirement) Nel blocco dei dati cancellazione della webapp deve essere mostrata anche la decodifica del motivo cancellazione e non solo il codice. Stessa cosa nel riepilogo dei dati finale in fase di cancellazione sempre nella webapp.

### Versione 5.11.5 (2020-09-10)

+ (Bug) WS1002 Errore controllo CN531 in caso di re-iscrizione soggetto AIRE
    + Il servizio di iscrizione poteva andare in errore in caso di reiscrizione di un soggetto che precedentemente era AIRE

### Versione 5.11.4 (2020-08-14)

+ (Bug) WEB - Codice Fiscale non valido per Mutazione Tutti i dati ed Eliminazione codice fiscale non validato.
    + In precedenza un codice fiscale non valido portava al messaggio "Il campo Codice fiscale contiene dei caratteri non validi" senza possibilità di proseguire nella mutazione tutti i dati e nella eliminazione dati - codice fiscale non validato

+ (Bug) WEB - Richieste allineamento dai trasmesse dai consolati
    + Per i comuni non subentrati si presentava un errore nella verifica della validità del codice fiscale.

### Versione 5.11.3 (2020-08-04)

+ (Bug) WEB - Validazione campo protocollo comune
    + L'applicazione web non accetta alcuni valori validi secondo gli xsd per il campo protocollo comune.

+ (Bug) EC056 - Anomalia in caso di alcuni diacritici nel nome comune
    + E' stata corretta la denominazione translitterata di 16 comuni, che portava ad una anomalia anche quando il comune era corretto.
    
+ (Bug) 2011 correzione data definizione pratica nella risposta NRIS
    + La data definizione pratica contenuta nelle NRIS poteva essere errata.
    
+ (Bug) 6001 - Errore in caso di idSchedaSoggettoANPR intestatario con spazi
    + Il servizio poteva non interpretare correttamente spazi prima o dopo  l'idSchedaSoggettoANPR per cui si richiede il certificato
    
### Versione 5.11.2 (2020-07-17)

+ (Bug) 5001 EN469 modifica testo messaggio utente (issue: [https://github.com/italia/anpr/issues/2152](https://github.com/italia/anpr/issues/2152))
    + Il messaggio ora dovrebbe essere maggiormente di aiuto nel capire come procedere in caso di blocco.

### Versione 5.10.7 (2020-07-03)

+ (Bug) Backport patch 5.11.1 in produzione

+ (Requirement) Disponibilità funzione "Richieste di allineamento dati trasmesse dai consolati" ai comuni non subentrati (issue: [https://github.com/italia/anpr/issues/2122](https://github.com/italia/anpr/issues/2122))
    + Viene abilitata la visualizzazione delle funzionalità di utilità e notifiche anche ai comuni non subentrati..

### Versione 5.11.1 (2020-07-01)

+ (Bug) 3002 - Esito ricerca per famiglia a partire da codice fiscale
    + In alcuni casi la ricerca per famiglia a partire dal codice fiscale poteva andare in errore invece di restituire il messaggio che nessuno soggetto è stato trovato.

### Versione 5.11.0 (2020-06-27)

+ (Requirement) A006 - Tabella di decodifica tipo mutazione AIRE (id tabella 50)
    + Censimento tabella dei tipi mutazione AIRE (id 50).

### Versione 5.10.6 (2020-06-22)

+ (Requirement) 4005 - Messaggio fine validità richieste elaborate (issue: [https://github.com/italia/anpr/issues/2122](https://github.com/italia/anpr/issues/2122))
    + Il servizio 4005 ora informa quando è stat superato il termine entro il quale è possibile scaricare la richiesta (non meno di 3 mesi dalla data di produzione).

+ (Bug) WEB - Validazione campo frazione
    + L'applicazione web non accetta alcuni valori validi secondo gli xsd per il campo frazione.

### Versione 5.10.5 (2020-06-19)

+ (Bug) 7001 - Correzione tabella 2 stati esteri
    + Il record con id 197 non compariva nello scarico. Inoltre il layout delle colonne è stato riportato a quello precedente alla patch 5.10.3

### Versione 5.10.4 (2020-06-17)

+ (Bug) WEB - Iscrizione per altri motivi di altro soggetto in elenco esteso operazioni
    + A volte nell'elenco operazioni esteso della web app o del 3003/3007 potevano comparire iscrizioni nella stessa famiglia del soggetto.

### Versione 5.10.3 (2020-06-16)

+ (Bug) WEB Errata visualizzazione documenti storici - Permesso di soggiorno (issue: [https://github.com/italia/anpr/issues/2103](https://github.com/italia/anpr/issues/2103))
    + Corretta visualizzazione di Documenti storici con annualità diversa e medesima numerazione.

+ (Bug) 7001 - Disallineamento servizio scarico tabella decodifica 2 stati esteri
    + L'elenco degli stato esteri (tabella 2) restituito dal servizio 7001 non conteneva alcuni record presenti nella tabella ufficiale pubblicata.

### Versione 5.10.2 (2020-06-10)

+ (Bug) WEB - Caricamento file AIRE subentro
    + In alcuni casi particolari la validazione del file AIRE restituiva un errore di fine riga errato.

### Versione 5.10.1 (2020-06-04)

+ (Requirement) Integrazione patch 5.9.3 / 5.94 su ramo 5.10

### Versione 5.9.4 (2020-06-04)

+ (Requirement) Rimozione controllo EN494 acquisizione specie altre lingue
    + Nell'acquisizione dell'indirizzo in altre lingue non è più obbligatorio in nessun caso acquisire la specie. (in seguito alle verifiche effettuate con i comuni bilingue tedesco)

### Versione 5.9.3 (2020-06-01)

+ (Requirement) Estrazione elenco esteso - aggiunta ultimo annullamento mutazione famiglia
    + A volte l'ultimo annullamento effettuato su una operazione riguardante la famiglia del soggetto poteva non comparire.

### Versione 5.10.0 (2020-05-28)

+ (Requirement) 6001 - rimozione controllo EN181 per certificato residenza e stato di famiglia (issue: [https://github.com/italia/anpr/issues/1937](https://github.com/italia/anpr/issues/1937))
    + Il controllo EN181 scatta se viene richiesto qualsiasi certificato quando è presente un procedimento aperto. Tale controllo deve essere eliminato se vengono richiesti i certificati di residenza, residenza AIRE e stato di famiglia.

### Versione 5.9.2 (2020-05-28)

+ (Bug) 6001 - WEB - Elenco operazioni soggetto - Non compare la risposta
    + Al posto della risposta può comparire la richiesta nella funzione  Consultazione Soggetto - Elenco operazioni

### Versione 5.9.1 (2020-05-21)

+ (Requirement) WS 5013 REVOCA DATO - ELIMINAZIONE TUTORE e CF
    + Nel WS 5013 sono stati implementati il tipo 9 - tutore e 12 - codice fiscale non validato. L'eliminazione dei dati è possibile con le stesse regole applicate per paternità e maternità, quindi non solo a valle del subentro.

+ (Bug) WSDL - eliminazione restrizione tipoDataAnagrafica
    + La validazione di molte data è stata resa più stringente e questo poteva causare problemi a chi usava il vecchio formato per la data decorrenza della testata. Solo per la data decorrenza in testata siamo tornati al tipo xs:date.

### Versione 5.9.0 (2020-05-14)

+ (Requirement) WS [3003/3007] - estensione elenco operazioni soggetto
    + Nel WS 3003/3007 viene data la possibilità tramite apposito parametro di includere nell'elenco operazioni anche quelle che riguardano esclusivamente i dati della scheda famiglia (es. motivo costituzione, id famiglia attribuito dal comune). Tali operazioni, non visualizzate nella lista nella versione precedente, possono essere bloccanti ai fini degli annullamenti.

+ (Requirement) Web - arricchimento informazioni elenco operazioni
    + E' stato aggiunto un tooltip con informazioni aggiuntive sulle singole operazione nell'elenco operazioni della consultazione.

### Versione 5.8.2 (2020-05-08)

+ (Bug) Subentro - Validazione "CODICE ISCRIZIONE AIRE" e fornitura AIRE
    + Analogamente a quanto avviene per i soggetti APR, nel subentro non verranno più accettati id comunali del soggetto con spazi in mezzo.

### Versione 5.8.1 (2020-04-29)

+ (Bug) Integrazione version 5.7.2 su verione 5.8.1

+ (Bug) Validazione codice fiscale AIRE in subentro
    + La validazione del codice fiscale nella fornitura AIRE del subentro va resa simile a quella dei soggetti APR (in particolare non verrà più accettato lo spazio nel codice fiscale).

### Versione 5.7.2 (2020-04-28)

+ (Bug) 3002 - Anomalia ricerca per carta di identità (issue: [https://github.com/italia/anpr/issues/1818](https://github.com/italia/anpr/issues/1818))
    + Quando veniva effettuata una ricerca per cartà identità indicando contemporaneamente il nome e cognome, non veniva valutato il filtro sulla carta di identità.
    
+ (Bug) ws 5005: Ripristino indirizzo ante subentro per più soggetti (codice mut.6): errore bloccante EN415 (issue: [https://github.com/italia/anpr/issues/1810](https://github.com/italia/anpr/issues/1810))
    + Casistica simile a quella della issue #976 per il ws 5001.

+ (Bug) [1001] ES043 in iscrizione per nascita (issue: [https://github.com/italia/anpr/issues/2045](https://github.com/italia/anpr/issues/2045))
    + Ora i controlli ES043 ed ES042 accennano senzacognome.
 
+ (Bug) Web - Errore salvataggio dati carta identità in iscrizione AIRE per altri motivi
    + Da webapp non era possibile salvare la carta di identità nella sezione documenti del cittadino, a causa di una anomalia della validazione.
    
+ (Bug) Web - Errore annullamento certificati cumulativi
    + Se da web app si provava ad annullare un certificato cumulativo cercandolo per nome e cognome del soggetto l'applicazione andava in errore.   

+ (Bug) WEB - Lunghezza Massima numero carta di identità da 9 a 20
    + La lunghezza massima numero carta di identità viene portata da 9 a 20 caratteri.

+ (Bug) Web - Data di scadenza massima carta identita' 2020
    + La da di scadenza massima per la carta di identità era limitata a 2020 da interfaccia di selezione (date picker). Era comunque possibile impostare date superiori digitandolo direttamente nel box dell'anno.

+ (Bug) 5013 - Revoca dati in assenza di id soggetto anpr
    + La revoca dati falliva se tra le generalità per ricerca non era indicato l'idsoggetto anpr.

+ (Bug) ws 4005 - errore 99 quando viene verificato lo stato di una operazione inesistente
    + Il servizio 4005 generava un errore sulla verifica stato di una richiesta inesistente. Ora viene restituito un errore EN122.

### Versione 5.8.0 (2020-04-23)

+ (Requirement) 7002 - Ora viene restituito un diagnostico separato se la richiesta è ancora da elaborare (issue: [https://github.com/italia/anpr/issues/1706](https://github.com/italia/anpr/issues/1706))
    + In precedenza il 7002 restituiva l'esito EN122 (nessun risultato trovato) anche se la richiesta era ancora in elaborazione. Ora viene restituito anche un apposito diagnostico se la richiesta è ancora in elaborazione.

+ (Requirement) Web - Estensione elenco operazioni soggetto (issue: [https://github.com/italia/anpr/issues/1074](https://github.com/italia/anpr/issues/1074))
    + Nell'applicazione web vengono incluse nell'elenco operazioni anche quelle che riguardano esclusivamente i dati della scheda famiglia (es. motivo costituzione, id famiglia attribuito dal comune). Tali operazioni, non visualizzate nella lista nella versione precedente, possono essere bloccanti ai fini degli annullamenti.

### Versione 5.7.1 (2020-04-22)

+ (Requirement) CN531 - Integrazione messaggio di errore (issue: [https://github.com/italia/anpr/issues/1917](https://github.com/italia/anpr/issues/1917))
    + Nel messaggio di errore del controllo EN531 devono restituiti sia la denominazione del comune che ha lasciato  
il procedimento aperto che il numero di tale procedimento. 

+ (Requirement) Visualizzazione stato/territorio provenienza in casi di rimpatrio da AIRE (issue: [https://github.com/italia/anpr/issues/1222](https://github.com/italia/anpr/issues/1222))
    + Nei casi di rimpatrio di un cittadino AIRE, nell'oggetto provenienza non verrà più visualizzato il comune di iscrizione AIRE ma lo stato/territorio di provenienza
    
+ (Requirement) Visualizzazione stato/territorio provenienza in casi di rimpatrio da AIRE (issue: [https://github.com/italia/anpr/issues/1222](https://github.com/italia/anpr/issues/1222))
    + Nel caso di comuni non più esistenti (es. TRESIGALLO), per il luogo di nascita del coniuge scattava il controllo EC152 (bloccante) al posto di EC155 (warning).

+ (Bug) EC175 - Cancellazione per emigrazione in territorio (es. ARUBA) (issue: [https://github.com/italia/anpr/issues/1843](https://github.com/italia/anpr/issues/1843))
    + Il Controllo EC175, che verifica che lo stato estero presente nell'oggetto provenienza/destinazione sia presente tra gli stati asteri, deve accettare anche i territori (2003)

### Versione 5.7.0 (2020-03-31)

+ (Requirement) Fine supporto servizio richiesta paternità maternità 3001
    + Con il rilascio della versione ANPR03 di ANPR, questo servizio sarà supportato solo per i 3 mesi di supporto alla precedente versione.

+ (Requirement) 5014 - Estensione risposta NRIS servizio di rettifica
    + Vengono aggiunte le sezioni previste dagli XSD per la risposta al fine di fornire nelle NRIS le informazioni sul soggetto modificato.

+ (Bug) Patch scarico massivo comune in ambiente di test / presubentro
    + In ambiente di test / presubentro le richieste massive di scarico comune potevano fallire.

+ (Bug) 6001 - Certificato storico di residenza per soggetto cancellato nello stesso comune
    + Se il soggetto viene cancellato e poi reiscritto nello stesso comune, può risultare impossibile emettere lo storico di residenza. 

### Versione 5.6.16 (2020-03-26)

+ (Requirement) Ottimizzazione elaborazione richieste 4005
    + Serie di interventi per rendere più veloce l'elaborazione delle richieste asincrone 4005.

+ (Bug) Web - Mutazione famiglia convivenza - campo isolato
    + Il campo isolato da web consente di inserire solo 10 caratteri mentre da servizio è possibile inserirne fino a 20. Deve essere ampliato il campo

### Versione 5.6.15 (2020-02-20)

+ (Requirement) Stampa da web app prospetti annuali
    + Il ws 4003 prevede l'inserimento di una richiesta  produzione di prospetti di supporto alle elaborazioni statistiche di tipo mensile o annuale. La richiesta viene elaborata in modalità asincrona, il risultato è una risposta di tipo XML di cui è possibile effettuare il download.  Dalla web app è possibile richiedere sia l'elaborazione che la stampa. La funzionalità di stampa è integrata solo per i prospetti mensili. E' necessario integrare le stampe dei prospetti annuali.

+ (Bug) Verifica congruenza tipo operazione da annullare
    + Non sempre veniva verificata la congruenza tra il tipo dichiarato e il tipo reale dell'operazione che si sta tentando di annullare (in particolare in caso si provi ad annullare un subentro, la qual cosa non è permessa, il sistema poteva andare in errore)

### Versione 5.6.14 (2020-02-16)

+ (Bug) Web - Lughezza massima 80 caratteri noteCancellazione
    + La webapp non controllava correttamente la lunghezza massima di 80 caratteri del campo note cancellazione.

+ (Bug) Soggetto registrato con stato nascita non valido
    + In caso sia stato registrato un soggetto con stato di nascita non valido per la nascita (ES codiceStato 508, BERMUDA) la mutazione AIRE poteva fallire.
    
+ (Bug) Gestione date limite cambio ora legale anomale
    + In alcuni anni passati, il cambio ora legale non seguiva regole precise ( vedi http://toi.inrim.it/it/ienitlt.html ). In alcuni casi, a seconda del comportamento del gestionale comunale, tali date limite possono non venire interpretate correttamente (es. 1979-05-27+02:00).
    
+ (Bug) Web - Mutazione famiglia convivenza - campo isolato
    + Il campo isolato da web consente di inserire solo 10 caratteri mentre da servizio è possibile inserirne fino a 20. Deve essere ampliato il campo

### Versione 5.6.13 (2020-02-11)

+ (Bug) Errore caricamento elenco province relative all'atto di Unione Civile (issue: [https://github.com/italia/anpr/issues/1928](https://github.com/italia/anpr/issues/1928))
    + Se la data formazione atto viene inserita direttamente, invece di usare il calendario, viene caricato un elenco province errato (ad esempio compare Littoria al posto di Latina).
    
+ (Bug) Servizio 6001 - Bug certificati cumulativi di contratto di convivenza (issue: [https://github.com/italia/anpr/issues/1934](https://github.com/italia/anpr/issues/1924))
    + Il certificato cumulativo di contratto di convivenza non reperisce correttamente i dati del convivente.

### Versione 5.6.12 (2020-01-31)

+ (Requirement) Gestione del cambio di residenza tra diversi Comuni: controllo bloccante per procedimenti aperti (issue: [https://github.com/italia/anpr/issues/1910](https://github.com/italia/anpr/issues/1910)[https://github.com/italia/anpr/issues/1193](https://github.com/italia/anpr/issues/1193))
    + Nel caso in cui a carico del cittadino esiste un procedimento non concluso la mutazione di residenza (sia di un singolo cittadino che della famiglia) è inibita.    

+ (Requirement) Escludere operazioni di sistema dallo scarico operazioni (issue: [https://github.com/italia/anpr/issues/1907](https://github.com/italia/anpr/issues/1907))
    + Alcune operazioni di sistema di ANPR (come la 8046) venivano riportate nello scarico operazione 4005. Tali operazioni sono state rimosse perchè non di interesse del gestionale. 

+ (Bug) Gestione rettifica data decorrenza residenza (issue: [https://github.com/italia/anpr/issues/1893](https://github.com/italia/anpr/issues/1893))
    + A volte la rettifica (5014) della data decorrenza residenza poteva rendere non consultabile la posizione di un soggetto prima della data decorrenza operazione.

### Versione 5.6.11 (2020-01-15)

+ (Bug) Web - Decodifica posizione professionale A e B (issue: [https://github.com/italia/anpr/issues/1882](https://github.com/italia/anpr/issues/1882))
    + La consultazione non decodificava posizione professionale A e B.

### Versione 5.6.10 (2019-12-20)

+ (Bug) Validazione date con spazi del tracciato AIRE subentro
    + Ora viene verificato che nelle date del tracciato AIRE non siano presenti spazi.

+ (Bug) Servizio 6001 - certificati residenza AIRE - stampa duplicata indirizzoi  (issue: [https://github.com/italia/anpr/issues/1828](https://github.com/italia/anpr/issues/1828))
    + Nei certificati residenza AIRE quando è presente il territorio viene stampata 2 volte la residenza che a volte non è l'attuale.

### Versione 5.6.9 (2019-11-28)

+ (Requirement) Controllo sulle date con anno superiore a 4 cifre
    + E' stato attivato un controllo sugli XSD dei servizi affinchè non vengano accettate date con anno superiore alle 4 cifre. (il controllo è stato già attivato al momento del subentro e a breve sarà propagato anche ai servizi)..

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

