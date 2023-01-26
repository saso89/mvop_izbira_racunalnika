# Izdelava odločitvenega modela DEX za izbiro televizorja
Seminarska naloga pri predmetu Modeliranje večkriterijskih odločitvenih procesov

Avtor: Sašo Bobnar

[Fakulteta za informacijske študije v Novem mestu](https://www.fis.unm.si/).

Študijski program: Računalništvo in spletne tehnologije, 2. stopnja.

Študijsko leto 2022/2023.

## Model

Pri spletni aplikaciji uporabljamo model izbira_televizorja, ki je bil ustvarjen v [programskem orodju DEXi](https://kt.ijs.si/MarkoBohanec/dexi.html). Model je dostopen na [povezavi](https://github.com/saso89/mvop_nakup_televizorja/blob/main/nakup_televizorja.dxi). Podroben opis je napisan v obliki seminarske naloge in je dostopen v obliki [PDF datoteke](https://github.com/saso89/mvop_nakup_televizorja/blob/main/Seminarska_naloga_Bobnar.pdf).

![DEXiSmal](https://user-images.githubusercontent.com/93672119/214931088-927f5744-b7a4-4703-b748-737bb7d4890c.gif)

 
## Namestitev aplikacije

1. Kloniramo ali prenesemo repozitorij mvop_nakup_televizorja.
2. Za uspešno uporabo potrebujemo [Python 3.11](https://www.python.org/downloads/release/python-3110/), [django 4.1.5](https://docs.djangoproject.com/en/4.1/topics/install/) ter po potrebi še dodatne knjižnice, na katere nas opozori ukazni poziv.
3. V ukaznem pozivu (CMD) navigiramo do lokacije repozitorija (kjer se nahaja manage.py, to je v mapi mvop).
4. Uporabimo ukaz `py manage.py runserver`.
5. Ko se strežnik zažene, v poljubnem brskalniku v naslovno vrstico vpišemo naslov `https://127.0.0.1:8000/nakup_televizorja/index`. Delovanje aplikacije je bilo testirano na brskalniku Google Chrome (različica 109.0.5414.119).
6. Naslov `https://127.0.0.1:8000/nakup_televizorja/index` vsebuje obrazec za oceno modela televizorja na podlagi DEX modela, medtem ko naslov `https://127.0.0.1:8000/nakup_televizorja/results` vsebuje rezultate našega ocenjevanja.
