# VAJA: Točkovni diagram

Na dveh enostavnih primerih si bomo ogledali, kako lahko uporabimo točkovni diagram za detekcijo podobnosti podobnosti med danimi zaporedji. V enem primeru bomo uporabili kratko zaporedje, v drugem pa kar cel genom, a relativno kratek – bakterijski.

## Naloga 1: primerjava dveh krajših zaporedij

S pomočjo spletnega programa [EMBOSS DotMatcher](http://emboss.bioinformatics.nl/cgi-bin/emboss/dotmatcher) primerjajte med seboj aminokislinski zaporedji proteinov:
* človeški N-CAM-1 (*neural cell adhesion molecule 1*)
* miotilin (*myotilin*)

Smiselno je, da za neko zaporedje (če ga primerjate samega s seboj) oz. par zaporedij preizkusite nekaj kombinacij nastavitev (vrednosti praga in velikosti okna) in ugotovite, katere nastavitve vam dajo najbolj jasno sliko, ob tem pa ne izgubite relevantnih elementov primerjave (ponovitve ipd.). Podatke o slednjih lahko razberete iz zapisa v znirki UniProt.

Naloga:
* Z variacijo navedenih parametrov si oglejte, kako se spreminja občutljivost in količina šuma pri različnih vrednostih parametrov za ak-zaporedji danih proteinov.
* Ali v točkovnem diagramu opazite kakšen izrazit vzorec? Razložite!
* Sedaj pa primerjajte še nt-zaporedji celotne kodirajoče regije mRNA za omenjena proteina. Kakšen je rezultat take primerjave in zakaj?

Na kratko o orodju DotMatcher... Orodje DotMatcher je sprogramirano tako, da za posamezne pare ij (i so ostanki iz 1. zaporedja, j pa iz 2. zaporedja) prebere vrednosti iz matrike zamenjav (privzeta EBLOSUM62 (=BLOSUM62) za ak-zaporedja, za nt-zaporedja pa EDNAFULL), nato pa izračuna vsoto nekaj zaporednih ostankov (ta parameter nastavimo z velikostjo okna – *window size*), na koncu pa znak v matriki nariše le, če je vsota enaka ali pa presega prag (*treshold*). Zaporedja, ki jih primerjate, vstavite v program v formatu FASTA.

![EMBOSS DotMatcher](slike/emboss_dotmatcher.png)

Obstajajo še drugi programi za točkovne diagrame, seznam najdete [tukaj](https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics)).

## Naloga 2: Primerjava genomskih zaporedij

Kot omenjeno je primerjava zelo dolgih genomskih zaporedij nekoliko dolgotrajnejša oz. zahteva več procesorske moči. Izvedli jo bomo na namenskem strežniku prek spleta, obstaja pa več takih storitev:
* [D-GENIES](http://dgenies.toulouse.inra.fr/) - **D**ot plot large **Gen**omes in an **I**nteractive, **E**fficient and **S**imple way
* [SynMap](https://genomevolution.org/coge/SynMap.pl) - *generates a syntenic dotplot between two organisms and identifies syntenic regions*
* [YASS](https://bioinfo.cristal.univ-lille.fr/yass/yass.php) - *genomic similarity search tool*

Med zadnjim testom orodje D-GENIS ni delovali, zato bomo uporabili SynMap. Primerjali bomo celotno genomsko zaporedje dveh sevov bakterije *E. coli*, in sicer seva K-12 MG1655 in CFT073. Zaporedji lahko najdete v zbirki Nucleotide na strežniku NCBI, sta pa dostopni tudi direktno v orodju.

Kakšen je rezultat in kaj mislite, zakaj je takšen?

Kaj je posebnega na sevu CFT073? Namig se skriva v članku [*Genome reannotation of Escherichia coli CFT073 with new insights into virulence*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2785843/).