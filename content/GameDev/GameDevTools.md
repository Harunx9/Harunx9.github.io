Title: Narzędzia przydatne w tworzeniu gier
Date: 2017-03-15 20:00
Category: Gamedev
Tags: DSP2017, Gamedev, Tools
Authors: Szymon Wanot
Status: published

Jako, że słowo się rzekło, teraz więcej postów o tematyce związanej z szeroko pojętym gamedevem. Dziś chciałbym przybliżyć wam kilka fajnych narzędzi, które można wykorzystać tworząc własny silnik do gry.

[Tiled](http://www.mapeditor.org/) - Darmowy

Ze wszystkich programów z Tiled korzystam chyba najwięcej. Jest to prosty i intuicyjny edytor poziomów do gier.  Mimo swojej prostoty pozwala jednak na wiele. Po pierwsze możemy to z Tilei poukładać poziomy, dodać background.  Edytor posiada system warstw, dzięki czemu możemy w łatwy sposób dodać do mapy tła, obrazy oraz obiekty, które po odpowiednim zparsowaniu w silniku możemy używać jako miejsca kolizji, punkty startowe czy ścieżki dla sztucznej inteligencji. Ciekawą opcja jest implementacja w silniku autoreloadu plansz. Po spięciu takiej funkcjonalności z Tiled otrzymujemy możliwość edycji live naszych plansz. Cały projekt jest darmowy choć możemy wesprzeć twórcę dotacją lub zapłacić za edytor na itch.io. 

![Tiled](/images/gdtools/Tiled.png)

[Paint of Persia](https://dunin.itch.io/ptop) - Darmowy

Jest to bardzo ciekawe narzędzie pozwalające na tworzenie rotoskopowych animacji naszych gier. W skrócie polega to na tym, że nagrywamy kamerą lub bierzemy gotowy film i na jego podstawie możemy odrysować ruchy postaci. Takie podejście powoduje, że dostajemy bardzo realistyczną i szczegółową animacje postaci czy innych obiektów. Z ciekawostek taki sposób tworzenia animacji został po raz pierwszy wykorzystany w klasycznym Prince of Persia z 1989 roku.

![Paint of Persia](/images/gdtools/pop.png)

[Pyxel Edit](http://pyxeledit.com/) Płatny

Bardzo ciekawy program do tworzenia grafiki pixelartowej. Posiada on wsparcie do tworzenia tilesetów do map oraz animacji poklatkowej. Fajnym dodatkiem jest sugestia barw do cieniowania, rozjaśniania jest to szczególnie przydatne, jeżeli jest się takim antytalenciem graficznym jak ja.

![Pyxel Edit](/images/gdtools/pyxeledit.png)

[Krita](https://krita.org/en/) Darmowy

Kolejny program graficzny tym razem nieco podobny z możliwościami do popularnego Photoshopa. U mnie świetnie się sprawdza do konceptów postaci czy plansz oraz rozrysowywania logiki. Koniecznie używajcie go z tabletem graficznym, ponieważ wtedy pokazuje prawdziwy pazur.

![Krita](/images/gdtools/krita.png)

[Gimp](https://www.gimp.org/) Darmowy

Z obowiązku należy wspomnieć o tym programie graficznym. Wiem, że nadal jest popularny, ale mi obecnie zastępuję go w całości Krita, która działa szybciej i ma więcej fajnych możliwości. Mimo to Gimp jest nadal niezłą propozycją dla początkujących, ponieważ obsługa programu jest bajecznie prosta a jeżeli nie wiemy jak coś zrobić, to w sieci znajdziemy masę tutoriali, które na pewno nam pomogą.

[ShoeBox](https://renderhjs.net/shoebox/) - Darmowy

Shoebox może przy pierwszym podejściu wyglądać niepozornie, ale jest to tak na prawdę bardzo rozbudowane narzędzie do manipulacji teksturami. Przy jego pomocy możemy: 

- pakować tekstury w atlasy, 
- ripować tekstury,
- odczytywać sprite'y np. SpriteFonty,
- generować BitmapFonty,
- pakować animacje ,
- dodawać pivot pointy(origin) do naszych sprite'ów,
- tworzyć nine slice sprite'y do UI,
- inne pomniejsze funkcjonalności.

Jak widać jest tego sporo. Program polecam również dlatego, że jest darmowy a napisanie importera do wygenerowanych poprzez niego atlasów i spritesheet'ów nie powinno być problemem.

![Shoebox](/images/gdtools/shoebox.png)

[TexturePacker](https://www.codeandweb.com/texturepacker) Płatny

Ostanie narzędzie to typowy packer pozwalający na stworzenie spritesheet'ów lub atlasów tekstur. Dodatkowo program pozwala na optymalizacje assetów poprzez kompresje, co daje nam lżejsze assety np. na komórkach, gdzie ekran jest mniejszy, przez co nie widać różnicy. Z programem współpracuje sporo silników dostępnych na rynku, ale nie ma też problemu w napisaniu własnego importera.