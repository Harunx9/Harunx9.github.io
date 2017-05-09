Title: Eventy jak w C# w C++
Date: 2017-03-31 21:00
Category: Gamedev
Tags: DSP2017, Gamedev, Tools
Authors: Szymon Wanot
Status: published

Cześć.
Niestety w tym tygodniu nie miałem czasu za dużo popracować nad silnikiem. Co prawda pisze system scen, ale mam to tak rozgrzebane, że nie jestem w stanie tego podsumować. Mimo tego udało mi się zrobić jedną fajną rzecz, którą chciałem się z wami podzielić. Implementując silnik pomyślałem, że będę od czasu do czasu musiał powiadamiać pewne elementy sceny o tym, że np. GameObject zyskał nowy komponent czy childa lub coś innego się wydarzyło się, co ma jakieś znaczenie dla innych GameObjectów czy logiki gry. Początkowo chciałem zaimplementwotać EventBus'a, wiecie taki statyczny z subscriberami i publisherami, ale pomyślałem tak skoro udało mi się zaimplementować system typów to może uda się przenieść do C++ eventy podobne do tych C#. Myśląc niedługo zdecydowałem się spróbować a oto efekty pracy.  Na potrzeby rozwiązania zaimplementowałem Event handler nie parametryzowany i nie parametryzowany, binding funkcji handlującej dany event, oraz makra pozwalające w łatwy sposób tworzyć binding. Jako, że kod jest na githubie a dokładnie (TU)[https://github.com/Harunx9/2DXngine/tree/master/2DXngine.Core/src/Utils/Events] nie będę osobno omawiał handlerów tylko pokaże jak działa całość na podstawie jednego z nich. W całej implementacji chodziło mi o coś takiego jak mamy w C#, czyli :

    ::csharp
    someObject.SomeEvent += HandlerFunction; //przypinanie eventu
    someObject.SomeEvent -= HandlerFunction; //odpinanie eventu

Co prawda mój system jest pewnie dużo prostszy, ale w sumie działa podobnie mimo paru ograniczeń. Przykładowy handler wygląda tak:

    ::cpp
    class EventHandler
    {
    public:
        EventHandler& operator+=(Binding<EventArgs> &binding)
        {
            _subscribers[binding.get_code()] = binding.get_func();
            return *this;
        }

        EventHandler& operator-=(Binding<EventArgs> &binding)
        {
            _subscribers.erase(binding.get_code());
            return *this;
        }

        bool isUsed() { return _subscribers.empty() == false; }

        void invoke(EventArgs args)
        {
            auto tmp = this->_subscribers;
            for (auto& subscriber : tmp)
            {
                subscriber.second(args);
            }
        }

        void operator()(EventArgs args)
        {
            this->invoke(args);
        }

        inline static int get_nextID()
        {
            return _curretnId++;
        }
    private:
        static int _curretnId;
        std::map<int, std::function<void(EventArgs)>> _subscribers;
    };

Całość jak widać udało mi się zrobić nadpisując operatory : +=. -= oraz (). Jest to wielka siłą C++ ale jak wiemy "with great power comes great responsibility", więc nie polecam stosować nadpisania operatorów do każdego problemu. Dodatkowo ze względu na to, żeby wygodniej usuwało się subskrybentów zaimplementowałem statyczne generowanie kolejnych id dla bindingów, tak aby były one w miarę unikalne, a jednocześnie myślę, że nikt wartości int nie przekroczy, jeżeli będzie chciał korzystać z tego silnika. Aby taka sytuacja nastąpiła musiał by ktoś na prawdę nadużywać eventów. Aby można było dodawać eventy stworzyłem oto taką strukturę: 

    ::cpp
    template<typename TEventArgs>
    struct Binding
    {
        Binding() {}
        Binding(int code, std::function<void(TEventArgs)> func)
        {
            this->_code = code;
            this->_func = func;
        }

        int get_code() const { return this->_code; }
        std::function<void(TEventArgs)> get_func() const { return this->_func; }

    private:
        int _code;
        std::function<void(TEventArgs)> _func;
    };

Enkapsuluje ona id bindingu oraz wskaźnik na funkcje. Z mojej wiedzy wynika, że std::function to nowy typ dostępny od C++11(na studiach uczyłem sie C++98, więc dla mnie jest to nowość), więc zobaczymy jak się sprawdzi jak na razie w testach wygląda dobrze, więc mam nadzieje, że nie będzie z nią problemów wydajnościowych.
Do tego dodałem jeszcze 2 makra automatyzujące tworzenie bindingów. I to tyle implementacji, jeżeli ktoś chce zobaczyć przykłady użycia to znajdują się one w unit testach. Mam nadzieję że taka implementacja się sprawdzi. Jak skończę implementacje GameObject' u wraz ze zdarzeniami zmian jego struktury to dam wam znać. Jeżeli ktoś ma jakieś pomysły, rady, opinie to jak zawsze zapraszam do sekcji komentarzy.
