Title: Ogólna architektura silnika - system Encji/GameObject'ów
Date: 2017-03-21 18:20
Category: Gamedev
Tags: DSP2017, Gamedev
Authors: Szymon Wanot
Status: published

Ostatni post tego cyklu był o zarządzaniu scenami, dziś postaram się nieco napisać o tym co powinno być na scenie, aby gra posiadała jakiś gameplay. Mowa tu będzie o Aktorach, Encjach lub GameObjetach w zależności od biblioteki/engine'u nazwa może się różnić, ale to ciągle to samo. Takim elementem może być na scenie wszystko, od postaci gracza do przeciwników, przedmiotów do zbierania itp.  Istnieją dwie drogi do implementacji GameObject'ów w tym artykule opiszę drogę z dziedziczeniem, natomiast component model będzie opisany oddzielnie. 

Droga implementacji za pomocą dziedziczenia wygląda w następujący sposób:

- tworzymy abstrakcję, która powinna zawierać: pozycję, nazwę , wysokość, szerokość ; jeżeli nie korzystamy z biblioteki fizycznej to należy tu również zdefiniować zmienne potrzebne do jej obsługi. Dodatkowo obiekt powinien zawierać abstrakcje dla aktualizacji oraz rysowania obiektu,
- tworzymy kolejno obiekty dziedzicząc z bazowego,
- w momencie kiedy zauważamy, że dane obiekty mają ze sobą jakieś cechy wspólne tworzymy dla nich wspólną abstrakcje.

Na tak może wyglądać przykładowa hierarchia:

![GameObjects](/images/go_graph.png)

Takie podejście ma swoje plusy i minusy. Zacznijmy od tego co uważam za pozytywne strony takiej implementacji. Po pierwsze pozwala ona szybko wystartować, ponieważ na początku nie mamy skonceptualizowanego całego gameplay'u, chcemy np. zrobić platformówkę to pomoże nam to zrobić prototyp w parę dni. Jeżeli projekt jest mały to również to podejście się sprawdzi, ponieważ nie będzie miał on dużej ilości elementów. Problem tego podejścia zaczyna się kiedy gra zaczyna rosnąć, ponieważ każdy nowy GameObject wymaga nowej klasy a każda kategoria GameObject'ów dodatkowej abstrakcji. Prowadzi to do bardzo dużej ilości plików oraz skomplikowanej i nieraz wielopoziomowej hierarchii dziedziczenia. Taki kod staje się trudny do utrzymania. Dodatkowo testowanie tak stworzonych encji jest prawie niemożliwe. Poza tym problematyczne staje się dodawanie nowych funkcji go istniejących GameObject'ów, gdy chcemy coś dodać musimy modyfikować istniejący kod, co w efekcie może prowadzić do zepsucia już działających funkcji. 
Mimo tego co napisałem polecam to podejście, jeżeli zaczynasz swoją przygodę z grami. Pozwoli Ci to jak już pisałem szybko wystartować i szybko pokazać prototyp innym ludziom, co jest bardzo istotne pod względem zbierania feedbacku na temat gry. Jeśli jednak wasza gra stanie się większa powinniście iść w stronę component modelu, który opisze w następnym poście.