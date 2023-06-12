# NetGene 2 - napovedovanje mest izrezovanja


**Avtorja**: Andraž Rotar in David Valte

**Datum predstavitve**: 2022-05-04

---
## Namen vaje
Uporabiti program za napoved mest izrezovanja intronov na pre-mRNA.

---
## Program

Program: **[NetGene2 - 2.42](https://services.healthtech.dtu.dk/service.php?NetGene2-2.42)**

Avtorji programa: Brunak S., Engelbrecht J., Knudsen S., Korning P., Tolstrup N., Rouzé P. [DTU Health Tech](https://www.dtu.dk/english)

Reference:
Brunak, S.; Engelbrecht, J.; Knudsen, S.; (1991). **Prediction of human mRNA donor and acceptor sites from the DNA sequence.** Journal of molecular biology, 220(1), 49–65. [10.1016/0022-2836(91)90380-o](https://pubmed.ncbi.nlm.nih.gov/2067018/)

Hebsgaard, S. M.; Korning, P. G.; Tolstrup, N.; Engelbrecht, J.; Rouzé, P.; Brunak, S.; (1996). **Splice site prediction in Arabidopsis thaliana pre-mRNA by combining local and global sequence information.** Nucleic acids research, 24(17), 3439–3452.  [10.1093/nar/24.17.3439](https://doi.org/10.1093/nar/24.17.3439)


### Opis programa
RNA izrezovanje je proces, ki sledi transkripciji DNA v pre-mRNA. V tem procesu encimski kompleks sestavljen iz snRNP proteinov iz pre-mRNA izreže introne. To je kritična točka v post-transkripijcski regulaciji genskega izražanja in razširi fukcionalni proteom. Introni se lahko izrežejo na različnih mestih, kar omogoča nastanek več izoformov iz istega gena.

Program NetGene2 deluje kot nevronska mreža, ki deluje na podlagi večplastnega vzvratnega postopka učenja. Prva plast (input layer) sprejme vhodne podatke, druga (hidden layer) jih obdela in jim pripiše neko skrito vrednost, tretja (output layer) pa jih interpretira in poda, s tem da upošteva vrednost določeno v drugi stopnji. Nevronsko mrežo so naučili na osnovi dveh nalog, in sicer detekcije kodirajočih nukleotidov napram nekodirajočim nukelotidom ter predvidevanjem mest izrezovanja. Za vhodne podatke so uporabili zbirko GenBank, iz katere so uporabili 146 genov. Od teh so jih 109 porabili za treniranje programa, 37 pa za testiranje programa.

### Vhodni podatki

NetGene2 lahko sprejme gensko DNA zaporedje iz organizmov: *H. Sapiens*; *C. Elegans*; *A. Thaliana*;. Sprejme datoteko v obliki .fasta formata, ki pa ne sme vsebovati zaporedja krajšega od 200 nukleotidov ali daljšega od 100.000 nukleotidov.

---
## Navodila

Kot vhodne podatke uporabite:

- **Human interleukin 1-beta (IL1B) gene, complete cds** ([M15840.1](https://www.ncbi.nlm.nih.gov/nuccore/186281))
- **Homo sapiens tumor protein p53 (TP53)** ([NG_017013.2](https://www.ncbi.nlm.nih.gov/nuccore/NG_017013.2))

### Primer 1 - IL1B

**Postopek dela**
1. V okno *Sequence* prilepimo naše FASTA zporedje. Če želimo, lahko zaporedje še poimenujemo.
2. Izberemo organizem.
3. Kliknemo **Send file**
4. Kritično ovrednotimo rezultate.

### Primer 2 - p53

**Postopek dela**

Ponovimo zgornji postopek.

### Pričakovani rezultati in razlaga

Pričakovani rezultat se ne sklada s tistimi v GenBanku. Na enem H-mestu napove mesto introna pravilno, na drugem H-mestu pa zgreši.

![p53](s16-netgene2-p53.png)

Graf predstavlja verjetnost (y os) in število nukleotida na zaporedju (x os)

![graf](s16-netgene2-graf.png)
