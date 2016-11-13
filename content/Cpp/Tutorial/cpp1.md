Title: C/C++: Konfiguracja środowiska
Date: 2016-10-16 01:00
Category: C/C++
Tags: blog, tutorial, programming
Authors: Szymon Wanot
Status: published

No i stało się, pierwszy techniczny post na blogu. Na samym początku muszę się Wam do czegoś przyznać, a mianowicie od mojego ostatniego razu z C/C++ minęły około 2 lata. Wracam do tego języka pisząc niewielkich rozmiarów silnik do gier. Doszedłem do wniosku, że fajnym pomysłem będzie szybkie przejście przez podstawowe elementy tego języka. A nuż jeszcze ktoś na tym skorzysta. 

Całość kursu będzie oparta o Visual Studio 2015 Community i system operacyjny Windows 10. Osoby, które używają Linuksa, również powinny z tego materiału skorzystać (niestety konfigurację środowiska musicie zrobić w własnym zakresie). Ze swojej strony proponuję zapoznać się ze środowiskiem Code Blocks na Linuksa (z tego co pamiętam to nie jest ono złe).  

Na ten moment wydaje się być wszystko jasne, więc startujemy z konfiguracją    środowiska Visual Studio 2015 Community. Konfigurację należy pobrać z oficjalnej strony Microsoftu: https://www.visualstudio.com/vs/ . 
Co ważne Visual Studio 2015 Community nie instaluje kompilatora C++ automatycznie, więc należy zaznaczyć to w instalatorze, tak jak na poniższym screenie:


![Alt install](/images/cpp1/vsIntall.PNG)

Po instalacji, która zajmie trochę czasu, należy uruchomić Visual Studio 2015 Community i zalogować się na konto Microsoft. Gdy już wszystko mamy skończone, klikamy File > New > Project. Naszym oczom powinno ukazać się następujące okienko, z którego wybieramy Win32 Console Application:

![Alt install](/images/cpp1/Createcppproj.PNG)

Gdy wszystko poszło zgodnie z planem, powinno wyświetlić się nam następujące okienko dialogowe, w którym klikamy Next:

![Alt install](/images/cpp1/cppproj1.PNG)

Na następnym dialogu wybieramy opcje, tak jak na poniższym screenie, aby utworzyć pusty projekt C++:

![Alt install](/images/cpp1/cppproj2.PNG)

Po wcześniejszych operacjach powinieneś otrzymać pusty projekt, do którego trzeba dodać nasz pierwszy plik z kodem źródłowym programu. Zrobimy to naciskając prawym klawiszem myszy na ikonie projektu:

![Alt install](/images/cpp1/fileadd.PNG)

Powinno się nam rozwinąć Menu kontekstowe, z którego wybieramy Add > New Item. 
Z dialogu wybieramy .cpp file i nazywamy plik main.cpp., klikamy ok i w ten oto sposób mamy pierwszy plik.
Każdy program w C/C++ zaczyna się od funkcji main, która musi mieć pewną zdefiniowaną strukturę:

    ::cpp
    int main()
    {
        return 0;
    }


Po naciśnięciu Ctrl + F5 rozpocznie się kompilacja, która jeśli się powiedzie pojawi się puste okienko wiersza poleceń. Nasz program uruchomił się i wykonał, oczywiście nic nie widzimy poza pustym ekranem, ponieważ nasz program nic jeszcze nie robi. By zmienić ten stan rzeczy wypiszemy standardowe “Hello World”. W związku z tym musimy do istniejącej funkcji main odrobinę dopisać:

    ::cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        cout << "Hello World" << endl;
        return 0;
    }

Widzimy, że pojawiło się trochę nowych rzeczy, które po kolei omówię. Dyrektywa #include <iosteram> mówi, że do naszego programu importujemy moduł wejścia wyjścia w naszym przypadku będzie to wyjście na konsole systemową. Kolejna linijka, czyli using namespace std; to powiedzenie kompilatorowi, że ma nam pozwolić używać ad hoc funkcji ze standardowej przestrzeni nazw. O przestrzeniach nazw powiem jeszcze w dalszej części kursu. Linijka cout << "Hello World" << endl; jest opowiedzialna za wypisanie na wyście konsoli systemowej napisu “Hello World” i przejście kursora do nowej lini. 
To tyle w tej części za niedługo kolejne zmagania z C++.
