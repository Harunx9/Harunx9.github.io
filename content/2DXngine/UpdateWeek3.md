Title: 2DXngine: aktualizacja po trzecim tygodniu
Date: 2017-03-25 10:00
Category: Gamedev
Tags: DSP2017, 2DXngine
Authors: Szymon Wanot
Status: published

Witam W tym tygodniu udało mi się po pierwsze popracować trochę więcej. Jak policzę tak to mniej więcej to wyszło około 24 godziny. Nie było też już większych problemów implementacyjnych.

W ciągu tego tygodnia udało mi się zrobić do końca GameObject - właściwie całość jest  już działająca. Testy również w większości są napisane, oczywiście ta klasa będzie rozwijana w miarę potrzeb, ale na razie wydaje mi się, że spełnia ona swoje założenia funkcjonalne. Drugą rzeczą, którą udało mi się skończyć to GameObjectManager jeszcze musze do niej dopisać testy co pewnie uczynię w najbliższym czasie, więc pewnie wyjdą jakieś błędy implementacyjne. Dodatkowo stworzyłem początkową strukturę klas dla systemu scen, czyli scenę abstrakcyjną i manager scen. Myślę, że teraz właśnie te elementy systemu będę rozwijał. 

Przydałoby się też rozpocząć manager assetów i renderer, więc nie wiem czy nie zrównoleglę prac, bo chciałbym żeby wreszcie coś zaczęło się wyświetlać, ponieważ na razie jedyne co się wyświetla to zielone kropki przy testach jednostkowych. To żeby jak największa cześć silnika była przetestowana to jednak dla mnie priorytet jak już pisałem zresztą. Implementacja pójdzie przez to wolniej, ale potencjalnie będzie mniej problemów później. Staram, się tez trzymać TDD, ale często mam prace, które wymagają ode mnie stworzenia api bez wiedzy jak ono ma wyglądać co utrudnia TDD,  ale myślę, że jeszcze trochę praktyki i może uda mi się tak wytwarzać kodzik. 

Z rzeczy związanych z silnikiem to powstaje już artykuł o tym rozpoznawaniu i porównywaniu typów w C++, ale jeszcze potrzebne są ostatnie szlify, aby wszedł na bloga więc myślę, że po weekendzie się pojawi na blogu. To chyba tyle, widzę że jest tego mało, ale niestety ostanie implementacje nie są niczym ciekawym. W C++ nie mam LINQ i większość mojego czasu pochłaniają implementacje wyszukiwania dodawania i usuwania w kolekcjach C++, no niestety taka specyfika języka i projektu.  Myślę, że jak dojdziemy do renderowania i zarządzania assetami to będę miał więcej ciekawych rzeczy do napisania. Tymczasem trzymajcie się do następnego update'u.