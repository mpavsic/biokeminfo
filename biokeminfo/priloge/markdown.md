# Markdown

## Kaj je Markdown?

**Markdown** je enostaven označevalni jezik (*markup language*) za oblikovanje golega besedila, ki nam omogoča, da vanj vnesemo določene "obogatitve" (npr. **odebeljen** ali *poudarjen* tekst). Pogosto se uporablja na spletnih forumih in datotekah "premeri me". Primer tovrstne datoteke je `README.md`, ki je del repozitorija, iz katerega je ustvarjena ta spletna stran. Tudi datoteka HTML, ki jo trenutno berete, je ustvarjena iz datoteke *markdown*. Ravno ta pretvorba, torej iz golega besedila v (X)HTML, je bila mišljena kot primarna uporaba *markdown*-a. Danes je na voljo kopica programov, ki omogočajo pretvorbo tudi v druge formate in pa dodatne funkcionalnosti.

### Kratka zgodovina

*Markdown* je leta 2004 izumil John Gruber v sodelovanju z Aaronom Swartzem; nekaj osnovnih informacij o zgodovini, razvoju in sintaksi je na [Wikipedii](https://en.wikipedia.org/wiki/Markdown). Avtor vzdržuje tudi [lastno stran](https://daringfireball.net/projects/markdown/), kjer opisuje obe komponenti jezika: **sintakso** (o njej nekoliko več spodaj) in sam **program** ```markdown``` (napisan v Perlu), ki poskrbi za pretvorbo v format HTML. Njuna specifikacija sintakse ni bila nedvoumna, kar je vodilo v razvoj številnih implementacij in posledično zmešnjave. Kasneje je bila predlagana standardna nedvoumna specifikacija sintakse, imenovana [**CommonMark**](https://commonmark.org).

### Splošne značilnosti

Jezik je precej lahek v smislu, da je za opis izgleda besedila potrebno malo dodatnih znakov, datoteka z besedilom v tem formatu pa je enostavno berljiva tudi v primeru, ko ni pretvorjena v HTML (na primer, *poudarjeno* bomo v nepretvorjenem dokumentu še vedno zaznali, le nekoliko drugače bo izgledalo: \*poudarjeno\*). Datoteke tipa *markdown* so sicer čisto običajne tekstovne datoteke - odpremo in urejujemo jih lahko kar v Notepadu (Windows) ali TextEditorju (macOS), vsekakor je pa dobrodošlo, da jih vidimo tudi oblikovane. Za slednje lahko uporabimo kar JupyterLab ali pa katerega od številnih prevajalnikov.

Jezik Markdown je lahek tudi v smislu, da se ga je enostavno naučiti - več o tem v nadaljevanju, kjer so predstavljeni najpogostejši primeri uporabe.


## Sintaksa

Sintaksa je zraven programa, ki golo besedilo pretvori v format HTML, ena od osnovnih komponent jezika. Opisuje, na kak način dosežemo določeno oblikovanje. Obstaja več variant sintakse, zadnja verzija **CommonMark Markdown** pa je dosegljiva [tukaj](https://spec.commonmark.org/current/). Vse to deluje (tudi) v zvezkih JupyterLab.

V nadaljevanju je predstavljenih nekaj najpogostejših primerov osnovne sintakse. Pri vsakem primeru je prikazano oblikovano besedilo, spremlja pa ga surova oblika. Do slednje pridemo tako, da uporabimo t.u. **ubežne znake**, ki omogočajo, da znaki za oblikovanje niso interpretirani kot taki. Na primer, kako dosežemo, da ```*poudarjeno*``` ni prikazano kot *poudarjeno*? To je zelo enostavno - pred vsak znak, ki določa oblikovanje, damo levo poševnico (```\``` ali _backslash_). Daljše odseke, za katere ne želimo, da so pretvorjeni v HTML, lahko opišemo kot kodo (tak odsek besedila zaobjamemo z \`\`\`, ki jih postavimo pred začetek in za koncem takega odseka).


### Razdelki

Besedilo lahko razdelimo na razdelke tako, da pred naslov razdelka damo enega ali več znakov ```#``` (deluje do 6. nivoja):
```
# Naslov
## Podnaslov
### Podpodnaslov
```

### Seznami

V vsako vrstico, ki je del seznama, na začetek dodamo *zvezdico* (```*```). Tako bo seznam zapisan kot ...

```
* prva alineja
* druga alineja
* tretja alineja
```
prikazan tako:

* prva alineja
* druga alineja
* tretja alineja

Seznam lahko pripravimo tudi kot oštevilčen, tudi v večih nivojih:

1. prva točka
2. druga točka
   * prva poddtočka
   * druga poddtočka
3. tretja točka
   * še ena podtočka

koda za zgornji seznam pa je:

```
1. prva točka
2. druga točka
   * prva poddtočka
   * druga poddtočka
3. tretja točka
   * še ena podtočka
```

### Poudarjeno, odebeljeno

Oblikovanje besedila kot *podarjeno*, **odebeljeno** ali ***poudarjeno in odebeljeno hkrati*** je zelo enostavno!

To bi v Markdown zapisali na naslednji način:

```
Oblikovanje besedila kot *podarjeno*, **odebeljeno** ali
***poudarjeno in odebeljeno hkrati*** je zelo enostavno!
```

Namesto znaka ```*``` lahko uporabimo ```_```, končni rezultat je v obeh primerih rezultat je enak. Torej, ```_kloniranje_``` se izpiše kot _kloniranje_. Priporočljivo je, da se odločimo za eno od oblik in jo konsistentno uporabljamo.

### Povezave

Vstavljanje povezav je enostavno - če želimo npr. povezavo z imenom UL FKKT, ki kaže na spletno stran fakultete, torej [UL FKKT](http://www.fkkt.uni-lj.si), napištemo to takole:
```
[UL FKKT](http://www.fkkt.uni-lj.si)
```

### Slike

Slike enostavno prikažemo tako:
```![logo](https://mpavsic.github.io/biokeminfo/_static/logo.png```

Zgornja vrstica nam da:

![logo](https://mpavsic.github.io/biokeminfo/_static/logo.png)

Beseda ```logo``` je alternativno besedilo (*alt text*), ki se prikaže takrat, ko same slike ni moč prikazati.

### Matematične formule

Sintaksa za matematične formule je enaka kot pri LaTeX. Samo formulo objamemo z ```$$``` (torej pred in za formulo). Na primer, zapis

```
(1+2+3+4+5+\cdots+n)(1+2+3+4+5+\cdots+n)=\frac{(n+1)^2n^s}{4}
```
nam da

$$
(1+2+3+4+5+\cdots+n)(1+2+3+4+5+\cdots+n)=\frac{(n+1)^2n^2}{4}
$$

Še en primer - zapis

```
$$
\lim_{n \to \infty}
\sum_{k=1}^n \frac{1}{k^2}
= \frac{\pi^2}{6}
$$
```

se izpiše kot

$$
\lim_{n \to \infty}
\sum_{k=1}^n \frac{1}{k^2}
= \frac{\pi^2}{6}
$$

Formule lahko izpisujemo tudi kar znotraj besedila oz. v isti vrstici (*inline*), kar dosežemo z objemom formule v enojen ```$```. Tako lahko do izpisa $y=\delta sin(x)$ pridemo z ```$y=\delta sin(x)$```.

### Tabele
Tabele pravzaprav niso del osnovne sintakse, a jih tukaj vseeno omenjamo. Pri tabelah prva vrstica vsebuje glavo (*header*), naslednja določa poravnavo (določimo z dvopičjem), sledi pa vsebina. Enostaven primer z razlago:

```
| Tabele        | so             | simpl! |
| ------------- |:--------------:| -----: |
| stolpec 3 je  | poravnan desno |    500 |
| stolpec 2 pa  | sredinsko      |     20 |
```

se izriše kot

| Tabele        | so             | simpl! |
| ------------- |:--------------:| -----: |
| stolpec 3 je  | poravnan desno |    500 |
| stolpec 2 pa  | sredinsko      |     20 |


Ali poravnava deluje ali ne je odvisno od prevajalnika. V JupyterLab poravnava deluje, povsod pa ne. Isti rezultat bi dobili, če bi tabelo zapisali nekoliko manj urejeno, na primer tako (pomembno je le, da uporabimo vsaj tri minuse, torej ```---```):

```
| Tabele | so | zakon! |
| --- |:---:| ---: |
| stolpec 3 je | poravnan desno | 500 |
| stolpec 2 pa | sredinsko | 20 |
````

### Citati
Citate (*quotes*) zapišemo tako, da vrstico začnemo z ```>```. Zapis

```>To je citat!```

se torej izpiše kot

>To je citat!

## Sintaksa v tej knjigi
Datoteke v tej knjigi, tudi besedilni odseki zvezkov JupyterLab, so napisani v razširjeni obliki **CommmonMark Markdown**, prav tako pa je uporabljena sintaksa iz bogatega [**MyST Markdown**](https://myst-parser.readthedocs.io), ki omogoča bombončke kot so stranski oblački z beležkami ipd.


##  Povezave

* [sintaksa CommonMark Markdown](https://spec.commonmark.org/current/) (uradna stran)
* [MyST Markdown](https://myst-parser.readthedocs.io) (stran z dokumentacijo)
* [Markdown Guide](https://www.markdownguide.org) je pregledna stran z navodili za uporabo, vključno s [*plonkcem* (*cheatsheet*)](https://www.markdownguide.org/cheat-sheet/)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) (eden od osebnih repozitorijev na GitHub)