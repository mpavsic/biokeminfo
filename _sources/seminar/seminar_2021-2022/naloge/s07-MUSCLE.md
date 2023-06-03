# Poravnava zaporedij z MUSCLE

**Avtorja**: Tinkara Butara, Gaja Starc

**Datum predstavitve**: 2022-04-28 

---
## Namen vaje
Naučili se bomo uporabljati program za poravnavo več zaporedij in spoznali za katera zaporedja je primeren.

---
## Program

Program: **[MUSCLE 3.8](https://www.ebi.ac.uk/Tools/msa/muscle/)**

Avtorji programa: Robert C. Edgar, [drive5](https://www.drive5.com/)

Reference:
-	Edgar, R.C. (2004) **MUSCLE: multiple sequence alignment with high accuracy and high throughput.** *Nucleic Acids Research* 32: 1792–1797. [10.1093/nar/gkh340](https://doi.org/10.1093/nar/gkh340)
- 	Edgar, R.C. (2004) **MUSCLE: a multiple sequence alignment method with reduced time and space complexity.** *BMC Bioinformatics* 5: 113. [10.1186/1471-2105-5-113](https://doi.org/10.1186/1471-2105-5-113)
- 	Madeira, F.; Park, Y.M.; Lee, J.; Buso, N.; Gur, T.; Madhusoodanan, N.; et al. (2019) **The EMBL-EBI search and sequence analysis tools APIs in 2019.** *Nucleic Acids Research* 47: W636–W641. [10.1093/nar/gkz268](https://doi.org/10.1093/nar/gkz268)

### Opis programa

MUSCLE je zelo zmogljiv program za poravnavo več zaporedij. Poravna lahko 5000 zaporedij povprečne dolžine 350 aminokislinskih ostankov v 7 minutah. Deluje v treh stopnjah. Najprej zgenerira poravnavo več zaporedij, pri čemer poudarja hitrost pred natančnostjo. Izračuna razdaljo za vsak par neporavnanih zaporedij in na osnovi podobnosti izračuna matriko razdalj med pari. Sledi izdelava binarnega drevesa na osnovi matrike razdalj z uporabo metode za hierarhično gručenje (UPGMA) ali z združevanjem parov. Progresivna poravnava je zgrajena tako, da sledi zapovrstju razvejitev drevesa, rezultat česar je poravnava vseh vnešenih zaporedij. 

Cilj druge stopnje je izboljšava drevesa in izdelava nove progresivne poravnave na osnovi le-tega. Največja nenatančnost prve stopnje je namreč aproksimacija razdalj med neporavnanimi zaporedji in posledično izdelava suboptimalnega drevesa. Ta stopnja se po potrebi večkrat ponovi. Podobnost para zaporedij se izračuna na osnovi njegove poravnave znotraj trenutne poravnave več zaporedij. Novo drevo je skonstruirano na osnovi izračuna matrike Kimura razdalj (razdalje za poravnan par) in z iskanjem skupkov (ang. clustering) po tej matriki. Predhodna drevesa se nato primerja z novimi. Pri tem se identificira notranje vrzeli, kjer je prišlo do spremembe v zaporedju razvejitev. Sledi izgradnja nove progresivne poravnave - obstoječa poravnava se ohrani za vsako poddrevo pri katerem se zaporedje razvejitev ne spremeni. 

Tretja stopnja izvaja ponavljajoče se izpopolnjevanje poravnave. Z izbrisom roba (točka razvejitve) se drevo razdeli na dve ločeni poddrevesi. Sledi izračun poravnave zaporedij v obeh poddrevesih. Profil (večkratna poravnava) vsakega poddrevesa je pridobljen iz trenutne poravnave več zaporedij. Stolpci, ki vsebujejo le vrzeli, so zavrženi. Ohranjeni profili pa so ponovno medsebojno poravnani z uporabo poravnave profil-profil. Na osnovi nove poravnave med profiloma se izračuna ocena vsote parov (angl. sum of pairs) za poravnavo. Če je poravnava boljša, se ohrani, sicer se zavrže. Tretja stopnja se izvaja dokler ni dosežena določena stopnja konvergence ali s strani uporabnika določena meja. 

MUSCLE se uporablja za poravnavo več zaporedij pri čemer je omejitev 500 zaporedij ali datoteka velikosti 1 MB. Program ni namenjen poravnavam parov zaporedij.

![Opis programa](s07-MUSCLE-opis_programa.png)


### Vhodni podatki
Kot vhodne podatke lahko vnesemo več zaporedij v formatih GCG, FASTA, EMBL, GenBank, PIR, NBRF, PHYLIP ali UniProtKB/Swiss-Prot. Lahko jih navajamo posamično v ustrezno okence ali kot datoteko.

---
## Navodila

### Vhodni podatki

Kot vhodne podatke uporabite:
- [aminokislinsko zaporedje prokatepsina L pri različnih organizmih](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/seminar/s07-MUSCLE-vhod1.txt)
- [aminokislinska zaporedja različnih encimov](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/seminar/s07-MUSCLE-vhod2.fasta)

### Postopek dela
1.	Odpremo [MUSCLE 3.8](https://www.ebi.ac.uk/Tools/msa/muscle/).
2.	Naložimo datoteko ali prilepimo aminokislinska zaporedja v podprtem formatu v ustrezno okno.
3.	Lahko izberemo izhodni format ali uporabimo privzetega (ClustalW).
4.	Poženemo program.

### Pričakovani rezultati in razlaga
![Rezltat1](s07-MUSCLE-rezultat1.PNG)

Rezultat se ujema z rezultatom, ki ga dobimo s Clustal Omega.
Filogenetsko drevo je glede na povezave med organizmi smiselno.

![Rezultat2](s07-MUSCLE-rezultati_zdruzeni.PNG)

V tem primeru se filogenetski drevesi ne ujemata. Nenavadna je bližnja sorodnost nekaterih človeških encimov z encimom RUBISCO pri špinači. 
Uporaba kratkega izmišljenega zaporedja 'random' ilustrira, da je pri uporabi kratkih zaporedij enostavno dobiti dobro poravnavo. 