Title: 2DXngine update wersja 0.2.x-alpha
Date: 2017-10-04 08:00
Category: Gamedev
Tags: 2DXngine
Authors: Szymon Wanot
Status: published

Cześć. Od Daj się poznać 2017 minęło kilka miesięcy, więc czas na mały update tego co w 2DXngine się dzieje. Jak widzicie nie poddałem się i nadal rozwijam framework oraz dodaje nowe funkcjonalności. Co zatem się zmieniło od ostatniego razu? Jest tego dość sporo, więc mogę coś niechcący pominąć. Ostatni update miał miejsce jakoś w maju lub początkiem czerwca, w tym czasie silnik zyskał sporo elementów i udało mi się pozbyć masy błędów oraz  bugów.
Na początek może lista co się udało zrobić jako nowe elementy:

- bazowe komponenty 2D,
- podpięcie do CI,
- podstawowe MVP narzędzi do silnika, 
- logger, Renderowanie multi render target, PostProcessing,
- integracja z Tiled,
- Itp. Itd.

Teraz przejdźmy do konkretów. Jeżeli chodzi o komponenty bazowe to w ramach tego powstały elementy pozwalające na wyświetlanie spriteów, animacji poklatkowych, obłsugę transformacji 2d, kolizje itp. Ilość komponentów będzie pewnie rosła, ale na razie zaimplementowane zostało niezbędne minimum. Kolejnym fajnym krokiem jest podpięcie silnika do CI AppVeyor jest to usługa, która pozwala na kompilacje, testowanie, release naszych aplikacji. Na razie ogarnąłem tylko build i testy o czym pisałem w [TYM](https://harunx9.github.io/appveynor-darmowe-ci-dla-projektow-open-source.html#appveynor-darmowe-ci-dla-projektow-open-source) artykule. 

Kolejnym elementem jaki rozpocząłem z rzeczy około silnika są narzędzia, na razie jest to MVP texture packera, ponieważ musiałem to zrobić dla testów. Dalsza implementacja oczywiście nastąpi, ale silnik ma obecnie większy priorytet. Nażedzia są pisane w .NET CORE tak, że są muliplatformowe. Ciekawym elementem jest integracja z [Tiled](http://www.mapeditor.org/). Daje ona możliwość sparsowania mapy, ale i tworzenia całych scen. Cały mechanizm omówię osobno w innym artykule. 
Z innych rzeczy udało mi się dodać logowanie do konsoli wraz z ustaleniem poziomu logowania, post processing oraz renderowanie sceny na wielu render targetach i sklejanie ich potem osobno.

To były co ważniejsze rzeczy jak myślę. Teraz co dalej i kiedy wyście z alfy tak na prawdę myślę, że wersja 0.3 powinna już być betą. Do tego czasu musze zastąpić MS bulid multiplatformowym Cmake i wykonać jeszcze parę testów z renderowaniem tile map. Jeżeli chodzi o przyszłość to chcę zrobić releasowanie silnika, jako statycznej biblioteki oraz generowanie projektu z silnikiem, exe i wszystkimi potrzebnymi zależnościami. Takie podejście mocno usprawni pracę z silnikiem, ponieważ obecnie należy ściągnąć silnik usunąć elementy z testowego projektu i dopiero wtedy można zaczynać prace. Nowe podejście powinno wygenerować projekt z kodzikiem silnika oraz drugim projektem, który ma być implementacją gry.

To tyle. Jak chcesz to zapraszam do spróbowania 2DXngine do jakiś małych projektów. Oczywiście jak zawsze zapraszam do sekcji komentarzy.