# Poravnave

## Matrike zamenjav
Pri izračunu poravnav nukleotidnih ali aminokislinskih zaporedij uporabljamo za vrednotenje t. i. matrike zamenjav (*substitution matrices*), kjer so zapisane vrednosti za identičnost oz. zamenjavo nekega ostanka z drugim. Matrike so lahko izračunane na osnovi različnih vhodnih podatkov, najpogosteje pa se uporabljajo take, ki so izračunane na osnovi poravnav zaporedij sámih. Za nukleotidna zaporedja najpogosteje uporabljamo matriko EDNAfull, za aminokislinska zaporedja pa matrike iz družine BLOSUM.

## Poravnava zaporedij

### Globalna poravnava zaporedij Needleman-Wunsch
Algoritem Needleman-Wunsch ([Wikipedia](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)) vam da optimalno globalno poravnavo dveh zaporedij. Delovanje algoritma si lahko "vizualiziramo" tako, da zaporedji izpišemo v matriko, vrednosti matrike pa izračunamo s sledenjem različnih poti med posameznimi celicami, pri čemer zmeraj vzamemo tisto pot (ali več) med posameznimi celicami, ki vodijo do večje vrednosti.

Za lažje razumevanje priporočam igranje s spletnim programčkom, ki za dve poljubni zaporedji ob spreminjanju vrednosti za ujemanje, neujemanje ter vrzeli prikaže matriko s puščicami za sledenje, hkrati pa ob premiku miškinega kazalca na posamezno polje v matriki izpiše vse alternativne poti oz. vrednosti, ki bi se na nekem mestu nahajale, če bi uporabili alternativne poti.

Povezava: [https://bioboot.github.io/bimm143_W20/class-material/nw/](https://bioboot.github.io/bimm143_W20/class-material/nw/)