Title: Ogólna architektura silnika - component model 
Date: 2017-04-11 18:20
Category: Gamedev
Tags: DSP2017, Gamedev
Authors: Szymon Wanot
Status: published

Poprzedni post z tego cyklu traktował o tym jak tworzyć GameObjecty za pomocą hierarchii dziedziczenia. Jak już pisałem sposób ten staje się nieczytelny, w miarę rozwoju projektu, ale pozwala szybko wystartować. Dla większych gier GameObjecty tworzymy w nieco inny sposób używając nie dziedziczenia, a kompozycji stąd nazwa component model. W tej implementacji GameObject sam z siebie jest tylko agregatorem dla komponentów. To one nadają mu właściwe funkcjonalności. Przykładowo  jak do obiektu dodamy komponenty:

- tekstura z animacjami nietoperza,
- odtwarzacz animacji poklatkowych,
- kontroler sztucznej inteligencji,
- drzewo zachowań dla SI latających.

Tak otrzymamy nietoperza, który będzie latał zgodnie z konfiguracją SI. Już na pierwszy rzut oka widać, że component model daje możliwości pewnej separacji i ponownego użycia raz napisanej logiki GameObjectów - jeżeli zrobimy logikę podążania za graczem, to może jej używać kilka obiektów na scenie itp. Jak już wiemy jak to mniej więcej ma wyglądać teoretycznie to przyjrzymy się jakie elementy są potrzebne, aby wygodnie się tak skonstruowanym systemem GameObjectów posługiwać. Ja zawsze implementuję takie elementy:

- GameObjectManager - Manager posiada wszystkie GameObjecty na scenie, można się do niego odwołać ze samej sceny, podsystemów sceny, i gameobjectów. Jest to obiekt zarządzający całą hierarchią, można za jego pomocą dodawać, wyszukiwać i usuwać obiekty, 
- GameObject - w tym podejściu jest on jedynie kontenerem na komponenty i nie wykonuje sam żadnej logiki. Można za jego pomocą dodawać, usuwać i wyszukiwać komponenty oraz dodawać nowe gameobjecty jako dzieci. Celowo napisałem również, że nie wykonuje on żadnej logiki. Ja w swoich implementacjach stosuje update serivce i draw service, który ma listę komponentów do aktualizacji i rysowania. W razie jakiś zmian komponenty są na nowo zbierane ze wszystkich gameobjectów. Jest to bardziej optymalne od strony wykonania i zgodne z zasadami Data-Oriented Design.

Jeśli chodzi o komponenty to je również dziele na grupy:

- Behaviors - komponenty aktualizowane co klatkę, może to by np. kontroler postaci czy kontroler sztucznej inteligencji,
- Drawables - komponenty graficzne, które będą rysowane co klatkę, np. sprite'y, animacje, efekty,
- DataComponents - komponenty przechowujące dane, do których odwołują się inne komponenty, np. komponent przechowujący informacje o położeniu gameobjetu na scenie.

Jako, że komponenty mogą korzystać z innych komponentów w ramach jednego gameobjectu lub hierarchii rodzic - dziecko, należy zaimplementować jakiś system rozwiązywania zależności przy inicjalizacji komponentu. Można to zależnie od języka programowania zaimplementować na kilka sposobów. 
Component model jest, więc dość złożoną, ale jednocześnie skalowalną implementacją struktury sceny. Pracowałem z jego pomocą nad paroma produkcjami. W razie jakichś niejasności lub pytań zapraszam do komentowania.