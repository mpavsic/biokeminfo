# Seminarji 2022/2023

Seminar se izvaja v dveh skupinah, vsaka ima nekoliko drugačno nalogo.

| Skupina | Termin 1   | Termin 2   |
|---------|------------|------------|
| [skupina A](#skupina-a)       | 2023-05-05 | 2023-05-12 |
| skupina B       | 2023-05-19 | 2023-05-26 |

Vsaka skupina ima torej dva termina:
- **termin 1** je namenjen skupnemu reševanju vzorčnega problema;
- **termin 2** je namenjen samostojnemu reševanju problema, pri katerem ima vsak posameznik drugačne vhodne podatke, rezultate analiz ter interpretacijo pa je potrebno po zaključku tega termina oddati.

---
## Skupina A

### Uvod
Na raziskovalnem inštitutu, kjer se ukvarjajo z iskanjem novih potencialno industrijsko uporabnih encimov iz slabše okarakteriziranih organizmov, je prišlo do obsežnega požara. Pri tem je bila uničena vsa lokalno shranjena laboratorijska dokumentacija, po nesreči pa so ugotovili, da že nekaj let zaradi malomarnosti IT osebja sistem za izdelavo varnostne kopije na drugi lokaciji ni deloval. Vse, kar je ostalo, je nekaj potencialno pomembnih vzorcev DNA, ki so ostali v kletnem zamrzovalniku, a brez dokumentacije žal ni mogoče ugotoviti, kaj je uporabno in pomembno ter kaj ne. Vaša naloga je, da poizkusite iz tega materiala izluščiti, za kaj gre in ali se izplača z delom nadaljevati. Na pomoč raziskovalca, ki je vzorce pripravil, ne morete računati, saj je iz obupa delo pustil in odšel na kolesarjenje okoli sveta.

Ne preostane vam nič drugega kot do, da določite nukleotidna zaporedja vključkov v standardnem klonirnem vektorju, ki je bil v uporabi v tem laboratoriju pri kloniranju zapisov za nove encime. Vaš izhodiščni podatek je eno izmed tako določenih nukleotidnih zaporedij.

### Termin 1
Vhodni podatek (zaporedje):
```
>seq1
TCGGGAACCAGCAACTCCGGTACTTGGGCTTCCGACAAGCTGATCTCTGATGGCTACAA
GTGGGACGTCAAGATCCCTGACAGCATTGCTTCTGGTAACTACGCTGTTCGTCACGAGA
TCATTGCCCTCCACAGCGCCAACAACGTCGGTGGTGCCCAGAACTACCCTCAATGCATC
AACCTCGAGGTCAAGAGCTCCGGCTCCGACAACCCTGAGGGTGTTGTTGGCACTGAGCT
GTACACTGCCCAGGACAAGGGTATTTACGTCAACATCTACTACCCCGGCTTCACTGCCG
ACGAGTATGACATGCCCGGCCCTGCTCTCTACACCGGTGGCTCTGGCTCTGGCTCTGCT
CCTGCTTCGTCCGCCTCTGCTTCCTCGACTGCCCAGGCCAGTTCGACCTCCGCTGCATC
TGCTTACTCGTCCGCCGCTTCGTCTGCTCAGACCACTTATGCCGCTTCGTCCGCCGAGG
CCTACTCTGCCTCTTCGTCCACTGCTGCTCCCGTCACCACCCAGGCTGCCGTTG
```

Druge pomembne informacije:
- [splošna navodila](navodila.md)
- [predloga za poročilo za skupino A](seminar-predloga_a.md)

Primer delno rešene naloge, ki naj bo za zgled za pripravo seminarske naloge, je dostopen [tukaj](naloge/s00-primer.md).

### Termin 2

V spodnji tabeli so navedene oznake seminarjev in imena, Vhodni podatek (zaporedje) najde vsaj v delu pod tabelo (imena zaporedij so oznake seminarjev, format FASTA). Seminarska naloga naj bo pripravljena v skladu z [navodili](navodila.md) in ob upoštevanju [predloge za skupino A](seminar-predloga_a.md).

| Priimek, ime            | Oznaka |
| ----------------------- | ------ |
| Agrež, Tim-David        | S01    |
| Bohorč, Leila           | S02    |
| Bohte, Janja            | S03    |
| Fink, Luka              | S04    |
| Frelih, Nika            | S05    |
| Karčovnik, Maša         | S06    |
| Kobal, Mia              | S07    |
| Kolander, Patricija     | S08    |
| Novel, Matija           | S09    |
| Pečovnik Wutt, Naja     | S10    |
| Pojbič, Taja            | S11    |
| Poljanšek, Aleš         | S12    |
| Pucihar, Samo           | S13    |
| Rajterič, Lara          | S14    |
| Rak, Karin              | S15    |
| Šenica Pavletič, Primož | S16    |
| Trost, Teo              | S17    |
| Tušek, Marcel           | S18    |
| Vranješ, Tin            | S19    |


```
>S01
LRAELLVGNWSDRLGGFDPDAASHLLSDGDHITAVADQLTGLVASGGWDGVNVDLELVRR
RDSRGLVAFVTALRERLPATASITIDVSARTSATAYRAGGYRLAELAAVV

>S02
QSFNGARRYVDILRKFEQMGPVNWSKTVWSFHYYNGTFSLGVNNNSAKDGGRAALSYIKA
RYPILCTETNWWMEPPRSVLINGLEALEDVQVGWTLLRRPNQTTPPASPS

>S03
MILSPVIGSGSTSSKIRASGTTTERSLADRFAEVFNILDFGAQPNDPAFDNRTSIQAALD
AAFQKGGGVVEIPDGTFWLSGTGNAVDGCVRIRSNTTLRGAGMGLSRLKL

>S04
LARLVETLGLRRIVLVGHDWGGPVALAYAASRPDNVAALVLSNTWAWPVHRDPRLAAFAA
LAGGPPGRWLIRHHDALVRALPLAVGDRQRLSATAHRCYRTVRATPAARD

>S05
VSMPGIWSQVGLHCRTVGADCPFEVSGFSFAGVPGVVIGHNADVAWGFTNLGPDVTDLYL
EKIRGERWLYDGAYRPLSIRKEVIKVRGGDDFDLTVRSTKHGPLLSDVST

>S06
NTLGFPPVWATAQHGGFDMLATENSRTGSPIKGEIDLDNRNLMGFSMGGGGVLLAAGEMG
TGYKSAIALAPWLGQYSPAYENIQEPMLVLGSENDELAYYSDVFYASLPT

>S07
DNETLFDIIQYKAPLATSTAVRARMQTLGNSLVMFSQGVPFFQAGDDLLRSKSLDRNSFN
SGDWFNRLDFTYQSNNWGVGLPPAGDNQSMWPTMQPLLANPALRPTPEDI

>S08
PWLQLIGPQYIELAFQTAARADPQAKLTYNDYDIELDTPEQEVKRGQVLLLLRRLHARGV
PVQAVGIQSHLQATGPRPGVGLITFIRQVATMGLDVYITEMDVNTHALEG

>S09
PVHAPGRRDKAPDEPEADAAVTSAAGVVLVILSADCLPVLIAARDGGSVAAAHAGWRGLA
AGVLEATVAAVRTSPAELVAWIGPGIGAGSYEVDARVHAAFVDADADAAH

>S10
RAIKVEVYDWDRNGSHDFIGEFTTSYRELARGQSHFNVYEVVNPRKKMKKKKYLNSGTVT
LLSFTVEAEHTFLDYIRGGTQLNFTVAIDFTASNGEWQLCPPGVFIWGSC

>S11
MKYLDEFRDEARALAILKEIVKLGTKEVSFMEICGSHTHTISKSGLRGVLPGNIKLISGP
GCPVCVTAQSEIDAVVNFADTNTDVIITTFGDMLRVPGSFSSLEQARGRG

>S12
WASYGYIVFQPTHMDSRSLGFETKRDNLREFYTQMLTVTDTRRQDMSFVLDSLSLIEEMV
PELKGKMDTTKLIAAGHSMGAATAMLVSGMKLVNPMDGSEESSEEDRFKT

>S13
MIYQLSTLPYGNDALEPHISRETIEFHYGRHHQAYVANLNNLVPGTEFEGLALEEVVKQA
SGAIFNNSAQIWNHTFYWNCLAPSGGGEPDGDLAQAIADVFGSFEVFKEK

>S14
MKYPDKKITAYLLTLLLSTTAQASHNHQRPDSHAPAGIMGDHIMDKDEVMLSYRYMAMTM
DGNLNGTNSIPTPLPGFMVSPLNMDMKMHMSGIMYAPTEKLTLSLMTSIL

>S15
KLGERIGKELGIPGYFYEKAAKEAKRKNLANCRSGEYEGLKEKLVNPEWKPDFGPAEFNS
NVSKSGCTAISARDFLIAYNINLNTTSTRRANAIAFDIREAGRIKREGNP

>S16
SEHYTDKFTIPFDGLASTEKEKDLSILQAMVDAGYLTTDEISAVEEMDNDDIFYETLLKD
FEINLNTLAEQNLSSPRAVLANIKEMAEELKDVGIADELPKRIDSCEDND

>S17
MSWTVRNSLFSHNRAVGYGANPARPGTPGGGSGGAIYNDGNTFTLNLCGTRIEDNAAREG
GGAIFFVSNDRTGTLRIEDSVLRKNPSDGFETAGYPGIFYLGSGPPVVVN

>S18
MVKGGVPFPMLSDGGGKVGSVFGVYLEDAGVEARGRFIIDPDGIIQGFEVLTPPVGRNIN
ESIRQIHAFQHVRNSKGTEATPSGWRPGKQTLKPGPDLVGKVWEVWKTKM

>S19
DADNISIEGNGIIDGQGFEKYYPIKEGIYRPYIIRFIRCNFVKIKDVTLLNSAAWVQHYI
ECDDLLIDGITVRSYSNKNNDGLNIEGCQRVTVTRCNIDSEDDSIVLKTL
```