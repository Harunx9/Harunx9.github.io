Title: .NET klasy internal a testy jednostkowe
Date: 2017-09-18 19:00
Category: .NET
Tags: blog, .net, programming, c#
Authors: Szymon Wanot
Status: published
            
Cześć. Dużo się ostatnio naoglądałem i naczytałem o DDD i architekturze port-adapter i tak zacząłem rozmyślać jak to osiągnąć, choćby w kontekście tooli, które piszę do swojego silnika.

Z tego co zauważyłem, to w projektach z którymi przyszło mi pracować, większość klas jest publiczna. Jest to zrozumiałe, chcemy mieć testy lub nie mamy testów, ale wszyscy piszą public, więc co to za problem. No niestety problem jest, wynika on z tego, że udostępniamy całe API na świat zewnętrzy, nawet jeżeli pewne komponenty nie powinny być dostępne na zewnątrz. Generalnie na zewnątrz powinniśmy udostępnić interfejsy i te implementacje, które mają być tam wykorzystane lub mogą zostać odziedziczone. W ramach powtórzenia w .NET mamy 3 specyfikatory dostępu dla klas, czyli public, internal, private oraz keyword sealed, który służy do ograniczenia możliwości dziedziczenia. Z tych wszystkich możliwości najpopularniejsze jest public, natomiast momenty gdzie widziałem zastosowanie sealed mógłbym policzyć na palcach jednej ręki. Podobnie jest w bibliotekach, choć zdarzają się momenty lepsze. Co do słowa kluczowego  internal to praktycznie w ogóle nie widziałem jego użycia i wszystkie klasy mają w większości public.

Co zrobić w momencie, jeżeli chcemy pisać kod ładnie, czytelnie i udostępniać implementacje tylko tam gdzie jest ona potrzebna. Długo szukałem na to odpowiedzi jak pisać implementacje, tak abym testował to co potrzebuje a udostępniał to co chce. Mamy tu tak naprawdę 2 opcje :

- testujemy tyko publiczne API. Ma to sens, bo jest to to co chcemy udostępnić na zewnątrz, więc musi to działać i tyle. Mimo to wydaje mi się, że pisanie dodatkowych testów by się przydało.
- mówimy kompilatorowi do jakiego projektu udostępniamy nasze internale.

Już widzę te pochodnie purystów, że to hack i tak nie powinno się robić, ale nie powinno się też pisać testów w dll implementujących nasze funkcjonalności. Co należy zrobić, aby klasy internal udostępnić na zewnątrz wystarczy w AssemblyInfo dodać oto takie dwie linijki:

    ::csharp
    using System.Runtime.CompilerServices;
    [assembly: InternalsVisibleTo("OUR.TEST.DLL.NAME")]

Działa na pełnym .Net i Core oraz pozwala o wiele lepiej strukturyzować i testować nasz kod. Co do słowa kluczowego sealed, to polecam stosować zawsze, gdy nie jesteśmy pewni, że będzie potrzeba rozszerzania funkcjonalności klasy. W razie potrzeby ktoś świadomie będzie musiał to sealed usunąć lub w przypadku jakieś biblioteki opakować ją i na pewno spowoduje to dyskusje w zespole, czy na pewno należy tak zrobić. To na tyle. A co wy myślicie o zaprezentowanych tu praktykach. Zapraszam jak zawsze do sekcji komentarzy.
