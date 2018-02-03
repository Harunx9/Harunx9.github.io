Title: Jak stać się junior developerem - Tutorial
Date: 2017-11-20 00:00
Category: Inne
Tags: blog, inne, it, praca
Authors: Szymon Wanot
Status: published

Cześć. Ostatnio nie mam zbyt wiele czasu pisać, ale jest jeden temat na który powinienem się wypowiedzieć. Kilku moich znajomych próbuje się przekwalifikować z jakieś innej dziedziny na programistę lub dostać prace w it, więc zadają mi pytania jak to zrobić. Jestem dość specyficzną osobą, to znaczy odnalazłem pasję w programowaniu i poza pracą prowadzę tego oto bloga, rozwijam swój autorski silnik do gier oraz narzędzia do niego, więc poświęcam na swój rozwój sporo czasu i zdaje sobie sprawę, że nie każdy tak chce/może/jest w stanie. Zastrzegę na początku, że to co tu pisze to moje prywatne opinie i mogą się one różnić od tego co jest na rynku pracy w Twojej miejscowości. Będę sporo odwoływał się do wymagań na .NET developera, ponieważ taką technologią zajmuje się w pracy, choć postaram się to zminimalizować i jak najbardziej uogólnić.

###Co trzeba umieć?

To jest punkt tak na prawdę najtrudniejszy, ponieważ rozbija się o technologię i w tym momencie powiem nieco co trzeba umieć jako taki początkujący .NET developer. Po pierwsze niezależne od technologii warto by znać:

- język w którym będziemy programować - wiem banalne i głupie, ale jak ktoś by chciał programować jako .NET/C# to miło żeby ogarniał elementy języka takie jak - Linq, delegaty, funkcje lambda, bo jest to jakiś wyróżnik C# względem innych języków i te elementy na co dzień się stosuje w normalnej pracy.
- programowanie obiektowe - teraz widzę to święte oburzenie, ale nie znajomość języka to nie to samo co programowanie obiektowe, bo można znać C# i pisać klasy po 5k linijek nie korzystać z kompozycji, polimorfimzu i jakichkolwiek dobrych praktyk separacji kodu w klasy. Mimo, że nie mam bardzo długiego stażu, to przeszedłem kilka projektów i cześć z nich nie miała nic wspólnego z programowaniem obiektowych mimo, że były klasy.
- wzorce projektowe - to jest nieco dla mnie kontrowersyjne, bo sam ich na pamięć nie znam. Bardziej jest to na takiej zasadzie, że mam jakieś zadanie i nie mam na niego pomysły to sięgam do wzorców i często tam znajduję jakieś pomysły na implementacje
- SOLID - są to ogóle zasady dobrego programowania sprowadzające się do dobrych praktyk. Jeżeli znasz SOLID to jesteś w stanie za ich pomocą zaimplementować wzorce projektowe nie znając ich.
- system kontroli wersji  GIT/SVN - jest to narzędzie niezwiązane z samym programowaniem. Pomaga ono we współpracy wielu developerów. Generalnie działa ono tak, że jest jakieś jedno centralne repozytorium, gdzie przechowuje się kod i można tam za ich pomocą ten kod dodawać. Git i SVN są najbardziej popularne generalnie polecam zacząć od Git'a, ale SVN też można jeszcze gdzie nie gdzie spotkać.

To jest moim zdaniem takie minimum, które należałoby umieć. Co do wzorców to tak jak napisałem może nie tyle żeby na pamięć je znać tylko bardziej tak orientować się, że są i że jak mamy problem z jakąś implementacją to mogą nam pomóc.

Poza tymi rzeczami teraz taki Junior .NET Developer powinien liznąć co nieco ekosystemu, czyli wiedzieć coś o NuGET, Visual Studio itp. Kolejną sprawą są frameworki. Ja miałem akurat takie szczęście, że na uczelni przeszliśmy właściwie przez wszystko odnoście .NET, czyli aplikacje konsolowe, okienkowe i webowe. Każdy język ma jakieś swoje frameworki, które trzeba znać. Tu oczywiście też nie na pamięć, ale jak aplikujemy do aplikacji webowych to takie MVC i WebAPI trzeba znać.

