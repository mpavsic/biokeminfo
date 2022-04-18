# SignalP – napovedovanje signalnih peptidov

**Avtorja**: Urša Zevnik, Žan Žnidar

**Datum predstavitve**: 2022-04-20

---
## Namen vaje
Uporabiti program za napoved signalnih peptidov in njihovih cepitvenih mest.

---
## Program

Program: **[SignalP 6.0](https://services.healthtech.dtu.dk/service.php?SignalP-6.0)**

Avtorji programa: Felix Teufel, José Juan Almagro Armenteros, Alexander Rosenberg Johansen, Magnús Halldór Gíslason, Silas Irby Pihl, Konstantinos D Tsirigos, Ole Winther, Søren Brunak, Gunnar Von Heijne, Henrik Nielsen; [Technical University of Denmark](https://www.dtu.dk/)

Reference:
- Teufel, F.; Almagro Armenteros, J.J.; Johansen, A.R.; Gíslason, M.H.; Pihl, S.I.; Tsirigos, K.D.; Winther, O.; Brunak, S.; von Heijne, G.; Nielsen, H. (2022) **SignalP 6.0 predicts all five types of signal peptides using protein language models.** *Nature Biotechnology*, 1–3. [10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3)
- Nielsen H, Engelbrecht J, Brunak S, von Heijne G. **Identification of prokaryotic and eukaryotic signal peptides and prediction of their cleavage sites.** *Protein Eng.* 1997 Jan;10(1):1-6. [10.1093/protein/10.1.1.](https://doi.org/10.1093/protein/10.1.1)



### Opis programa
Signalni peptid je kratko (do 30 AK) aminokislinsko zaporedje, ki omogoča sortiranje in translokacijo proteina. V ožjem pomenu besede je signalni peptid N-končni signal, ki pri evkariontih usmerja skozi membrano ER, pri prokariontih pa skozi plazmalemo. Sestoji iz pozitivno nabitega N-konca, osrednjega hidrofobnega dela s tendenco do tvorbe α-vijačnice in C-konca, kjer se zaporedje cepi. Program SignalP lahko napove le te vrste signalnih zaporedij, kar pomeni, da C-končnih signalnih peptidov, jedrnih lokalizacijskih signalov in drugih signalov za vstop v organele (razen v ER) ne bo našel.

Poleg tega SignalP ne deluje pri celotnem bakterijskem deblu *Tenericutes*, za katerega je značilen nekoliko neobičajen način translokacije (npr. sploh nimajo signalne peptidaze 1). Program nanje še ni bil prilagojen, zato signalnih zaporedij ne najde ali pa jih napove z nizko verjetnostjo (20&nbsp;%).

SignalP deluje na osnovi različnih algoritmov umetne inteligence. Enega od njih predstavljajo **jezikovni modeli**, ki v osnovi skušajo napovedati naslednjo, prejšnjo ali skrito besedo v stavku. Podlaga za učenje so besedila v želenem jeziku. Ker so tudi proteini v svojem bistvu *jezik, ki ga celica razume*, lahko ustrezno prirejene jezikovne modele uporabimo tudi za aminokislinska zaporedja.  

Pomenskost podatkov iz jezikovnega modela nadaljuje pot v **pogojno naključno polje**. Ta v času učenja vzame označene podatke in prilagaja parametre oz. lastnosti uteži (npr. koliko vpliva hidrofobnost neke AK, kako vplivajo sosednje AK) po principu pogojne verjetnosti, dokler ne doseže zadovoljivih rezultatov.

Skozi ti dve (že naučeni) plasti potujejo tudi vhodni podatki uporabnika. Rezultat je verjetnost za posamezno vrsto signalnega peptida in verjetnost, da je na nekem položaju cepitveno mesto.



### Vhodni podatki
Aminokislinsko zaporedje v besedilnem (enočrkovnem) ali FASTA-zapisu.

---
## Navodila

### Vhodni podatki
Kot vhodne podatke uporabite:
- aminokislinsko zaporedje šaperona iz *E. coli.* (*Chaperone protein PapD*, UniProt ID [P15319](https://www.uniprot.org/uniprot/P15319))
- aminokislinsko zaporedje glicerol-3-fosfat oksidaze bakterije *Mycoplasma pneumoniae* (*Glycerol 3-phosphate oxidase*, UniProt ID [P75063](https://www.uniprot.org/uniprot/P75063))



### Postopek dela
1. Odpremo [SignalP-6.0](https://services.healthtech.dtu.dk/service.php?SignalP-6.0).
2. V okno prilepimo aminokislinsko(a) zaporedje(a) v FASTA ali enočrkovnem formatu ali naložimo datoteko.
3. Če izbrana zaporedja pripadajo evkariontskemu organizmu, označimo Eukarya, da preprečimo iskanje tipov signalnih zaporedij, ki jih pri teh organizmih sploh ni.
4. Izberemo, ali želimo krajši ali daljši output format. *Izbira krajšega je smiselna, ko sočasno vnesemo veliko število zaporedij, drugače pa izberemo daljšega, kjer zraven dobimo še grafe.*
5. Ponavadi je dovolj, če izberemo hitrejši način. *Počasnejši je bolj natančen, predvsem pri določanju točne meje signalnega zaporedja, vendar vzame šestkrat več časa.*


### Pričakovani rezultati in razlaga
![Napoved signalnih peptidov za šaperon E. coli](s01-signalp-rezultat.png)

Vodoravna os na grafu prikazuje aminokislinsko zaporedje, navpična pa verjetnost. Rdeča polna črta nam nakazuje N-končni del signalnega peptida, oranžna hidrofobno regijo, rumena pa C-konec signalnega peptida. Zelena črtkana črta označuje mesto cepitve. Rdeča črtkana črta pa predstavlja nesignalni del proteina.

Rezultat se sklada z označbo v UniProtu.
