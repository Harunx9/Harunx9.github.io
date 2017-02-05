Title: Akka.NET: Instalacja i obowiązkowy “Hello world”
Date: 2016-12-06 00:00
Category: .NET
Tags: blog, .net, programming, c#, actror model, Akka.NET, Akka
Authors: Szymon Wanot
Status: published

Jakiś czas temu pisałem na temat aktor model z perspektywy pracy z nim. Osoby, które spotykają się z tym tematem po raz pierwszy odsyłam do poprzedniego posta.
W tej serii mam zamiar przedstawić Wam Akka.NET, czy port aktor modelu prosto z JVM. Zabawę zaczniemy od prostego “Hello world”. W  późniejszym czasie stworzymy w Akka nowy projekt konsolowy.
Instalacja Akka w konsoli Package Manager wygląda następująco:

    ::powershell
    Install-Package akka


Jak wszystko zrobiliśmy poprawnie to powinniśmy mieć zainstalowaną w projekcie bibliotekę Akka i jej zależności. Zaczniemy nieco od tyłu, ponieważ zdefiniujemy wiadomość, którą nasz pierwszy aktor otrzyma:

    ::csharp
    public class HelloWorldMsg
    {
        public string Message { get; private set; }
 
        public HelloWorldMsg(string message)
        {
            Message = message;
        }
    }


Tak skonstruowany komunikat powinien spełniać założenie o niezmienności wiadomości. Istnieje jeszcze jeden sposób napisania obiektu readonly, ale na razie taka forma powinna nam wystarczyć. Przejdźmy teraz do setupu aktora, który będzie odbierał nasze wiadomości. 
Akka posiada 3 typy podstawowe dla aktorów: ReceiveActor, TypedActor, UntypedActor. Do naszego “Hello world” użyjemy ReceiveActor :

    ::csharp
    public class HelloWorldActor : ReceiveActor
    {
 
        public HelloWorldActor()
        {
            Receive<HelloWorldMsg>(msg => Console.WriteLine(msg.Message));
        }
    }


Każdy aktor w systemie musi dziedziczyć po jednym z dwóch wymienionych wyżej typów. Receive działa w taki sposób, iż rejestrujemy za pomocą generycznej funkcji Receive<T>(Action<T> handler) typ wiadomości i reakcję na to kiedy dany typ przyjdzie do aktora. W naszym przypadku jest to wypisanie na ekran konsoli tego co przyszło w property Message w naszej powitalnej wiadomości. Aby skorzystać z naszego przygotowanego aktora należy skonstruować funkcję main w następujący sposób:

    ::csharp
    class Program
    {
        static void Main(string[] args)
        {
            var system = ActorSystem.Create("TutorialSystem");
 
            var actor = system.ActorOf<HelloWorldAcxtor>("HelloActor");
 
            actor.Tell(new HelloWorldMsg("Hello actor system world"));
 
            Console.ReadKey();
        }
    }


Jeżeli wszytko poszło zgodnie z planem to powinniśmy otrzymać w naszej konsoli wypisane "Hello actor system world". W tym pierwszym wprowadzającym poście to na tyle. W kolejnym zajmiemy się możliwościami komunikacji z aktorami oraz tworzeniem nieco większej ich liczby. 
