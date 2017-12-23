Procedura 004. Dati obbligatori popolati non correttamente
=================================================================

In quanto segue si riporta la procedura suggerita ai Comuni per la gestione delle anomalie: 

- EHR41 - I campi comune rilascio carta di identità @ e  codice consolato rilascio @ devono essere valorizzati in alternativa
- EN306 - Presenza del coniuge e assenza del matrimonio
- ES027 - La descrizione della località è obbligatoria per la residenza estera
- ES028 - Per la residenza estera deve essere presente almeno uno tra i seguenti campi: indirizzo, presso, contea-provincia, CAP
- ES048 - Occorre impostare in alternativa  il comune o la località estera del matrimonio
- ES049 - Indicare almeno il cognome o il nome del soggetto
- ES050 - Occorre impostare in alternativa codice  comune ISTAT  o stato estero di nascita
- ES057 - Specificare in alternativa che il soggetto è senza cognome o senza nome
- ES061 - Il cognome deve essere assente se il campo SenzaCognome è impostato
- ES062 - Il nome deve essere assente se il campo SenzaNome è impostato
- ES067 - Occorre impostare in alternativa il  comune o la località estera di decesso del coniuge
- ES092	- Soggetto senza scheda famiglia/convivenza associata
- EN383 - Presenza dei dati della parte unita civilmente (o convivente)  e assenza dei dati relativi alla unione civile (o convivenza di fatto)

Precondizione
^^^^^^^^^^^^^
Per dare seguito alla presente procedura è necessario che l'ufficiale d'anagrafe disponga dell'accesso al sistema gestionale del Comune (APR o AIRE locale) con diritti di lettura e aggiornamento delle schede soggetto/famiglia/convivenza.

Diagramma della procedura
^^^^^^^^^^^^^^^^^^^^^^^^^
La seguente figura sintetizza la procedura per la gestione delle anomalie.

.. image:: image/IMAGE_004.png

Descrizione azione
^^^^^^^^^^^^^^^^^^
In quanto segue si riporta una descrizione delle azioni previsti per la presente procedura.

AZIONE 004_001 - VERIFICA
-------------------------
L'ufficiale d'anagrafe verifica i dati anagrafici associati al soggetto interessato dall'errore sul sistema gestionale del Comune (APR o AIRE locale) con l'obiettivo di constatare che i dati inoltrati al sistema ANPR coincidono con quelli registrati.

AZIONE 004_002 – NUOVO INOLTRO
------------------------------
Poiché i dati inoltrati al sistema ANPR non coincidono con quelli presenti nel sistema gestionale del Comune (probabilmente per problemi nella procedura di estrazione e predisposizione dei file di subentro utilizzata) è necessario provvedere nuovamente all'estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire l'inoltro al sistema ANPR.

AZIONE 004_003 – RECUPERO DATI MANCANTI
---------------------------------------
Ove possibile, l'ufficiale di anagrafe provvede a recuperare i dati mancanti e/o a eliminare i dati che risultano erroneamente popolati, se necessario anche attraverso il riscontro con gli atti di stato civile, al fine di assicurare la completezza delle informazioni per la scheda soggetto interessato dall'anomalia, in particolare per quelle anomalie che si consiglia di rimuovere prima del subentro.  Successivamente provvede ad aggiungere i dati sull'APR o AIRE locale per dare seguito ad una nuova estrazione dei dati e alla predisposizione dei file di subentro al fine di provvedere ad eseguire l'inoltro al sistema ANPR. 
