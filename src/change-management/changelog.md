# Changelog


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
    + Nell'istituzione della Convivenza,  viene rimosso il controllo ES008 che verifica l'uguaglianza tra la data decorrenza dell'operazione  e la data di nascita del responsabile della convivenza

+ (Bug) 6001 richiesta dati, noteIndirizzo vuote (issue: [https://github.com/italia/anpr/issues/924](https://github.com/italia/anpr/issues/924))
    + Quando il campo noteIndirizzo non contiene valori significativi non viene più restituito dal servizio 6001 come già avviene per il servizio 3002.

+ (Bug) Correzione encoding wsdl da distribuire per i comuni (issue: [https://github.com/italia/anpr/issues/807](https://github.com/italia/anpr/issues/807))
    + L'encoding dell tipoDato.xsd non era sempre corretto per gli ultimi diacritici aggiunti.

+ (Bug) Web - Blocco mutazione tutti i dati per validazione data scadenza permesso di soggiorno
    + Alcune date formalmente valide non impedivano (come il 31/12/8999) bloccavano la possibilità di eseguire una mutazione tutti i dati da web.

+ (Requirement) Estensione caratteri amessi per alcuni tipi XSD (slash e cancelletto) (issue: [https://github.com/italia/anpr/issues/902](https://github.com/italia/anpr/issues/902)[https://github.com/italia/anpr/issues/907](https://github.com/italia/anpr/issues/907))
    + Verranno accettati il carattere "/" per l'elemento descrizioneLocalita del tipo Località e il carattere "#" per gli elementi denominazione e numeroCivico del tipoToponimoEstero.

+ (Bug) Ricerca di convivenza senza responsabile nè soggetti restituisce EN122
    + Solo l'applicazione web adesso restituisce un soggetto fittizio con cognome e nome "RESPONSABILE CONVIVENZA ASSENTE" al fine di poter restituire gli altri dati sulla convivenza.

### Versione 4.1.13 (2018-11-08)

+ (Bug) Certificati bug testo normativo sigillo digitale (issue: [https://github.com/italia/anpr/issues/915](https://github.com/italia/anpr/issues/915))
    + Nei certificati in ambiente di produzione per emissione=2 appare il testo normativo previsto per il sigillo digitale che non è ancora previsto.

+ (Requirement) Possibilità di upload file subentro solo con nuove regole in tutti gli ambienti (issue: [https://github.com/italia/anpr/issues/819](https://github.com/italia/anpr/issues/819))
    + In nessun ambiente (in particolare anche produzione) sarà possibile l'upload delle forniture del subentro con le regole precedenti.

+ (Bug) Carattere euro nell'annotazione certificato (issue: [https://github.com/italia/anpr/issues/807](https://github.com/italia/anpr/issues/807))
    + Nelle righe di annotazione dei certificati deve essere permesso anche il carattere euro.

+ (Bug) Web - Ricerca per codice fiscale con omocodia specie 4+
    + Ora la validazione dell'applicazione web per il codice fiscale è allineata a quella dei servizi [lunghezza minima (11), massima (16) e valori che siano lettere minuscole, maiuscole, numeri]


+ (Bug) Controllo presenza dati unione per certificato stato civile
    + In alcuni casi veniva emesso il certificato di unione civile anche in mancanza dei dati.


+ (Requirement) Nuova gestione annullamento carta identità
    + Sul sito web è stata inserita la possibilità di revocare o annullare una carta di identità emessa dal sito web di ANPR o acquisita tramite i servizi di registrazione

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
    + Implementare la consultazione scheda individuale del ws 3002 utilizzando come parametri di ricerca anche  i campi "senzaNome"  o "senzaCognome". 

+ (Bug) Elenco operazioni soggetto: errore reperimento alcune tipologie di rettifica 5014 (issue: [https://github.com/italia/anpr/issues/725](https://github.com/italia/anpr/issues/725))
    + L'elenco delle operazioni comunicate da ANPR per un cittadino non riporta  alcune tipologie di rettifica effettuate con il ws 5014

### Versione 4.1.1 (2018-09-30)

+ (Requirement) Fine validità major version con codDestinatario ANPR00 (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617)[https://github.com/italia/anpr/issues/775](https://github.com/italia/anpr/issues/775)[https://github.com/italia/anpr/issues/819](https://github.com/italia/anpr/issues/819))
    + Implementazione meccanismo per gestione fine validità versioni depcrecate.

### Versione 4.1.0 (2018-09-12)

+ (Requirement) WB 24 Bilinguismo
    + L'intervento prevede la gestione delle informazioni relative agli indirizzi in altre lingue al fine di produrre i certificati per i paesi ove vige il bilinguismo. 

+ (Requirement) WB 30 Stampa scheda dati individuale
    + I comuni hanno segnalato la necessità di poter stampare i dati parziali di una persona presente in Anpr. Oltre alla visura completa, già disponibile, viene richiesto quindi di produrre una stampa delle schede individuali limitata ai dati di interesse specifico. Gli interventi riguardano solo il sito web di Anpr e sono descritti nel documento MI-04-AN-13. 

### Versione 4.0.27 (2018-09-28)

+ (Bug) Web - Validazione numero sentenza mutazione tutti i dati
    + Le regole di validazione del campo numero sentenza non erano allineate nell'applicazione web.

### Versione 4.0.26 (2018-09-13)

+ (Bug) Restrizioni XSD per ANPR01 (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617))
    + Corrette regole validazione xsd per alcuni tipoQuesturaRilascio, tipoDenominazioneToponimoTranslitterato e tipoDescrizioneLocalitaTranslitterata

### Versione 4.0.25 (2018-09-11)

+ (Bug) Web - Caricamento provincia littoria / latina
    + L'applicazione web, in alcuni menu a tendina, presentava il comune di Littori al posto di Latina.

+ (Bug) procedura di elaborazione prospetto riepilogativo mensile:  ricalcolo valori aggregati
    + Revisione elaborazione dati del prospetto riepilogativo mensile, con particolare riferimento al calcolo della popolazione residente al 1 del mese che sarà ricalcolato partendo dai dati presenti sul DB  e non dal saldo del prospetto precedente.  

### Versione 4.0.24 (2018-09-07)

+ (Bug) Validazione web denominazione comune
    + Errore nella validazione del nome comune nell'applicazione web.

+ (Bug) Il tipo dato xsd siglaProvincia deve accettare solo valori di lunghezza 2
    + Venivano accettati valori anche di un carattere perl a sigla provincia.

+ (Bug) Controllo presenza codice specie se specie fonte vale 1
    + Modificato il controllo ES023 per verificare sempre la presenza del codice specie quando specie fonte è 1.

### Versione 4.0.23 (2018-09-04)

+ (Bug) WA: selezione comune per creazione richiesta elenchi e prospetti
    + Creazione richiesta xml per elenchi e prospetti: la ricerca non può essere pilotata solo con il codice ISTAT di un  comune perchè potrebbe lo stesso codice può essere appartenuto ad altro comune cessato. 

+ (Bug) ws 3007: gestione della casistica di assenza di notifiche nel periodo di riferimento  (issue: [https://github.com/italia/anpr/issues/758](https://github.com/italia/anpr/issues/758))
    + WS 3007 -  richiesta elenco notifiche riferite ad un determinato arco temporale: in assenza di occorrenze di interesse restituisce le altre tipologie di eventi comunicati nel periodo

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
    + Nelle pagine di ricerca per CF e risoluzione disallineamenti viene restituito un errore in caso di CF con doppia omocodia es BLDMMD88A0MZ34A deve essere rimosso tale controllo

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
    + Il pattern accettato per il campo tipoRigaAnnotazione passa da ([0-9À-ža-zA-Z\- &apos;/.,])* a ([0-9À-ža-zA-Z\- &apos;/.,()])*.

+ (Bug) Modifica visualizzazione monitoraggio operazioni
    + Corretto il reperimento del valore riportato nella colonna "Data di elaborazione dell'operazione"

+ (Bug) Regole validazione file aire subentro
    + La data di iscrizione AIRE diventa abbligatoria nel file AIRE.

### Versione 4.0.14 (2018-07-03)

+ (Bug) Web - Validazione denominazione convivenza
    + La denominazione della convivenza nel web non usava le stesse regole di validazione dei servizi.

+ (Bug) Gestione encoding diacritici certificati (issue: [https://github.com/italia/anpr/issues/744](https://github.com/italia/anpr/issues/744))
    + Alcuni diacritici non venivano trattati correttamente nel PDF dei certificati (6001)

+ (Bug) Web - residenti temporanei: gestione soggetti cancellati da ANPR 
    +  Sito web di ANPR -  residenti temporanei: gestione soggetti cancellati da ANPR

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
    + Mancata  visualizzazione del TAB residenza se l'origine dell'indirizzo è una revisione dell'onomastica comunale o una rettifica post accertamenti, nei servizi di mutazione ed iscrizione.

### Versione 4.0.9 (2018-06-11)

+ (Bug) Blocco upload file subentro
    + Il modulo di upload dei file del subentro ora blocca l'invio se il comune non è inserito correttamente nel piano dei subentri. (in precedenza il messaggio aveva solo valore di avviso).

+ (Bug) Modifica controllo di congruenza date in inserimento matrimonio/legame e convivenza (issue: [https://github.com/italia/anpr/issues/705](https://github.com/italia/anpr/issues/705))
    + Modifica controllo di congruenza date per consentire la chiusura di una convivenza di fatto nella stessa data della stipula di un matrimonio/legame

### Versione 4.0.8 (2018-06-07)

+ (Bug) Bug controllo certificati APR su stato civile Divorziato (issue: [https://github.com/italia/anpr/issues/692](https://github.com/italia/anpr/issues/692))
    + E' necessario permettere la produzione di certificato non solo se ci sia l'atto di annullamento ma in alternativa la sentenza di fine matrimonio.

+ (Bug) WS 5008 - controllo comune di nascita
    + Nel WS 5008 il controllo di validità comune di nascita CN332 deve scattare solo se sono cambiati i dati anagrafici. Per verificare se è variato il luogo di nascita utilizzare denominazione e provincia

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
    + Viene resa più rigorosa la verifica dei campi a testo libero. Tale restrizione è applicata solo indicando la versione ANPR01 nel tag codDestinatario della richiesta

+ (Requirement) WB 5 - Gestione cod destinatario per versione (issue: [https://github.com/italia/anpr/issues/617](https://github.com/italia/anpr/issues/617))
    + Nel campo codDestinatario viene indicata la versione dei tracciati XSD: ANPR00 è la versione di partenza (fino alla release 3.x) ANPR01 dalla release 4.0

+ (Requirement) WB 29 - Mutazione dati del decesso (issue: [https://github.com/italia/anpr/issues/510](https://github.com/italia/anpr/issues/510))
    + Nuova mutazione con codice  22 per il servizio 5008.

+ (Requirement) WB 25 Rettifica indirizzo post accertamenti  (issue: [https://github.com/italia/anpr/issues/508](https://github.com/italia/anpr/issues/508))
    + ws 5001: gestione del nuovo codice mutazione 8 che identifica una rettifica indirizzo  emersa in fase di accertamenti  legati ad una richiesta di cambio residenza. 

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
    + In Amministrazione nella funzione di Gestione dati del comune, nella ricerca dati del sindaco è stato modificato il controllo sul comune di nascita quando sono presenti caratteri speciali .

### Versione 3.7.0 (2018-05-18)

+ (Requirement) WB 14.1 GESTIONE DATA DECORRENZA LEGAME E RETTIFICA ALTRE DATE
    + L'intervento include: la gestione data decorrenza legame nei servizi subentro (S001) di registrazione (ws 1001, 1002, 5001, 5005, A001, A002, A006, 2001, 2003) e consultazione (ws 3002)  oltre che da web In particolare nel tracciato di subentro e nel tracciato del servizio 3002 è stata aggiunta  la data di decorrenza legame la rettifica delle seguenti date da ws 5014 e da web: Data ultimo aggiornamento scheda Data di iscrizione nel comune Data di ingresso nella famiglia

+ (Requirement) WB 15 Inserimento Comune o Stato Estero di Provenienza in A002
    + L'intervento prevede l'indicazione del comune o dello stato estero di provenienza nel servizio di iscrizione AIRE sia per il WS A002 che nella funzione accessibile da Web Nel tracciato del servizio A002 è stato aggiunto l'oggetto non obbligatorio relativo alla "Provenienza"

+ (Requirement) Semplificazione protocollo di sicurezza per inoltro notifiche verso gli endpoint dei Comuni
    + Eliminazione della Mutual Authentication che costringeva ad esporre un endpoint del Comune con il relativo certificato Server. Utilizzo del protocollo TLS sbilanciato, per permettere l'esposizione dell'endpoint con un certificato emesso da una CA pubblica. La riservatezza delle informazioni è garantita dalla crittografia del contenuto della notifica con la chiave pubblica del certificato assegnato ad ogni Comune (CO-9999).

+ (Requirement) WB 10 Integrazione  ws 5008 per completamento dati da subentro di un soggetto AIRE (cod. mutazione = 21)
    + Per la gestione del completamento dati da subentro di un soggetto AIRE si introduce nel ws 5008 “Mutazione tutti i dati”  e nella funzionalità web il  nuovo codice mutazione 21  (Dati integrativi AIRE). Il tracciato del servizio rimane immutato

