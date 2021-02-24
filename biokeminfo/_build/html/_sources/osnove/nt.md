# Nukleotidna zaporedja

Obstajajo tri glavne zbirke nukleotidnih zaporedij, ki pa pravzaprav vsebujejo enake podatke, saj med njimi poteka redna (dnevna) izmenjava oz. sinhronizacija:
* [**GenBank**](https://www.ncbi.nlm.nih.gov/genbank/) na strežniku [NBCI](https://www.ncbi.nlm.nih.gov/) (National Center for Biotechnology Information),
* [**ENA** (European Nucleotide Archive)](https://www.ebi.ac.uk/ena/) na strežniku [EBI](https://www.ebi.ac.uk) (European Bioinformatics Institute) in
* [**DDBJ** (DNA Data Bank of Japan)](https://www.ddbj.nig.ac.jp/).

GenBank je zbirka, ki se od zgoraj navedenih uporablja najpogosteje, zato jo bomo uporabljali tudi mi. Do zbirke lahko dostopamo na več osnovnih načinov: 
* spletni iskalnik Entrez, ki omogoča dostop tudi do drugih podatkov/zbirk, npr. do aminokislinskih zaporedij, struktur makromolekul, PubMed ipd. - gre za način dostopa, ki je podoben oz. enak kot za [PubMed pred brskalnika](../vaje/pubmed_web.md);
* programski dostop do Entrez z uporabo NCBI E-utilities (enako kot za [programski dostop do PubMed](../vaje/pubmed_eutilities.ipynb);
* iskanje po GenBank s programom BLAST (iskanje podobnih zaporedij);
* prek strežnika FTP z anonimnim dostopom, od koder lahko prenesemo datoteke v formatu ASN.1 ([ftp](tp://ftp.ncbi.nlm.nih.gov/ncbi-asn1)) in kot ploske datoteke - *flatfile* ([ftp](ftp://ftp.ncbi.nlm.nih.gov/genbank)).

Mi si bomo tukaj ogledali dostop prek spletnega vmesnika in E-utilities, iskanje z BLAST pa bomo spoznali v okviru ene kasnejših vaj.