Title: Komponentowe CLI część 1. Potrzeba oraz dostępne rozwiązania
Date: 2017-08-27 12:00
Category: .NET
Tags: blog, .net, programming, c#, .netcore, cli 
Authors: Szymon Wanot
Status: published

Cześć. Ostatni post o automatycznej rejestracji komponentów w Autofac był jedynie wstępem do tego co chcę osiągnąć w narzędziach, które obecnie pisze. Co do samych narzędzi to chciałbym mieć takie oto rozwiązania:

- Texture packer - narzędzie do pakowanie spritesheetów i animacji, które będzie rozumiał 2DXngine,
- Project generator - generuje podstawowy projekt 2DXngine z odpowiednią wersją silnika. Tworzy podstawową strukturę plików, kompiluje projekt, itp.,
- Asset Packer - jak już uda mi się jakoś zaimplementować to w C++, to chciałbym mieć możliwość spakowania wszystkich assetów do jakiegoś formatu binarnego, tak żeby zajmowały mniej miejsca i gra się do nich szybciej odwoływała.

Jak widomo im dalej w las tym więcej rośnie drzew, więc pewnie jeszcze mi jakieś pomysły dojdą. Ale po kolei. Myśląc nad tym jak takie toole z commandline zaprojektować doszedłem do wniosku, że fajne by było jakby miały one architekturę bazującą na pluginach. Co to znaczy? Chciałbym, aby sam program odpalał to co znajdzie sobie w swoim katalogu lub katalogu plugins w DLL i zarejestruje do kontenera zależności. Pozwoli mi to na bardzo wygodne dodawanie nowych komend czy zmienianie istniejących np. poprzez dodanie nowych algorytmów pakujących bez ingerencji w kod już istniejący. 

Przykładem niech będzie pakowanie tekstur. Najprostszym algorytmem pakowania jest pakowanie takich samych obrazów bez ich przycinania. Takie jakie znajdujemy w folderze pakujemy, generujemy XML i zwracamy, np. jakiś user potrzebuje algorytm pakowania takich samych tekstur z wycinaniem pustych pikseli, żeby zaoszczędzić miejsce. Bierze on wtedy IDE, dociąga Nuget z bazowymi typami, implementuje algorytm i w komendzie dokłada swoją DLL do katalogu z texture packer'em. Przy starcie program powinien dodać do kontenera Di nowy algorytm i jeżeli w parametrach pojawi się dodatkowo crop na true to zostanie on wykonany. Jak widzimy funkcjonalność zostanie dodana bez dodatkowych ingerencji w podstawowy kod, przynajmniej w teorii. Dodatkowym ograniczeniem mojego pomysłu jest multiplatfromowość, ponieważ chciałbym, aby narzędzia działały na każdej platformie.

Drugim problem dość łatwo rozwiązałem wybierając .NET Core, który w teorii ma działać nie tylko na różnych wersjach okienek, ale i na Linuksie i Apple. Tak jak napisałem teoretycznie, bo na razie tego nie sprawdzałem i opieram się na tym co Microsoft pisze na swoich stronach. 

Co do frameworków ułatwiających tworzenei aplikacji CLI to nie mam dużego doświadczenia, ale dokonałem przeglądu i na .NET Core znalazłem coś takiego jak [commandline](https://github.com/gsscoder/commandline) jest to bardzo dobra ,ponieważ korzystałem z niej kiedyś implementując migrator do mongo dla jednego z projektów. Pozwala ona tworzyć komendy jako klasy i potem za pomocą parsera je wytwarzać, niestety dodanie nowej komendy powoduje dodanie nowej linijki na reakcje, co zrobić kiedy się ona sparsuje. W kodzie wygląda to w następujący sposób:

    ::csharp
    [Verb("add", HelpText = "Add file contents to the index.")]
    class AddOptions {
      //normal options here
    }
    [Verb("commit", HelpText = "Record changes to the repository.")]
    class CommitOptions {
      //normal options here
    }
    [Verb("clone", HelpText = "Clone a repository into a new directory.")]
    class CloneOptions {
      //normal options here
    }

    int Main(string[] args) {
      return CommandLine.Parser.Default.ParseArguments<AddOptions, CommitOptions, CloneOptions>(args)
        .MapResult(
          (AddOptions opts) => RunAddAndReturnExitCode(opts),
          (CommitOptions opts) => RunCommitAndReturnExitCode(opts),
          (CloneOptions opts) => RunCloneAndReturnExitCode(opts),
          errs => 1);
    }

Dodawanie kolejnych wywołań zdyskwalifikowało niestety tą bibliotekę. Oprócz tego znalazłem kilka praserów, ale niczego co spełniło by moje oczekiwania. W takim wypadku postanowiłem sam zaimplementować rozwiązanie bazujące na pluginach. 

W kolejnym artykule przejdziemy do implementacji mojego rozwiązania, Tak z ciekawości czy zna ktoś ewentualnie jakieś podobne rozwiązanie pozwalające na łatwe tworzenie pluginów z DI. Jak coś to piszcie w komentarzach, bo ja sam nie umiałem nic sensownego znaleźć, a poświęciłem temu trochę czasu.

