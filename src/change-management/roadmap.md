# Prossime versioni

NOTA : Le date riportate si riferiscono alla previsione orientativa di disponibilità in produzione.

### Versione 5.1-RC (2019-02-07)

+ (Requirement) Superamento vincoli annullamento (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + E' stato reso possibile effettuare annullamenti per ripristino posizione anagrafica anche se la mutazione di residenza non è l’ultima operazione effettuata sul soggetto (ma non vi siano altre mutazioni di residenza) Sono stati eliminati i vincoli sugli annullamenti impediti da operazioni su soggetti collegati (es. coniugi o legami parentela)

+ (Requirement) Sezione famiglia risposta 3002 (solo ANPR02) (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Solo nella interrogazione per famiglia/convivenza con codDestintario ANPR02 viene restituito un blocco esplicito opzionale della famiglia. [Presentazione Major Versione 5](https://github.com/italia/anpr/files/2831691/PresentazioneSH_15_01_2019.pptx)

+ (Requirement) Avvisi nella risposta del 3002 (solo ANPR02) (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Solo in caso di chamata con codDestintario ANPR02 viene aggiunta una sezione di anomalie anche in caso di risposta OK del servizio 3002. [Presentazione Major Versione 5](https://github.com/italia/anpr/files/2831691/PresentazioneSH_15_01_2019.pptx)

+ (Requirement) Scarico massivo dei dati di un comune (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Consente di scaricare i dati di un comune da ANPR al solo scopo di utilizzarli nel caso di cambio gestionale comunale. Tale soluzione provvisoria prevede la generazione di una fornitura di tutti i soggetti di un Comune sotto forma di file compresso, che verrà consegnato al Comune tramite PEC.  

+ (Requirement) Web - Amministrazione gestione ip (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Nel menù Amministrazione - gestione dati comune aggiunta la possibilità di inserire, dismettere, riabilitare uno o più indirizzi IP da far abilitare per l'utilizzo dei servizi ANPR

+ (Requirement) Estensione del servizio revoca dato (issue: [https://github.com/italia/anpr/issues/1077](https://github.com/italia/anpr/issues/1077))
    + Estensione del servizio revoca dato per i seguenti dati: - Matrimonio / Convivenza / Unione civile - Permesso di soggiorno - Carta di identità - Atto di nascita

### Versione 5.2-RC (2019-02-28)

+ (Requirement) Presentazione dettaglio soggetto nella consultazione della webapp (issue: [https://github.com/italia/anpr/issues/1031](https://github.com/italia/anpr/issues/1031))
    + A fronte del nuovo prospetto sintetico della consultazione, sarà possibile accedere anche al dettaglio completo.

+ (Requirement) Revisione risposte servizi di registrazione (solo ANPR02)
    + Anche la risposta dei servizi di registrazione diventa sintetica. Vale a dire che invece di tutti i dati dei soggetti variati, vengono fornite solo la sintesi del risultato e gli eventuali dati generati da ANPR (idanpr, codice fiscale ecc). [Presentazione Major Versione 5](https://github.com/italia/anpr/files/2831691/PresentazioneSH_15_01_2019.pptx)

### Versione 5.3-RC (2019-03-14)

+ (Requirement) Refactor servizio di consultazione/estrazione
    + I servizi 3003 e 3007 vengono spostati nella famiglia 4000. Il servizio 3005 nella famiglia 7000. [Presentazione Major Versione 5](https://github.com/italia/anpr/files/2831691/PresentazioneSH_15_01_2019.pptx)

# Roadmap

+ (Requirement) Accesso tramite CIE/CNS/SPID
    + Accesso all'applicazione InterrogazioneCittadino, per la consultazione dei propri dati, con CNS,CIE e credenziali SPID.

