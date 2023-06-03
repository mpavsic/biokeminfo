# Pregledovalnik genoma GDV

**Avtorja**: Nuša Brdnik, Mark Loborec

**Datum predstavitve**: 2022-05-04

---
## Namen vaje
Vizualizacija genov, zaporedij, anotacij in drugih podatkov znotraj genoma. Pregledovanje in navigacija po genomu.

---
## Program

Program: **[Genome Data viewer 5.3.1](https://www.ncbi.nlm.nih.gov/genome/gdv/)**

Avtorji programa: Avtorji niso navedeni. National Center for Biotechnology Information.(https://www.ncbi.nlm.nih.gov/)

Reference:
- Rangwala SH, Kuznetsov A, Ananiev V, Asztalos A, Borodin E, Evgeniev V, Joukov V, Lotov V, Pannu R, Rudnev D, Shkeda A, Weitz EM, Schneider VA. **Accessing NCBI data using the NCBI Sequence Viewer and Genome Data Viewer (GDV).** *Genome Res.* January 2021 31: 159-169.  doi:10.1101/gr.266932.120. PMID: 33239395.



### Opis programa

Genome Data Viewer podpira več kot 1500 različnih genomov. Na prvi strani programa lahko vidimo njihovo filogenetsko drevo. Ko izberemo organizem program vizualizira eksperimentalno pridobljene podatke. Vzame zaporedje iz podatkovnih zbirk in jih prikaže na grafičen način. Različne anotacije za kodirajoče regije, introne, eksone, izražanje genov in jih postavi ob genom.
Genome Data Viewer sprejema iskalne zahtevke v obliki genov, lokacijie v genomu, fenotipa in dbSNP idjev. Lahko tudi ročno pregledujemo genom ali pa se premikamo po kromosomih ali delih kromosomov. Različni assembly-ji so različe serije sekvenciranja oz zbirke podatkov.



### Vhodni podatki

Vhodni podatki so imena genov, lokacija v genomu, fenotip... Program ni zahteven, iščemo lahko tudi tekstovno ali preko BLASTa.

---
## Navodila

### Vhodni podatki

V obliki seznama navedite vhodne podatke, zgled je spodaj. Če gre za podatke iz drugih zbirk (npr. iz zbirke aminokislinskih zaporedij), jih navedite kot povezave na ustrezne zapise. Izogibajte se temu, da bodo morali kolegi podatke sami iskati po podatkovnih zbirkah, saj bo to bistveno zavleklo predstavitev. Vhodne podatke si morate zamisliti in poiskati sami - uporaba tistih, ki jih program sam predlaga kot primer, ni dovoljena.

Kot vhodne podatke uporabite (to je primer):
- človeški genom
- gen za Oksitocin (OXT)


### Postopek dela
1. Odprite Genome Data Viewer. Prepričajte se, da je izbrani genom človeški (Homo Sapiens)
2. Za iskalni zahtevek vnesite OXT. Za assembly izberite GRCh38.p14.
3. Na zaslonu lahko sedaj vidimo lokacijo gena (številka kromosoma in na katere zaporedne baze vsebuje), kodirajočo regijo, smer branja gena, eksone in introne ter končni protein.
4. S klikom na ikono zobnika v zgornjem desnem kotu in nadalnjim klikom na NCBI recommended tracks set bomo dodali še tirnice, ki prikazujejo izražanje (expression)
5. Če se z miško ustavimo na določenem delu tirnice se pojavi okno z anotacijami (pogosto dolžino, natančno lokacijo (od do baznega para), in hiperpovezavo do drugih podatkovnih podatkovnih zbirk)



### Pričakovani rezultati in razlaga
Vidimo okno z vizualizacijo gena na genomu in drugimi podatki.

[Okno z rezultati](s12-genome_data_viewer_slika1.png)

Program deluje za vse genome, ki jih vsebuje.