Title: Własny TypeInfo w C++
Date: 2017-03-27 19:10
Category: Gamedev
Tags: DSP2017, Gamedev, C++
Authors: Szymon Wanot
Status: published

Cześć, dziś chciałem pokazać jak zrobiłem system informacji o typach obiektów w silniku 2DXngine, który powstaje w ramach konkursu "Daj się poznać". Taki feature był mi porzebny do wysukiwania po typie komponentów z GameObjectu. Nie chciałem używać standardowego  TypeId, ponieważ mądrzejsi ode mnie mówią, że jest to powolne, i że refleksja w  runtime jest ogólnie zła. Dlatego należy pomyśleć tak, aby jak najwięcej zrobić w compile time. Tak jak już wiecie dopiero uczę się C++, więc przejrzałem trochę Internet i w moim rozwiązaniu mocno inspirowałem się [TYM](http://www.axelmenzel.de/articles/rtti) artykułem. Podobnie jak w nim moje rozwiązanie opiera się na makrach i TypeCache, ale po kolei. Aby zarejestrować typ używam takich oto makr:

    ::cpp
    #define DECLARE_TYPE_INFO(Type, BaseType)                                            \
                                                                                         \
    template<>                                                                           \
    struct TypeIdInfo<Type>                                                              \
    {                                                                                    \
        static TypeInfo getType()                                                        \
        {                                                                                \
            static const TypeInfo typeInfo = getOrRegisterTypeInChache(#Type, #BaseType);\
            return typeInfo;                                                             \
        }                                                                                \
    };                                                                                   \


To makro dodaję w plikach .h., jeżeli nie ma bazowego typu zostawiam "" . Będę musiał to przemyśleć w przyszłości, na razie to rozwiązanie mi nie przeszkadza.

    ::cpp
    #define DEFINE_TYPE_INFO(Type)                                 \
                                                                   \
    template<>                                                     \
    struct RegisterType<Type>                                      \
    {                                                              \
        RegisterType()                                             \
        {                                                          \
            TypeIdInfo<Type>::getType();                           \
        }                                                          \
    };                                                             \
    static const RegisterType<Type> CAT(registerType, __COUNTER__);

Powyższe makro oddaje w plikach .cpp, żeby rejestracja nastąpiła automatycznie. Wykorzystany jest tu pewien trik, a mianowicie jeśeli zdefiniujemy generyczna statyczny const, to zostanie on wywołany przed funkcją main, co daje nam therad safe przy rejestracji naszych obiektów.
Funkcja rejestrująca wygląda w następujący sposób:

    ::cpp
    TypeInfo getOrRegisterTypeInChache(const char * name, const char * parentTypeName)
    {
        TypeInfo type;

        auto typeCache = TypeCache::get_instance();

        if (typeCache->get_typeAlreadyExist(name) == false)
        {
            int id = TypeCache::get_nextId();
            int paretnId = -1;
            if (strcmp("", parentTypeName) != 0)
            {
                TypeInfo* parentType = typeCache->get_typeByRef(parentTypeName);

                if (parentType)
                {
                    paretnId = parentType->get_id();
                }
            }

            type = TypeInfo(name, id, paretnId);
            typeCache->addType(type);
        }
        else
        {
            type = typeCache->get_typeByValue(name);
        }

        return type;
    }

W skrócie zagląda ona do TypeCache, czy dany typ jest już tam zarejestrowany i jeżeli jest to go zwraca, a jeżeli nie to tworzy nowy. W 99 procentach przypadków będzie nam oddawała już wygenerowany TypeId, ponieważ jak już napisałem rejestracja odbywa się automatycznie przed funkcją main. Ze względu na to, że całość kodu jest na githubie nie będę dokładnie omawiał implementacji TypeCache i TypeInfo, jeżeli kotś jest ciekawy to zapraszam [TU](https://github.com/Harunx9/2DXngine/tree/master/2DXngine.Core/src/TypeInformation). Zaimplementowany system informacji o typie pozwala mi na to, że mogę w łatwy sposób wyszukiwać instancji obiektów ,które reprezentują daną klasę, ale i wyszukiwać prze klasy bazowe. Przykładowo może poszukać wszystkich komponentów dziedziczących po UpdateableComponents. System ten ma niestety jedno ograniczenie a mianowicie, aby dawał on informacje deterministyczne obiekty mogą dziedziczyć tylko i wyłącznie po jednej klasie bazowej. Oczywiście można by go bardziej rozwinąć tak, aby wprowadzić interfejsy czy wielodziedziczenie, ale na razie nie widzę takie potrzeby, ponieważ z założenia hierarchia dziedziczenia komponentów jest raczej dość liniowa, więc myślę, że na potrzeby silnika rozwiązanie jest wystarczające. Pozostaje jeszcze kwestia optymalizacji ale to, że tak powiem wyjdzie podczas implementacji gry na silniku, więc na razie nie jestem w stanie sprawdzić jak mocno takie otrzymywanie informacji o typie spowolni wykonywanie logiki gry. To chyba na tyle, jeżeli chodzi o moje podejście to systemu informacji o typach. Jeżeli macie jakieś pytania czy uwagi to zapraszam do sekcji komentarzy.