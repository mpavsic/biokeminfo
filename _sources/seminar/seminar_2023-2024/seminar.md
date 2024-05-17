# Seminar 2023/2024

## Skupine in termini

Seminar se izvaja v dveh skupinah:

| Skupina | Glavni termin           | Dodaten termin          | Rok za oddajo         |
|:--------|:------------------------|:------------------------|:----------------------|
| 1       | 2024-05-10 (8.00–11.00) | 2024-05-24 (8.00–11.00) | 2024-05-27 (do 12.00) |
| 2       | 2024-05-17 (8.00–11.00) | 2024-05-24 (8.00–11.00) | 2024-05-27 (do 12.00) |

Vsak mora priti na glavni termin, udeležba na dodatnem terminu je opcijska:
- **glavni termin** je namenjen uvodnim navodilom ter začetku reševanja danega problema z namigi izvajalca predmeta (reševanje dokončate doma);
- **dodaten termin** je namenjen reševanju težav, na katere bi naleteli med dokončanjem seminarske naloge – tu bo spet prisoten izvajalec predmeta, ki vam bo po potrebi dal namige za razrešitev težav.

---
## Splošne informacije

Na seminarju boste reševali enostaven [problem](#problem-in-naloga), ki je v osnovi za vse enak, razlika je pa v tem da vsak posameznik dobi drugačen [vhodni podatek](#vhodni-podatki).

---
## Problem in naloga

Prišli ste v novo službo na raziskovalnem institutu ter tam zasedli delovno mesto predhodnega sodelavca instituta, ki so ga odpustili (med drugim) zaradi neurejenega laboratorijskega dnevnika in posledično nesledljivosti raziskav. Raziskovalna skupina, v katero ste prišli, se sicer ukvarja z metagenomiko, zanimajo jih mikrobni proteini, ki bi lahko bili industrijsko in/ali medicinsko zanimivi. Za vašim sodelavcem je ostal kup neurejenih podatkov, med drugim gre za nukleotidna zaporedja v zamrzovalniku shranjenih plazmidnih konstruktov, osnovanih na klonirnem vektorju pUC57, ki v multipli klonirni regiji vsebujejo fragmente z bolj ali manj popolnimi zapisi za mikrobne proteine.

Vaša naloga je, da identificirate protein, ki je v celoti ali zgolj delno zapisani na vstavljenem fragmentu, ter preko izvedbe različnih bioinformatskih analiz poizkušate ugotoviti čim več karakteristih tega in pa njemu podobnih proteinov. Pri tem analiza izvajate na aminokislinskem zaporedju celotnega proteina, ne zgolj na tistem njegovem fragmentu, ki je zapisan na vključku. Pri tem uporabite orodja, ki ste jih spoznali na vajah pri Biokemijski informatiki (po želji lahko poiščete in uporabite še kakšna druga orodja). Do nekaterih odgovorov morda ne bo moč priti neposredno iz zapisov za vaš protein v različnih zbirkah – v teh primerih si morate pomagati z zapisi za sorodne proteine, zapisi za katere so morda bolje anotirani, na osnovi tega pa lahko sklepate na karakteristike vašega proteina

Rezultati analiz naj bodo najmanj:
- ime in izvorni organizem proteina
- lokalizacija, topologija (če je membranski)
- velikost proteina
- domenska zgradba
- post-translacijske modifikacije
- funkcija proteina (in substrat, če gre za encim)
- sorodni proteini (poravnava, filogenetsko drevo)
- najbolj in najmanj ohranjene regije, tudi v luči funkcije proteina
- podobni evkariontski proteini (če so; če jih ni to demonstrirajte z ustrezno analizo) – organizem, protein, funkcija, ...
- potencialna funkcijska povezanost z drugimi proteini, morebitne medproteinske interakcije (poglejte tudi pri morebitnih sorodnih evkariontskih proteinih)
- struktura oz. model strukture (tudi superpozicija pro- in evkariontskih variant) – eksperimentalno določena struktura, model (pripravite sami, pokomentirajte zanesljivost)
  - pri pripravi modela uporabite AlphaFold2 (v obliki ColabFold, kot nad vajah) ali pa nov strežnik [AlphaFold3](https://alphafoldserver.com), ki je na voljo od 8. maja 2024 (potrebujete Google račun, omejitev je 10 modelov na dan)
  - modele struktur lahko izrišete z MolStar, Chimera ali PyMOL

Rezultate analiz v obliki besedila (rezultati, vaši komentarji/diskusija) zapišite v datoteko formata MarkDown, ki jo opremite s povezavami na spremljajoči slikovni material z rezultati analiz. Vse slike morajo biti iz vaših lastnih analiz!

Če ste na neko karakteristiko proteina zgolj sklepali na osnovi podobnosti z drugimi proteini, to jasno navedite in opišite.

---
## Vhodni podatki

Za vsako študentko oz. vsakega študenta je pripravljena vhodna datoteka, ki vsebuje zaporedje celotnega plazmidnega konstrukt. Vsak plazmidni konstrukt vsebuje vključek, ki vsebuje celoten ali zgolj delni zapis za največ en mikrobni protein.

| skupina | priimek, ime | vhodni podatek |
|:--------|:-------------|:---------------|
| 1 | Bajec, Lana | [S01](naloge/s01-input.md) |
| 1 | Ferjančič, Lara | [S02](naloge/s02-input.md) |
| 1 | Habot, Hanna | [S03](naloge/s03-input.md) |
| 1 | Hudobivnik, Laura | [S04](naloge/s04-input.md) |
| 1 | Janc, Nika | [S05](naloge/s05-input.md) |
| 1 | Jordan Ferbežar, Uma | [S06](naloge/s06-input.md) |
| 1 | Klinar, Brina | [S07](naloge/s07-input.md) |
| 1 | Kociper, Debora | [S08](naloge/s08-input.md) |
| 1 | Kolenc, Klara | [S09](naloge/s09-input.md) |
| 1 | Kolnik, Dan | [S10](naloge/s10-input.md) |
| 1 | Kristl, Simon | [S11](naloge/s11-input.md) |
| 1 | Kunstelj, Karin | [S12](naloge/s12-input.md) |
| 1 | Majerle, Nina | [S13](naloge/s13-input.md) |
| 1 | Mohar, Teja | [S14](naloge/s14-input.md) |
| 1 | Osterc, Igor | [S15](naloge/s15-input.md) |
| 1 | Perc, Anže | [S16](naloge/s16-input.md) |
| 1 | Polutnik, Patricija | [S17](naloge/s17-input.md) |
| 1 | Snedec, Andraž | [S18](naloge/s18-input.md) |
| 1 | Trobiš, Veronika | [S19](naloge/s19-input.md) |
| 1 | Varlamov, Mark | [S20](naloge/s20-input.md) |
| 1 | Veler, Jakob Urh | [S21](naloge/s21-input.md) |
| 1 | Vogrič, Vanja | [S22](naloge/s22-input.md) |
| 1 | Matek, Nik | [S23](naloge/s23-input.md) |
| 2 | Bervar, Amber | [S24](naloge/s24-input.md) |
| 2 | Boštjančič, Ava | [S25](naloge/s25-input.md) |
| 2 | Bregar, Jana | [S26](naloge/s26-input.md) |
| 2 | Cankar, Nina | [S27](naloge/s27-input.md) |
| 2 | Čarman, Jasna | [S28](naloge/s28-input.md) |
| 2 | Čerenak, Blaž | [S29](naloge/s29-input.md) |
| 2 | Dular, Maj | [S30](naloge/s30-input.md) |
| 2 | Frantar, Mark | [S31](naloge/s31-input.md) |
| 2 | Gomiršek, Katarina | [S32](naloge/s32-input.md) |
| 2 | Gričar Vintar, Peter | [S33](naloge/s33-input.md) |
| 2 | Hvalec, Jan | [S34](naloge/s34-input.md) |
| 2 | Kosovel, Tina | [S35](naloge/s35-input.md) |
| 2 | Kozel, Vid | [S36](naloge/s36-input.md) |
| 2 | Kramar, Zala | [S37](naloge/s37-input.md) |
| 2 | Lešnik, Tjaša | [S38](naloge/s38-input.md) |
| 2 | Longar, Špela | [S39](naloge/s39-input.md) |
| 2 | Makuc, Nika | [S40](naloge/s40-input.md) |
| 2 | Mulalić, Anita | [S41](naloge/s41-input.md) |
| 2 | Oman Sušnik, Tonja | [S42](naloge/s42-input.md) |
| 2 | Pajnhart, Lara | [S43](naloge/s43-input.md) |
| 2 | Pšeničnik, Tiara | [S44](naloge/s44-input.md) |
| 2 | Puhov, Špela | [S45](naloge/s45-input.md) |
| 2 | Robek, Tinkara | [S46](naloge/s46-input.md) |
| 2 | Škarabot, Anja | [S47](naloge/s47-input.md) |
| 2 | Trontelj, Domen | [S48](naloge/s48-input.md) |

---
## Navodila za izdelavo seminarske naloge

1. Prenesite datoteko s [predlogo](https://mpavsic.github.io/biokeminfo/_sources/seminar/seminar_2023-2024/seminar-predloga.md) (na primer tako desni klik na povezavo -> "Shrani kot...").
   - Če upoštevamo MarkDown oblikovanje bi vsebina predložne datoteke, pretvorjene v html, izgledala [tako](./seminar-predloga.md).
2. Datoteko preimenujte v `s##.md`, pri čemer `s##` predstavlja kodo vašega seminarja, določenega v tabeli z vhodnimi podatki.
3. Vsebino prenešene datoteke uredite oz. njeno vsebino nadomestite z vašo – za pisanje lahko uporabite običajen program za delo s tekstovnimi datotekami, priporočam pa uporabo kakšnega specializiranega programa, ki omogoča predogled. Primeri: [Visual Studio Code](https://code.visualstudio.com/) ali pa kar [JupyterLab](../priloge/jupyterlab.ipynb), ki ga sicer uporabljamo za delo z datotekami tipa ipynb (IPython Notebook).
   - Nekatere dele datoteke morate odstraniti – gre za vrstice, ki se začnejo z znakom `>`.
   - Pri oblikovanju datoteke Markdown si pomagajte z [navodili za Markdown sintakso](../../priloge/markdown.md).
   - V datoteko vključite tudi reference do relevantnih slik, ki prikazujejo rezultate analiz. **POZOR!!!** Slike morajo biti poimenovane po ključu `s##-opis.png`, pri čemer je `s##` koda vašega seminarja, `opis` pa kratek opis slike brez šumnikov, presledkov in drugih nenavadnih znakov (samo ASCII črke in številke 0–9 ter znak za minus in podčrtaj (*underscore*)). Primer: `s23-poravnava_zaporedij.png`.
   - Reference na slike morajo biti vstavljene v Markdown datoteko. Primer reference na sliko: `![poravnava](s23-poravnava_zaporedij.png)`.
4. **Datoteko Markdown** in **priložene pravilno poimenovane slike** oddate prek posebne povezave v spletni učilnici UL FKKT do roka, navedenega v tabeli s [termini](#termini).

```{admonition} Poimenovanje datotek
:class: warning
Obvezno se držite navodil za poimenovanje datotek! Prav tako se pred oddajo prepričajte, da boste naložili le eno MarkDown datoteko, vse ostale datoteke (slike) pa bodo ustrezno naslovljene v njej s povezavami.
```