# VAJA: Iskanje podobnih zaporedij z BLAST

Pri vaji bomo uporabljali spletno različico programa **BLAST** (Basic Local Alignment Search Tool), ki teče na strežniku NCBI na tem naslovu: [https://blast.ncbi.nlm.nih.gov](https://blast.ncbi.nlm.nih.gov).

Do tega strežnika lahko dostopamo tudi prek API (npr. iz Pythona), kjer uporabimo REST, kar smo že spoznali; tak način dostop je opisan [tukaj](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=DeveloperInfo). BLAST lahko poganjamo tudi lokalno, t. j. na lastnem računalniku, pri čemer pa seveda potrebujemo tudi neko zbirko zaporedij, po kateri bomo iskanje izvajali.

---
## Naloga 1: enostavno iskanje
Na novo smo prišli v raziskovalni laboratorij, kjer moramo nadaljevati z raziskovalnim projektom njihovega prejšnjega sodelavca. Čaka nas nehvaležno delo, da uredimo epice z vzorci plazmidov. Ta prejšnji sodelavec je bil namreč precej nemaren, saj je za seboj pustil kup pomanjkljivo označenih vzorcev. Tako smo recimo naleteli na epico, ka kateri piše »pET-22/insert«. Le kaj je ta insert?

Plazmid smo poslali na sekvenciranje, pri tem pa uporabili univerzalni smerni in protismerni oligonukleotid, ki se vežeta na del zaporedja za T7 promoter (pod katerim so vključki za izražanje v plazmidih sistema pET) oz. T7 terminator. Dobljeni zaporedji smo lahko sestavili v enotno zaporedje, ki je priloženo spodaj.

**Vprašanje**: Za kateri protein kodira vključek v vektorju?

```
GGAATTGTGAGCGGATAACAATTCCCCTCTAGAAATAATTTTGTTTAA
CTTTAAGAAGGAGATATACATATGGGTATGACACGTATGCTGCTGGAG
TGCTCCCTGAGCGATAAGCTTTGCGTGATCCAGGAGAAACAATATGAG
GTGATTATCGTGCCGACCTTGTTGGTGACCATCTTTCTTATTCTGCTG
GGCGTGATTCTGTGGCTGTTTATTCGCGAGCAACGCACGCAACAGCAG
CGCTCTGGCCCACAGGGAATCGCGCCCGTGCCTCCGCCACGCGATCTC
TCCTGGGAAGCGGGCCACGGGGGAAACGTAGCCCTCCCCCTGAAAGAA
ACGTCGGTGGAAAATTTCCTGGGGGCGACTACCCCAGCACTCGCGAAA
CTGCAGGTTCCGCGCGAACAGTTGTCTGAAGTATTGGAGCAGATTTGC
AGCGGGTCATGTGGGCCTATTTTTCGTGCGAACATGAACACAGGCGAT
CCTAGTAAACCCAAATCTGTCATCCTGAAAGCCCTGAAGGAACCGGCC
GGATTGCATGAAGTTCAGGACTTTCTTGGCCGTATTCAGTTTCACCAG
TATCTTGGCAAACATAAAAACTTGGTGCAACTGGAAGGCTGCTGCACC
GAGAAACTGCCGCTGTACATGGTATTGGAAGACGTCGCCCAGGGGGAT
CTGCTGTCATTCCTGTGGACATGTCGCCGCGACGTGATGACTATGGAT
GGCCTGCTGTACGATCTGACTGAAAAACAGGTGTACCATATCGGTAAA
CAGGTGTTACTCGCGCTTGAATTTCTGCAGGAAAAGCACCTGTTCCAT
GGTGACGTGGCGGCCCGCAATATTTTAATGCAGTCTGATTTGACCGCG
AAACTGTGCGGGTTGGGTTTAGCGTATGAAGTTTATACGCGCGGCGCT
ATTTCTTCCACCCAGACAATCCCGCTCAAATGGTTAGCACCCGAGCGC
CTGCTTCTTCGCCCAGCATCGATCCGCGCGGATGTTTGGTCTTTCGGC
ATCTTACTGTACGAGATGGTCACTCTTGGCGCGCCACCCTATCCGGAA
GTCCCGCCCACCAGTATCCTGGAGCATCTGCAGCGCCGCAAAATTATG
AAGCGCCCAAGTAGCTGCACGCATACAATGTACTCTATCATGAAAAGC
TGCTGGCGTTGGCGCGAAGCGGACCGCCCGTCCCCGCGCGAACTGCGC
CTTCGTCTTGAAGCAGCCATTAAAACGGCCGATGATGAGGCCGTCCTG
CAGGTCCCGGAATTGGTTGTTCCGGAATTATACGCTGCGGTGGCCGGG
ATTCGCGTGGAAAGCCTGTTTTATAACTACAGTATGCTGTAACTCGAG
CACCACCACCACCACCACTGAGATCCGGCTGCTAACAAAGCCCGAAAG
GAAGCTGAGTTGGCTGC
```

---
## Naloga 2: homologi


1. V zbirki Genbank (t.j. Nucleotide na NCBI) poiščite zaporedje mRNA za inzulin pri zlatem hrčku (*Mesocricetus auratus*).
2. S tem zapisom (uporabite celotno zaporedje, ne samo kodirajočo regijo) iščite z `blastn` (*nucleotide blast*) po (za iskanje prilepite zaporedje v FASTA formatu, lahko pa tudi brez naslovne vrstice, ali pa uporabite kar kodo za dostop - *accession code*):
   * celotni zbirki `nr` (*non-redundant database* - oglejte si, iz česa je sestavljena!) in med zadetki identificirajte najbolj smiselen zadetek, ki predstavlja človeški homolog, in
   * po zaporedjih v zbirki Human Genomic plus Transcript (Human G+T); spet, identificirajte človeški homolog.

**Vprašanja**:
* Pri vsakem iskanju si oglejte rezultate iskanja (stran posameznega iskanja pustite odprto, da boste lažje primerjali rezultate obeh iskanj med seboj) in identificirajte vrednosti, ki vam jih izračuna BLAST (pomagajte si s slikami s predavanj).
* Kako veliki sta zbirki, po katerih ste iskali? Kakšno je razmerje velikosti zbirk, po katerih ste iskali, ter kakšno je razmerje vrednosti E za zgoraj omenjena zadetka (človeški homolog)?
* Če vzamemo 10-krat večjo zbirko, kakšna bo E-vrednost za isti zadetek, če se nahaja v tej večji zbirki?
* Katero drugo različico programa blast bi lahko uporabili za namen iskanja homolognega proteina pri človeku, če iščemo z nukleotidnim zaporedjem?

---
## Naloga 3: iskanje s kratkim zaporedjem


1. Kaj pa, če za iskanje uporabimo neka kratka nukleotidna zaporedja? Recimo, da si jih izdelamo tako, da naredimo naključna zaporedja... Uporabite orodje [SeqGen](http://www.cbs.dtu.dk/biotools/SeqGen-1.0/)  ki vam lahko zgenerira naključna nukleotidna in aminokislinska zaporedja, ter za začetek zgenerirajte 3 nukleotidna zaporedja dolžine 25.
2. S temi tremi zaporedji pojdite v blastn in jih skupaj (v formatu FASTA) prilepite v iskalno polje (iščete lahko namreč z večimi zaporedji hkrati); vse nastavitve pustite na privzetih vrednostih, posebej pazite pa na:
   * zbirka: nr,
   * spremenite program: blastn (Somewhat similar sequences)
   * izključite možnost Automatically adjust parameters for short input sequences

**Vprašanja**:
* Ste našli kakšne zadetke? Če da, kolikšna je identičnost ter vrednost poravnave in vrednost E?
* Kaj bi to pomenilo v praksi? Namig: PCR.


1. Iskanje ponovite na podoben način, s tem da uporabite program blastp in iščite s tremi naključnimi aminokislinskimi zaporedji. Upoštevajte, da je algoritem za blastn in blastp nekoliko drugačen; medtem, ko je za blastn potrebno točno ujemanje z besedo (to potem služi kot seme za poravnavo) je za blastp potrebno približno ujemanje z besedo, dobljeno z razkosanjem in variiranjem iskalnega zaporedja). Uporabite:
   * zbirka: nr,
   * program: blastp
   * izključite možnost Short queries
2. Če ne dobite zadetkov, povečajte največjo vrednost E, za katero prikaže rezultate.

**Vprašanje**: Kakšni so sedaj rezultati iskanja (v primerjavi z iskanjem z naključnimi nukleotidnimi zaporedji)?

---
## Naloga 4: ortologi
Naloga se nanaša na protein alfa-aktinin, ki je pomemben za urejanje aktinskih filamentov v snope in mreže, najdemo pa ga tako v mišičnih kot tudi nemišičnih celicah.


1. Koliko genov za α-aktinin ima miš in kje se izražajo? Katereo zbirko ste uporabili in zakaj? Kakšne so druge alternative iskanja?
2. S pomočjo programa BLAST (Basic Local Alignment Search Tool) poiščite človeški ortolog mišjega α-aktinina 1. Kako lahko preverite, da ste dejansko našli ortolog?
3. Poiskusite poiskati homolog mišjega α-aktinina 1 pri etrušanski rovki. Katero obliko orodja BLAST je najbolj smiselno uporabiti in zakaj?
4. Kaj pa mišjega α-aktinina 1 pri evropskem bobru? Kakšen način iskanja z BLAST je najprimernejši in zakaj?

![Etruščanska rovka](https://upload.wikimedia.org/wikipedia/commons/f/ff/Suncus_etruscus.jpg)
*Etruščanska rovka je najmanjši sesalec na svetu, v povprečju tehta manj kot 2 g. Njena velikost oz. masa je na spodnji meji, ki še omogoča ohranjanje stalne telesne temperature.* Vir slike: [Wikipedia](https://en.wikipedia.org/wiki/Etruscan_shrew).

---
## Naloga 5: Virusni genom
"V roke" dobimo pacienta, okuženega z nekim virusom. Iz njegove sluznice uspemo izolirati virus in ga namnožiti v celični kulturi ter posekvencirati kratek del njegovega genoma. Zaporedje je spodaj.

```
GTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGC
TGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTT
GACAGGACACGAGTAACT
```

**Vprašanje 1**: Za kateri virus najverjetneje gre in kako je sestavljen genom tega virusa?

Virusi pogosto sintetizirajo več sicer posamičnih proteinov kot eno polipeptidno verigo (poliprotein), ki ga potem kakšen virusni encim (proteaza) cepi na posamezne odseke, ki predstavljajo funkcionalne proteine. Ima takšno proteazo tudi naš virus? Kateremu odseku genoma ustreza?

**Vprašanje 2**: Če bi načrtovali inhibitor te proteaze z namenom blokiranja procesiranja poliproteina in s tem inhibiranja virusnega replikacijskega cikla, katero znano proteinsko strukturo bi lahko uporabili za analizo in za modeliranje strukture naše proteaze na osnovi homologije?

---
## Naloga 6: PSI-BLAST
PSI-BLAST je kratica za position-specific interative BLAST, kjer se zadetki iskanja uporabijo za pripravo pozicijsko utežene matrike zamenjav, slednja pa za novo (ponovljeno - iterirano) iskanje. Tako so na ključnih (ohranjenih) mestih bolje (pozitivno) točkovani ak-ostanki, ki so značilni za neko pozicijo, kar omogoča detekcijo bolj oddaljenih homologov, pri katerih je morda dobro ohranjenih zgolj nekaj ak-ostankov, ključnih za npr. katalizo (če govorimo o encimih). Iskanje se lahko potem še večkrat ponovi, pri vsaki iteraciji lahko dodamo nova najdena zaporedja za izdelavo nove pozicijsko-utežene matrike (PSSM).

Zanimajo nas homologi proteina s spodnjim zaporedjem. Za analizo bomo uporabili zbirko dobro anotiranih zaporedij UniProt/Swissprot, torej ne celotne zbirke nr (non-redundant). Radi bi tudi ugotovili, kateri so ak-ostanki zaporedja, ključni za delovanje tega proteina.

```
MKDTDLSTLLSIIRLTELKESKRNALLSLIFQLSVAYFIALVIVSRFVRYVNYITYNNLV
EFIIVLSLIMLIIVTDIFIKKYISKFSNILLETLNLKINSDNNFRREIINASKNHNDKNK
LYDLINKTFEKDNIEIKQLGLFIISSVINNFAYIILLSIGFILLNEVYSNLFSSRYTTIS
IFTLIVSYMLFIRNKIISSEEEEQIEYEKVATSYISSLINRILNTKFTENTTTIGQDKQL
YDSFKTPKIQYGAKVPVKLEEIKEVAKNIEHIPSKAYFVLLAESGLRPGELLNVSIENID
LKARIIWINKETQTKRAYFSFFSRKTAEFLEKVYLPAREEFIRANEKNIAKLAAANENQE
IDLEKWKAKLFPYKDDVLRRKIYEAMDRALGKRFELYALRRHFATYMQLKKVPPLAINIL
QGRVGPNEFRILKENYTVFTIEDLRKLYDEAGLVVLE
```

Potek:
1. Z iskalnim zaporedjem sprožite iskanje z blastp in zbirko UniProt/Swissprot (sicer bo preveč zadetkov, pa radi bi samo anotirane). Preglejte in pokomentirajte rezultate. Kaj je funkcija tega proteina, katerega zaporedje imate podano zgoraj?
2. Sedaj iskanje ponovite, ista zbirka, kot algoritem pa izberite psi-blast. Dobite nekaj zadetkov. Iskanje ponovite enkrat ali večkrat z dodajanjem novih zaporedij.
3. Naredite poravnavo več zaporedij (iz BLAST, z orodjem COBALT) in prenesite poravnavo.
4. Naredite sequence logo in ga analizirajte, tudi v luči v UniProt/Swissprot anotiranih zadetkov.
5. Kako je pa s strukturami homolognih proteinov?

 

Relevantne povezave:
* WebLogo:
   * verzija 2: [https://weblogo.berkeley.edu](https://weblogo.berkeley.edu)
   * verzija 3: [http://threeplusone.com/weblogo/](http://threeplusone.com/weblogo/)

