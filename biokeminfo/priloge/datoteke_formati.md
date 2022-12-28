# Pogosti formati datotek

Na tej strani najdete opise nekaterih formatov datotek, s katerimi se srečuje bioinformatik.

## FASTA

To je eden najpogostejših formatov v bioinformatiki, uporablja pa se za zapis aminokislinskih in nukleotidnih zaporedij. Ime izhaja iz imena programa [FASTA](https://en.wikipedia.org/wiki/FASTA) za primerjavo zaporedij oz. iskanje podobnih zaporedij, ki sta ga razvila Pearson in Lipman leta 1985 ([zadnja verzija programa](https://github.com/wrpearson/fasta36) na GitHub; [spletni vmesnik](https://www.ebi.ac.uk/Tools/sss/fasta/) na strani EBI). Včasih se temu formatu reče kar *Pearson* po imenu enega od avtorjev programa, ali pa *Pearson/FASTA*.

Format je nadvse preprost – prva vrstica se začne z znakom "večje" (`>`), ki mu v **isti vrstici** sledi ime zaporedja, nato pa v drugi vrstici sledi zaporedje sámo. Slednje se lahko sicer razteza čez več vrstic. Primer zaporedja z imenom HEPC_LARCR:

```text
>HEPC_PIG
MALSVQIRAACLLLLLLVSLTAGSVLPSQTRQLTDLRTQDTAGATAGLTPVAQRLRRDTHFPICIFCCGCCRKAICGMCCKT
```

V isto datoteko lahko shranimo več zaporedij, kar je prikazano na primeru treh kratkih nukleotidnih zaporedij:

```text
>oligo1
AGCTGCGATAGAGGCTCGCGATGCTA
>oligo2
AGGAGATAGAGAGATGCGCGCGCCGC
>oligo3
AGCTAGCCTAGATGCGCTAGATCGAT
```

Za večjo preglednost lahko zaporedja ločimo s praznimi vrsticami, kot je prikazano na primeru zaporedij proteina hepcidina iz štirih različnih organizmov:

```text
>HEPC_PIG
MALSVQIRAACLLLLLLVSLTAGSVLPSQTRQLTDLRTQDTAGATAGLTPVAQRL
RRDTHFPICIFCCGCCRKAICGMCCKT

>HEPC_RAT
MALSTRIQAACLLLLLLASLSSGAYLRQQTRQTTALQPWHGAESKTDDSALLMLK
RRKRDTNFPICLFCCKCCKNSSCGLCCIT

>HEPC_HUMAN
MALSSQIWAACLLLLLLLASLTSGSVFPQQTGQLAELQPQDRAGARASWMPMFQR
RRRRDTHFPICIFCCGCCHRSKCGMCCKT

>HEPC1_DANRE
MKLSNVFLAAVVILTCVCVFQITAVPFIQQVQDEHHVESEELQENQHLTEAEHRQ
TDPLVLFRTKRQSHLSLCRFCCKCCRNKGCGYCCKF
```

Več o FASTA formatu lahko preberete na [Wikipediji](https://en.wikipedia.org/wiki/FASTA_format).

### Posebne oblike

Obstaja več formatov, izvedenih iz osnovnega, nekaj jih je opisanih v nadaljevanju.

#### FASTQ

FASTQ je posebna različica formata FASTA, ki zraven zaporedja vsebuje še oceno kvalitete zaporedja za vsak ostanek posebej. Je standardni format, ki se uporablja za zapis zaporedij, določenih z visoko zmogljivimi sekvenatorji (*high-throuput sequencing*). Format se uporablja zgolj za zapis nukleotidnih zaporedij.

Več o formatu na [Wikipediji](https://en.wikipedia.org/wiki/FASTQ_format).

#### Poravnan FASTA format

Poravnava v formatu FASTA (*aligned FASTA format*) je izvedenka, kjer je v isti datoteki FASTA zapisanih več zaporedij, ki so enako dolga – enake dolžine sicer niso zato, ker vsebujejo enako število nukleotidnih/aminokislinskih ostankov, ampak ker so zaporedja dejansko poravnana in so vanje vstavljeni znaki `-` kot oznake za vrzeli.

Kot primer si oglejmo poravnavo štirih aminokislinskih zaporedij hepcidina, poravnanih s programom Clustal Omega, prikazanih v standardnem formatu Clustal (neporavnana zaporedja so prikazana pri opisu snovnega formata FASTA, kjer je razvidno, da niso enako dolga):

```text
CLUSTAL O(1.2.4) multiple sequence alignment

HEPC1_DANRE      MKLSNVFLAAVVILTCVCVFQITAVP-FIQQVQDEHHVESEELQENQHLTEAEHRQTDPL	59
HEPC_RAT         MALSTRIQAACLLLL-LLA-SLSSGAYLRQQTRQ-----TTAL-QPWHGAESKTDDSALL	52
HEPC_PIG         MALSVQIRAACLLLL-LLV-SLTAGSVLPSQTRQ-----LTDL-RTQDTAGATAG-LTPV	51
HEPC_HUMAN       MALSSQIWAACLLLLLLLA-SLTSGSVFPQQTGQ-----LAEL-QPQDRAGARAS-WMPM	52
                 * **  : ** ::*  : . .:::   : .*. :        * .  . : :       :

HEPC1_DANRE      VLFRTKRQSHLSLCRFCCKCCRNKGCGYCCKF	91
HEPC_RAT         MLKRRKRDTNFPICLFCCKCCKNSSCGLCCIT	84
HEPC_PIG         AQR-LRRDTHFPICIFCCGCCRKAICGMCCKT	82
HEPC_HUMAN       FQRRRRRDTHFPICIFCCGCCHRSKCGMCCKT	84
                      :*:::: :* *** **:.  ** **  
```

To poravnavo lahko zapišemo v sicer manj preglednem "poravnanem FASTA" formatu:

```text
>HEPC1_DANRE
MKLSNVFLAAVVILTCVCVFQITAVP-FIQQVQDEHHVESEELQENQHLTEAEHRQTDPL
VLFRTKRQSHLSLCRFCCKCCRNKGCGYCCKF
>HEPC_RAT
MALSTRIQAACLLLL-LLA-SLSSGAYLRQQTRQ-----TTAL-QPWHGAESKTDDSALL
MLKRRKRDTNFPICLFCCKCCKNSSCGLCCIT
>HEPC_PIG
MALSVQIRAACLLLL-LLV-SLTAGSVLPSQTRQ-----LTDL-RTQDTAGATAG-LTPV
AQR-LRRDTHFPICIFCCGCCRKAICGMCCKT
>HEPC_HUMAN
MALSSQIWAACLLLLLLLA-SLTSGSVFPQQTGQ-----LAEL-QPQDRAGARAS-WMPM
FQRRRRRDTHFPICIFCCGCCHRSKCGMCCKT
```

Primer govori sam zase :)

## CSV in TSV

Datoteke **CSV** so enostavne tekstovne datoteke, v katerih so shranjeni tabelirani podatki. Vsaka vrstica v datoteki predstavlja vrstico tabele, v vsaki vrstici pa poseben ločitveni znak (*delimiting character*) ločuje posamezne celice oz. stolpce. V osnovi je ta ločitveni znak vejica (od tod izhaja ime *Comma Separated Values*), a ker format CSV ni standardiziran se v tovrstnih datotekah lahko kot ločitveni znak pojavlja tabulator, podpičje, presledek ipd. Uporaba drugačnega znaka kot je vejica je pogosta na primer v državah, kjer se že kot decimalni simbol uporablja vejica, tudi v Sloveniji, saj bi v tem primeru prišlo do napak pri interpretaciji, kje se konča in kje začne nova vrednost v posamezni vrstici. Več o formatu CSV lahko preberete na [Wikipediji](https://en.wikipedia.org/wiki/Comma-separated_values).

Na primer, tabelo

| T: Gene names | T: id | Intensity CD86_1 | Intensity CD86_2 |
|---------------|-------|------------------|------------------|
| DDX39A        | 29    | 16.9839          | 17.2317          |
| DDX3X;DDX3Y   | 34    | 16.3093          | 16.1811          |
| ACACB         | 35    | 23.5791          | 23.9303          |
| TNFRSF10B     | 37    | 19.4167          | 19.7823          |
| PLXNB2        | 38    | 19.529           | 21.4844          |
| FZD7          | 45    | 17.5487          | 15.8987          |

bi v formatu CSV zapisali kot

```text
T: Gene names,T: id,Intensity CD86_1,Intensity CD86_2
DDX39A,29,16.9839,17.2317
DDX3X;DDX3Y,34,16.3093,16.1811
ACACB,35,23.5791,23.9303
TNFRSF10B,37,19.4167,19.7823
PLXNB2,38,19.529,21.4844
FZD7,45,17.5487,15.8987
```

**TSV** je varianta, kjer se namesto vejice za ločevanje polj uporablja tabulator (*tab*), torej gre za *Tab Separated Values*. Končnica TSV se uporablja redkeje, včasih nosi datoteka v formatu TSV kar končnico CSV. Tabelo iz zgornjega primera bi kot TSV zapisali tako:

```text
T: Gene names	T: id	Intensity CD86_1	Intensity CD86_2
DDX39A	29	16.9839	17.2317
DDX3X;DDX3Y	34	16.3093	16.1811
ACACB	35	23.5791	23.9303
TNFRSF10B	37	19.4167	19.7823
PLXNB2	38	19.529	21.4844
FZD7	45	17.5487	15.8987
```

Datoteke formata CSV/TSV lahko odprete z običajnimi programi za delo s tekstovnimi datotekami (Notepad/Beležnica, TextEdit, ...), s specializiranimi programi za datoteke CSV, lahko pa kar z Microsoft Excel.


## PDB in PDBx/mmCIF

Gre za datoteke, v katerih shranjujemo strukturne podatke, pravzaprav koordinate atomov in spremljajoče podatke (anotacije, B-faktor, zasedenost, ...). Spet gre za posebej oblikovane tekstovne datoteke. Format PDB je starejši, razvit ob nastanku [World Wide Protein Data Bank](http://www.wwpdb.org/) (1971), prve zbirke, namenjene zbiranju, shranjevanju in dostopu do strukturnih podatkov bioloških makromolekul. Format je dolgo zadoščal vsem potrebam strukturnih biologov, a z razvojem novih metod in programov ter pojava modelov/struktur vedno večjih makromolekul(skih kompleksov) so se pokazale nekatere omejitve tega formata. Na primer, v datoteko PDB lahko shranimo modele iz največ 99.999 atomov ter iz največ 62 različnih polipeptidnih/polinukleotidnih verig; omejitev glede števila atomov izhaja iz širine polja, namenjenega za zapis zaporedne številke atoma (vsi atomi imajo unikatno številko!), ki lahko vsebuje zgolj 5 znakov. To je vodilo do nastanka formata PDBx/mmCIF (mmCIF = *macromolecular CIF*), ki je pravzaprav posebna izvedba formata CIF (*Crystallographic Information File*, [Wikipedia](https://en.wikipedia.org/wiki/Crystallographic_Information_File)), primarno namenjenega shranjevanju strukturnih podatkov manjših molekul.