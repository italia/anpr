	QUESTO DOCUMENTO É UNA BOZZA DI LAVORO

# Procedura 001 - Errore nel CF

> ritorna [*README*](../README.md) o [*Tabella anomalie ANPR*](../TAB01_ANOMALIE_ANPR.md)

In quanto segue si riporta la procedura suggerita ai Comuni per la gestione delle anomalie: 

- EA001 - *codice fiscale* lunghezza errata;
- EA029 - *codice fiscale* calcolato dai *dati angrafici* del comune non presente in Anagrafe Tributaria; 
- EA038 - soggetto con data di nascita non coincidente con quella presente nel *codice fiscale*;
- EA042 - soggetto con sesso non coincidente con quella presente nel *codice fiscale*;
- EA048 - *codice fiscale* formalmente errato.




## Precondizione
Per dare seguito alla presente procedura è necessario che l'ufficiale d'anagrafe disponga:

- accesso al sistema gestionale del Comune (APR o AIRE locale) con diritti di lettura e aggiornamento delle schede soggetto;
- accesso al sistema *SIATEL v2.0 - PuntoFisco* reso disponibile dall'Agenzia delle Entrate. 

## Diagramma della procedura
La seguente figura sintetizza la procedura per la gestione delle anomalie.

![Swimlane diagram procedura 001](image/IMAGE_001.png)

## Descrizione azione
In quanto segue si riporta una descrizione delle azioni previsti per la presente procedura.

### AZIONE 001_001 - VERIFICA
L'ufficiale d'anagrafe verifica i dati anagrafici associati al soggetto interessato dall'errore sul sistema gestionale del Comune (APR o AIRE locale) con l'obiettivo di constatare che i dati inoltrati al sistema ANPR coincidono con quelli registrati. **Si evidenzia che l'ufficiale di anagrafe provvede anche al riscontro che i dati registrati nell'APR o AIRE locali corrispondano con i dati registrati allo stato civile**

### AZIONE 001_002 - NUOVO INOLTRO
Poichè i dati inoltrati al sistema ANPR non coincidono con quelli presenti nel sistema gestionale del Comune (probabilemente per problemi nella procedura di estrazione e predisposizione dei file di subentro utilizzata) è necessario provvedere nuovamente all'estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire l'inoltro al sistema ANPR.

### AZIONE 001_003 - VERIFICA AT
L'ufficiale di anagrafe, tramite il sistema *SIATEL v2.0 - PuntoFisco* reso disponibile dall'Agenzia delle entrate, ricerca il soggetto nell'Anagrafe Tributaria e verifica il CF ad esso assegnato. Nel dettaglio attraverso le informazioni anagrafiche in suo possesso nome, cognome, sesso, luogo e data di nascita verifica se sull'Anagrafe Tributaria risulta soggetto ed in caso positivo prende nota del codice fiscale attribuito ad esso.

### AZIONE 001_004 - AGGIORNAMENTO CF E NUOVO INOLTRO
L'ufficiale di anagrafe, a valle del positivo riscontro con l'Agenzia delle entrate, provvede ad aggiornare il *codice fiscale* sul sistema gestionale del Comune per dare seguito ad una nuova estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire nuovamente l'inoltro al sistema ANPR.

### AZIONE 001_005 - CONVOCAZIONE CITTADINO
L'ufficiale di anagrafe convoca il cittadino per verificare se lo stesso è in grado di attestare il *codice fiscale* ad esso attribuito dall'Agenzia delle entrate, ad esempio verificando la tessera sanitaria in suo possesso.

### AZIONE 001_006 - AGGIORNAMENTO CF E NUOVO INOLTRO
L'ufficiale di anagrafe, a valle del positivo riscontro con il cittadino, provvede ad aggiornare il *codice fiscale* sul sistema gestionale del Comune per dare seguito ad una nuova estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire nuovamente l'inoltro al sistema ANPR.

### AZIONE 001_007 - CANCELLAZIONE CF E NUOVO INOLTRO
L'ufficiale di anagrafe, non avendo la possibilità di riscontrate il *codice fiscale* provvede alla cancellazione dei dati sul sistema gestionale del Comune per dare seguito ad una nuova estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire nuovamente l'inoltro al sistema ANPR.

## Riferimenti di interesse
Nello specifico della presente procedure risultano di interesse:

- [regole di codifica](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Home/CosaDeviFare/Richiedere/Codice+fiscale+e+tessera+sanitaria/Richiesta+TS_CF/SchedaI/Informazioni+codificazione+pf/) codice fiscale;


> ritorna [*README*](../README.md) o [*Tabella anomalie ANPR*](../TAB01_ANOMALIE_ANPR.md)
