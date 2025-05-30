# Kaj se lahko iz divje zabave nauči nemoralni biokemik?

Na divji zabavi se je tvoj prijatelj okužil z virusom, ki se je kasneje izkazal za hepatitis C. V hepatitis C virusu, za katerega ne obstaja cepivo in okuži okoli 1 miljona ljudi na leto, obstajajo elementi IRES (internal ribosome entry site) - interna vstopna mesta za ribosome. To so mesta, ki omogočajo translacijo kodirajočih regij mRNA neodvisno od m7G kape, ki je navadno vezavno mesto za malo podenoto ribosoma. Virusi jih pogosto uporabljajo, da dosežejo preferenčno translacijo lastnih mRNA v njihove proteine. Kot nadobudni biokemik, ki te bolj zanima raziskovanje kot pomoč prijateljem, je bolezen tvojega prijatelja odlična odskočna točka za raziskovanje.
Našel si naslednjo [mRNA](https://www.ncbi.nlm.nih.gov/nucleotide/AJ242651.1?report=genbank&log$=nucltop&blast_rank=4&RID=2DS3ZAHZ016), ki vsebuje IRES. Želiš raziskati vpliv te IRES na hitrost translacije v primerjavi z m7G kapo. To skleneš narediti v naslednjih korakih:

1. izvedba PCR reakcije
* Poišči podoben IRES v drugem organizmu (virusu), ki ne okuži ljudi.
* Katero žival moraš okužiti oziroma čigave celice moraš uporabiti (Namig: v več člankih o tej temi je ta organizem naveden.)?
* Je v RNA zapisih tega organizma prisotno podobno zaporedje, ki bi lahko motilo PCR reakcijo?
* Pripravi primerne začetne oligonukleotide za izvedbo PCR reakcije na IRES. Uporabi orodje za načrtovanje teh oligonukleotidov dostopno na tej [povezavi](https://www.ncbi.nlm.nih.gov/tools/primer-blast/). Pazi, da uporabiš primerne parametre: razširi območje Tm, izberi primerno bazo podatkov in organizem. Navadno za PCR reakcijo uporabljamo začetne oligonukleotide, ki so 18-24 bp dolgi, a je boljše izbrati večji razpon.

2. priprava mRNA konstrukta
Želiš sestaviti vektor, ki pod nadzorom enega promotorja vsebuje: m7G kapo, protein 1, IRES in protein 2. Ker želiš odstraniti čim več spremenljivk moraš izbrati proteina, ki imata podobne lastnosti izražanja (dolžina, hitrost translacije ...) in zlahka izmeriš njuno koncentracijo. (Namig: proteini s podobnimi lastnostmi izražanja so homologi.)
* Koncentracijo katerih proteinov zlahka merimo v celici? (Namig: 🟩🟨🟥)
* Poglej, če so ti proteini homologni.
* Lahko te proteine izražamo tako v prokariontskih kot evkariontskih celicah?