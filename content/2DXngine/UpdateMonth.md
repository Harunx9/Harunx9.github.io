Title: 2DXngine podsumowanie pierwszego miesiąca pracy
Date: 2017-04-08 20:40
Category: Gamedev
Tags: DSP2017, 2DXngine
Authors: Szymon Wanot
Status: published

Cześć, dawno nic nie pisałem na temat projektu, ale nie oznacza to, że nic w tym temacie się nie dzieje. Mam parę problemów natury filozoficznej przy podejmowaniu kilku decyzji, ale o tym może później. Zacznijmy od tego co udało się zrobić, co jest w trakcie realizacji. Z rzeczy zrealizowanych należało by wymienić:

- system rozpoznawania typów,
- system GameObjectów,
- component model,
- eventy,
- system scen.

Właściwie do wszystkiego mam też napisane testy. Jedynie pominąłem system scen ze względu na to, że nie wiem jeszcze czy po implementacji renderera i zarządzania assetami nie będę musiał wykonać w nim jakiś większych zmian. Zmieniłem teraz też podejście do tego co chcę zrobić. Po pierwsze chciałbym mieć do końca tego miesiąca proof of concpet, który jest działający, czyli mogę dodać do sceny game object i wyrenderować go, poruszać nim i w ogóle. Wiem, że to nie cały silnik, ale pozwoli mi to zboczyć czy idę w dobrym kierunku. Po zakończeniu tego etapu dopisze testy dla sceny i elementów nie Open GL'owych. 
W obecnym momencie skupiam, się więc nad następującymi rzeczami :

- wczytywaniem tekstur,
- zarządzaniem assetami,
- renderowaniem 2d

Każdą z tych rzeczy mam mocno rozgrzebaną, dodatkowo jeżeli chodzi o renderowanie jak już pisałem mam pewne problemy, co do wyboru technologii. Open GL jest już na rynku parę lat i jest co powoduje, że różnych materiałów na jego temat jest sporo. Z drugiej strony mamy nowe api czyli Vulcan'a, które jak już napisałem jest nowe co powoduje, że mniej na jego temat informacji. Bardzo dużo czasu zajął mi więc wybór pomiędzy tymi bibliotekami, jednak ostatecznie uznałem, że użyje Open GL z tym, że postaram się go na tyle opakować w swoje klasy, żeby w momencie kiedy będę gotowy przejść na Vulcana, to to zrobię bez zmiany api w samym silniku lub niewielkimi zmianami. Zobaczymy oczywiście jak to wyjdzie. 
Kolejną sprawą do której się przymierzam to wielowątkowości. W obecnym momencie silnik działa w jednym wątku, ale czytam na ten temat, więc myślę, że za jakiś czas spróbuje coś zadziałać, aby jakieś elementy działały w osobnych wątkach.  
To na razie na tyle zobaczymy co przeniesie ten miesiąc i na ile uda mi się zrobić to co chciałbym, aby było skończone.
