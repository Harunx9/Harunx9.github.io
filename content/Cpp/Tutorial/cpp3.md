Title: C/C++: Instrukcje warunkowe if i switch
Date: 2016-11-29 01:00
Category: C/C++
Tags: blog, tutorial, programming
Authors: Szymon Wanot
Status: published

Zdaję sobie sprawę z tego,że ostatni post był nieco przydługi i zostało w nim przekazane więcej elementów, dlatego zdecydowałem się na nieco mniejsze objętościowo posty (jeżeli jakiś temat będzie nieco dłuższy to podzielę go na kilka postów, zamiast starać się upchać wszystko razem). 
W trzeciej już części artykułów  o C++ omówimy dwie konstrukcje tego języka. Jako pierwszą na tapetę weźmiemy konstrukcje warunkową if..else. Instrukcja służy do rozgałęziania naszego kodu w zależności od spełnionego warunku. Podstawowa konstrukcja ma następującą budowę:

    ::cpp
    if (warunek)
    {
        //kod wykona się, jeżeli warunek jest prawdziwy
    }
    else
    {
       //kod wykona się, jeżeli warunek nie jest prawdziwy
    }


Przyjrzyjmy się na poniższy przykład: 

    ::cpp
    #include <iostream>
    using namespace std;

    int main()
    {
        int age = 18;

        if (age < 20)
        {
            cout << "masz mniej niz 20 lat" << endl;
        }
        else
        {
            cout << "masz 20 lub wiecej lat" << endl;
        }
    }

Powyższy kod wypisze “masz mniej niż 20 lat”, ponieważ zmienna age ma przypisaną wartość 18. W ramach instrukcji warunkowej if możemy kolejne wywołania if deklarować bezpośrednio po else:

    ::cpp
    #include <iostream>
    using namespace std;
 
    int main()
    {
        int age = 20;
 
        if (age < 20)
        {
            cout << "masz mniej niz 20 lat" << endl;
        }
        else if(age == 20)
        {
            cout << "masz 20 lat" << endl;
        }
        else
        {
            cout << "masz 20 lub wiecej lat" << endl;
        }
    }

W tym przypadku prawdziwy jest środkowy warunek, czyli “age == 20”, więc do konsoli zostanie wpisany tekst “masz 20 lat”. W C/C++ używana jest jeszcze jedna konstrukcja warunkowa a mianowicie switch. Podstawowa jej budowa wygląda w następujący sposób:

    ::cpp
    switch (input)
    {
        case elem1:
            // kod wykona się , jeżeli element input jest równy elem1
            break;
        case elem 2:
            // kod wykona się, jeżeli element input jest równy elem2
            break;
        default:
            // kod wykona się, jeżeli element input nie 
            //został dopasowany z żadnym elementem powyżej
            break;
    }

Popatrzmy na kolejny przykład:

    ::cpp
    #include <iostream>
    using namespace std;
 
    int main()
    {
        int item_count = 2;
 
        switch (item_count)
        {
            case 0:
                cout << "Nie masz zadnych przedmiotow" << endl;
                break;
            case 1:
                cout << "Masz 1 przedmiot" << endl;
                break;
            case 2:
                cout << "Masz 2 przedmioty" << endl;
                break;
            default:
                cout << "Masz więcej niż 2 przedmioty" << endl;
                break;
    }
}

W tym przypadku na konsole zostanie wypisany tekst “Masz 2 przedmioty”, ponieważ zmienna item_count ma wpisaną wartość 2. Spróbuj sam zmienić wartość zmiennej item_count, aby zobaczyć różnice kiedy będzie posiadała wartość 0, 1, oraz 3 i więcej.
Konstrukcja switch jest jednak najczęściej wykorzystywana z typem wyliczeniowym, czyli “enum”. Enum tak w największym uproszczeniu pozwala na nazwanie nam liczb, które mają znaczenie w naszej logice. Typ enum konstruujemy w następujący sposób:

    ::cpp
    enum NazwaTypu
    {
        Opcja1,
        Opcja2,
        Opcja3
    };

Przykładem niech będzie wypisanie typu broni w grze:

    ::cpp
    #include <iostream>
    using namespace std;
 
    enum WeaponType
    {
        MELLE,
        RANGE,
        THROW
    };
 
    int main()
    {
        WeaponType type = WeaponType::RANGE;
 
        switch (type)
        {
            case WeaponType::MELLE :
                cout << "Bron do walki w zwarciu" << endl;
                break;
            case WeaponType::RANGE:
                cout << "Bron do walki zasiegowej" << endl;
                break;
            case WeaponType::THROW:
                cout << "Bron rzucana" << endl;
            break;
        }
    }

W dużej grze taki kod oczywiście nie miałby racji bytu, ale dla unaocznienia jak działa typ wyliczeniowy nadaje się jak najbardziej. W tym poście to byłoby na tyle do zobaczenia w kolejnej części kursu C/C++
