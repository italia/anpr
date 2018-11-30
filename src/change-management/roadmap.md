# Prossime versioni


# Roadmap

+ (Requirement) Scarico massivo dei dati di un comune
    + Consente di scaricare i dati di un comune da ANPR al solo scopo di utilizzarli nel caso di cambio gestionale comunale. Tale soluzione provvisoria prevede la generazione di una fornitura di tutti i soggetti di un Comune sotto forma di file compresso, che verrà consegnato al Comune tramite PEC.  

+ (Requirement) Web - Amministrazione gestione ip
    + Nel menù Amministrazione - gestione dati comune viene aggiunta la possibilità di inserire, dismettere, riabilitare uno o più indirizzi IP da far abilitare per l'utilizzo dei servizi ANPR

+ (Requirement) Estensione del servizio revoca dato
    + Estensione del servizio revoca dato per i seguenti dati: - Matrimonio / Convivenza / Unione civile - Permesso di soggiorno - Carta di identità - Atto di nascita

+ (Requirement) Accesso tramite CIE/CNS/SPID
    + Accesso all'applicazione InterrogazioneCittadino, per la consultazione dei propri dati, con CNS,CIE e credenziali SPID.

+ (Requirement) Ottimizzazione risposta servizio consultazione 3002
    + In conseguenza della decisione di permettere l'accesso al servizio 3002 anche per i comuni non subentrati e nell'ambito dell'ottimizzazione delle prestazioni rese necessarie dall'aumento del carico si è reso necessario modificare il comportamento del servizio di consultazione soggetto / famiglia / convivenza.
 Con riferimento alle sezioni della risposta de servizio 3002, vedi [tabella decodifica 16](https://www.anpr.interno.it/portale/tabelle-di-riferimento), qualora la ricerca trovi più di un soggetto, verrà restituita solo la sezione generalità (senza tenere conto delle eventuali altre sezioni indicate, compresa la scheda individuale completa). Le ricerche che si traducono in un solo soggetto continuano a comportarsi come prima.
