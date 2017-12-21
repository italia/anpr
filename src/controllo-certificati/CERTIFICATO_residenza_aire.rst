Residenza AIRE 
=========================================================================================

Di seguito sono riportati i **controlli e le condizioni sui dati** che inibiscono l'emissione del presente certificato.
	
Certificabilità soggetto
^^^^^^^^^^^^^^^^^^^^^^^^
- Se Soggetto non certificabile



- Se Soggetto non iscrivibile e forzaCertificazione assente o uguale a 0



- Se Soggetto interdetto e forzaCertificazione assente o uguale a 0



- Se Soggetto parzialmente certificabile e forzaCertificazione assente o uguale a 0

 

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



- Se il campo paEstera=2 (destinazione d'uso = CERTIFICATO RILASCIATO PER PROCEDIMENTI DISCIPLINATI DALLE NORME SULL'IMMIGRAZIONE) o paEstera=3 (destinazione d'uso = AI SENSI DELL'ART. 40, D.P.R. 445/2000 IL PRESENTE CERTIFICATO E' RILASCIATO PER CAUSE GIUDIZIARIE) e il certificato non è esente da bollo



- Se l'importo dei diritti segreteria è previsto (certificato non esente) ma è pari a 0 



- Se certificato non esente e importo bollo = 0,00 euro.

 

Combinazioni certificati su cumulativi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Se richiesto con certificati previsti solo per i residenti 

Controlli soggetto APR/AIRE
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Se richiesto per soggetti residenti 

Soggetto cancellato
^^^^^^^^^^^^^^^^^^^
- Se richiesto per un soggetto cancellato anagraficamente 

- Se il soggetto è cancellato per decesso 

Controlli specifici
^^^^^^^^^^^^^^^^^^^
 
