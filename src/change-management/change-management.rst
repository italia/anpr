Change management
-----------------

Premessa
~~~~~~~~

Il documento descrive le convenzioni di base utilizzate ogni qualvolta
sia necessario apportare modifiche software ad ANPR.

Le convenzioni che si adottano tengono conto della necessità di:

-  comunicare con il minimo sforzo la risoluzione di problemi e
   l'introduzione di nuove funzionalità tra comuni, software house, e
   SOGEI;

-  coordinare con il minimo sforzo il test di nuove versioni di ANPR tra
   comuni, software house, e SOGEI;

-  garantire la compatibilità delle nuove versioni di ANPR con quelle
   precedenti per un periodo di tempo necessario per l'adeguamento dei
   software anagrafici.

Per far fronte a queste necessità il processo di change management
introduce:

-  una codifica delle versioni di ANPR che esprime l'entità dei
   cambiamenti introdotti in una nuova versione di ANPR;

-  una metodologia di aggiornamento del software graduale che consente
   di testare i software anagrafici con le nuove versioni di ANPR e di
   adeguare i medesimi software all'evoluzione dei contratti WSDL;

-  meccanismi per descrivere in modo succinto e rendere facilmente
   consultabili sia i cambiamenti introdotti in una nuova versione di
   ANPR che i cambiamenti pianificati in future versioni di ANPR.

Codifica delle versioni
~~~~~~~~~~~~~~~~~~~~~~~

Rappresentare l'entità dei cambiamenti attraverso una codifica delle
versioni permette di comunicare in modo semplice la natura dei
cambiamenti contenuti in una nuova versione di ANPR.

La codifica delle versioni segue il `Versionamento
Semantico <http://semver.org/lang/it/>`__. Ogni versione di ANPR viene
rappresentata da tre valori progressivi:

**MAJOR.MINOR.PATCH** (esempio: 2.1.10)

La semantica di questa codifica è la seguente:

1. Un numero di versione normale DEVE essere nella forma X.Y.Z, dove X,
   Y, e Z sono interi non negativi, e NON DEVONO contenere zeri
   iniziali. X è la versione major, Y è la versione minor, e Z è la
   versione patch. Ogni elemento DEVE incrementare come numero a sé. Per
   esempio: 1.9.0 -> 1.10.0 -> 1.11.0.

2. Una volta che un pacchetto versionato è stato rilasciato, i contenuti
   di quella versione NON DEVONO essere modificati. Qualsiasi modifica
   DEVE essere rilasciata come una nuova versione.

3. La versione Patch Z (x.y.Z \| x > 0) DEVE essere incrementata solo se
   sono introdotte correzioni retrocompatibili di bug. Una correzione di
   un bug è definita come una modifica interna che corregge un
   comportamento errato.

4. La versione Minor Y (x.Y.z \| x > 0) DEVE essere incrementata se
   nell'API pubblica è introdotta una nuova funzionalità
   retrocompatibile. Essa DEVE essere incrementata se qualsiasi
   funzionalità dell'API pubblica è marcata come deprecata. Essa DEVE
   essere incrementata se sono introdotti all'interno del codice privato
   nuove funzionalità o miglioramenti sostanziali. Essa PUÒ includere
   modifiche di livello patch. La versione Patch DEVE essere reimpostata
   a 0 quando la versione Minor è incrementata. Esempio: La versione
   Minor viene incrementata quando si ha una nuova versione del WSDL,
   retrocompatibile con la versione precedente, che aggiunge dei campi
   opzionali, modifiche ai controlli, ulteriori metodi, o nuovi end
   point.

5. La versione Major X (X.y.z \| X > 0) DEVE essere incrementata se
   nell'API pubblica è introdotta qualsiasi modifica non
   retrocompatibile. Essa PUÒ includere modifiche di livello minor e
   patch. Le versioni patch e minor DEVONO essere reimpostate a 0 quando
   la versione major è incrementata.

