# VAJA: Programski dostop do GenBank (Python)

Tudi pri tej vaji bomo, podobno kot pri dostopu do PubMeda, uporabljali [BioPython](https://biopython.org). Navodila z zgledi so na voljo v [BioPython Tutorial and Cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html).

Najprej si oglejte in preizkusite delovanje delov kode v zgledih, nato pa z ustrezno kombinacijo nekaterih delov kode iz zgledov ter prilagoditvijo kode rešite nalogo na dnu zvezka.

---
## Zgledi

### Dostop do GenBank

Dostop do GenBank je mogoč direktno z uporabo modulov v **BioPython**, podobno kot to velja za PubMed (modul Bio.Entrez, ki smo ga spoznali [tukaj](pubmed_eutilities.ipynb)). Tudi tokrat se moramo za uporabo E-utilities identificirati z e-poštnim naslovom. Če *accession code* poznamo, lahko uporabimo funkcijo `efetch`, sicer pa izvedemo iskanje z `esearch` in šele nato prenesemo zapis(e) z `efetch`, v obeh primerih pa rezultate preberemo z `read`.

Pa kar gremo k primeru, ki ilustrira branje enega zapisa - tako torej dostopamo do zapisa, če poznamo **kodo za dostop** (*accession code*). Če ne napišemo verzije zapisa nam vrne zadnjo (najnovejšo) verzijo, sicer pa lahko verzijo sami določimo tako, da *accession code* napišemo v obliki NM_005985.4 (če je osnovna koda NM_005985).

Kot zbirko (`db`) izberemo *nucleotide*, podatke pa prenesemo v obliki teksta (`retmod='text'`).

from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'sem.napisite.vas@e-postni.naslov' # identificiramo se

acode = 'NM_005985'   # koda zapisa

handle = Entrez.efetch(db='nucleotide', rettype='fasta', retmode='text', id=acode)
seq_record = SeqIO.read(handle, 'fasta')

print('%s z %i značilnostmi' % (seq_record.id, len(seq_record.features)))   # koliko značilnosti je?
print(seq_record.seq)   # izpis zaporedja
print(seq_record)   # izpis celotnega objekta

Vidimo, da smo pridobili zapis, a nima nič značilnosti, spodaj pa je zaporedje. Zakaj ni nič značilnosti, če pa jih najdemo na GenBank? Povezava do zapisa: [https://www.ncbi.nlm.nih.gov/nuccore/NM_005985](https://www.ncbi.nlm.nih.gov/nuccore/NM_005985) (značilnosti so v delu *features*).

Mi značilnosti nismo pridobili zato, ker smo zapis prenesli v formatu FASTA. Če zadevo ponovimo v formatu GenBank (gb)...

handle = Entrez.efetch(db='nucleotide', rettype='gb', retmode='text', id=acode)
seq_record = SeqIO.read(handle, 'gb')

print('%s z %i značilnostmi' % (seq_record.id, len(seq_record.features)))
print(seq_record)   # izpis celotnega objekta

Če preštejemo značilnosti v zapisu na spletu vidimo, da jih je dejansko toliko. Sem spadajo CDS, misc_feature itd.

Lahko izpišemo tudi nekatere druge karakteristike objekta (podrobneje o tem [tukaj](https://biopython.org/wiki/SeqRecord)), na primer ID in opis:

print(seq_record.id)
print(seq_record.description)

### Shranjevanje zapisa v datoteko

Zapis lahko tudi shranimo v lokalno datoteko v formatu Genbank ali FASTA. Pozor, da spodnja koda deluje morate imeti v mapi, kjer se nahaja trenutno ta datoteka `ipynb`, ustvarjeno mapo `izhod`!

SeqIO.write(seq_record, 'izhod/genbank-sample_output.gb', 'gb')   # GenBank Flat File
SeqIO.write(seq_record, 'izhod/genbank-sample_output.fasta', 'fasta')   # FASTA

Če bi iskanje ponavljali z različnimi kodami za dostop (pa tudi sicer) je smiselno, da kot ime datoteke uporabimo kar kodo zapisa v zbirko GenBank. To lahko naredimo tako:

SeqIO.write(seq_record, 'izhod/genbank-%s.gb' % seq_record.id, 'gb')
SeqIO.write(seq_record, 'izhod/genbank-%s.fasta' % seq_record.id, 'fasta')

### Ekstrakcija dela zapisa in prevajanje

Zapis preberemo iz datoteke s `SeqIO.parse`, ekstrahiramo pa lahko določeno značilnost, na primer kodirajoče zaporedje (CDS) - seveda to velja na primer pri mRNA, značilnosti pa so prisotne samo v zapisu GenNank, pri FASTA formatu pa seveda ne. CDS lahko tudi prevedemo z uporabo določene kodne tabele (navodila na BioPython: [Translation Tables](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc26)) in dobimo nov objekt, iz katerega lahko izpišemo samo zaporedje (kako bo izpisan kodon STOP lahko tudi nastavimo). 

from Bio.Seq import Seq
for rec in SeqIO.parse('izhod/genbank-sample_output.gb', 'gb'):
    if rec.features:
        for feature in rec.features:
            if feature.type == 'CDS':
                print(feature.location)
                print(feature.qualifiers['protein_id'])
                print(feature.location.extract(rec).seq)
                print(feature.location.extract(rec).translate(table='Standard', stop_symbol='*'))
                print(feature.location.extract(rec).translate(table='Standard', stop_symbol='').seq)

---
## Naloga

### Ozadje
Znano je , da se sestava kodirajoče in nekodirajoče regije nekoliko razlikuje, kar je opisano tudi na [Wikipediji](https://en.wikipedia.org/wiki/Coding_region): "*The coding region is thought to contain a higher GC-content than non-coding regions. There is further research that discovered that the longer the coding strand, the higher the GC-content. Short coding strands are comparatively still GC-poor, similar to the low GC-content of the base composition translational stop codons like TAG, TAA, and TGA.*"

Nekajna to temo lahko preberete tudi v članku [Both selective and neutral processes drive GC content evolution in the human genome](https://dx.doi.org/10.1186/1471-2148-8-99).

### Naloga
Vaša naloga je, da pripravite program, ki bo za dano kodo zapisa **izračunal delež GC (v %) v CDS in pa v zaporedju, ki ni del CDS (torej v 5'- in 3'-neprevedeni regiji)*.

Da bo analiza smiselna, je smiselno uporabiti genomsko zaporedje. Lahko za primer vzamete virusni genom SARS-CoV-2, en tak zapis je [GenBank MT066156](https://www.ncbi.nlm.nih.gov/nuccore/MT066156) ali pa kratek genom kakšne bakterije (pobrskajte po GenBank in omejite rezultate na genomsko DNA dolžine med $10^6$ in $1.5 \times 10^6$ bp, da ne bo analiza trajala predolgo). Podite pozorni - genomi vsebujejo več kodirajočih regij, ki jih morate za to analizo združiti v eno zaporedje.

### Namigi
* Za izračun deležev GC si oglejte prvo (analiza kratkega nukleotidnega zaporedja), tam je tudi ilustrirano, kako dobite dolžino zaporedja. Izpis programa naj bo takšen, da bo jasno, kaj je kar - podobno, kot ste to naredili pri prvi vaji za izračun temperature tališča oligonukleotida.
* Morda se naloga sliši kompleksna, a v resnici ni - s stavkom `if` lahko prečešete vhodno zaporedje za posamezne regije CDS in za vsako od njih izračunate število G+C, ki ga prištejete (uporabite `+=`) k skupnemu številu G+C.
* Število G+C v nekodirajočih regijah lahko enostavno dobite tako, da izračunate število G+C v celotnem zaporedju, od katerega odštejete število G+C v vseh kodirajočih regijah.

Predlagani koraki programa:
1. Preberite zapis v formatu GenBank (`gb`).
2. Izračunajte dolžino celotnega zaporedja: `len` (primer pri [V01](nt-oligo_analiza.ipynb)).
3. Preštejte G-je in C-je v celotnem zaporedju: `.count('C')` in `.count('G')` (primer pri [V01](nt-oligo_analiza.ipynb)).
4. Definirajte dve spremenljivki (nastavite na `0`):
   * za število G+C v vseh CDS (npr. `gc_cds`)
   * za skupno dolžino vseh CDS (npr. `len_cds`)
5. Z zanko `for` (zgled zgoraj) prečešite vse CDS, pri tem pa vsakič število G+C v analiziranem CDS dodajte k vrednosti `gc_cds`, dolžino analiziranega CDS pa dodate k vrednosti `len_cds` (za dodajanje uporabite `+=`).
6. Število G+C v nekodirajočih regijah dobite tako, da od števila G+C v celotnem zaporedju odštejete `gc_cds` (to naredite šele, ko prečešete vse CDS).
7. Dolžino nekodirajočih regij dobite tako, da od celotne dolžine zaporedja odštejete vsoto dolžin vseh CDS (`len_cds`).
8. Na osnovi `gc_cds` in `len_cds` izračunajte delež GC v CDS.
9. Na osnovi G+C v nekodirajočih regijah in njihove skupne dolžine (izračunano zgoraj) izračunajte še delež GC v nekodirajočih regijah.

*Priporočam, da kode v zgledu ne spreminjate temveč si jo skopirate nekje tukaj spodaj ali v nov zvezek, tako da ohranite delujočo kodo za morebitni troubleshooting. Prav tako spremenite imena izhodnih datotek, ki jih program kreira.*

### V razmislek
* Kaj pa, če analizirano zaporedje vsebuje prekrivajoče se CDS? Je vaš algoritem na to prilagojen? Če ne, kako bi ga prilagodili?
* Pri analizi smo izračunali odstotek GC parov kar po vseh CDS hkrati (povprečenje), s tem pa smo nekaj informacij izgubili, npr. o razponu deleža GC ter o porazdelitvi deleža GC glede na dolžino CDS. Razmislite, kako bi analizo izvedli, da bi prišli do teh informacij in kako bi jih vizualizirali.