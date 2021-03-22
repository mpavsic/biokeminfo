# VAJA: Poravnava zaporedij NW & SW (Python)

V Pythonu lahko z uporabo paketa [BioPython](https://biopython.org) na enostaven način delamo poravnave aminokislinskih zaporedij. Uporaba algoritmov, ki dajo matematično optimalno poravnavo (npr. **Needleman-Wunsch** in **Smith-Waterman**), je v primeru manjšega obsega vhodnih podatkov popolnoma normalno izvedljiva na domačem računalniku. V primeru daljšega računanja se lahko uporabi ("pokliče" iz Pythona) orodja na npr. strežniku EMBOSS (opis API-ja za to je tukaj je v [članku]( http://europepmc.org/article/MED/30976793)).

Mi si bomo pogledali enostavne primere poravnave, kjer lahko poljubno variiramo parametre (npr. uporabljena matrika zamenjav ter kazni za vrzeli) in opazujemo, kakšne poravnave dobimo. Kot pri preteklih vajah so spodaj že pripravljeni zgledi kode, ki s spremljajočim besedilom ilustrirajo uporabo, na dnu datoteke pa je enostavna naloga, ki ilustrira možnost variacije parametrov.

---

## Zgledi

### Definicija zaporedja

Najprej bomo __definirali objekt, ki vsebuje zaporedje__, oz. dva taka objekta. To lahko naredimo na več načinov, eden je direktna ustvaritev, kjer sami podamo zaporedje. Zaporedja lahko preberemo tudi iz *lokalno shranjene datoteke* v različnih formatih (npr. Genbank ali FASTA) ter seveda tudi iz *spletnih podatkovnih zbirk (npr. Genbank ali UniProt)*, kar smo si že pogledali na prejšnjih vajah.

Torej, objekt definiramo podobno kot pri eni izmed začetnih vaj z BioPython:

from Bio.Seq import Seq
seq1 = Seq('AAKCLVMKAEMNGSKLGRRAKPEGALQNNDGLYDPDCDESGLFKAKQCNGTSMCWCVNTAGVRRTDKDTEITC')
seq2 = Seq('KTRCQLEREHILGAAGGADAQRPTLQGMFVPQCDEYGHYVPTQCHHSTGYCWCVDRDGRELEGSRTPPGMRPPC')

Lahko smo še malce bolj kreativni in zraven zaporedja samega definiramo še kakšne pripise ([dokumentacija](https://biopython.org/wiki/SeqRecord)):

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq1 = SeqRecord(Seq('AAKCLVMKAEMNGSKLGRRAKPEGALQNNDGLYDPDCDESGLFKAKQCNGTSMCWCVNTAGVRRTDKDTEITC'),
                 id='P16422', name='EpCAM',
                 description='epithelial cell adhesion molecule, 63-135')
seq2 = SeqRecord(Seq('LTKCQEEVSHIPAVHPGSFRPKCDENGNYLPLQCYGSIGYCWCVFPNGTEVPNTRSRGHHNC'),
                 id='P04233', name='HG2A',
                 description='HLA class II histocompatibility antigen gamma chain, 210-271')
print(seq1)
print(seq1)

Analogno bi lahko naredili tudi za DNA.

V primeru, da zaporedje oz. objekt definiramo na zgornji način, izpišemo zaporedje sámo tako:

print(seq1.seq)

---
### Izbor matrike zamenjav

Naslednja zadevščina, ki jo zraven zaporedja potrebujemo za izračun poravnave, je __substitucijska matrika__. Dober nabor le-teh smo že dobili preko BioPythona, slednji pa nam tudi omogoča definicijo čisto poljubne matrike (matrike so definirane kot slovarji - _dictionary_).

Pa poglejmo, kaj imamo na voljo! Seznam matrik je dostopen preko tega spletnega naslova: https://biopython.org/DIST/docs/api/Bio.SubsMat.MatrixInfo-module.html

Lahko pa tudi samo pokukamo, kaj imamo v trenutno nainstalirani verziji BioPythona na razpolago:

from Bio.Align import substitution_matrices
matrix_list = substitution_matrices.load()
print(matrix_list)

Izberemo matriko ter jo izpišemo, da vidimo, kako je pravzaprav zapisana (spodaj ne razširjen zapis kode):

from Bio.Align import substitution_matrices
matrix_name = 'BLOSUM62'
matrix = substitution_matrices.load(matrix_name)
print(matrix)

Drug način je takle, dobimo enako (izpis je izključen):

Če nas zanima neka konretna vrednost iz matrike, na primer vrednost za substitucijo valina in izolevcina, lahko to naredimo na prav enostaven način:

print(matrix['V', 'I'])

Dobro, to je bilo nekaj uvoda, sedaj pa gremo k stvari - poravnavam!

---
### Globalna poravnava

Za poravnavo zaporedij imamo v [BioPython](https://biopython.org) na voljo več orodij. Eno izmed njih, modul __[pairwise2](https://biopython.org/DIST/docs/api/Bio.pairwise2-module.html)__, omogoča izračun poravnave dveh zaporedij z dinamičnim programiranjem, med drugim preko algoritmov Needleman-Wunsch in Smith-Waterman.

# pairwise2 lahko definiramo kot aln, da vsakič ne izpisujemo pairwise2
from Bio import pairwise2 as aln

Za ilustracijo bomo poravnavo izvedli na nt-zaporedjih. Pa jih definirajmo, enostavno, kot _string_:

seq1 = 'AGCCGA'
seq2 = 'ACTA'

Globalno poravnavo (ali več njih) dobimo tako:

alignments = aln.align.globalxx(seq1, seq2)
print(alignments)

Na ta način dobimo v `poravnave` seznam (_list_) poravnav, od katerih je vsaka predstavljena kot terka (_tuple_), sestavljena iz prvega in drugega zaporedja, sledijo pa tri številke:
* vrednost poravnave (_score_ kot float),
* začetno mesto poravnave (štejemo od 0),
* končno mesto poravnave.

Ime funkcije, v našem primeru `globalxx`, je dejansko sestavljeno iz 3 komponent oblike `<alignment type>XX`. Prvi parameter oz. ime samo določa vrsto poravnave (`global` ali  `local` za globalno oz. lokalno poravnavo), druga parametra pa določata, kako se upoštevajo ujemanja in neujemanja (prvi znak) ter vrzeli (drugi znak). Pomen teh stikal je podrobneje opisan v [dokumentaciji](https://biopython.org/docs/1.77/api/Bio.pairwise2.html).

Možnosti za ujemanja/neujemanja:

| vrednost | pomen |
| :--- : | :---- |
| x | brez posebnih vrednosti (ujemanje = 1, neujemanje = 0) |
| m | ujemanje je vrednost za identične znake, sicer gre za neujemanje |
| d | vrednost za posamezni par znakov se prebere iz slovarja |
| c | vrednosti da callback funkcija |

Množnosti za vrzeli:

| vrednost | pomen |
| :--- : | :---- |
| x | brez kazni za vrzeli (oz. kazen je enaka 0) |
| s | enake kazni za odprtje in razširitev vrzeli za obe zaporedji |
| d | različne kazni za odprtje in razširitev vrzeli za posamezni zaporedji |
| c | vrednosti da callback funkcija |

Vrednost poravnave je vedno izračunana po naslednji enačbi:
$$S = \sum s_{a,b} + \sum (I + (n-1) E)$$

pri čemer je $s_{a,b}$ vrednost iz matrike zamenjav (substitucijske matrike), $I$ in $E$ pa kazni za odprtje oz. razširitev vrzeli.

V bolj pregledno obliko lahko poravnavo preoblikujemo z uporabo `format_alignment` (pozor - spodaj je prikazano, kako izpišemo vse poravnave, ki smo jih dobili - vse imajo enako vrednosti):

from Bio.pairwise2 import format_alignment
for a in alignments:
    print(format_alignment(*a))

Če bi želeli vrednosti za ujemanje in neujemanje posebej nastaviti (opis je nekaj polj višje), lahko to naredimo na način, prikazan spodaj. Bodite pozorni, kako je koda zapisana tokrat - v obliki zanke `for`.

for alignment in aln.align.globalmx(seq1, seq2, 2, -1):
    print(format_alignment(*a))

Še en primer - določimo kazen za odprtje in razširitev vrzeli. Uporabimo lahko tudi ključne besede, kar pomaga pri razumevanju, kaj je kaj.

for alignment in aln.align.globalms(seq1, seq2, match=2, mismatch=-1, open=-10, extend=-5):
    print(format_alignment(*a))

Izpis lahko tudi prilagodimo - več o tem lahko preberemo v [opisu modula pairwise2](https://biopython.org/DIST/docs/api/Bio.pairwise2-module.html). Spodaj je primer.

Lahko izpišemo zgolj npr. vrednost poravnave (prikazano je za prvo poravnavo v seznamu poravnav):

print(alignments[0].score)

Pri samem izračunu poravnave lahko nastavimo še nekatere parametre kot je (vir: [opis modula pairwise2](https://biopython.org/DIST/docs/api/Bio.pairwise2-module.html)):
* `penalize_extend_when_opening`: boolean (default: False) - ali naj bo odprtje vrzeli dodatno kaznovano še kot ena razširitev ali ne (false = vrzel dolžine 1 je kaznovana samo s kaznijo za odprtje)
* `penalize_end_gap`: boolean - ali naj kaznujemo končne vrzeli, privzeto je vključeno pri globalni poravnavi, pri lokalni to odpade
* `gap_char`: string (default: '-') - kakšen znak naj se uporabi za vrzel
* `force_generic`: boolean (default: False) - če vklopimo, se bo uporabil generičen neoptimiziran algoritem za dinamično programiranje (počasno!)
* `score_only`: boolean (default: False) - vrni samo vrednost poravnave brez poravnave same
* `one_alignment_only`: boolean (default: False) - vrni samo eno poravnavo

Primer:

alignments = aln.align.globalxx(seq1, seq2, gap_char='Š', one_alignment_only=1)
from Bio.pairwise2 import format_alignment
print(format_alignment(*alignments[0]))

Tu je recimo ilustrirano, kako dobimo samo vrednost poravnave:

alignments = aln.align.globalxx(seq1, seq2, score_only=1)
print(alignments)



Že iz prejšnjega prikaza, še bolj nazorno pa iz preoblikovanega, lahko vidimo, da imamo dve poravnavi - ena ima blizu 3'-konca vrzel v obeh zaporedjih, druga pa na tem mestu neujemanje. Vrednost obeh je enaka, saj je kazen tako za odprtje vrzeli kot vrednost za neujemanje enaka 0.

BioPython sicer ne vsebuje substitucijskih matrik za nukleotidna zaporedja, tako da bi relevantno matriko morali sami uvoziti in nato uporabiti kot _dictionary_. Tega na tem mestu ne bomo počeli.

---
### Lokalna poravnava

Poglejmo si še primer lokalne poravnave:

seq3 = 'AGGGGATAAGACTCCGCTTAGAATAGCTAGAATAGCCG'
seq4 = 'ACTCCGCTT'
alignments_local = aln.align.globalxx(seq3, seq4)
for a in alignments_local:
    print(format_alignment(*a))

Predvidevam, da z zgornjimi rezultati nismo zadovoljni. Poizkusimo drugače, določimo kazni za vrzeli:

alignments_local2 = aln.align.localxs(seq3, seq4, -1, 0)
for a in alignments_local2:
    print(format_alignment(*a))

Naj bo nukleotidnih zaporedij zaenkrat dovolj, gremo na aminokislinska zaporedja!

### Globalna in lokalna poravnava aminokislinskih zaporedij

Najprej definirajmo naši zaporedji (to je kopija kode od zgoraj):

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq1 = SeqRecord(Seq('AAKCLVMKAEMNGSKLGRRAKPEGALQNNDGLYDPDCDESGLFKAKQCNGTSMCWCVNTAGVRRTDKDTEITC'),
                 id='P16422', name='EpCAM',
                 description='epithelial cell adhesion molecule, 63-135')
seq2 = SeqRecord(Seq('LTKCQEEVSHIPAVHPGSFRPKCDENGNYLPLQCYGSIGYCWCVFPNGTEVPNTRSRGHHNC'),
                 id='P04233', name='HG2A',
                 description='HLA class II histocompatibility antigen gamma chain, 210-271')

from Bio.Align import substitution_matrices
from Bio import pairwise2
matrix = substitution_matrices.load('BLOSUM62')
alignments = pairwise2.align.globaldx(seq1.seq, seq2.seq, matrix)
print(alignments)

Izpišimo še lepo eno oblikovano poravnavo:

print(pairwise2.format_alignment(*alignments[0]))

Analogno lahko delamo tudi lokalno poravnavo, za slednjo pa pač naredimo tako: 

alignments = pairwise2.align.localdx(seq1.seq, seq2.seq, matrix)
print(pairwise2.format_alignment(*alignments[0]))

---

## Naloga

Poglejmo sedaj, kako se lahko z variacijo parametrov kaj naučimo. Najprej analizirajmo, ali sta poravnavi aminokislisnkega zaporedja (primer zgoraj) sploh v redu. Napnite oči!

Če poravnavi nisva v redu predlagajte izboljšane parametre za poravnavo in sicer:
* primerno matriko,
* kazni za vrzeli.

Analizirajte, kako variacija parametrov (ločeno!) vpliva na poravnavo. Rezultate primerjajte s poravnavo, ki jo naredite s spletno verzijo orodja Needle na strežniku [Pairwise Sequence Alignment @ EBI](https://www.ebi.ac.uk/Tools/psa/).