# VAJA: Dostop do GenBank v brskalniku

V Okviru te vaje si bomo ogledali najpogostejši in najenostavnejši način dostopa do podatkov v zbirki GenBank, t.j. dostop z uporabo brskalnika.

Do GenBank dostopamo na naslovu: [https://www.ncbi.nlm.nih.gov/genbank/](https://www.ncbi.nlm.nih.gov/genbank/).

Iskanje lahko zožimo z uporabo kompleksnejših poizvedb (*Advanced search* - napredno iskanje, podobno kot pri PubMed), prav tako pa lahko rezultate filtriramo z uporabo številnih filtrov (spet, podobno kot pri PubMed): vrsta zaporedja (tRNA, mRNA, genomsko zaporedje), organizem, ... Filtri so razporejeni na levi in desni strani rezultatov (v osnovi so vse možnosti filtriranja na levi, na desni pa so nekatere možnosti posebej izpostavljene), kot je prikazano na spodnji zaslonski sliki.

![GenBank iskanje in filtriranje](slike/genbank_web_primer1.png)


---
## Naloga

V zbirki GenBank izvedite iskanja, kjer poiščete spodaj navedene zapise (vsaka točka je ločeno iskanje, rezultat iskanja je zapis v zbirko z določeno kodo za dostop) ter prek pregleda zapisa odgovorite na vprašanja:
* **zaporedje mRNA za mišji lizocim 1**, ki vsebuje celotno kodirajočo regijo
  * vprašanje 1: Iz kolikih eksonov je sestavljen zapis?
  * vprašanje 2: Kateri nukleotid je najpogostejši na koncu 3'-neprevedene regije mRNA? Je to pričakovano?
* **zaporedje mRNA za človeški protein p53** in sicer táko, ki vsebuje celotno kodirajočo regijo v osnovni (nemutirani) obliki - protein p53 ("varuh genoma") oz. gen *TP53* je pri raku eden najpogosteje mutiranih, proteinski namreč produkt kontrolira ključne točke v celičnem ciklu ter preprečuje delitev celic s poškodovanim genomom in ima s tem tumor-supresorsko vlogo, okvarjen protein pa to sposobnost okvarjeno
  * vprašanje 1: Kolikšen delež zaporedja mRNA predstavlja kodirajoče zaporedje?
  * vrpašanje 2: Katera regija je daljša, 5' ali 3'-neprevedena regija? Je to pričakovano?
* **zaporedje mRNA za protein p53 iz katerekoli glive**
  * vprašanje: Koliko ustreznih zapisov je v GenBank?
* **zaporedje alanil-tRNA pri *E. coli***
  * vprašanje 1: Kateri kodon (nukleotidno zaporedje) prepozna tRNA?
  * vprašanje 2: Vsebuje ta tRNA zgolj običajne ribonukleotide?
* **zaporedje kromosoma št. 13 pri ribici zebrici** (iščemo primarni združek (*primary assembly*) zaporedij)
  * vprašanje 1: Kako dolgo je nukleotidno zaporedje tega kromosoma?
  * vprašanje 2: Kakšne lastnosti oz. regije (*features*) so anotirane in kako je to bilo narejeno?
  * vprašanje 3: Kaj menite, da pomeni *unk100* v delu zapisa CONTIG (=soseska)?

**Dodatna vprašanja** (za odgovor se malo razglejte po enem od zapisov v brskalniku):
* Kako pridemo do celotnega nukleotidnega zaporedja nekega zapisa v GenBank v formatu FASTA?
* Kako pridemo do dela nukleotidnega zapisa v formatu FASTA, ki ustreza zgolj regiji CDS?


---
## Dodatna literatura
* kratek video-vodič [How to use GenBank](https://www.youtube.com/watch?v=j7hV10gYz1Q)
* [NCBI Minute: A Beginner's Guide to Genes and Sequences at NCBI](https://www.youtube.com/watch?v=QIZ8QH6JcC8&t=890s) na uradnem YouTube kanalu NCBI
