# Ochrana rybníků

Online aplikace k projektu Ochrana rybníků včetně úložiště dat.

## TODO list
- [ ] Webová prezentace
    - [x] Základní prezentace
    - [ ] Fotogalerie
    - [ ] Katalog rybníků
    - [x] Admin na fotogalerie
- [x] Skladiště dat
- [ ] Prezentace pro záchrané programy ryb
- [ ] Kalendář návštev lokalit
    - [x] Základní aplikace
    - [x] Více učastníků návštevy lokality najednou
    - [x] Více rybníků v rámci jedné aktivity
    - [ ] Design kalendáře


## Chyby
- [ ] Náhled obrázku nevygeneruje stránka, pouze admin
- [ ] Při exportu kalendáře do XLS je pro datum a čas volí datový typ string místo datetime


## Použité balíky
Django==4.1
django-imagekit==4.1.0
Pillow==9.2.0
psycopg2==2.9.3
python-decouple==3.6
xlwt==1.3.0

## Použité balíky pro vývoj
django-extensions==3.2.0
ipython==8.4.0
