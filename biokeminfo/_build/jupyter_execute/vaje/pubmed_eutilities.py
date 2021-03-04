# DEMO: Programski dostop do PubMed 

Na primeru si bomo ogledali, kako iščemo pu zbirki PubMed prek programskega dostopa.

## BioPython
Uporabili bomo [**BioPython**](https://biopython.org), ki vsebuje orodja za delo z bio-podatki (zaporedja, strukture ipd.); podrobnejša navodila najdete na njegovi domači strani, še posebej uporabna je "kuharica" [Biopython Tutorial and Cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html), kjer najdete različne primere uporabe z razlagami (težava je le v tem, da nekateri primeri iz kuharice ne delujejo, saj niso bili posodobljeni glede na novo verzijo BioPythona). To ne bo edina uporaba BioPythona - uporabljali ga bomo namreč tudi pri drugih vajah.

Del BioPythona, ki nam omogoča iskanje zbirkah na strežnikih NCBI, med drugim PubMed, se imenuje **Bio.Entrez**, zanj je v okviru BioPython na voljo [dokumentacija](https://biopython.org/docs/1.75/api/Bio.Entrez.html).

### Modul Bio.Entrez

Modul Bio.Entrez nudi več funkcij, nekaj jih je navedenih tukaj (ostale so opisane v dokumentaciji):
* `esearch` (Entrez Search) - z njim iščemo po zbirki/zbirkah, vrne nam pa primarne ključe za dostop (ID), ki se jih nato uporabi za prenos posmeznih zapisov z npr. `efetch`;
* `efetch` (Entrez Fetch) - zapise (kot vhod podamo ključe ID) prenesemo v zahtevanem formatu;
* `esummary` (Entrez Summary) - za zapise (ID) nam prenese njihove kratke opise;
* `read` - analizira rezultate v XML, ki nam jih vrnejo zgoraj navedene funkcije;
* `egquery` - za iskalni pojem nam vrne število zadetkov v posameznih zbirkah, do katerih dostopamo prek Entrez;
* `einfo` - vrne nam imena polij ipd.

Modul Bio.Entrez je dejansko osnovan na API (*application programming interface*) za Entrez, za katerega obstaja uradna dokumentacija na strežnikih NCBI:
* [A General Introduction to the E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25497/),
* [Entrez Programming Utilities Help](https://www.ncbi.nlm.nih.gov/books/NBK25501/).


**Opozorila**:
* Pri programskem dostopu do Entrez se morate identificirati z e-poštnim naslovom (v primerih spodaj, če jih boste poganjali, nastavite vrednost `Entrez.email` na vaš naslov.
* Če boste poizvedbe izvajali z visoko frekvenco (npr. zelo veliko število poizvedb na minuto) vas lahko strežnik začasno blokira. Podobno velja za visoko frekvenco poizvedb s prenosom velike količine podatkov (npr. velikega števila celotnih zapisov).

---
## Zgledi

V nadaljevanju je prikazano nekaj zgledov, ki demonstrirajo poizvedovanje s programskih dostopom do Entrez.

### Seznam zbirk

Najprej si oglejmo, katere podatkovne zbirke so nam na voljo prek tega vmesnika. 

from Bio import Entrez
Entrez.email = 'sem.napisite.vas@e-postni.naslov'   # identificiramo se!
handle = Entrez.einfo()
record = Entrez.read(handle)
handle.close()
print(record)   # to nam izpiše vrednost, ki je slovar

Vidimo, da je `record` zapisan kot slovar, vrednost ključa `DbList` (Database List, ki je dejansko seznam zbirk) pa dobimo tako:

print(record['DbList'])   # izpiše nam vrednost ključa DbList (Database List)

Na voljo imamo torej zbirko *pubmed* (literaturna zbirka), zbirko aminokislinskih (*protein*) in nukleotidnih zaporedij (*nucleotide*) , struktur (*structure*) itd.

### Iskanje

Na tem mestu se bomo osredotočili na iskanje po zbirku Pubmed, zato bomo vrednost `db` (database) ustrezno nastavili na *pubmed*. Definirati moramo tudi iskalni pojem (v spodnjem primeru `search_term`) - slednjega lahko definiramo kar z navedbo ene ali več besed, s katerimi želimo iskati po PubMedu, lahko pa uporabimo naprednejšo sintakso in sicer na enak način kot prek naprednega spletnega vmesnika za iskanje po tej podatkovni zbirki, kar smo si ogledali [pri prejšnji vaji](pubmed_web.md). Če si želimo kompleksnejšo poizvedbo, si celoten iskalni pojem najenostavneje zgradimo tako, da gremo na [Pubmed Advanced Search Builder](https://pubmed.ncbi.nlm.nih.gov/advanced/), zgradimo iskanje, ter vsebino iskalne škatle (*query box*) skopiramo in prilepimo kot vrednost `search_term`.

Pri iskanju moramo zraven zbirke in iskalnega pojma definirati še *retrieval mode* oz. `retmode` (včasih še *retrieval type* - `rettype`), možne vrednosti so navedene v [pomoči](https://www.ncbi.nlm.nih.gov/books/NBK25499/table/chapter4.T._valid_values_of__retmode_and/).

Spodaj je en tak primer, kjer za iščemo po imenih člankov, zanimajo pa nas samo taki, kjer se v imenu (*Title*) pojavi *coronavirus*, kjerkoli pa mora biti zraven tega še beseda *Tasmania* (iskanje sicer ni oblutljivo na velike in male črke, to pomeni, da ni *case-sensitive*). Kot rezultat dobimo slovar, ki vsebuje število zadetkov (*count*), seznam številk PMID zapisov oz. člankov (*IDList*) in uporabljen iskalni pojem (kot ga interpretira PubMed, vključno z [MeSH](https://www.ncbi.nlm.nih.gov/mesh/)).

# štetje zapisov
# from Bio import Entrez
# Entrez.email = 'sem.napisite.vas@e-postni.naslov' # identificiramo se
search_term = '(coronavirus[Title]) AND Tasmania' # definiramo iskanje
handle = Entrez.esearch(db='pubmed', term=search_term, retmode='xml')
records = Entrez.read(handle)
handle.close()
print(records)

Če nas zanima število zadetkov si lahko to vrednost enostavno izpišemo. Ali koda pravilno deluje lahko preverimo tudi tako, da iskanje izvedemo z uporabo [brskalnika](https://pubmed.ncbi.nlm.nih.gov/?term=%28coronavirus%5BTitle%5D%29+AND+%28Tasmania%5BAbstract%5D%29).

count = int(records['Count']) # pretvorimo Count v celo število
print(count) # izpišemo število zadetkov

### Prenos zapisov

Kot vidimo po zbirki iščemo z uporabo *esearch*, če pa želimo prenesti zapise, pa uporabimo *efetch* in sicer v kombinaciji s seznamom PMID (v *IdList*).

Za primer si oglejmo, kako je sestavljen edem izmed zapisov. Spodnja koda vzame prvo kodo PMID v seznamu *IdList* ter prenese in izpiše vsebino zapisa:

first_record = records['IdList'][0]   # prvi zapis v seznamu
print('Prvi zapis je:' + first_record)   # izpis kode PMID prvega zapisa v seznamu
one_pubmed_entry = Entrez.efetch(db='pubmed', id=first_record, retmode='xml')
single_record = Entrez.read(one_pubmed_entry)
print(single_record)   # izpis zapisa

### Izpis dela zapisa

Vidimo, da je zapis kar ena *solata*, tako da se v njem malce težko znajti. Spodnja koda nam recimo za vsak PMID izpiše povzetek, če je ta na voljo (tu spet vzamemo vse zadetke prejšnjega iskanja), kar je že nekako lepše.

for identifier in records['IdList']:
    pubmed_entry = Entrez.efetch(db='pubmed', id=identifier, retmode='xml')
    result = Entrez.read(pubmed_entry)
    article = result['PubmedArticle'][0]['MedlineCitation']['Article']
    if 'Abstract' in article:
        print(article['Abstract']['AbstractText'][0])

### Shranjevanje rezultatov v CSV

Rezultate lahko shranimo tudi lokalno, na primer v obliki datoteke CSV (*Comma Separated Values*; kratka razlaga je med [drobnarijami](../priloge/drobnarije.md)). Kaj bi pravzaprav počeli z lokalno shranjenimi podatki? Na primer, lahko bi izvajali rudarjenje po tekstu (*text mining*), kjer bi analizirali so-pojavljanje določenih besed (npr. imen proteinov ali genov), so-avtorstva, geografsko porazdelitev raziskav (pri avtorjih je namreč dopisana njihova afiliacija), ... Sicer je za obširnejše analize najbolje prekopirati kar celotno zbirko MEDLINE, a to je že druga zgodba.

Spodnji zgled ilustrira uporabo knjižnice [**Pandas**](https://pandas.pydata.org/) in sicer:
* definira slovar *articles_with_abstracts*,
* za vsako kodo PMID prenese zapis ter ga doda v slovar pod ključem, ki je enak PMID,
* pretvori slovar v *Pandas dataframe*,
* shrani *dataframe* kot datoteko csv.

import pandas as pd
articles_with_abstracts = {}   # ustvarimo slovar

# spodnja koda je podobna kot zgoraj, le da ne izpisuje povzetkov
for identifier in records['IdList']:
    pubmed_entry = Entrez.efetch(db='pubmed', id=identifier, retmode='xml')
    results = Entrez.read(pubmed_entry)
    article = results['PubmedArticle'][0]['MedlineCitation']['Article']
    if 'Abstract' in article:
        articles_with_abstracts[identifier] = article['Abstract']['AbstractText'][0]

# print(articles_with_abstracts)   # to bi nam izpisalo slovar
df = pd.DataFrame(list(articles_with_abstracts.items()), columns=['PMID', 'Abstract'])
print(df)   # izpis dataframe
df.to_csv('izhod/pubmed-search_output.csv')   # shranimo kot datoteko CSV

---
## Dodatne informacije

### Drugi načini programskega dostopa
Iskanje po Pubmed z uporabo BioPython-a je, kot ste videli zgoraj, lahko malce zakomplicirano. Primer poenostavitve interakcije je [PyMed](https://pypi.org/project/pymed/), ki so ga avtorji uporabili za analizo znanstvene literature na temo COVID-19 - članek [COVID-19: A scholarly production dataset report for research analysis](https://doi.org/10.1016/j.dib.2020.106178). Kako so podatke pridobili je dostopno v repozitoriju na GitHub [breno-madruga/dib-covid-datased](https://github.com/breno-madruga/dib-covid-dataset), ki si ga lahko prenesete in ogledate.

Drug tak primer je Entrezpy, ki je opisan v članku [Entrezpy: a Python library to dynamically interact with the NCBI Entrez databases](https://doi.org/10.1093/bioinformatics/btz385). Relevantne povezave [koda v repozitoriju](https://gitlab.com/ncbipy/entrezpy), [dokumentacija](https://entrezpy.readthedocs.io/). 

Zgoraj omenjeni PyMed in Entrezpy sta dosegljiva prek upravljalnika paketov **pip**. Priporočljivo je, da si razne programe, ki jih morda potrebujete samo za test, nameščate v virtualno okolje, kar je na kratko opisano [tukaj](../priloge/python.md).