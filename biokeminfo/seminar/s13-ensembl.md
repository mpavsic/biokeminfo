# Ensembl genome browser 106

**Avtorja**: Klara Kočman, Martin Stanonik

**Datum predstavitve**: 2022-05-04

---
## Namen vaje
Pregled izbranega gena vretenčarskega organizma ter vpogled v mutacije na izbranem genu.

---
## Program

Program: [Ensembl](https://www.ensembl.org/index.html)

Avtorji programa: European Bioinformatics Institute https://www.ebi.ac.uk/ 

Reference:
-Cunningham , F., Allen, J. E., Allen, J., Alvarez-Jarreta, A., Ridwan Amode, M., Armean , I. M., Austine-Orimoloye, O., Azov, A. G., Barnes, I., Bennett, R., Berry, A., Bhai, J., Bignell, A., Billis,K., Boddu, S., Brooks, L., Charkhchi, M., Cummins , C., Da Rin Fioretto, L., Davidson, C., Dodiya, K., Donaldson, S., Houdaigui, B., E., Naboulsi, T., E., Fatima, R., Giron, C. G., Genez, T., Martinez, J. G., Guijarro-Clarke, C., Gymer, A., Hardy, M., Hollis, Z., Hourlier, T., Hunt, T., Juettemann, T., Kaikala, V., Kay,M., Lavidas, I., Le, T., Lemos, D., Marugán, J. C., Mohanan, S., Mushtaq, A., Naven, M., Ogeh, D. N., Parker, A., Parton, A., Perry, M., Piliˇzota, I., Prosovetskaia, I., Sakthivel, M. P., Salam, A. I. A., Schmitt, B. M., Schuilenburg, H., Sheppard, D., Pérez-Silva, J. G., Stark, W., Steed, E., Sutinen, K., Sukumaran, R., Sumathipala, D., Suner, M. M., Szpak, M., Thormann, A., Tricomi, F. F., Urbina-G ́omez, D., Veidenberg, A., Walsh, T. A., Walts, B., Willhoft, N., Winterbottom, A., Wass, W., Chakiachvili, M., Flint, B., Frankish, A., Giorgetti, S., Haggerty, L., Hunt, S. E., IIsley, G. R., Loveland, J. E., Martin, F. J., Moore, B., Mudge, J. M., Muffato, M., Perry, E., Ruffier, M., Tate, J., Thybert, D., Trevanion, S. J., Dyer, S., Harrison, P. W., Howe, K. L., Yates, A. D., Zerbino, D. R., Flicek, P.; 2022 **Ensembl 2022.***Nucleic Acids Res* 50, D988â“D995.
[10.1093/nar/gkab1049](https://doi.org/10.1093/nar/gkab1049)

### Opis programa

Samo človeški genom sestavlja na milijarde baznih parov, ki tvorijo okoli 25000 genov. Genom nam sam po sebi ne pove veliko, zato potrebujem orodje s pomočjo katerega se lažje orientiramo ter vsebuje vse potrebne informacije glede genov v genomu. 
Program je bil razvit s namenom dostopa do najnovejših podatkov. Razvit je bil leta 1999 za pregled človeškega genoma, vendar se danes uporablja tudi za gene ostalih vretenčarjev. Podatki zaporedja se vnesejo v sistem za beleženje genov (zbirka programske opreme imenovane pipeline). Ta ustvari niz predvidenih lokacij gena ter poravnav glede na kodirajoča se zaporedja ter jih shrani v MySQL zbirki. 
V Ensemblu se nahajajo programsko in ročno pregledani geni, združeni v tako imenovani GENECODE GENESET. Poleg anotacij so v programu tudi orodja za pregled variacij genov, primerjalno genomiko ter pregled regulacijskih značilnosti. S pomočjo programa lahko tudi raziskujemo podrobnosti genskih regij, na katerem mestu se zgodi kakšna mutacija ter kako nevarne so te mutacije. 
Leta 2009 so odprli spletni portal za iskanje genomov rastlin, gliv, bakterij, protistov in metazojev.

### Vhodni podatki

Ime gena vrentenčarja

---
## Navodila
- Kakšna mutacija v zbirki dbSNP se zgodi na mestu 108329199 v genu ATM? Ali je nevarna, kakšno bolezen povzroči?
- Koliko mutacij povzroči izgubo stop kodona na tem genu?

### Vhodni podatki
Za vhodni podatek uporabite:
- gen ATM(atm, Genebank ID. [472](https://www.ncbi.nlm.nih.gov/gene/472)

### Postopek dela
1. V iskalno okence vpišite ime gena ATM
2. Dobite seznam genov, ki najbolj utrezajo podanem imenu. Na desni je podan najboljši rezultat, ki se tudi nahaja na vrhu seznama, na katerega kliknite 
![Primer-ENSEMBL](s13-ensembl-slika1.png)
3. Pred sabo imate prikazano tabelo z označenimi regijami ter kje so kodirani eksoni ter introni. Na levi strani se nahaja tabela na kateri kliknite Variant table
4. Prikaže se vam tabela z mogočimi mutacijami v tem genu.
![Primer-ENSEMBL](s13-ensembl-slika2.png)
5. Z uporabo filtrov poiščite želene mutacije
6. Za prvo vprašanje vpišemo v tabelo mesto kjer se mutacija pojavi ter filtriramo po zbirki dbSNP
7. Na spletno mesto OMIM vpišem podani gen. Pod molecular genetics, na levi strani, poiščemo tabelo kjer se nahajajo želene variacije in identificiramo bolezen ki jo mutacija povzroča.
8. Pri drugi nalogi pa z filtri podanimi nad tabelo izločimo želene mutacije. 

### Pričakovani rezultati in razlaga
V Ensemblu:
- v tabeli se nam, ko s pomočjo filtrov najdemo pravo mutacijo, prikaže kje ter kakšna se mutacija pojavi, kaj povzroči, če je patogena ter njen ID in v tabeli različni algoritmi predvidijo nevarnost mutacije. Če se rezultati teh algoritmov razlikujejo je potrebno izvesti dodatno raziskavo glede te mutacije.
- Naši prvi mutaciji je prikazano da je nevarna, ker se spremeni bazni par (single nucleotide change:SNP)(A/G) in posledično aminokislinsko zaporedje v proteinu (missense variant). Algoritmi pa podajo različne verjetnosti nevarnosti zato gremo preverit mutacijo v OMIM. 
![Primer-ENSEMBL](s13-ensembl-slika3.png)
- V drugi nalogi je prikazano da samo dve mutaciji povzročita izgubo stop kodona.
![Primer-ENSEMBL](s13-ensembl-slika4.png)
Vse mutacije se zgodijo na 11 kromosomu kjer se gen nahaja.

V OMIM:
- v tabeli, do katere prideš z zgornijimi navodili, je značeno koliko mutacij se pojavi v podanem genu, kakšno bolezen povzročajo ter njihov ID v različnih zbirkah
- O naši mutaciji v prvi nalogi (22 mutacija) je zapisano da povzroča raka na limfatičnem sistemu (Mantle cell lymphoma).
![Primer-OMIM](s13-ensembl-slika5.png)

