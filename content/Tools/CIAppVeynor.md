Title: AppVeyor darmowe CI dla projektów Open Source
Date: 2017-09-25 07:00
Category: Inne, tools
Tags: inne, tools, CI, appveyor
Authors: Szymon Wanot
Status: published
Slug:appveynor-darmowe-ci-dla-projektow-open-source

Cześć. Jakiś czas temu natchnęło mnie i postanowiłem ogarnąć coś, żeby 2DXnegine budował się na serwerze Continous Integration. Dla niezaznajomionych z tematem Continous Integration to taki twór, który po każdym commicie będzie pobierał do siebie nasze źródła, kompilował je i odpalał testy - po tym wszystkim możemy gdzieś naszą zbudowaną aplikacje wystawić i robić jeszcze inne cuda, o których jeszcze nie pomyślałem. Na rynku istnieje parę usług CI dla projektów open source. Przy wyborze kierowałem się wsparciem dla MSBuild, ponieważ przez moje lenistwo nie zmieniłem jeszcze MSBuild'a na coś bardziej niezależnego od Visual Studio. To ograniczenie wykluczyło sporo serwisów, ale okazało się, że istnieje  darmowa usługa dla projektów open source wspierająca MSBuild, a jest to [AppVeyor](https://www.appveyor.com/). Jest to system oparty na windowsach, więc nadaje się rónież świetnie dla projetów .net'owych o czym też będzie w tym artykule. Zacznijmy od konfiguracji AppVeyor dla projektu C++. Na początku dodajemy na Dashboardzie serwisu nowy projekt z naszych repozytoriów githubowych. Jak projekt się utworzy to przechodzimy do zakładki settings i rozpoczynamy konfiguracje.
W zakładce General konfigurujemy format numeru build'a oraz branch z jakiego chcemy robić build:

![alt](/images/ci/BasicConfig.png)

Następnie w zakładce Environments konfigurujemy Visual Studio z którego chcemy buildować solucje oraz ewentulanie skrypty, kóre mają się odpalić porzed buildem. W moim przypadku musiałem dodać klonowanie submodułów git.

![alt](/images/ci/BuildEnv.png)

Aby uruchomić testy należy ze skryptu odpalić exe, które je zawiera. Ja używam [googletest](https://github.com/google/googletest). Jedynie co musiałem zrobić to usunąć testy używające OpenGL, ponieważ AppVeyor ma jakieś problemy z tymi testami, których nie udało mi się rozwiązać.

![alt](/images/ci/TestsCI.png)

Aby testy się wyświetliły w odpowiedniej zakładce trzeba wyeksportować je w odpowiednie miejsce. Skrypt eksportujący dodajemy w zakładce General. 

![alt](/images/ci/TestUpload.png)

Teraz jeszcze krótko na temat projektów .Net Core. Jak już mówiłem pisze również toole do swojego silnika. Postanowiłem je również dodać do CI. W przypadku .Net Core jest dużo prościej niż w C/C++. Zmianami jakie należy poczynić to dodanie restorowania nugetów przed buildem.

![alt](/images/ci/CorebeforeBuild.png)

Dodatkowo, jeżeli chcemy odpalić testy to również musimy je odpalić za pomocą commandline'owego narzędzia dotnet:

![alt](/images/ci/CoreTesting.png)

To w sumie tyle, każdy projekt builduje mi się na commita. W przyszłości pobawię się jeszcze z tworzeniem jakiś paczek, które będzie można pobrać zainstalować i używać, ale to na razie jeszcze pieśń przyszłości. Generalnie AppVeyor jako usługa bardzo mi się podoba ze względu na łatwość i szybkość konfiguracji. A jakie wy macie doświadczenia z usługami CI?