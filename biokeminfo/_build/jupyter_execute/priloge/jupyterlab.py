# JupyterLab

Pri programiranju bomo uporabljali vmesnik [JupyterLab](https://jupyter.org), ki omogoča vizualno lépo sestavljanje kode in spremljajočega besedila. Vse skupaj je zapakirano v eno datoteko, imenovano **zvezek** (*notebook*), ki vsebuje tudi izhod kode (*output*). Zvezek je sicer tekstovna datoteka s končnico ipynb (**iPy**thon **N**ote**b**ook), za pravilen prikaz in uporabo (t.j. poganjanje kode) pa ga moramo odpreti v ustreznem programu (lokalno nainstaliran JupyterLab ali z uporabo katere od spletnih storitev, npr. [Binder](http://mybinder.org)). 

## Zgradba zvezka
Vsak zvezek je sestavljen in enega ali večih segmentov, imenovanih **celice**, ki si sledijo v določenem zaporedju. Celice lahko vsebujejo **kodo** (tip celice *Code*) ali **spremljajoče besedilo**, oblikovano z [*Markdown*](markdown.md) (tip celice *Markdown*). Določeno celico v že pripravljeni datoteki začnemo urejati tako, da eno- (za kodo) ali dvo-kliknemo nanjo (za *Markdown*). Nastavljen tip celice je povezan z barvanjem kode in pa seveda z interpretacijo tega, kar je v njej napisano - ali naj se prikaže in oblikuje kot besedilo ali pa se naj izvede kot koda. Celice dodajamo preko bližnjic na tipkovnici ali preko menija.

Celice s spremljajočim besedilom lahko obravnavamo kot komentarje (kodo lahko še vedno komentirate direktno v celici, kjer se nahaja, z uporabo znaka #), ki delijo kodo na več ločenih, a medsebojno vseeno lahko povezanih kosov. Če bi vsebino celic s kodo prenesli v pravilnem vrstnem redu v tekstno datoteko _py_ in jo zagnali v Pythonu, bi zadeva delovala popolnoma enako.

Ko v neko celico vnesemo vsebino ali jo spremenimo, moramo (ponovno) zagnati program, ki interpretira njeno vsebino in jo izvede (koda) oz. prikaže oblikovano (besedilo). In kako to naredimo?

## Bližnjice

Enostavno! Ko smo v določeni celici lahko iz menija zgoraj izberemo ustrezno možnost, lahko pa pritisnemo tipko _Esc_ (_escape_) na tipkovnici, na ta način skočimo iz načina vpisovanja, ter s pritiskom na tipko za črko ```m``` ali ```y``` skočimo na način *Markdown* oz. *Code*. Končno oblikovanje oz. zagon kode dosežemo z izbiro iz menija ali uporabo bližnjic na tipkovnici, ki jih je malo morje. Nekaj jih je navedenih tukaj:

* ```Shift + Enter```: zaženemo trenutno celico (ne glede na vsebino - oblikovanje besedila ali zagon kode)
* ```Ctrl + Enter```: zaženemo izbrane celice
* ```Alt + Enter```: zaženi trenutno celico in vstavi novo spodaj

Ostale lahko najdete v pomoči za JupyterLab.

## Primer

Pa poglejmo, kako naredimo nekaj zelo enostavnega! Spodaj je ena celica s kodo. Lahko jo poljubno spreminjate in s kombinacijo tipk ```Ctrl + Enter``` pogledate, kaj je rezultat - slednji se izpiše pod celico s kodo.

a = 5
b = 8
c = a + b
print(c)

Med celicami je s kodo je lahko tudi celica (ali več njih) z besedilom. Ko celico s kodo zaženemo, lahko izhod te celice deluje kot vhod za celice spodaj, recimo takole...

d = c * 5
print(d)

Za test lahko pobrišemo vse izhode in sicer v meniju izberemo ```Kernel > Restart Kernel and Clear All Outputs```. Nato zaženemo samo drugo celico s kodo. Kaj se zgodi? Zaženimo zdaj prvo celico s kodo, nato pa ponovno drugo. Torej? :)

Mislim, da je zdaj jasno, kako se zadevi streže. V nadaljevanju je še na kratko opisano, kako uporabljamo [*Markdown*](markdown.md), da si lahko delamo lepe zapiske.

## Povezave

* [JupyterLab](https://jupyterlab.readthedocs.io) (dokumentacija)