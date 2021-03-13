# Poimenovanje datotek

## Uvod

Moderni operacijski sistemi dopuščajo kar precej svobode pri poimenovanju datotek (*files*) in map (direktorijev, torej *folders* ali *directories*), k temu pa je vsekakor prispeval standard za konsistentno kodiranje, prikaz in delo z besedilom [UNICODE](https://en.wikipedia.org/wiki/Unicode). Kakšne so možnosti za poimenovanje je povezavo z datotečnim sistemom (*file system*, tudi *filesystem*), ki določa, kako so podatki shranjeni in kako do njih dostopamo.

Poglejmo najprej malce v zgodovino. Na primer, star datotečni sistem FAT16 (*16-bit [File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)*), v uporabi v operacijskem sistemu [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS) in (pra)starih različicah sistema Microsoft Windows, je omogočal imena datotek formata 8.3, kjer je bila glavnina imena omejena na do 8 znakov (seveda ne katerihkoli), sledila je pika, nato pa trije znaki, ki so predstavljali t.i. končnico datoteke (*file extension*) in so s tem na nek način sporočali, kakšni podatki so v datoteki in na kakšen način so zapisani.

Podoben sistem `ime.končnica` je še danes splošno v uporabi, le da imamo v dolžini in znakih imena več svobode, podobno velja tudi za končnico.

## Priporočila za poimenovanje datotek in map

Pri poimenovanju datotek in map si izdelajte shemo oz. smernice, po katerih boste poimenovali vse datoteke in mape. Bolj ohlapno shemo uporabljajte na splošno, za vsak specifični projekt (npr. diplomska naloga) pa si shemo podrobneje definirajte.

* Datotekam dajte unikatna imena, pri kreiranju imen pa konsistentno uporabljajte shemo, ki ste si jo zamislili.
* Pri oblikovanju sheme za poimenovanje datotek "glejte v prihodnost" - poizkusite predvideti situacije, ko boste morali v ime vključiti še kakšen parameter.
* Imena naj ne bodo predolga. Poizkusite se omejiti na do 25 znakov. Nekatere besede lahko skrajšate, npr. `ver` namesto `verzija`.
* Za lažje razvrščanje datotek slednje oštevilčite, pri tem pa uporabljajte vodilne ničle, torej v imena dajte `001`, `002` ... `015` ... `123` ipd. namesto `1`, `2` ... `15` ... `123`, da bo razvrščanje dobro delovalo (npr. v drugem primeru bo `123` pred `2`!), pri tem pa seveda predvidite največje število datotek in temu ustrezno prilagodite dolžino zaporedja številk.
* Uporabljajte končnice datotek, da z njimi opišete vsebino (npr. `.fasta` za zaporedja v formatu FASTA, `.png` za slike v formatu PNG, `.gb` za zapise v obliki GenBank).
* Uporabljajte male črke, razen v izjemnih primerih, ko želite kaj res pudariti (npr. `PREBERIME.txt`), pri (daljših) imenih iz večih besed pa uporabite velike začetnice za posamezno besedo (npr. `PavsicM-Diplomska_naloga-Biokemija_2021.docx`.
* Ne uporabljajte znakov, ki bi lahko bili problematični v drugih operacijskih/datotečnih sistemih in pri drugih uporabnikih v mednarodnem okolju. Na primer, izogibajte se šumnikom.
* Izogibajte se presledkom, raje uporabljajte vezaje (`-`) ali podčrtaje oz. *underscores* (`_`).
* Pri zapisovanju datumov uporabljajte mednarodni standard `YYYY-MM-DD` ali `YYYYMMDD`. Če je datum v takem formatu na začetku imena, bodo datoteke avtomatsko razvrščene po datumih.

## Primeri

Spodaj je nekaj primerov slabe in dobre prakse, ki ilustrirajo uporabo zgoraj navedenih smernic.

| slabo | dobro|
|:----------|:----------|
| `Pavšič seminar verzija 5.docx` | `Pavsic-Seminar_v5.docx`    |
| `besedilozaseminarskonalogo.txt` | `Seminarska_naloga-besedilo.txt` |
| `7. januar 2017 sekvenciranje.doc` | `sekvenciranje_2017-01-07.doc` (sploh uporabno, če imamo več datotek stila `sekvenciranje_YYYY-MM-DD.doc`) |
| `GST wilt type sequence fasta.txt` | `GST_wt-seq.fasta` (ali celo samo `GST_wt.fasta` oz. `GST_wt.seq`) |
| `diploma slike + besedilo kočna verzija fkkt.docx` | `Diploma-slike_besedilo-koncna_ver.docx` |

