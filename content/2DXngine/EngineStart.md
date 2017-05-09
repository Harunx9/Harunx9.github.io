Title: 2DXngine: start projektu
Date: 2017-03-01 16:00
Category: Gamedev
Tags: DSP2017, 2DXngine
Authors: Szymon Wanot
Status: published

Cześć,
Jako, że "Daj Się Poznać 2017" dziś wystartowało, to ja również chciałbym wystartować z projektem konkursowmym.
Po długim namyśle zdecydowałem się na napisanie silnika w C++. Zanim przejdę do pokazania co zrobiłem, chciałem po krótce  określić ramy projektu.  Napisanie kompletnego silnika z edytorem w czasie 3 miesięcy z moim obecnym stanem wiedzy o C++ jest nierealne, więc  ograniczyłem zakres prac tak, aby udało się zrobić coś działającego. 
Do implementacji tzw.  "must have" powinny wejść:

- game objecty z component modelem,
- bazowe komponenty,
- system scen,
- system sztucznej inteligencji oparty na drzewach zachowań,
- asset loader,
- obsługa dźwięku i muzyki,
- renderer 2D pozwalający na obsługę shaderów GLSL,
- wczytywanie animacji poklatkowych,
- prosty system fizyki i/lub integracja z Box2D,

Przygotowałem jeszcze takie rzeczy z kategorii "nice to have" (gdy uda mi się zaimplementować rzeczy z powyższej listy):

- wczytywanie mapy z plików Tmx generowanych przez edytor Tiled,
- możliwość pracowania z Tiled w trybie livereload,
- kompilator assetów pozwalający je pakować w zdefiniowane paczki,
- streaming poziomów pozwalający doczytywać dynamiczne dane (pozwoli to na wyeliminowanie doczytywania pomiędzy lokacjami),
- integracja z językiem skryptowym Lua.

Ze wszystkich "nice to have" najfajniej było by zrobić te z Tiledem oraz skryptowanie Lua, ale zobaczymy jak mi pójdzie.
Kolejną fajną rzeczą była by wielowątkowa pętla gry z render commandami, ale to już wyższa szkoła jazdy i na pewno teraz nie dam rady tego zaimplementować. 
Jako, że projekt startuje nie będzie w tym poście za dużo kodu raczej opowiem o tym co i jak będę robił. 
Po pierwsze link do repo na github jest -> [TU](https://github.com/Harunx9/2DXngine). 
Druga sprawa to taka krótka prezentacja bibliotek z których będę korzystał:

- SDL2 - jest to bibliotek ułatwiająca wiele spraw mutliplatformowych takich jak korzystanie z systemu plików, wyświetlanie okienka, proste rysowanie 2D, przechwytywanie inputu z urządzeń wskazujących itd. Generalnie jest to taki toolbox pomagający pisać mniej kodu. Po więcej odsyłam do dokumentacji -> [TU](https://wiki.libsdl.org/FrontPage)
- Glm - biblioteka matematyczna udostępniona przez G-Truc Creations  -> [TU](https://www.opengl.org/sdk/libs/GLM/). Jest to lib typu single header więc wystarcza jeden plik nagłówkowy aby jej używać. Dodatkowo zawiera ona wszystkie typy matematyczne takie jak macierze czy wektory które potrzebne są w pracy z opengl.
- GLEW - bibliotek pozwalająca pisać multiplatformowy kod OpenGl. Teoretycznie do renderowania grafiki mógłbym użyć tego co daje mi SDL2, ale musiałbym zrezygnować z shaderów. Ze wzgleu na to, że shadery dają fajne możliwości do robienia efektów specjalnych renderer 2D zaimplementuję sam co pozwoli na skorzystanie z całości API OpenGL 4+.

Z ciekawych rzeczy myślałem aby użyć jakiegoś multiplatformowego build systemu np. Cmake czy Scons. Po namyśle stwierdziłem jednak, że na razie będę używał tego co oferuje w temacie Visual Studio 2015, czyli MSBuild. Jeśli w przyszłości zajdzie taka potrzeba spróbuje coś zmienić w tym temacie.
Kolejną sprawą jest jakość kodu. Postaram się z mojej strony wykorzystywać nowości języka C++ a, że jest ich sporo to pewnie nieraz będę się zastanawiał co wybrać. 
Drugą sprawą w temacie jakości jest pisanie kodu zgodnie z zasadami Data-Oriented Design. Jeżeli ktoś nie wie o czym mówię polecam obejrzeć tą prezentacje -> [TU](https://www.youtube.com/watch?v=rX0ItVEVjHc). 
W telegraficznym skrócie chodzi o to, aby tworzyć kod przyjazny dla cache naszego procesora a nie koniecznie z zasadami SOLID. Pozwala to bardzo mocno zoptymalizować czas wykonania algorytmów. Jak sam się poduczę tego to napiszę o tym jakiś osobny wpis. 
Ostatnią sprawą jest moja potrzeba porządkowania i mierzenia swojej pracy. Zobaczymy jak to pójdzie ale engine będzie miał taki quasi kanbanowy board na Trello będę się starał tam wypisywać taski jakie realizuje -> [TU](https://trello.com/b/wJGa7Jm5/2dxngine). Poza tym po pierwszym miesiącu postaram się zdać raport ile godzin udało mi się zainwestować w rozwój silnika.
To chyba na tyle w tym tygodniu postaram się pospinać biblioteki uporządkować repo i zrobić jakieś takie podstawy na których potem będziemy budować resztę silnika.

PS. Taski na Trello są na razie bardzo ogóle podejrzewam, że jak będę implementował konkretny feature to to jakoś podzielę.
