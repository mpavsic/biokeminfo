# Napoved lokalizacije proteinov - DeepLoc
**Avtorja**: Ena Kartal, Nataša Vujović

**Datum predstavitve**: 2022.04.20

-----
## Namen vaje
Namen vaje se je naučiti uporabljati DeepLoc za napoved lokalizacije evkariontskih proteinov na osnovi njihovega aminokislinskega zaporedja.

-----
## Program
Program: [**DeepLoc - 1.0 - Services - DTU Health Tech**](https://services.healthtech.dtu.dk/service.php?DeepLoc-1.0)

Avtorji programa: Jose Juan Almagrp Armenteros, DTU Bioinformatics, University of Copenhagen, (https://www.dtu.dk/english)

Reference:
-Almagro Armenteros, J.J.; Sønderby, C.K.; Sønderby, S.K.; Nielsen, H.; Winther, O.; (2017) **DeepLoc: prediction of protein subcellular localization using deep learning.** *Bioinformatics*,[10.1093/bioinformatics/btx431](https://doi.org/10.1093/bioinformatics/btx431)
### Opis programa
Program DeepLoc uporablja globoke nevronske mreže(deep neural networks) za napovedovanje subcelične lokalizacije proteinov, ki temeljijo samo na informaciji o zaporedju. Model za napovedovanje uporablja ponavljajočo se nevronsko mrežo, ki obdeluje celotno zaporedje proteinov in mehanizem, ki identificira proteinske regije, pomembne za subcelično lokalizacijo. Model je bil usposobljen in preizkušen na naboru podatkov o proteinih, ki so pridobljeni iz najnovejše izdaje UniProt, v kateri eksperimentalno označeni proteini sledijo ostrejšim kriterijim kot prej. Model doseže dobro natančnost(78% za 10 kategorij in 92% za topne ali membransko vezne).
![DeepLoc](s04-deeploc-pregled.jpg)
### Vhodni podatki
Aminokislinska zaporedja evkariontskih proteinov v FASTA formatu. Deluje za proteine, ki vsebujejo več kot 10 in ne več kot 6000 aminokislin.

-----
## Navodila
### Vhodni podatki
Kot vhodne podatke uporabite :

- aminokislinsko zaporedje človeškega inzulisnekga receptorja (UniProtKB ID [P06213])
  (https://www.uniprot.org/uniprot/P06213#sequences)
- aminokislinsko zaporedje citokroma b pri pekarskem kvasu- baker's yeast (UniProtKB ID [P00163]
  (https://www.uniprot.org/uniprot/P00163#sequences)
### Postopek dela
-Odprite spletno stran UniProt in kopirajte aminokislinsko zaporedje v FASTA formatu.
-Odprite spletno stran DeepLoc in prilepite aminokislinsko zaporedje v okvir.
-Izberite opcijo Blosum62, potem pa Submit.
### PriÄŤakovani rezultati in razlaga:
Program za prvi primer pravilno poda subcelično lokalizacijo proteinov. Eksperimentalno določeno lokacijo lahko preverimo v UniProtu.
Pri drugem zaporedju program poda napačen rezultat. To se zgodi, ko vzamemo primer aminokislinskega zaporedja proteina za taksonomsko skupino, ki ima omejeno število podatkov ampak je eksperimentalno določena subcelična lokacija proteina.
