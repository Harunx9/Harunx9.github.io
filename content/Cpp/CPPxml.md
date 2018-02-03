Title: PugiXML, czyli proste prasowanie XML w C/C++
Date: 2017-10-11 19:00
Category: C/C++
Tags: programming, Gamedev
Authors: Szymon Wanot
Status: published

Cześć. Jakiś czas temu stanąłem przed potrzebą wyboru jakiegoś rozwiązania do pracy z plikami XML. W C/C++ jest kilka bibliotek do obsługi XML'i:

- TinyXML,
- RapidXML,
- LibXML2,
- BoostXML,
- PugiXML.

Jak pewnie można się domyślić po tytule, to mój wybór padł na bibliotekę [pugixml](https://pugixml.org/). Wybrałem tak dlatego, że jej Api najbardziej przypomina to co mamy w C# pod nazwą XDocument i jest to składająca się z 3 plików biblioteka, więc możemy ją po prostu wrzucić w projekt i  nie trzeba się bawić z dodawaniem lib i dll co w C++ jest momentami nieco trudne. Skoro już wiadomo co i jak to przyjrzyjmy się jak można używać biblioteki. Przykłady będą oparte na wczytywaniu spritesheet'a animacji w 2DXngine, ponieważ tam też tej biblioteki użyłem. Załóżmy, że mamy oto taki XML:

    ::xml
    <animations>
        <animation name="animationName1">
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
        </animation>
        <animation name="animationName2">
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
            <frame number="0" x="0" y="0" width="50" height="50" offsetx="0" offsety="0"/>
        </animation>
    </animations>

Aby zaczytać pliczek musimy napisać takie oto linijki kodu:

    ::cpp
    pugi::xml_document doc;
    pugi::xml_parse_result result = doc.load_file("/path/to/file.xml");

Następnie wyciągamy główny element animation który pozwoli nam potem iterować po kolejnych animacjach:

    ::cpp
    auto  root = doc.child("animations");
    for (auto& animation : root.children("animation"))
    {
	    //impl
    }

Do atrybutów możemy się odnieść w następujący sposób:

    ::cpp
    int x = frame.attribute("x").as_int();
    int y = frame.attribute("y").as_int();
    int width = frame.attribute("width").as_int();
    int height = frame.attribute("height").as_int();
    int offsetx = frame.attribute("offsetx").as_int();
    int offsety = frame.attribute("offsety").as_int();

Całkiem fajną funkcjonalnością jest możliwość wymuszenia rzutowania na porządany typ. Co do zapisywania XML, to nie testowałem tego sam, ponieważ nie mam takiej potrzeby, ale w [dokumentacji](https://pugixml.org/docs/quickstart.html) jest napisane, że się da i jakieś mega skomplikowane nie jest. Biblioteka działa szybko, co było jednym z wyznaczników kiedy wybierałem to rozwiązanie. 
To w sumie na tyle. A wy jakich bibliotek używacie do obsługi XML?
