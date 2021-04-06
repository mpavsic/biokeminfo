# VAJA: Poravnave več zaporedij


---
## Naloga 1: enostavna poravnava več zaporedij

Ločeno pripravite poravnavo približno desetih ak-zaporedij za alfa in beta verigo hemoglobina (HBA oz. HBB) iz različnih organizmov (pri tem za beta verigo uporabite zaporedja iz istih organizmov kot ste jih uporabili za alfa verigo) ter primerjajte drevesi, ki jih dobite z metodo združevanja sosedov (NJ, neighbour joining).

Za izračun poravnave uporabite [**Clustal Omega**](https://www.ebi.ac.uk/Tools/msa/clustalo/), drevo skonstruirajte s **Clustal Phylogeny** (direktna povezava iz Clustal Omega), oglejte pa si ga v programu phylo.io, kjer lahko vizualizirate dve drevesi hkrati in ju primerjate. Opazite kakšne razlike?

Drevesi lahko enostavno primerjate tako, da podatke za njihov izris (to niso zaporedja, ampak razdalje!) prilepite v program [Phylo.io](https://phylo.io/).

---
## Naloga 2: klasifikacija domen

### Ozadje
Pri tej vaji bomo »uporabili« zaporedji dveh proteinov, s katerimi smo že delali in sicer EpCAM in Trop2 (proteina sta paraloga). Za kakšna proteina gre si lahko preberete npr. v zbirki UniProt. Vse domene niso anotirane, med drugim ne majhna prva domena zunajceličnega dela, ki se nahaja med signalnim peptidom (le-ta se seveda odcepi) in tiroglobulinsko domeno (TY). To domeni članki pogosto klasificirajo kot EGF-podobno domeno (EGF = epidermal growth factor) in sicer na osnovi njene velikosti/majhnosti ter števila cisteinskih aminokislinskih ostankov.

### Naloga
Na osnovi poravnav več zaporedij omenjene domene (za proteine EpCAM in Trop2 iz večih organizmov, ter EGF-podobne iz večih organizmov) podprite ali ovržite klasifikacijo te domene kot EGF-podobne domene. Preverite pravilnost poravnave s pomočjo anotacij v UniProt.

Za to domeno iz proteinov EpCAM in Trop2 ter tudi za EGF-podobne domene pripravite tudi ločene poravnave več zaporedij, na njihovi osnovi pa t. i. sequence logo ter ju primerjajte. Logo pripravite s pomočjo programa [WebLogo](http://weblogo.threeplusone.com/).

---
## Naloga 3: povezava med HIV in SIV

### Ozadje
Sindrom pridobljene imunske pomanjkljivosti (AIDS) se razvije zaradi okužbe z virusom HIV (human immunodeficiency virus). Pri človeku poznamo dva tipa virusa HIV in sicer HIV-1 in HIV-2, ki sta si med seboj precej podobna, je pa HIV-2 nekoliko bolj razširjev v zahodni Afriki, prav tako pa je nekoliko manj infektiven kot virus HIV-1. Podobne viruse so odkrili tudi pri drugih primatih, npr. opicah, kjer se virus imenuje SIV (simian immunodeficiency virus). HIV in SIV spadata med lentiviruse, le-ti pa med retroviruse, katerih genom je predstavlja enoverižno RNA (ssRNA). Po vstopu v gostiteljske celico se ssRNA preko reverzne transkripcije prepiše v dsDNA, ta pa se vstavi v genom gostiteljske celice, kjer potem služi kot matrica za nove kopije virusne RNA. Okužba z virusom HIV/SIV se prične z vezavo virusnega delca na gostiteljsko celico, pri tem pa gre za interakcijo med proteinom gp120 virusne ovojnice ter proteinom CD4 celic imunskega sistema (TH limfociti (celice pomagalke), monociti, makrofagi).

Po trenutno splošno sprejeti teoriji je virus SIV v preteklosti preskočil medvrstno bariero med opicami in ljudmi, domnevno med lovom na opice in uživanjem opičjega mesa, kjer so ljudje prišli v stik s krvjo okuženih opic. Virus se je kasneje nekoliko prilagodil, tako da je za ljudi postal bolj infektiven (učinkovitejše širjenje), in sicer preko mutacij v proteinu gp120.

### Naloga

Preko konstrukcije poravnav več ak-zaporedij proteina gp120 virusov HIV-1, HIV-2 ter variant SIV in izrisa filogenetskega drevesa poizkusite ugotoviti, kakšna je povezava med njimi. V poravnavo vključite vsaj 25 zaporedij, obvezno pa tudi proteine gp120 SIV iz šimpanza (Pan troglodytes) ter mangabeja (Cercocebus atys in sorodniki).

Oris postopka reševanja:
1. poiščite primerna ak-zaporedja (Uniprot in/ali BLAST)
2. zaporedja vnesite v datoteko formata FASTA, za imena pa dodajte HIV1, HIV1 oz. SIV ter kratko ime/kratico, s katero opišete organizem (pri SIV)
3. pripravite poravnavo s spletnim programom Clustal Omega, kjer si lahko drevo tudi ogledate
4. podatke za izris drevesa prilepite v program phylo.io, nato pa protein gp120 iz SIV šimpanza nastavite kot outgroup
5. analizirajte podobnost in sklepajte na evolucijsko sorodnost med HIV1, HIV2 in različnimi SIV

 
Alternativni postopek: poravnavo s Clustal Omega lahko sprožite neposredno iz UniProt, kjer si zaporedja, ki jih želite poravnati, dodate v košarico (Basket).

Za pripravo MSA lahko uporabite tudi kakšno drugo orodje, recimo [T-COFFEE](http://tcoffee.crg.cat/).