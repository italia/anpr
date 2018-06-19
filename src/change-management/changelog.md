# Changelog

### Versione 3.7.0 (2018-05-18)

+ (Requirement) WB 14.1 GESTIONE DATA DECORRENZA LEGAME E RETTIFICA ALTRE DATE
    + L'intervento include: la gestione data decorrenza legame nei servizi subentro (S001) di registrazione (ws 1001, 1002, 5001, 5005, A001, A002, A006, 2001, 2003) e consultazione (ws 3002)  oltre che da web In particolare nel tracciato di subentro e nel tracciato del servizio 3002 è stata aggiunta  la data di decorrenza legame la rettifica delle seguenti date da ws 5014 e da web: Data ultimo aggiornamento scheda Data di iscrizione nel comune Data di ingresso nella famiglia

+ (Requirement) WB 15 Inserimento Comune o Stato Estero di Provenienza in A002
    + L'intervento prevede l'indicazione del comune o dello stato estero di provenienza nel servizio di iscrizione AIRE sia per il WS A002 che nella funzione accessibile da Web Nel tracciato del servizio A002 è stato aggiunto l'oggetto non obbligatorio relativo alla "Provenienza"

+ (Requirement) Semplificazione protocollo di sicurezza per inoltro notifiche verso gli endpoint dei Comuni
    + Eliminazione della Mutual Authentication che costringeva ad esporre un endpoint del Comune con il relativo certificato Server. Utilizzo del protocollo TLS sbilanciato, per permettere l'esposizione dell'endpoint con un certificato emesso da una CA pubblica. La riservatezza delle informazioni è garantita dalla crittografia del contenuto della notifica con la chiave pubblica del certificato assegnato ad ogni Comune (CO-9999).


+ (Requirement) WB 10 Integrazione  ws 5008 per completamento dati da subentro di un soggetto AIRE (cod. mutazione = 21)
    + Per la gestione del completamento dati da subentro di un soggetto AIRE si introduce nel ws 5008 “Mutazione tutti i dati”  e nella funzionalità web il  nuovo codice mutazione 21  (Dati integrativi AIRE). Il tracciato del servizio rimane immutato

### Versione 3.7.1 (2018-05-23)

+ (Bug) Gestione autorità sentenza (issue: [https://github.com/italia/anpr/issues/680](https://github.com/italia/anpr/issues/680))
    + Nel campo autorità della sentenza sono ora ammesse le parentesi tonde

+ (Bug) Comune residenza sindaco
    + In Amministrazione nella funzione di Gestione dati del comune, nella ricerca dati del sindaco è stato modificato il controllo sul comune di nascita quando sono presenti caratteri speciali .

### Versione 3.7.2 (2018-05-23)

+ (Bug) Webapp Validazione numero sentenza
    + L'applicazione web bloccava il carattere slash nel numero sentenza.

### Versione 3.7.3 (2018-05-28)

+ (Bug) Correzione esito servizio di rettifica (issue: [https://github.com/italia/anpr/issues/690](https://github.com/italia/anpr/issues/690))
    + Il servizio restituiva un esito positivo mentre avrebbe dovuto restituire un errore ES127.


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

### Versione 4.0.1 (2018-05-04)

+ (Bug) Estensione hotfix 3.6.6 sulla versione 4.0.1

### Versione 4.0.2 (2018-05-07)

+ (Bug) Estensione hotfix 3.6.7 sulla versione 4.0.2

### Versione 4.0.3 (2018-05-10)

+ (Bug) Estensione hotfix 3.6.8 sulla versione 4.0.3

### Versione 4.0.4 (2018-05-17)

+ (Bug) Estensione hotfix 3.6.9 sulla versione 4.0.4

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

### Versione 4.0.6 (2018-05-28)

+ (Bug) Modifica regex elemento piano dell'indirizzo (issue: [https://github.com/italia/anpr/issues/676](https://github.com/italia/anpr/issues/676))
    + Estensione valori ammessi per elemento piano. Ora viene accettato anche il trattino.

+ (Bug) Integrazione versioni 3.7.2 / 3.7.3 su versione 4.0.6

### Versione 4.0.7 (2018-06-05)

+ (Bug) Verifica dati soggetto per mutazione
    + Nei servizi di mutazione, c'era un errore nella gestione dei dati del soggetto ricercato quando i dati non sono congruenti (es. viene passato un cognome relativo ad un identificativo soggetto diverso).

+ (Bug) Verifica senza giorno / senza anno in caso di mutazione dati anagrafici
    + La data di nascita non veniva sempre confrontata correttamente in caso di senza giorno / senza giorno mese.

### Versione 4.0.8 (2018-06-07)

+ (Bug) Bug controllo certificati APR su stato civile Divorziato (issue: [https://github.com/italia/anpr/issues/692](https://github.com/italia/anpr/issues/692))
    + E' necessario permettere la produzione di certificato non solo se ci sia l'atto di annullamento ma in alternativa la sentenza di fine matrimonio.

+ (Bug) WS 5008 - controllo comune di nascita
    + Nel WS 5008 il controllo di validità comune di nascita CN332 deve scattare solo se sono cambiati i dati anagrafici. Per verificare se è variato il luogo di nascita utilizzare denominazione e provincia

### Versione 4.0.9 (2018-06-11)

+ (Bug) Blocco upload file subentro
    + Il modulo di upload dei file del subentro ora blocca l'invio se il comune non è inserito correttamente nel piano dei subentri. (in precedenza il messaggio aveva solo valore di avviso).

+ (Bug) Modifica controllo di congruenza date in inserimento matrimonio/legame e convivenza (issue: [https://github.com/italia/anpr/issues/705](https://github.com/italia/anpr/issues/705))
    + Modifica controllo di congruenza date per consentire la chiusura di una convivenza di fatto nella stessa data della stipula di un matrimonio/legame

### Versione 4.0.10 (2018-06-12)

+ (Bug) sito web ANPR: errata gestione tipo indrizzi 10 ed 11
    + Mancata  visualizzazione del TAB residenza se l'origine dell'indirizzo è una revisione dell'onomastica comunale o una rettifica post accertamenti, nei servizi di mutazione ed iscrizione.


