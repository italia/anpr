Procedura 010. Inoltro file di subentro disabilitato
=====================================================

In quanto segue si riporta la procedura suggerita ai Comuni per la gestione delle anomalie: 

- EN003 - Lo stato del subentro attuale @ non consente l'invio del file
- EN032 - La data di invio del file @ deve essere compresa tra la data di inizio e la data fine subentro pianificate
- EN034 - Impossibile inviare altri file per un comune già subentrato
- EN037 - Esiste già una precedente fornitura di file attualmente in elaborazione
- EN040 - Esiste già una fornitura con progressivo @ in stato OK
- EN041 - Piano di subentro già presente per il comune
- EN362 - Prima di effettuare l'invio, occorre indicare l'indirizzo di PEC cui recapitare l'esito (funzione Amministrazione)


Precondizione
^^^^^^^^^^^^^
Creazione dei file che contengono i dati APR e AIRE, nel rispetto delle `modalità definite <https://www.anpr.interno.it/portale/documents/20182/23925/Invio+file+di+Subentro.pdf/e0c98d8d-363a-4ca3-adcf-3e9613632be4>`_ per il sistema ANPR. In merito si evidenzia che il pacchetto per la creazione del file AIRE è scaricabile dall'ambiente di test-comuni nella sezione strumenti di supporto. Si ricorda che in caso di mancato invio di uno dei due file, l'elaborazione di subentro non si avvia


Diagramma della procedura
^^^^^^^^^^^^^^^^^^^^^^^^^
La seguente figura sintetizza la procedura per la gestione delle anomalie.

.. image:: image/IMAGE_010.png

Descrizione azione
^^^^^^^^^^^^^^^^^^
In quanto segue si riporta una descrizione delle azioni previsti per la presente procedura.

AZIONE 010_001 - CONTATTA CALL CENTER
-------------------------------------
L'ufficiale d'anagrafe contatta il call center ANPR per avere riscontro sulle cause che impediscono l'inoltro dei file di subentro.

AZIONE 010_002 – NESSUNA ATTIVITA'
----------------------------------
Nel caso in cui non sia possibile riabilitare l'inoltro dei file di subentro da parte del Comune nessuna attività deve essere realizzata dall'ufficiale di anagrafe.

AZIONE 010_003 – NUOVO INOLTRO
------------------------------
L'ufficiale di anagrafe provvedere nuovamente all'inoltro al sistema ANPR nel rispetto delle procedure previste. 
