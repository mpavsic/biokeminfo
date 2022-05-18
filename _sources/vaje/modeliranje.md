# VAJA: Modeliranje na osnovi homologije

Pri modeliranju struktur proteinov lahko uporabljamo različne pristope, najhitrejši in najbolj zanesljivi so pa tisti, ki temeljijo na osnovi homologije. Na slednjo sklepamo iz podobnosti ak-zaporedij tarčnega proteina (tj. protein, ki ga modeliramo) in proteinov z znano (eksperimentalno določeno) strukturo iz zbirke struktur. Na voljo je kar nekaj orodij, ki temeljijo na različnih principih (modeliranje na osnovi homologije, *ab initio*, kombinacija pristopov) in algoritmih, morda najpogosteje pa se uporabljajo naslednja:
- [SWISS-MODEL](https://swissmodel.expasy.org/)
- [I-TASSER](https://zhanggroup.org/I-TASSER/)
- [Rosetta](https://www.rosettacommons.org/software), ki jo je treba z nekaj truda nainstalirati lokalno, dostopna pa je tudi preko strežnika [Robetta](https://robetta.bakerlab.org/)
- [AlphaFold2](https://github.com/deepmind/alphafold), ki ga lahko poganjamo lokalno ali pa izkoristimo [iPython Notebook v Google Colab](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)


## SWISS-MODEL

Eno izmed uporabnikom zelo prijaznih in za uporabo preprostih orodij je [SWISS-MODEL](https://swissmodel.expasy.org/):
![SWISS-MODEL vstopna stran](slike/modeliranje-swissmodel1.png)

Interaktivno modeliranje zaženemo s pritiskom na gumb `Start Modelling`. Kot vhodni podatek vnesemo ak- zaporedje v formatu FASTA (ali kar UniProt kodo zapisa), eventuelno lahko "projektu" določimo ime in opcijsko vpišemo še e-poštni naslov (v primeru, da modeliranje traja dlje in nas o rezultatih obvesti prek e-pošte). Na voljo imamo iskanje po predlogah (`Search For Templates`), kjer nam predlaga eno ali več možnih struktur kot predloge (izberemo eno ali več, za vsako nam naredi ločen model), ali pa kar kliknemo `Build Model`, kjer program sam izbere zanj najbolj smiselno predlogo in izračuna en model.
![SWISS-MODEL vnos](slike/modeliranje-swissmodel2.png)

Podrobnosti in navodila so opisana v [dokumentaciji](https://swissmodel.expasy.org/docs/help).

## AlphaFold2

AlphaFold2 lahko v osnovni varianti poganjamo v obliki iPython zvezka v storitvi Google Colab (zvezek je v Google Drive), a je ta način za vaje manj primeren, saj modeliranje lahko traja dlje časa (pri brezplačnem računu smo omejeni z računskimi viri), prav tako pa ni primeren za modeliranje večjih proteinov, saj hitro presežemo omejitve osnovnega brezplačnega uporabniškega računa.

Da bi pa bili modeli, izračunani z AlphaFold2, dostopni čim širši javnosti, so v EBI pripravili podatkovno zbirko vnaprej izračunanih modelov številnih proteinov, dne 2022-05-03 je šlo za 992.316 proteinov. Gre za celoten človeški proteom ter proteome nekaterih modelnih organizmov, vsi ti modeli pa so dostopni preko posebne spletne strani [AlphaFold2 EBI](https://alphafold.ebi.ac.uk/), povezave do modelov pa so dodane tudi v kategorijo *Structure* v zbirki [UniProt](https://www.uniprot.org/).

![AlphaFold Model Database](slike/modeliranje-alphafold_database.png)

Modele si lahko na Strani UniProt oz. v podatkovni zbirki na EBI ogledamo kot 3D modele, pobarvane glede na zanesljivost napovedi strukture (pLDDT, *per-residue confidence score*, v razponu od 0 do 100). Pri regijah z nizko pLDDT gre pogosto za strukturno neurejene regije.



---

## Naloga 1
Zanima nas struktura celotnega človeškega klavdina-7 (claudin-7). Poiščite strukturo/model oz. ga sami pripravite ter ga analizirajte v smislu realnosti.

Potek reševanja:
1. Glavne značilnosti človeškega klavdina-7 si oglejte v zbirki UniProt. Je morda v tej bazi povezava na že pripravljen model in če je, je ta model zadovoljiv? Kako bi lahko pripravili boljši model?
2. Pripravite model omenjenega proteina s programom [SWISS-MODEL](http://swissmodel.expasy.org/), model z [I-TASSER](http://zhanglab.ccmb.med.umich.edu/I-TASSER/) pa je že pripravljen (za ta program se je potrebno registrirati, izračun pa traja kak dan) in sicer:
   * rezultati modeliranja s privzetimi nastavitvami (kot vhodni podatek je bilo dano ak-zaporedje klavdina-7) so zbrani v datotekah:
      * posamezni modeli: [model1](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default-model1.pdb), [model2](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default-model2.pdb), [model3](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default-model3.pdb), [model4](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default-model4.pdb) in [model5](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default-model5.pdb)
      * [izpis strani](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default-log.pdf) z rezultati modeliranja v formatu PDF
      * celoten izhod: [ITASSER-CLDN7_HUMAN_default.zip](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/ITASSER-CLDN7_HUMAN_default.zip)
   * rezultati modeliranja, pri katerem eksplicitno NISO bile upoštevane strukture s PDB kodami 4p79 in 3x29 je v datoteki I-TASSER-hCldn7_excluded_4p79_3x29.zip (te strukture so v času priprave modela bile edine, ki so predstavljale smiselne predloge za strukturo, danes je to nekoliko drugače, saj je struktur več):
      * posamezni modeli: [model1](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29-model1.pdb), [model2](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29-model2.pdb), [model3](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29-model3.pdb), [model4](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29-model4.pdb) in [model5](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29-model5.pdb)
      * [izpis strani](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29.pdf) z rezultati modeliranja v formatu PDF
      * celoten izhod: [I-TASSER-hCldn7_excluded_4p79_3x29.zip](https://github.com/mpavsic/biokeminfo/blob/main/biokeminfo/vaje/izhod/I-TASSER-hCldn7_excluded_4p79_3x29.zip)
3. Poiščite tudi model tega proteina, izračunanega z AlphaFold2.
4.  Najboljše modele, dobljene iz posameznih orodij, primerjajte med seboj in s strukturo, uporabljeno kot predlogo za modeliranje na osnovi homologije (superpozicija v UCSF Chimera), prav tako pa jih ocenite v smislu “realnosti” (so modeli v skladu s pričakovanju na osnovi zapisa v zbirki UniProt?).

## Naloga 2
Vsak si naj izbere en protein (priporočam, da izberete bolj "eksotične" proteine ali pa proteine iz "eksotičnih" organizmov), za katerega:
1. z iskanjem po zbirki PDB preko programa BLAST preverite, ali je znana struktura točno tega proteina; če je znana struktura, ki pokriva večji del zaporedja izbranega proteina, si izberite drug protein;
2. izdelajte model s pomočjo programa SWISS-MODEL, in sicer za celotni protein (seveda odstranite morebitni signalni peptid in/ali proregije);
3. model, ki ga izračunate, in pa strukturo, uporabljeno kot predlogo, naložite v program UCSF Chimera in primerjajte preko superpozicije (*MatchMaker*).

Odgovorite na vprašanja:
1. Ali model pokriva celotno ak zaporedje, ki ste ga uporabili? Zakaj da oz. ne?
2. So med modelom in uporabljeno predlogo v katerih regijah večje razlike? Katerimi? Zakaj?
3. Kako je z zanesljivostjo modela vzdolž aminokislinskega zaporedja?
4. Bi lahko model kako izboljšali? Kako?