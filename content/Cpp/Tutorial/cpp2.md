Title: C/C++: Typy danych, zmienne i operatory
Date: 2016-10-31 01:00
Category: C/C++
Tags: blog, tutorial, programming
Authors: Szymon Wanot
Status: published

Witam ponownie, jeżeli to czytasz to znaczy, że wróciłeś po więcej C++. W tym wpisie postaram się przedstawić typy danych, operatory i koncepcję zmiennej. Zaczniemy od tego jakie możemy mieć zmienne w C++. 
Typów podstawowych jest sporo, więc postaram się omówić najpopularniejsze i najczęściej używane:

- int min: -2147483648 max: 2147483647 (liczby całkowite),
- float min: 1.17549e-38 max: 3.40282e+38 (liczby zmiennoprzecinkowe pojedynczej precyzji),
- double min: 2.22507e-308 max: 1.79769e+308 (liczby zmiennoprzecinkowe pojedynczej precyzji),
- short min: -32768 max: 32767 (małe liczby całkowite),
- long min: -2147483648 max: 2147483647 (duże liczby całkowite),
- char min: -127 max: 127 (typ do zapisu znaków),
- bool (typ logiczny posiadający dwie wartości: true (prawda) oraz false (fałsz)).

Do typów liczbowych możemy dodatkowo dodać przedrostek unsigned, co spowoduje, iż typ będzie mógł reprezentować tylko liczby dodatnie. Nie są to wszystkie możliwe typy danych, ale na początek powinno wystarczyć. 

Kolejną sprawą, którą chciałem omówić są zmienne i operatory. Zmienne mówiąc najprościej są to pojemniki w których przechowuje się różne wartości. Ponieważ C++ jest językiem silnie typowanym każda zmienna musi mieć jasno określony typ. W kodzie możemy zapisać to w następujący sposób:

    ::cpp
    #include <iostream>
    using namespace std;


    int main()
    {
        int myVariable; // deklaracja zmiennej
        myVariable = 10; // przypisanie wartości do zmiennej
        cout << myVariable << endl; // wypisanie wartości zmiennej na konsole
        return 0;
    }


Co ważne, jeśli nie przypiszemy wartości do zmiennej podczas uruchomienia programu otrzymamy błąd. Cały zapis da się nieco uprościć do niniejszej postaci:

    ::cpp
    #include <iostream>
    using namespace std;


    int main()
    {
        int myVariable = 20; // definicja zmiennej zmiennej
        cout << myVariable << endl; // wypisanie wartości zmiennej na konsole
        return 0;
    }


Jak można zauważyć deklaracja zmiennej z przypisaniem do niej wartości to tzw. definicja zmiennej. Spoko już wiemy czym są zmienne, możemy przejść do operatorów. Dzielą się one na kilka typów. Jako pierwsze na tapetę weźmiemy operatory matematyczne:

    ::cpp
    #include <iostream>
    using namespace std;


    int main()
    {
        int a = 1;
        int b = 30;
        cout << a + b << endl;   //dodawanie
        cout << b - a << endl;   //odejmowanie
        cout << b * b << endl;   //mnożenie
        cout << b / 3.0 << endl; //dzielenie
        cout << b % 2 << endl;   //modulo
        cout << "pre: " << ++a << " post: " << b++ << endl;   // pre i post inkrementacja
        cout << "pre: " << --a << " post: " << b-- << endl;   // pre i post dekrementacja
        a += b; // operator łączony w tym przypadku oznacza a = a + b
        cout << a << endl;  
        return 0;
    }

Poza operatorami matematycznymi C++ posiada również operatory logiczne:

    ::cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        bool a = true;
        bool b = false;
        
        bool c = a || b; // lub
        bool d = a && b;  // i


        cout << c << endl;
        cout << d << endl;
        cout << !b << endl; // negacja
    }

Kolejną grupą są operatory służące do porównywania wartości:

    ::cpp
    #include <iostream>
    using namespace std;


    int main()
    {
        int a = 10;
        int b = 15;


        int c = a == b; // czy a jest równe b
        int d = a < b;    // czy a mniejsze od b
        int dd = a <= b;// czy a mniejsze lub równe b
        int f = a > b;    // czy a większe od b
        int ff = a >= b;// czy a większe lub równe b
        int t = a != b;    // czy a różne od b
    }

Pozostaje jeszcze kwestia operatorów bitowych, ale ze względu na złożoność tematu zostaną one omówione w późniejszych wpisach. W obecnym momencie nie będą one potrzebne do omawiania kolejnych elementów języka C++.