6. Una versione di pre-rilascio PUÒ essere indicata aggiungendo
   immediatamente dopo la versione patch un trattino e una serie di
   identificatori separati dal punto. Gli identificatori DEVONO essere
   composti solo da alfanumerici ASCII e trattini [0-9A-Za-z-]. Gli
   identificatori NON DEVONO essere vuoti. Gli identificatori numerici
   NON DEVONO includere zeri iniziali. Le versioni di pre-rilascio hanno
   una precedenza inferiore rispetto alla versione normale associata.
   Una versione di pre-rilascio indica che la versione è instabile e
   potrebbe non soddisfare i requisiti di compatibilità intesi come
   indicato dalla versione normale ad essa associata. Esempi:
   1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92.

7. Metadati di build POSSONO essere indicati aggiungendo immediatamente
   dopo la versione patch o pre-rilascio un segno di addizione e una
   serie di identificatori separati dal punto. Gli identificatori DEVONO
   essere composti solo da alfanumerici ASCII e trattini [0-9A-Za-z-].
   Gli identificatori NON DEVONO essere vuoti. I metadati di build
   dovrebbero essere ignorati nella determinazione della precedenza
   delle versione. Perciò due versioni che differiscono solo per i
   metadati di build, hanno la stessa precedenza. Esempi:
   1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85.

8. La precedenza si riferisce a come le versioni sono confrontate l'una
   con l'altra quando poste in relazione d'ordine. La precedenza DEVE
   essere calcolata separando gli identificatori nell'ordine seguente:
   major, minor, patch e pre-release (i metadati di build non compaiono
   nella precedenza). La precedenza è determinata dalla prima
   discrepanza quando si confrontano ognuno di tali identificatori da
   sinistra a destra come segue: le versioni major, minor e patch sono
   sempre confrontate numericamente. Esempio: 1.0.0 < 2.0.0 < 2.1.0 <
   2.1.1. Quando major, minor, e patch sono uguali, una versione di
   pre-rilascio ha una precedenza inferiore rispetto alla versione
   normale. Esempio: 1.0.0-alpha < 1.0.0. La precedenza per due versioni
   di pre-rilascio con la stessa versione major, minor, e patch DEVE
   essere determinata confrontando ognuno degli identificatori separati
   dal punto da sinistra a destra finché si trova una discrepanza come
   segue: gli identificatori costituiti da sole cifre sono confrontati
   numericamente e gli identificatori con lettere o trattini sono
   confrontati lessicalmente secondo l'ordinamento ASCII. Gli
   identificatori numerici hanno sempre una precedenza più bassa
   rispetto agli identificatori non numerici. Un insieme più grande di
   identificatori ha una precedenza superiore rispetto a un insieme più
   piccolo, se tutti quanti i precedenti identificatori sono uguali.
   Esempio: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta
   < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0.

Classificazione delle modifiche
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La codifica delle versioni appena introdotta si basa sul saper
discernere quali cambiamenti all'API pubblica del servizio devono
considerarsi MINOR (cambiamenti retrocompatibili) e quali MAJOR
(cambiamenti non-retrocompatibili).

Viene qui presentata una classificazione delle modifiche più comuni al
WSDL di un generico servizio, indicando il tipo di cambiamento da esse
introdotto. La classificazione è tratta da `Web Service Contract Design
and Versioning for SOA di Thomas Erl et
al <http://dl.acm.org/citation.cfm?id=1468069>`__.

Cambiamenti retrocompatibili:

-  aggiungere una nuova operazione WSDL ed i relativi messaggi

-  aggiungere un nuovo tipo di porta WSDL e le relative operazioni

-  aggiungere un nuovo binding e definizione di servizio WSDL

-  aggiungere un nuovo elemento/attributo opzionale allo schema XML di
   un messaggio

-  ridurre la constraint granularity di un elemento/attributo dello
   schema XML di un messaggio

-  aggiungere una nuova wildcard allo schema XML di un messaggio

Cambiamenti non-retrocompatibili:

-  cambiare nome a un'operazione WSDL esistente

-  rimuovere un'operazione WSDL esistente

-  aggiungere un fault message a un'operazione WSDL esistente

