
![ANPR](src/_images/anpr.png)

Di seguito vengono elencati alcuni link che possono essere di aiuto nella ricerca di issue all'interno di github.


In generale trovate la documentazione a questo URL:

https://help.github.com/articles/searching-issues-and-pull-requests/

![Issue list](/img/search-issue.png)
Come puoi vedere il campo query ha possibilità di esprimere alcune restrizioni secondo un linguaggio ed una sintassi specifica.

**Di seguito alcune query di esempio:**

Issue non commentate affatto
https://github.com/italia/anpr/issues?utf8=✓&q=is:issue is:open comments:0

Issue che sono state commentate da un da un utente
[q=is:issue is:open commenter:gcarbonin](https://github.com/italia/anpr/issues?utf8=✓&q=is:issue%20is:open%20commenter:gcarbonin)

Issue non commentate che NON appartengono ad alcune categorie (-label)
[q=is:issue is:open comments:0 -label:chiarimento-normativo -label:"help wanted"](https://github.com/italia/anpr/issues?utf8=%E2%9C%93&q=is:issue%20is:open%20comments:0%20-label:chiarimento-normativo%20-label:%22help%20wanted%22)

Issue che contengono una qualche stringa nel titolo
[&q=is:issue is:open “registrazione” in:title](https://github.com/italia/anpr/issues?utf8=%E2%9C%93&q=is:issue%20is:open%20%E2%80%9Cregistrazione%E2%80%9D%20in:title)

Issue che sono state modificate ad una data specifica
(_il formato data é il seguente updated:YYYY-MM-DD_)
[q=is:issue is:open updated:2017-09-26](https://github.com/italia/anpr/issues?utf8=%E2%9C%93&q=is:issue%20is:open%20updated:2017-09-26)


Issue che sono state modificate negli ultimi gionri
[https://github.com/italia/anpr/issues?utf8=✓&q=is:issue is:open updated:>=2013-02-01](https://github.com/italia/anpr/issues?utf8=%E2%9C%93&q=is:issue%20is:open%20updated:%3E=2013-02-01)
