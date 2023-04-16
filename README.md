# Ochrana rybníků

Online aplikace a web k projektu Ochrana rybníků včetně úložiště dat.

## TODO list
- [ ] Webová prezentace
    - [x] Základní prezentace
    - [x] Fotogalerie
    - [x] Katalog rybníků
    - [x] Admin na fotogalerie
    - [x] Seznam rybníků na titulkní stránce
    - [x] Resize a cache obrázků na straně serveru
    - [x] Snížit průhlednost pozadí u fotogalerií
    - [x] Správné náhledy stránek na facebookovém příspěvku
    - [ ] Prozatimní zrušení dvojjazyčné mutace
    - [ ] Automatický zoom mapy u katalogu rybníků
    - [ ] Tabulka s daty u katalogu rybníků
    - [ ] Blog
    - [ ] Datum u fotogalerií
    - [ ] Relace na rybník ve fotogalerii, pokud se ho to týká
    - [ ] Odkazy v patičce
    - [ ] Partneři
    - [ ] Navigace na rybníku pod hlavičkou stránky
    - [ ] Navigace po stránce
    - [ ] Přepínače na různé mapové podklady map Seznamu
    - [ ] Data z telemetrických stanic
    - [ ] Doladit design u karty rybníků dle předlohy
    - [ ] Responzivní design
    
- [x] Skladiště dat
- [ ] Prezentace pro záchrané programy ryb
- [ ] Kalendář návštev lokalit
    - [x] Základní aplikace
    - [x] Více učastníků návštevy lokality najednou
    - [x] Více rybníků v rámci jedné aktivity
    - [ ] Design kalendáře


## Chyby
- [x] Automatický resize obrázků nefunguje
- [x] Náhled obrázku nevygeneruje stránka, pouze admin
- [ ] Při exportu kalendáře do XLS je pro datum a čas volí datový typ string místo datetime


## Použité balíky
Django==4.2
django-imagekit==4.1.0
Pillow==9.5.0
psycopg2==2.9.6
python-decouple==3.8
xlwt==1.3.0

## Použité balíky pro vývoj
django-extensions==3.2.1
ipython==8.12.0
