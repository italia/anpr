Storico residenza alla data 
=========================================================================================

.. WARNING::
	Il documento è da ritenersi in versione beta.
	
Di seguito sono riportati i **controlli e le condizioni sui dati** che inibiscono l'emissione del presente certificato.
	
Certificabilità soggetto
^^^^^^^^^^^^^^^^^^^^^^^^
- Se Soggetto non certificabile



- Se Soggetto non iscrivibile e forzaCertificazione assente o uguale a 0



- Se Soggetto interdetto e forzaCertificazione assente o uguale a 0



- Se Soggetto parz. cert. e forzaCertificazione assente o uguale a 0 

Procedimento amministrativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Se procedimento aperto e forzaCertificazione assente o uguale a 0 

Tipo richiedente PA
^^^^^^^^^^^^^^^^^^^
- Se il richiedente è una PA (tipoRichiedente=3) e estremiDocRiconoscmento assente; in questo campo è obbligatorio indicare gli estremi della richiesta 

Esenzione bolli
^^^^^^^^^^^^^^^
- Se motivo esenzione bollo = 99 - Altro motivo esenzione e Descrizione Esenzione Bollo assente



- Se il campo DescrizioneEsenzioneBollo contiene maggiore di 256 caratteri.



- Se il campo Esenzione diritti diverso da 0 e da 1



- Se motivo esenzione bollo=99 e esenzione diritti = 1 (esente) e il campo importo dei diritti di segreteria > 0



- Se il campo paEstera=2 ( destinazione d'uso = CERTIFICATO RILASCIATO PER PROCEDIMENTI DISCIPLINATI DALLE NORME SULL'IMMIGRAZIONE ) o paEstera=3 (destinazione d'uso = AI SENSI DELL'ART. 40, D.P.R. 445/2000 IL PRESENTE CERTIFICATO E' RILASCIATO PER CAUSE GIUDIZIARIE) ed il certificato non è esente da bollo



- Se l'importo dei diritti segreteria è previsto (certificato non esente) ma è pari a 0 



- Se certificato non esente e importo bollo = 0,00 euro.

 

Combinazioni certificati su cumulativi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Se richiesto con altri certificati (puo' essere richiesto solo singolarmente) 

Controlli soggetto APR/AIRE
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

Soggetto cancellato
^^^^^^^^^^^^^^^^^^^
 

 

Controlli specifici
^^^^^^^^^^^^^^^^^^^
- Se la data di riferimento del certificato è antecedente alla data di prima iscrizione del soggetto;



- Se la data di riferimento del certificato è antecedente alla data di subentro del comune di residenza del soggetto al momento del subentro stesso (prima residenza del soggetto registrata in ANPR);



- Se la data decorrenza della residenza è antecedente alla data di prima iscrizione del soggetto;



- Se la data di riferimento del certificato è antecedente alla data di cancellazione anagrafica o di decesso del soggetto;



- Se la data di decorrenza della residenza è assente. 
