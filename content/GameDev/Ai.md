Title: Ogólna architektura silnika - sztuczna inteligencja
Date: 2017-04-22 18:30
Category: Gamedev
Tags: DSP2017, Gamedev
Authors: Szymon Wanot
Status: published

Cześć. W dzisiejszych czasach bardzo popularne są gry sieciowe, więc opierające się o interakcje z innymi graczami. Mimo to sztuczna inteligencja nawet w  nich jest potrzeba, aby tworzyć bossów czy jakieś ciekawe eventy wraz z NPC w świecie gry. W dzisiejszym artykule przyjrzymy się jak stworzyć sztuczną inteligencje na miarę naszej gry, tak aby była ona wyzwaniem i spełniała pokładane w niej oczekiwania.

Chciałem tutaj przejść przez parę podejść do tematu i oprzeć je na paru przykładach. Temat niestety jest szeroki, a i ja nie mam pojęcia o wszystkich możliwych podejściach, więc ograniczę się do tego co w miarę znam - a wy jeżeli znacie jeszcze coś o czym tu nie piszę, to zapraszam jak zawsze do sekcji komentarzy. Nie przedłużając lećmy, więc z tematem.

SI podejście naiwne

Zakładając, że piszemy swoją pierwszą grę obiektowo, bez komponent modelu, nasza sztuczna inteligencja dla danego GameObjectu będzie znajdowała się w jego funkcji update. Może to wyglądać w następujący sposób

    ::cpp
    void update(float deltaTime)
    {
	    if(PlayerIsVisible)
	    {
		    AttackPlayer();
	    }
	    else
	    {
		    if(CollideFromLeft)
		    {
			    MoveRight()
		    }
		    else
            {
			    MoveLeft();
		    }
	    }
    }

Widzimy mniej więcej do czego takie podejście prowadzi. W pewnym momencie dodając kolejne interakcje metoda update stanie się nieczytelna. Jak już powiedziałem w artykule o GameObjectach na jakiś PoC czy prosty projekt jest to to ok, ale wyobraźmy sobie w taki sposób programować SI dla gry RTS.

Zaawansowe SI: Planner

Planner jest jednym z zaawansownych podejść do tworzenia SI w grach. Jako przykład użycia wyobraźmy sobie grę typu city builder (np. Banished). Każemy naszym osadnikom  wybudować dom. Zadanie to może być wykonywanie przez 5 ludzi na raz i potrzeba do niego 20 jednostek drewna i 5 jednostek kamienia. Planner powinien zachować się w następujący sposób:

- przydzielić nam 5 osadników,
- sprawdzić, czy w magazynie mamy 20 jednostek drewna, jeśli nie to wysłać osadników, aby je wytworzyli,
- sprawdzić czy w magazynie mamy 5 jednostek drewna, jeśli nie to wysłać osadników, aby je wytworzyli,
- kazać osadnikom przynieść surowce na miejsce budowy,
- kazać osadnikom wybudować dom,
- po zakończeniu zadania przydzielić osadników do innych prac.
	
Jak możemy zauważyć planer działa w następujący sposób:

![Planner](/images/si/planner_graph.png)

Jest to globalny system zarządzający każdym elementem SI na planszy. Mimo to świetnie sprawdza się w grach strategicznych czy city builderach, pewnie znalazłbym jeszcze inne zastosowanie.

Zaawansowane SI: Drzewo zachowań

Jest to bardziej modularne podejście do tematu sztucznej inteligencji. Sama nazwa mówi, że jest to podejście oparte na grafach. Pozwala ono pisać poszczególne zachowania, tworzyć jako osobne klasy, dzięki czemu komponujemy je ze sobą. W drzewie zachowań wyróżniamy następujące elementy:

- behavior - są to liście drzewa, które zwierając w sobie ewaluacje i sposób wykonaniu danego zachowania,
- selector - jest to kontener przechowujący zachowania, który podczas ewaluacji wybiera jedno ze swoich dzieci i rozpoczyna jego wykonanie,
- repeater - podobnie jak selektor pełni on role kontenera na zachowania z tym, że włącza on je cyklicznie jedno po drugim.

Dla dopełniania tego rozwiązania potrzebne są nam jeszcze 2 elementy evaluator, czyli komponent który sprawdzi czy nasze drzewo jest poprawnie skonstruowane oraz egzekutor, który zajmie się wybraniem i odpaleniem zachowania z drzewa, które jest w danym momencie adekwatne do zaistniałej w świecie gry sytuacji. Przykładowe drzewo może wyglądać w następujący sposób:

![BT](/images/si/bt_graph.png)

Ewaluacja zachowania zaczyna się zawsze od noda "Root" przechodzimy wszerz przez wszytkie kontenery i wybieramy  odpowiednie zachowanie. Istotne jest to, aby dobrze określić warunek wykonania danego zachowania, bądź kontenera tak, aby nie miał on kolizji z innymi elementami drzewa. 

To było by na tyle w tym poście. Piszcie w kometach jakie wy znacie inne podejścia do SI w grach komputerowych.
