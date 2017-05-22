	QUESTO DOCUMENTO É UNA BOZZA DI LAVORO

# Procedura 009 - Errori di quadratura

> ritorna [*README*](../README.md) o [*Tabella anomalie ANPR*](../TAB01_ANOMALIE_ANPR.md)

In quanto segue si riporta la procedura suggerita ai Comuni per la gestione delle anomalie: 

- EN011 - Totale schede soggetto dichiarato nel file incongruente con quello calcolato;
- EN012 - Totale schede soggetto dichiarato per l'intera fornitura incongruente con quello calcolato;
- EN017 - Totale persone di sesso femminile dichiarato nel file incongruente con quello calcolato;
- EN018 - Totale persone di sesso femminile dichiarato per l'intera fornitura incongruente con quello calcolato;
- EN019 - Totale persone di sesso maschile dichiarato nel file incongruente con quello calcolato;
- EN020 - Totale persone di sesso maschile dichiarato per l'intera fornitura incongruente con quello calcolato;
- EN021 - Totale schede famiglia dichiarato nel file incongruente con quello calcolato;
- EN022 - Totale schede famiglia dichiarato per l'intera fornitura incongruente con quello calcolato;
- EN023 - Totale schede convivenza dichiarato nel file incongruente con quello calcolato;
- EN024 - Totale schede convivenza dichiarato per l'intera fornitura incongruente con quello calcolato.


## Precondizione
Nessuna precondizione.


## Diagramma della procedura
La seguente figura sintetizza la procedura per la gestione delle anomalie.

![Swimlane diagram procedura 009](image/IMAGE_009.png)

## Descrizione azione
In quanto segue si riporta una descrizione delle azioni previsti per la presente procedura.

### AZIONE 009_001 - VERIFICA
L'ufficiale d'anagrafe verifica i dati relativi alla scheda soggetto/famiglia/convivenza sul sistema gestionale del Comune (APR o AIRE locale) con l'obiettivo di constatare che i dati inoltrati al sistema ANPR coincidono con quelli registrati.

### AZIONE 009_002 – NUOVO INOLTRO
Poichè i dati inoltrati al sistema ANPR non coincidono con quelli presenti nel sistema gestionale del Comune (probabilemente per problemi nella procedura di estrazione e predisposizione dei file di subentro utilizzata) è necessario provvedere nuovamente all'estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire l'inoltro al sistema ANPR.

### AZIONE 009_003 – DETERMINA LE CAUSE
L'ufficiale di anagrafe determina le cause che hanno determinato l'errore di squadratura evidenziato evidenziando le schede soggetto/famiglia/convivenza mancanti e/o inserite in maniera erronea al fine di assicurare la corrisponedenza tra la numerosità dichiarata e quelle inoltrate nel/nei file di subentro. 

### AZIONE 009_004 - AGGIORNAMENTO E NUOVO INOLTRO
L'ufficiale di anagrafe, a valle del consolidamento effettuato, provvede ad una nuova estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire l'inoltro al sistema ANPR.


> ritorna [*README*](../README.md) o [*Tabella anomalie ANPR*](../TAB01_ANOMALIE_ANPR.md)
