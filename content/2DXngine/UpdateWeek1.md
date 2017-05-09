Title: 2DXngine: aktualizacja po pierwszym tygodniu
Date: 2017-03-10 19:40
Category: Gamedev
Tags: DSP2017, 2DXngine
Authors: Szymon Wanot
Status: published

Cześć, jako, że mija pierwszy tydzień developmentu należało by wrzucić jakiś status update dotyczący projektu konkursowego. Jak wiadomo początki są trudne. Instalacja bibliotek ciągła się w nieskończoność, ale w końcu się udało. Ogólna struktura projektu w Visual Studio wygląda następująco:
![2DXngine struktura projektu](/images/engine_project.png) 
Tak jak napisałem nie mam jakiś alternatywnych build systemów, a chciałem mieć testy, stąd taka a nie inna struktura, ponieważ w C++ testy odpalają się normalnie z exe, a to co chcę testować musi być biblioteką. Jeżeli ma ktoś inny pomysł jak zrobić to lepiej to czekam, bo obecna konfiguracja idealna nie jest, ale pozwala pracować w miarę stosując TDD. Z tymi testami jeszcze zobaczymy jak będzie, ponieważ pewnie nie będę w stanie przetestować wszystkiego np. generowanie grafiki czy bardziej złożone interakcje. 
Zaimplementowałem podstawową klasę aplikacji dla Windowsa. Wyświetla ona okienko, inicjalizuje podstawowe zmienne, odpala pętle główną i będzie podstawą reszty silnika. Dodatkowo udało mi się dodać service locator i timer.
W trakcie implementacji jest system GameObjectów i scen, ponieważ te komponenty są od siebie zależne muszę je na razie implementować równolegle. Obecnie mocno działam, aby skończyć implementacje systemu komponentów. Niestety blokuje mnie na razie to jak zrobić w C++ system rozpoznawania typów obiektów. Nie chcę używać standardowego RTTI dlatego, że mądrzejsi ode mnie twierdzą, że wolne to i nie powinno się w grach tego stosować. Mocno zagłębiłem się już w ten temat i znalazłem parę przykładów implementacji, więc myślę, że na dniach uda mi się to skończyć możliwe, że nawet kiedy czytacie ten tekst system jest już w miarę ogarnięty. Poza tym kiedy uda mi się to zrobić planuję artkułów na ten temat, bo temat jest ciekawy i potrzebny.
Staram się również w miarę możliwości aktualizować [tablice](https://trello.com/b/wJGa7Jm5/2dxngine) na trello. Na chwilę obecną pare tasków zyskało checklisty a parę nowych tasków dojdzie do implementacji.
Z rzeczy których nie udało się zrobić to niestety nie udało mi się mierzyć czasu na toggl jak początkowo planowałem, więc będę musiał to zrobić od tej soboty, ponieważ planuje, że tydzień prac będę liczył od soboty do piątku. 