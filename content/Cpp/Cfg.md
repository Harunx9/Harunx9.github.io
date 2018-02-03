Title: Konfiguracja aplikacji za pomocą plików ini
Date: 2017-07-21 21:00
Category: C/C++
Tags: programming, Gamedev
Authors: Szymon Wanot
Status: published

Cześć. Dziś zajmiemy się konfiguracją aplikacji w C++. Temat przedstawię od strony mojego silnika 2DXngine. W przypadku C++ temat zewnętrznej konfiguracji nie jest tak oczywisty jak w przypadku C# i .NET, gdzie mamy pliki App i Web config. Taką konfiguracje w C++ możemy zapisać w plikach XML, ale jest to moim zdaniem format nie do końca czytelny dla człowieka. W swoich aplikacjach w C++ preferuję format ini, który wygląda następująco:

    [NazwaSekcji1]
    Właściwość1=Wartość1
    Właściwość2=Wartość2
    Właściwość3=Wartość3
    Właściwość4=Wartość4
    [NazwaSekcji2]
    Właściwość1=Wartość1
    Właściwość2=Wartość2
    Właściwość3=Wartość3
    Właściwość4=Wartość4

Jak dla mnie ten format jest dużo bardziej czytelny niż XML i dlatego go stosuje. W przypadku C++ w bibliotece standardowej nie ma klas i funkcji parsujących ini, musimy posilić się jakąś gotową biblioteką lub samemu napisać parsowanie takich plików. Jako, że programista powinien być leniwy w swojej pracy, to i ja zdecydowałem się skorzystać z czegoś gotowego. W C++ mamy sporo takich bibliotek ze względu na to, że potrzebowałam oprócz parsowania jeszcze dodatkowo zapis plików ini zdecydowałem się na [SimpleIni](https://github.com/brofield/simpleini). Sama nazwa już mówi ze biblioteka jest dość mała. Całość to właściwie jeden plik nagłówkowy, nop jeszcze 2 pliki pomocne przy encodingu UTF8 i to tyle. Z tego powodu nie budowałem biblioteki jaklo .lib tylko dodałem jej pliki do projektu. Teraz jak to wykorzystać:

    ::cpp
    CSimpleIniA inifile; 
    inifile.Load("cfg.ini"); // wczytanie pliku
    //wczytanie wartości z pliku
    bool isFullScreen = inifile.GetBoolValue("Graphics", "FullScreen");
    int windowWidth = (int)inifile.GetLongValue("Graphics", "WindowWidth", 640);
    int windowHeight = (int)inifile.GetLongValue("Graphics", "WindowHeight", 360);
    int openGLMinorVerion = (int)inifile.GetLongValue("Graphics", "GLMinor", 3);
    int openGLMajorVerion = (int)inifile.GetLongValue("Graphics", "GLMajor", 3);
    int doubleBufferToggle = (int)inifile.GetLongValue("Graphics", "DoubleBuffer", 1);

Jak widać odczyt danych jest dość prosty podajemy nazwę sekcji i nazwę właściwości oraz wartość która ma się pojawić defaultowo jak nie będzie jej w pliku. Jeżeli chcemy coś zapisać to musimy postąpić w następujący sposób:

    ::cpp
    CSimpleIniA inifile;
    inifile.SetBoolValue("Graphics", "FullScreen", true);
    inifile.SetLongValue("Graphics", "WindowWidth", 640);
    inifile.SetLongValue("Graphics", "WindowHeight", 360);

    inifile.SaveFile("newcfg.ini");

Zapisywanie wartości jest również dość proste, podobnie jak w odczycie podajemy nazwę sekcji, nazwę pola i wartość jaka ma być do niego zapisana. Na koniec wywołujemy funkcję save file ze ścieżką do  pliku w którym ma być to zapisane. W tym miejscu należy wspomnieć jak to działa w systemie Windows. Mianowicie jak mamy aplikacje zainstalowana w program files, to nie możemy tam zapisać plików bez uprawnień administratora, dlatego należy zapisywać dane w katalogu lokalnego użytkownika. W większości przypadków będzie to ścieżka:

    C:/Users/NazwaUsera/Documents/

SDL pozwala na pobranie ścieżki to tego katalogu za pomocą funkcji SDL_GetPrefPath("companyname", "appname"); więc jeżeli chcemy instalować u kogoś innego naszą aplikację należy o tym pamiętać, żeby konfiguracja użytkownika mogła zostać zapisana. To na razie na tyle jeżeli chodzi o konfigurację. Oczywiście samo SimpleIni powinno się opakować w jakieś własne klasy konfiguracyjne, tak żeby można było mieć to tego jakiś wygodny dostęp wszędzie w programie.
