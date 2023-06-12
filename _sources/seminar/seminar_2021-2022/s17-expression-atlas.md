# Expression Atlas – izražanje genov


**Avtorja**: Hana Glavnik, Tina Javeršek

**Datum predstavitve**: 2022-05-11

---
## Namen vaje
Spoznanje z zbirko Expression Atlas, kjer so prosto dostopne informacije o vzorcu izražanja genov RNA zaporedij, mikromrež ter izražanje proteinov iz študij proteoma. Pri tej vaji se bomo naučili iskanja po zbirki in branja rezultatov, ki nam jih zbirka ob iskanju vrne. 

---
## Program
Program: [Expression Atlas](https://www.ebi.ac.uk/gxa/home)

Avtorji programa: European Bioinformatics Institute, EMBL-EBI

Reference:
- Moreno P, Fexova S, George N, Manning JR, Miao Z, Mohammed S, et al. Expression Atlas update: gene and protein expression in multiple species. Nucleic Acids Research. 2022;50: D129–D140. (https://doi.org/10.1093/nar/gkab1030) 
- Misha Kapushesky, Ibrahim Emam, Ele Holloway, Pavel Kurnosov, Andrey Zorin, James Malone, Gabriella Rustici, Eleanor Williams, Helen Parkinson, Alvis Brazma, Gene Expression Atlas at the European Bioinformatics Institute, Nucleic Acids Research, Volume 38, Issue suppl_1, 1 January 2010, Pages D690–D698, (https://doi.org/10.1093/nar/gkp936)


### Opis programa
Expression Atlas je znanstveni vir, ki je odprt širši javnosti, kjer so prosto dostopne informacije o vzorcu izražanja genov iz RNA zaporedij,mikromrež ter izražanje proteinov iz študij proteoma. Podatke, ki jih vnesemo, atlas zbere, analizira in jih predstavi. S pomočjo tega dobimo odgovore na vprašanja, kje se izraža naš izbran gen in kako izražanje vpliva na stanje organizma ter razvoj bolezni. Zbirka črpa podatke iz različnih genomskih zbirk, kot so ArrayExpress, Gene Expression Omnibus (GEO), European Nucleotide Archive (ENA) in druge. Vsebuje podatke o genih 550 donorjev in 53 različnih tkiv, kar sestavlja skoraj 20.000  RNA-sekvenčnih knjižnic. Če bi zagnali analizo podatkov na našem lokalnem računalniku, bi trajalo približno 22 let in bi zavzelo do 78 terabajtov prostora, da bi dobili rezultate vseh vzorcev. Poleg podatkov, ki so jih pridobili pri raziskovanju zdravih vzorcev, zbirka vsebuje tudi raziskave rakavih tkiv, človeškega razvoja in primere razvoja modelnih organizmov ter celičnih linij. Expression atlas zajema podatke o več kot 60 različnih vrstah organizmov in več različnih bioloških stanjih.

Seti podatkov v zbirki so klasificirani kot osnovni ali diferencialni. Osnovne sete podatkov so pridobili iz visoko kvalitetnih RNA zaporedij, nanašajo pa se predvsem na zdrava tkiva, celične tipe, razvojne faze ali celične linije. Diferencialni seti podatkov obsegajo spremembe v ekspresiji genov med dvema stanjema- zdravimi in patološko spremenjenimi tkivi. 

Podatki o izražanju genov se najprej zberejo in organizirajo v visokokakovostne označene sete podatkov. Vsi ti se nato prepošljejo preko  tehnike oziroma principa vodovodnih cevi.Nato so predstavljeni na način, ki je prijazen uporabnikom in omogoča iskanje podatkov ter njihovo vizualizacijo. Vhodni podatek vpišemo v iskalnik in Expression atlas nam vrne različne eksperimente, tipe tkiva in celic, kjer se iskani gen izraža. Prav tako dobimo informacijo, pod katerimi pogoji nastopa naš gen kot markerski gen. Vsak eksperiment vsebuje tudi datoteke, ki jih lahko posameznik prenese za nadaljnje raziskovanje. 

Kot vhodne podatke uporabljamo ime gena, Uniprot identifikacijsko kodo,Gene Ontology identifikacijsko kodo ali bolezenskega stanja določenega organizma ali celotne vrste.  

### Vhodni podatki

Preko expression atlasa lahko iščemo z imenom iskanega gena,identifikacijsko kodo gena iz Uniprot ali Gene Ontology strani, prav tako lahko iščemo podatke za specifičen organizem in bolezen. Vrne nam pregled vseh eksperimentov, ki so trenutno na voljo za določen organizem.

---
## Navodila
### Vhodni podatki
- Shwachman-Diamond syndrome
- SBDS gen
- Marfan syndrome

### Postopek dela
- V iskalno vrstico vnesemo ime gena ali identifikacijsko kodo, ime bolezni,
- ko izberemo posamezni eksperiment, se nam prikažejo podatki, ki so del tega seta (ime eksperimenta, uporabljena tehnologija, zasnova eksperimenta in dopolnilne informacije),
- ob kliku na okence, ki pripada iskanemu genu in posameznem tkivu, nas usmeri na Ensembl, kjer dostopamo do podrobnosti regije, kjer se gen izraža,
- če izberemo diferencialno iskanje podatkov (Differential expression), dostopamo do eksperimentov, kjer primerjajo izražanje gena v zdravem in obolelem tkivu (celični liniji).

### Pričakovani rezultati in razlaga
Rezultati pri iskanju osnovnega izražanja genov (Baseline expression) se prikažejo kot toplotna karta, kjer posamezni odtenek modre barve predstavlja nivo izražanja gena. Posamezna vrstica prikazuje eksperiment, ki se nanaša na študijo transkripta (T) ali proteoma (P). Na vrhu toplotne karte (poševno) imamo podatke o tkivu, v katerem se je gen izražal.

![tabela1](s17-expression-atlas-1.jpg)
 
Ob kliku na posamezen eksperiment dostopamo do podatkov o izražanju gena v posameznih tkivih - podatki so ponovno prikazani s toplotno karto. Lahko izbiramo enote, v katerih so podani rezultati: TMP (transkripts per milion) ali FPKM (fragments per kilobase million).

![tabela2](s17-expression-atlas-2.jpg)

Ob iskanju diferencialnega izražanja genov so eksperimenti razvrščeni glede na logaritem z osnovo 2 fold change vrednosti.  

![tabela3](s17-expression-atlas-3.jpg)

