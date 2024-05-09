
```{note}
Dobrodošli na spletni strani - spletni knjigi **Biokemijska informatika**!

Pričujoča spletna knjiga je primarno študijsko gradivo za vaje pri predmetu **Biokemijska informatika** za študente univerzitetnega študijskega programa [Biokemija](https://fkkt.uni-lj.si/studij-in-studentje/univerzitetni-studijski-programi) na  [Fakulteti za kemijo in kemijsko tehnologijo (UL FKKT)](http://www.fkkt.uni-lj.si) na [Univerzi v Ljubljani](http://www.uni-lj.si).

Knjiga je sicer prosto dostopna in kot taka predstavlja enostavno dostopen in uporaben vir informacij tudi kasneje tekom študija Biokemije, prav tako pa bodo kaj uporabnega v njej našli tudi študenti drugih bio-orientiranih študijskih programov.
```

---
Predgovor
====

Knjiga je sestavljena iz nalog, podprtih s kratkim uvodom ter razlagami. Naloge so smiselno razvrščene v tematske sklope, njihovo zaporedje pa ni nujno povezano z zaporedjem izvajanja na vajah.

Naloge so dveh tipov:
- naloge, ki se nanašajo na uporabo spletnih podatkovnih zbirk ter spletnih ali lokalno nainstaliranih programov s "prijaznim" uporabniškim vmesnikom, kjer znanje programiranja ni potrebno; 
- programiranje v jeziku Python.

**Naloge z uporabo spletnih podatkovnih zbirk in orodij** se navezujejo na "operacije", s katerimi se boste tekom študija največ srečevali, prav tako pa tudi kasneje, če boste ostali v znanosti. Sem spada iskanje podatkov z brskalnikom po spletnih podatkovnih zbirkah (literatura, nukleotidna in aminokislinska zaporedja, strukture, interakcije ipd.) ter njihovo manipulacijo, analizo, ... (poravnave zaporedij, vizualizacija in analiza struktur, filogenetske analize ipd.). Skratka, te veščine so repertoar vsakega biokemika in molekularnega biologa.

**Drugi tip nalog bo od vas zahteval nekaj znanja programiranja** in nekoliko drugačen način razmišljanja. Danes je veščina programiranja vedno bolj pomembna, ne samo zato, da nekaj naredite popolnoma na novo, ampak da si lahko z lastnimi programi ali prilagoditvami obstoječih programov pomagate pri analizi bio-podatkov. [**Python**](https://www.python.org) ste spoznali že pri predmetu **Osnove programiranja** in privzeli bomo, da se še česa spomnite. No, če se ne, lahko znanje malce ponovite na tej [povezavi](https://www.youtube.com/watch?v=T7UqhDs8zj4&t=18s). :) Šalo na stran! (Mimogrede, jezik Python je ime dejansko dobil po [Letečem cirkusu Montyja Pythona](https://sl.wikipedia.org/wiki/Monty_Python).)

Vaje iz programiranja so zastavljene tako, da boste (ponavadi) dobili že delno izdelane dele kode, ki jih boste morali prilagoditi in pravilno sestaviti v končen izdelek. Podstrani, ki vsebujejo naloge iz programiranja, pa tudi nekatere druge podstrani, so napisane v obliki zvezkov [**JupyterLab**](priloge/jupyterlab.ipynb). Na tej strani so vidni kot koda in njen izhod, a s kodo tukaj ne morete interagirati. Zadeva pa postane bistveno bolj uporabna če:
- zvezek oz. zvezke prenesete na vaš računalnik in jih odpreti v okolju JupyterLab (to je priporočen način za na vajah) ali
- zvezek odprete v spletni storitvi Google Colab ali Binder (povezava je vidna v zvezkih JupyterLab desno zgoraj - ikona rakete). Priporočam Google Colab, saj deluje nekoliko hitreje, prav tako pa se vam spremembe zvezkov shranijo na vaš Google Drive. To ne velja za Binder - za ohranitev sprememb morate zvezek po koncu vaje oz. preden zaprete okno brskalnika shraniti lokalno (ga prenesete na vaš računalnik).

```{admonition} Opomba
:class: note
Spletna knjiga je v nastajanju in bo kot taka sproti dopolnjena in posodobljena. Priporočam, da si med zaznamke shranite samo osnovni naslov [https://mpavsic.github.io/biokeminfo](https://mpavsic.github.io/biokeminfo), saj se lahko naslovi podstrani v primeru reorganizacije vsebine spremenijo. Če v knjigi najdete napako mi to sporočite preko klika na ikono GitHub na vrhu dotične strani > 'Suggest edit' (predlagajte popravek) ali 'Open issue' (pokomentirajte).
```