Title: Automatyczna rejestracja zależności w Autofac na .NETCore
Date: 2017-08-20 00:00
Category: .NET
Tags: blog, .net, programming, c#
Authors: Szymon Wanot
Status: published
            
Cześć. Dawno mnie nie było, ale ostatnio w większym stopniu skupiłem się na 2DXngine, więc czasu na pisanie postów automatycznie jest mniej. Ze względu na to, że obecnie implementuję narzędzia potrzebne do pracy z silnikiem (repo jest [TU](https://github.com/Harunx9/Xngine.Tools)) chciałem nieco napisać o mechanizmach, które tam tworzę. Po pierwsze całość będzie napisana w .Net Core ze względu na to, że jest to framework multiplatformowy, a ja jeszcze Core nie próbowałem, a uważam, że czas zacząć. Po drugie narzędzi będzie parę, ale obecnie ze względu na to, że chce przetestować w silniku implementuje texture packera, czyli toola, który z kilku tekstur wygeneruje mi jedna i konfiguracje xml dzięki, której będę mógł rysować to co chce z tej dużej scalonej tekstury. .Net Core nieco się różni od tego co ma do zaoferowania pełna wersja .Net Framework, więc kod pokazywany może być nieco inny od tego co używacie na co dzień jako programiści C#.

Wstrzykiwanie zależności jest ważnym elementem każdej aplikacji, pozwala ono w wygodny sposób tworzyć i testować obiekty jako niezależne komponenty. W .Net mamy parę frameworków kontenerów wspierających wstrzykiwanie zależności. Ja ze względu na moje prywatne preferencje wybrałem [Autofac](https://autofac.org/). Słabą częścią wszystkich frameworków jest potrzeba ręcznej konfiguracji tego co chcemy żeby w danym kontenerze się znalazło. Autofac posiada możliwość konfiguracji za pomocą kodu C# jak i w Xml czy Json. Pomyślałem sobie, że można by było jakoś ten proces budowania kontenera i rejestracji komponentów zautomatyzować. W swoich dywagacjach znalazłem kilka możliwości:

- rejestracja wszystkiego z załadowanych dll, 
- rejestracja po nazwie - można za pomocą refleksji wyciągnąć typy, które posiadają jakąś nazwę lub zawierają jakieś słowo w nazwie np. typy których nazwa kończy się na Servic, 
- rejestracja po interfejsie agregującym - tworzymy interfejs np. IComponent i porem refleksja wyciągamy wszystkie typy, które go implementują, 
- rejestracja za pomocą atrybutów.

Podejście pierwsze z automatu odpadło, ponieważ prowadzi ono do tego, że będziemy mieć w kontenerze coś czego nie chcemy. Drugie podeście nie podoba mi się ponieważ, każdy nowy pattern powoduje potrzebę dodania nowej metody rejestracyjnej lub wywołanie jakieś ogólnej metody z nowym parametrem. Dodatkowo metoda ta zakłada to, że przestrzegane będą konwencje nazewnicze. Trzecie podejście już kiedyś wykorzystywałem, ma ono sporo plusów, ale jeden poważny minus, a mianowicie bindujemy wszystkie typy pod jeden interfejs. Teoretycznie może nie mieć to żadnych konsekwencji, ale jakoś tak chciałem spróbować czegoś innego. Na zasadzie eliminacji pewnie już widzicie, że spróbowałem podejścia z atrybutami.

Na implementację tego rozwiązania składają się 2 atrybuty:

    ::csharp  
    [AttributeUsage(AttributeTargets.Class, Inherited = true, AllowMultiple = true)]
    public sealed class DependencyAttribute : Attribute{}

    [AttributeUsage(AttributeTargets.Class, Inherited = true, AllowMultiple = true)]
    public sealed class NamedDependencyAttribute : Attribute
    {
        public string Name { get; }
        public NamedDependencyAttribute(string name)
        {
            Name = name;
        }
    }

Dodatkowo stworzyłem 2 extension method dla autofac'owego ContainerBuildera:

    ::csharp 
    public static void RegisterDependencies(this ContainerBuilder builder, Assembly[] assembiles)
    {
        foreach (var assembly in assembiles)
        {
            Type[] typesToRegiser = assembly
                .GetTypes()
                .Where(x => x.GetTypeInfo().GetCustomAttribute<DependencyAttribute>() != null)
                .ToArray();
            foreach (var typeToRegister in typesToRegiser)
            {
                var dependecyAttribute = typeToRegister.GetTypeInfo().GetCustomAttribute<DependencyAttribute>();
                    builder.RegisterType(typeToRegister).AsImplementedInterfaces();
            }
        }
    }
    public static void RegisterNamedDependencies(this ContainerBuilder builder, Assembly[] assembiles)
    {
        foreach (var assembly in assembiles)
        {
            Type[] typesToRegiser = assembly
                .GetTypes()
                .Where(x => x.GetTypeInfo().GetCustomAttribute<NamedDependencyAttribute>() != null)
                .ToArray();
            foreach (var typeToRegister in typesToRegiser)
            {
                var dependecyAttribute = typeToRegister.GetTypeInfo().GetCustomAttribute<NamedDependencyAttribute>();
                builder.RegisterType(typeToRegister).Named(dependecyAttribute.Name, typeToRegister);
            }
        }
    }

Ze względu na to, że używam .Net Core stworzyłem też finder dla Assembly, które nasza aplikacja potrzebuje do działania. W .Net Core nie ma AppDomain, więc poradziłem sobie w taki sposób:

    ::csharp
    public static Assembly[] GetCurrentAssemblyWithDependencies()
    {
        var currentDirectory = Directory.GetCurrentDirectory();
        var dllFiles = Directory.EnumerateFiles(currentDirectory, "*.dll", SearchOption.AllDirectories)
            .Select(x => Path.GetFileNameWithoutExtension(x))
            .Distinct();

        return dllFiles
            .Select(x => Assembly
                .Load(new AssemblyName(x)))
            .ToArray();
    }

    public static Assembly[] GetCurrentAssemblyWithDependenciesWithPattern(string pattern)
    {
        var currentDirectory = Directory.GetCurrentDirectory();
        var dllFiles = Directory.EnumerateFiles(currentDirectory, pattern, SearchOption.AllDirectories)
            .Select(x => Path.GetFileNameWithoutExtension(x))
            .Distinct();

        return dllFiles
            .Select(x => Assembly
                .Load(new AssemblyName(x)))
            .ToArray();
    }

A teraz usecase tego rozwiązania. Załóżmy, że mamy taką oto klasę XmlSerializer:

    ::csharp
    public interface IXmlSerializer
    {
        string SerializeToXmlString<T>(T entity) where T : class;
        T Deserialize<T>(string xmlString) where T : class;
        T Deserialize<T>(FileStream file) where T : class;
    }

    [Dependency]
    public class XmlSerializer : IXmlSerializer
    {
	    //impl
	}
	
I chcemy teraz żeby zarejestrować ją w naszym kontenerze to w programie, dla którego chcemy rejestrować w jego entry point robimy oto taki kodzik:

    ::csharp
    assembiles = AssemblyFinder.GetCurrentAssemblyWithDependencies();
    containerBuilder = new ContainerBuilder();
    containerBuilder.RegisterDependencies(assembiles);
    container = containerBuilder.Build();

I jeżeli będziemy chcieli rozwiązać takiego xml serializera, to robiy to w stranardowy dla autofac sposób:

    ::csharp
    var serializer = container.Resolve<IXmlSerializer>();

To tyle ode mnie. Powiedzcie co sądzicie o tym sposobie automatycznej rejestracji komponentów w kontenerze DI. Może macie jakieś inne ciekawe sposoby takiej automatyzacji?

!!!Aktualizacja!!!
Kontynuując implementacje zauważyłem, że podczas debug'owania aplikacji konsolowej dla .NET Core Directory.GetCurrentDirectory() zwraca co innego niż w testach. Dodałem więc przeszukiwanie folderów w głąb tak żeby odnaleźć potrzebne dll. 