###Czy studia pomogą?

Tu będzie mocno kontrowersyjnie, ale moim zdaniem studnia niczego sensownego was nie nauczą. Sam nieco żałuje, że nie zrezygnowałem po pierwszym roku studiów,ponieważ programowania uczyłem się głównie sam w domu po pracy. Później zwolniłem się i siedziałem przez około 6 miesięcy ucząc się po 8 godzin dziennie. Myślę, że regularna codzienna nauka a nie studia pozwoliły mi wcześnie znaleźć pracę. Studia owszem są fajne, ponieważ dają możliwość znalezienia ludzi, dzięki którym uczymy się szybciej, ale sam proces nauki to jednak i tak nasz wysiłek, którego nikt za nas nie wykona. 

###To co w takim razie zrobić ?

Teraz odpowiem na to znienawidzonym "to zależy". Jeżeli masz do 30 lub koło 30 lat i nie masz zobowiązań to idź na te studia. Tak jak napisałem powyżej nikt Ci tam wiedzy do głowy nie włoży, ale jak sam będziesz pracował to masz szanse poznać ludzi dzięki którym szybciej się rozwiniesz. Jeżeli nie masz czasu na studia to polecam najpierw jakiś kurs pokroju SoloLearn, TreeHouse, Code School. Część jest darmowa część jest płatana. Takie kursy dobrze uczą składni języka przez kolejne przykłady. Potem można sobie znaleźć jakieś ćwiczenia z danego języka i próbować je robić.

Alternatywą do dalszych ćwiczeń jest wymyślenie sobie jakiegoś projektu i próba jego implementacji. Pewnie zanim coś powstanie to wyrzucicie kod milion razy do kosza, ale dzięki temu nauczycie się najlepiej. Ważnym jest też żeby to co robicie było widoczne. I w tym miejscu polecam takie coś jak GgitHub. Jest to portal gdzie za darmo możecie sobie hostować wasze repozytoria gitowe. Generalnie należy wyróżnić się wśród kandydatów na stanowisko pracy. Jeżeli pokażemy własny projekt, pasję z jaką go realizujemy, to że się interesujemy tym programowaniem. Mamy dzięki temu większe szanse na dostanie się do pracy niż statystyczny magister informatyki nawet jeżeli ma 5 i wyróżnienie na dyplomie.

I teraz tak na zakończenie najważniejsza porada już na rozmowę kwalifikacyjną. Programista, który będzie Cię rekrutował to też człowiek i on też nie wie wszystkiego. Generalnie ważne jest to żeby nie wyidealizować sobie ludzi pracujących w tym zawodzie. Pozwoli to na większy luz podczas rozmowy co przełoży się na lepszy odbiór twojej osoby przez rekrutrów. Warto też pamiętać o tym, że my też nie musimy wiedzieć wszystkiego. Każdy ma jakąś specjalizacje, używał takich czy innych bibliotek, więc należy wyluzować, bo jak używałeś Autofac to Structure Map czy Castle Windsor też będzie używał bez problemu.

Podsumowując co należy zrobić to pisać kod po trzykroć, ponieważ programowanie to nauka przez powtarzanie. Im więcej piszemy tym lepiej piszemy. Po drugie warto znaleźć swoje zainteresowanie w programowaniu, ponieważ jak się czymś interesujemy to łatwiej przychodzi nam nauka. Ja odnalazłem swoje zainteresowanie w gamedevie i mimo, że na co dzień nie pracuje przy grach, to wykorzystuje masę zdobytej wiedzy w codziennej pracy. To czy iść na studia jest sprawą indywidualną. Sam znam kilku programistów, którzy studiów nie ukończyli i w niczym im to nie przeszkadza. 

To chyba na tyle. Jeżeli macie jakieś pytania czy uwagi to jak zawsze zapraszam do sekcji komentarzy.