-  aggiungere un nuovo elemento/attributo non opzionale allo schema XML
   di un messaggio

-  aumentare la constraint granularity di un elemento/attributo dello
   schema XML di un messaggio

-  cambiare nome a un elemento/attributo (opzionale o non) dello schema
   XML di un messaggio

-  rimuovere un elemento/attributo (opzionale o non) o una wildcard
   dallo schema XML di un messaggio

Metodologia di aggiornamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La metodologia di aggiornamento consente di adeguare i client di ANPR
alle nuove versioni senza interruzione di servizio.

La metodologia di aggiornamento:

-  adotta una strategia per introdurre cambiamenti non-retrocompatibili
   (rilascio nuova versione MAJOR),

-  stabilisce come i software anagrafici possano continuare ad operare
   durante l'introduzione di cambiamenti non-retrocompatibili,

-  adotta un processo di testing del software anagrafico con le nuove
   versioni di ANPR prima che le nuove versioni raggiungano l'ambiente
   di produzione.

Ogni qual volta sia necessario rilasciare una nuova versione MAJOR che
introduce cambiamenti non-retrocompatibili, il servizio deve garantire
la compatibilità con la versione MAJOR precedente per almeno 90 giorni
dalla messa in produzione.

A tal fine, nella parte comune a tutti i messaggi (``testataRichiesta``)
si utilizza l'attributo ``codDestinatario`` che identifica
l'applicazione di riferimento cioè quale versione MAJOR supporta il sw
anagrafico. Questo attributo è già obbligatorio e attualmente contiene
il valore "ANPR00"; tale valore verrà impostato ad “ANPR01” al rilascio
della prima MAJOR version e sarà progressivamente incrementato in
corrispondenza di un rilascio di una MAJOR version successiva.
L'attributo della versione viene controllato prima della validazione di
tutto il resto del messaggio per permettere ad ANPR di validare il
messaggio stesso con il WSDL più opportuno.

Ogni qual volta verrà rilasciata una nuova versione MAJOR, le versioni
MAJOR precedenti non vedranno ulteriori aggiornamenti MINOR e PATCH .

Per minimizzare le interruzioni di servizio è fondamentale testare i
software anagrafici con le nuove versioni di ANPR. Il rilascio di ogni
nuova versione di ANPR avviene in modo graduale per consentire di
effettuare test di integrazione con i software anagrafici e di riportare
problemi:

-  Una nuova versione di ANPR viene rilasciata inizialmente solo negli
   ambienti di test e pre-subentro, dove vi rimane per almeno 15 giorni.

-  Trascorsi i 15 giorni, se non vi sono segnalazioni aperte che
   riportino gravi problemi, la versione viene promossa alla fase di
   collaudo del Ministero e quindi in produzione.

Descrizione della versione
~~~~~~~~~~~~~~~~~~~~~~~~~~

Per garantire compatibilità durante l'aggiornamento è necessario avere
una descrizione puntuale della versione corrente di ANPR, accessibile in
modo programmatico.

A tal proposito è possibile utilizzare il servizio ``Status`` per:

-  richiedere la versione corrente dell'istanza di ANPR utilizzata
   chiamando il metodo ``GetVersion``. Questo metodo ritorna la versione
   completa (major, minor, patch).

-  richiedere tutte le versioni major supportate chiamando il metodo
   ``GetSupportedVersions`` .

I WSDL di quella versione saranno disponibili su GitHub all'indirizzo
https://github.com/italia/anpr/wsdl/ oppure su
https://www.anpr.interno.it/portale/documentazione-tecnica.

È inoltre possibile consultare l'elenco delle versioni supportate in
tutti gli ambienti nella seguente pagina: https://docs.anpr.it/status
(Nota: La pagina al momento è accessibile poiché il processo di change
management è in fase di implementazione).

Nota: Nel caso della web application, si assume che sia associata a una
specifica versione delle API dei webservices di backend, e verrà
indicato chiaramente nel footer la versione (in ambiente test e test
comuni anche con un link al changelog).

Storico delle versioni
~~~~~~~~~~~~~~~~~~~~~~

