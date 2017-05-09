Title: Ogólna architektura silnika - system scen
Date: 2017-03-08 17:10
Category: Gamedev
Tags: DSP2017, Gamedev
Authors: Szymon Wanot
Status: published

Dziś  trochę więcej opowiem na temat wysokopoziomowych wzorców stosowanych w grach komputerowych. Opisana poprzednio w artykule pętla gry jest bardzo nisko poziomowym elementem, mimo to jest niezbędna do implementacji dalszych podsystemów gry. System scen jest moim zdaniem drugim elementem, który dobrze jest zaimplementować, aby grę można było w łatwy sposób rozwijać.
Generalnie w implementacji chodzi o funkcjonalne podzielenie stanów aplikacji, co obrazuje poniższy rysunek:

![stany gry](/images/scene_graph.png)

Sama nazwa  "scena" wzięła się od tego, że grę komputerową można postrzegać jako pewno rodzaju przedstawienie, w którym obiekty na scenie są aktorami na planszy, która jest dla nich swoistą sceną. Aby taki pomysł w grze mógł zaistnieć potrzebujemy dwóch rzeczy:

- manager scen - jest to trzon całego systemu (do niego dodajemy i usuwamy sceny); odatkowo powinien on zarządzać, którą scenę należy uaktywnić,
- scena - bazowa abstrakcja z której czerpią pozostałe sceny; powinna ona posiadać możliwości aktualizacji aktorów oraz ich rysowania.

Można także dodać do sceny ładowanie specyficznej dla nich zawartości czy zapis ich stanu (choć ta ostatnia opcja jest zbędna, jeżeli mamy sensowny system zapisu gry). Ja często robię jeszcze parę dodatkowych abstrakcji np. UI Sceny czy Gameplay Sceny pozwalają one np. załadować się z pliku. Taka implementacja jest przydatna szczególnie, jeśli posiadamy w silniku edytor, który wygeneruje dla nas odpowiednie zasoby.
Ciekawą opcja jest dodanie do sceny czegoś na kształ zachowań odpalanych przed lub po aktualizacji stanu wszytkich obiektów na scenie. 
Takie podsystemy sceny można wykorzystać do np.:

- wykrywania kolizji pomiędzy aktorami na scenie,
- naliczania czasowych bonusów/kar dla danych aktorów,
- interakcji pomiędzy aktorami,
- zbierania przedmiotów,
- cyklicznego zapisu stanu gry,
- Itd…

System scen można jeszcze rozbudować o manager aktorów, który pozwoli na komfortowe ich wyszukiwanie w momencie kiedy będą nam do czegoś potrzebni.  To tyle jeśli chodzi o sceny i zarządzanie nimi, w następnym poście przejdę do game objectów. Na pewno temat będę jeszcze rozbudowywał przy innych elementach silnika, ale na razie tyle powinno wystarczyć.  