Lo storico delle versioni permette di rendere facilmente consultabili i
cambiamenti introdotti da una nuova versione di ANPR. Lo storico delle
versioni viene implementato tramite `ChangeLog <changelog>`__ : un file
di testo contenente un sommario dei cambiamenti presenti in ogni
versione di ANPR.

È possibile consultare lo storico delle versioni all'indirizzo:
https://docs.anpr.it/changelog (Nota: La pagina al momento è accessibile
poiché il processo di change management è in fase di implementazione.)

Al rilascio di una nuova versione lo storico dei cambiamenti della
versione stessa verrà anche pubblicato nella newsletter (nome newsletter
ancora da definire).

Il ChangeLog viene aggiornato ogni qual volta si rilascia una nuova
versione di ANPR. Il file è diviso in varie sezioni, una sezione per
versione, e le sezioni seguono un ordine cronologico inverso per
facilitare la lettura dei cambiamenti più recenti.

Ogni sezione del ChangeLog deve contenere:

-  La versione di ANPR a cui si riferisce

-  La data di rilascio

-  Una lista dei cambiamenti più importanti contenuti nella versione.

Se la nuova versione contiene un cambiamento relativo a una issue
segnalata nell'issue tracker, l'url della issue deve essere incluso nel
sommario.

Esempio di ChangeLog ANPR:

::

    # Versione 3.0.0 (data: 2017-06-30)

    - Rimosso metodo1234. Bisogna usare metodo3456 ora (issue:
      https://github.com/italia/anpr/issues/YYY)

    # Versione 2.2.0 (data: 2017-03-10)

    - Aggiunto metodo3456 per supportare casodusoW. Questo metodo sostituisce il
      metodo1234 che verrà rimosso nella nuova major release (issue:
      https://github.com/italia/anpr/issues/YYY)

    # Versione 2.1.10 (data: 2017-01-20)

    - Rimossa condizione di errore quando si effettua operazioneZ (issue:
      https://github.com/italia/anpr/issues/XXX)

    - Ridotta complessità computazionale nella chiamata al metodoX

    - Refactoring del moduloY

Cambiamenti Pianificati
~~~~~~~~~~~~~~~~~~~~~~~

In modo analogo allo storico delle versioni, è possibile consultare
anche un file di testo contenente i cambiamenti pianificati (Roadmap).
Per cambiamento pianificato si intende qualsiasi intervento (1)
cambiamento behavior sostanziale (major/minor) e/o (2) bugfix che
richiedono lunghi tempi per essere sistemati.

È possibile consultare i cambiamenti pianificati all'indirizzo:
`roadmap <roadmap>`__

Lo scopo della Roadmap è duplice: da un lato permette di facilitare la
comunicazione su quando verranno introdotte nuove funzionalità, da un
altro lato facilita la stesura del file di ChangeLog al momento del
rilascio di una nuova versione di ANPR.

Anche il file di Roadmap è diviso in varie sezioni. Ogni sezione
corrisponde ad una potenziale nuova versione di ANPR, e le sezioni
seguono un ordine cronologico inverso per facilitare la lettura dei
cambiamenti più recenti.

Ogni sezione della Roadmap è strutturata come il ChangeLog, con l'unica
differenza che non è obbligatorio specificare il numero di versione.

La Roadmap è particolarmente importante per comunicare quando verranno
risolte le issue segnalate nell'issue tracker, quindi anche il sommario
della roadmap dovrà includere l'url della issue segnalata.

Esempio di Roadmap ANPR:

::

    # Versione ?.?.? (data stimata: 2019-12-31)

    - Rimozione metodoABCD e metodoEFGH (issue:
      https://github.com/italia/anpr/issues/AAA)

    # Versione 3.?.? (data stimata: 2018-12-31)

    - Aggiunta metodoXYZ per supportare casoduso123 (issue:
      https://github.com/italia/anpr/issues/YYY)

    # Versione 3.2.? (data stimata: 2018-09-30)

    - Rimossa condizione di errore quando si effettua operazioneY (issue:
      https://github.com/italia/anpr/issues/CCC)
