Title: Komponentowe CLI część 2. Implementacja
Date: 2017-09-02 16:00
Category: .NET
Tags: blog, .net, programming, c#, .netcore, cli 
Authors: Szymon Wanot
Status: published

Cześć. Ostatnio przedstawiłem wam zamysł mojego modułowego systemu do tworzenia tooli CLI w .NET Core. To co będę prezentował w tym poście jest to implementacja POC, więc kod momentami jest robiony na szybko. Będę pisał o tym co myślę, że można jeszcze poprawić w dalszej części artykułu. Na początku zanim pojawi się kodzik opiszę na czym opiera się całe rozwiązanie. Aplikacje CLI postanowiłem zamodelować za pomocą handlerów. To co wpisujemy do konsoli to komenda, kolejne parametry to wartości obiektu komendy. Każda komenda ma odpowiadający jej handler, który po sparsowaniu argumentów jest tworzony z kontenera DI. Przykładowo wyglądająca komenda może mieć następującą implementacje:

    ::csharp
    [Command("help", Alias = "h", HelpText = "Help for cli")]
    public class HelpCommand
    {
        [CommandOptionsValue("command", Alias = "c", HelpText = "Type command name to get detailed help")]
        public string CommandName { get; set; }

        public string ErrorMessage { get; set; }
    }

Handler można zaimplmentować w następujący sposób

    ::csharp
    [CommandHandler("help")]
    public class HelpCommandHandler : ConsoleCommandHandler<HelpCommand>
    {
        private readonly IHelpGenerator _helpGenerator;

        public HelpCommandHandler(IHelpGenerator helpGenerator)
        {
            _helpGenerator = helpGenerator;
        }

        public override void Execute(HelpCommand command, TextWriter @out)
        {
            StringBuilder helpText;
            if (string.IsNullOrWhiteSpace(command.CommandName) == false)
            {
                helpText = _helpGenerator.GenerateForCommand(command.CommandName);
            }
            else
            {
                helpText = _helpGenerator.GenerateForProgram();
            }

            if (string.IsNullOrWhiteSpace(command.ErrorMessage) == false)
            {
                helpText.AppendLine("Error message");
                helpText.AppendLine(command.ErrorMessage);
            }

            @out.Write(helpText);
        }
    }

Cała funkcja Main sprowadza się jedynie do kilku linii i generalnie wygląda tak:

    ::csharp
    class Program
    {
        static void Main(string[] args)
        {
            var containerBuilder = new ContainerBuilder();
            containerBuilder
                .RegisterDependencies(AssemblyFinder.GetCurrentAssemblyWithDependencies());
            containerBuilder.RegisterConsoleCommands();

            var app = new CommandLineApplication(
                new AutofacCommandResolver(containerBuilder.Build()), Console.Out);

            app.Run(args);
        }
    }

Dodatkowo dodając kolejne komendy nic się nie zmieni poza nowymi plikami w odpowiednich libkach, więc tak na prawdę wystarczy mieć jedną aplikacje i dodać kilka dll, które będą zwierać nowe komendy i tak będziemy komponować swoje aplikacje. O tym pisałem już we wcześniejszym artykule, więc od teorii przejdźmy do implementacji. Podobnie jak w przypadku automatycznej rejestracji oparłem całe rozwiązanie o atrybuty, choć mam pewne wątpliwości, ale to później. Atrybutów jest kilka:

    ::csharp

    [System.AttributeUsage(AttributeTargets.Class, Inherited = false, AllowMultiple = true)]
    public sealed class CommandAttribute : Attribute
    {
        public string Name { get; private set; }
        public string Alias { get; set; }
        public string HelpText { get; set; }

        public CommandAttribute(string name)
        {
            Name = name;
        }
    }

    [System.AttributeUsage(AttributeTargets.Property, Inherited = false, AllowMultiple = true)]
    public sealed class CommandOptionsValueAttribute : Attribute
    {
        public string Name { get; private set; }
        public string Alias { get; set; }
        public bool Required { get; set; }
        public object DefaultValue { get; set; }
        public string HelpText { get; set; }

        public CommandOptionsValueAttribute(string name)
        {
            Name = name;
        }
    }

    [AttributeUsage(AttributeTargets.Class, Inherited = false, AllowMultiple = true)]
    public sealed class CommandHandlerAttribute : Attribute
    {
        public string CommandName { get; }

        public CommandHandlerAttribute(string commandName)
        {
            CommandName = commandName;
        }
    }

Pierwszy atrybut dajemy nad klasę, która ma być komendą, a drugi nad właściwości w klasie komendy, które będą wartościami opcji komendy. CommandHandlerAttribute należy dać nad klasę, która ma być handlerem dla danej komendy. Co istotne nazwa komendy i handlera musi być taka sama, ponieważ inaczej nie zostaną one dobrze sparsowane. Muszę pomyśleć nad tym jak to inaczej zrobić, żeby ominąć ten problem, ale na razie nie wydaje mi się to wielką niedogodnością. 
Bazowa klasa handlera wygląda w następujący sposób:

    ::csharp
    public interface IConsoleCommandHandler
    {
        void ExecuteFromParsedArgs(CommandLineParsedArgs args, TextWriter @out);
    }

    public abstract class ConsoleCommandHandler<T> : IConsoleCommandHandler
        where T : class, new()
    {

        public void ExecuteFromParsedArgs(CommandLineParsedArgs args, TextWriter @out)
        {
            T command = CommandFactory.Create<T>(args);
            Execute(command, @out);
        }

        public abstract void Execute(T command, TextWriter @out);
    }

Dodatkowy interfejs jest nam potrzebny dla rozwiązywania zależności przez kontener DI, ale o tym później. Jak widzimy metoda ExecuteFromParsedArgs przyjmuje sparsowane argumenty. Klasa argumentów wygląda tak:

    ::csharp
    public class CommandLineParsedArgs
    {
        public string CommandName { get; }
        public Dictionary<string, string> CommandOptionsValues { get; }

        public CommandLineParsedArgs(string commandName, 
            Dictionary<string, string> commandOptionsValues)
        {
            CommandName = commandName;
            CommandOptionsValues = commandOptionsValues;
        }

        string GetValueFor(string option)
        {
            return CommandOptionsValues[option];
        }
    }

Sam parser natomiast dziełem sztuki nie jest (bo powinienem to zrobić za pomocą tokenów), ale działa. Kodzik wygląda oto w taki sposób:

    ::csharp
    public class CommandLineArgsParser
    {
        private readonly string _argDelimiter;
        private readonly char[] _valueDelimiters;
        private readonly int _commandIndexPlacement;

        public CommandLineArgsParser(
            string argDelimiter,
            char[] valueDelimiters,
            int commandIndexPlacement)
        {
            _argDelimiter = argDelimiter;
            _valueDelimiters = valueDelimiters;
            _commandIndexPlacement = commandIndexPlacement;
        }

        public CommandLineParsedArgs Parse(string[] args)
        {
            if (args.Any() == false)
                throw new EmptyArgsException();

            string commandName = ParseCommandName(args);
            Dictionary<string, string> options = ParseCommandOptions(args);

            return new CommandLineParsedArgs(commandName, options);
        }

        private Dictionary<string, string> ParseCommandOptions(string[] args)
        {
            args = args.Skip(1).ToArray();
            var options = new Dictionary<string, string>();
            string curretnOption = string.Empty;
            string currentValue = string.Empty;

            foreach (var arg in args)
            {
                bool removeOption = true;
                bool addToDict = true;

                var delimiter = _valueDelimiters
                    .FirstOrDefault(arg.Contains);

                if (default(char) != delimiter)
                {
                    curretnOption = arg
                        .Split(delimiter)
                        .First()
                        .Replace(_argDelimiter, "");

                    currentValue = arg
                        .Split(delimiter)
                        .Last();
                }
                else
                {
                    if (arg.Contains(_argDelimiter))
                    {
                        curretnOption = arg.Replace(_argDelimiter, "");
                        removeOption = false;
                        addToDict = false;
                    }

                    if (curretnOption != string.Empty &&
                        arg.Contains(_argDelimiter) == false)
                    {
                        currentValue = arg;
                    }
                }

                if (addToDict)
                    options.Add(curretnOption, currentValue);

                if (removeOption)
                    curretnOption = string.Empty;
                currentValue = string.Empty;
            }

            return options;
        }

        private string ParseCommandName(string[] args)
        {
            var commandName = args[_commandIndexPlacement];

            return commandName;
        }
    }

W przyszłości to pewnie zmiennie, ale na razie działa, jest przetestowane, więc niech na razie takie zostanie. W handlerze jest jeszcze jeden, który zamienia argumenty na komendę, a mianowicie CommandFactory:

    ::csharp
    public static class CommandFactory
    {
        public static T Create<T>(CommandLineParsedArgs args) where T : class, new()
        {
            Type[] commands = FindCommand(args);

            if (commands.Count() > 1)
                throw new TooManyCommandsWithSameNameException(args.CommandName);

            var commandType = commands.First();

            var instance = Activator.CreateInstance<T>();

            foreach (var prop in instance.GetType().GetProperties())
            {
                var attribute = prop.GetCustomAttribute<CommandOptionsValueAttribute>();
                if (attribute != null)
                {
                    SetPropertyValue(args, instance, prop, attribute);
                }
            }

            return instance;
        }

        private static void SetPropertyValue<T>(CommandLineParsedArgs args, T instance, PropertyInfo prop, CommandOptionsValueAttribute attribute) where T : class, new()
        {
            var arg = args
                    .CommandOptionsValues
                    .FirstOrDefault(x =>
                        x.Key == attribute.Name ||
                        x.Key == attribute.Alias);

            if (arg.IsDefault() && attribute.Required)
                throw new RequiredOptionNotFoundException(attribute.Name);

            if (arg.IsDefault() == false)
                prop.SetValue(instance, Convert.ChangeType(arg.Value, prop.PropertyType));
            else if (attribute.DefaultValue != null)
                prop.SetValue(instance, Convert.ChangeType(attribute.DefaultValue, prop.PropertyType));
            else
                prop.SetValue(instance, Convert.ChangeType(prop.PropertyType.GetDefaultValue(), prop.PropertyType));
        }

        private static Type[] FindCommand(CommandLineParsedArgs args)
        {
            return AssemblyFinder
                   .GetCurrentAssemblyWithDependencies()
                   .SelectMany(x => x.GetTypes()
                       .Where(z => z.GetTypeInfo().GetCustomAttribute<CommandAttribute>() != null &&
                       (z.GetTypeInfo().GetCustomAttribute<CommandAttribute>().Name == args.CommandName ||
                        z.GetTypeInfo().GetCustomAttribute<CommandAttribute>().Alias == args.CommandName
                       ))).ToArray();
        }
    }

Wiem, że jest to refleksja w wersji hard, ale spełnia swoje zadanie i mapuje sparsowane argumenty na instancje klasy komendy. Całe rozwiązanie składa w całość CommandLineApplication:

    ::csharp
    public sealed class CommandLineApplication
    {
        private readonly ICommandResolver _resolver;
        private readonly TextWriter _out;

        public CommandLineApplication(ICommandResolver resolver, TextWriter @out)
        {
            _resolver = resolver;
            _out = @out;
        }

        public void Run(string[] args)
        {
            var parser = new CommandLineArgsParser("--", new[] { '=', ':' }, 0);
            try
            {
                var parsedArgs = parser.Parse(args);
                var handler = _resolver.ResolveCommandHandler(parsedArgs);
                if (handler != null)
                {
                    handler.ExecuteFromParsedArgs(parsedArgs, _out);
                }
            }
            catch (Exception e)
            {
                var help = _resolver.ResolveCommandHandler<HelpCommandHandler>("help");
                help.Execute(new HelpCommand { ErrorMessage = e.Message }, _out);
            }
        }
    }

I to w sumie na tyle z podstawowego frameworka. Przejdziemy teraz do resolvera. Jest to w podstawowym wydaniu interfejs, ponieważ nie chciałem wiązać się silnie z żadną bibliotekę do dependeny injection. Wygląda on tak:

    ::csharp
    public interface ICommandResolver
    {
        IConsoleCommandHandler ResolveCommandHandler(CommandLineParsedArgs args);
        T ResolveCommandHandler<T>(string name);
    }

Pierwsza metoda rozwiązuje handler jako interfejs co pozwoli mi go potem wywołać za pomocą sparsowanych elementów. Druga funkcja powinna zwrócić konkretny handler. Na powyższym przykładzie używam tego do wyświetlania helpa, więc się przydaje. W sowim rozwiązaniu zaimplementowałem handler przy użyciu Autofa,c ale można użyć dowolnego innego kontenera. Kod relovera jest prosty i wygląda tak:

    ::csharp
    public sealed class AutofacCommandResolver : ICommandResolver
    {
        private readonly IContainer _container;

        public AutofacCommandResolver(IContainer container)
        {
            _container = container;
        }

        public IConsoleCommandHandler ResolveCommandHandler(CommandLineParsedArgs args)
        {
            try
            {
                var commandName = GetQualifiedCommandName(args.CommandName);
                var commandType = GetCommandType(commandName);
                return _container.ResolveNamed(commandName, commandType) as IConsoleCommandHandler;
            }
            catch (Exception ex)
            {
                throw new CommandNotFoundException(args.CommandName, ex);
            }
        }


        public T ResolveCommandHandler<T>(string name)
        {
            return _container.ResolveNamed<T>(name);
        }

        private string GetQualifiedCommandName(string commandName)
        {
            var commandType = AssemblyFinder
                .GetCurrentAssemblyWithDependencies()
                .SelectMany(x => x.GetTypes()
                    .Where(t => t.GetTypeInfo().GetCustomAttribute<CommandAttribute>() != null))
                .FirstOrDefault(x =>
                    x.GetTypeInfo().GetCustomAttribute<CommandAttribute>().Name == commandName ||
                    x.GetTypeInfo().GetCustomAttribute<CommandAttribute>().Alias == commandName
                );

            string retName = string.Empty;
            if (commandType != null)
                retName = commandType.GetTypeInfo().GetCustomAttribute<CommandAttribute>().Name;

            return retName;
        }

        private Type GetCommandType(string name)
        {
            return AssemblyFinder.GetCurrentAssemblyWithDependencies()
                 .SelectMany(x => x.GetTypes()
                     .Where(
                        t => t.GetTypeInfo().GetCustomAttribute<CommandHandlerAttribute>() != null))
                 .FirstOrDefault(x => x.GetTypeInfo()
                         .GetCustomAttribute<CommandHandlerAttribute>().CommandName == name);
        }
    }

Na koniec najważniejszy element, czyli automatyczna rejestracja handlerów zaimplementowana jako rozszerzenie do ContainerBuildera:

    ::csharp
    public static class CommandLineAutofacExtensions
    {
        public static void RegisterConsoleCommands(this ContainerBuilder containerBuilder)
        {
            Type[] commandsToRegister = AssemblyFinder
                .GetCurrentAssemblyWithDependencies()
                .SelectMany(x => x.GetTypes()
                    .Where(t => t.GetTypeInfo()
                        .GetCustomAttribute<CommandHandlerAttribute>() != null))
                .ToArray();

            foreach (var command in commandsToRegister)
            {
                var commandAttribute = command.GetTypeInfo().GetCustomAttribute<CommandHandlerAttribute>();
                containerBuilder.RegisterType(command).Named(commandAttribute.CommandName, command);
            }
        }
    }

I to już tyle. Dzięki tym elementom jestem w stanie za pomocą dodania kolejnych dll sterować tym jakie komendy ma aplikacja, ponieważ dzięki assembly finder, który omawiałem w [tym](https://harunx9.github.io/automatyczna-rejestracja-zaleznosci-w-autofac-na-netcore.html#automatyczna-rejestracja-zaleznosci-w-autofac-na-netcore) rejestruje to co znajdzie się w folderze z aplikacją. Jak uda mi się dokończyć texture packera to pokażę jak działa całość w akcji a pewnie przy okazji dokonam poprawek, błędów niezauważonych na etapie pisania/tworzenia podstawy. Zastanawiam się również nad przeniesieniem tego do biblioteki .NET Standard, ale to dopiero jak będę miał napisane na tym ze dwie wyszczególnione w poprzednim artykule aplikacje. A wy co o tym myślcie? Czy takie podejście ma sens i może być wykorzystywane?  Czy macie może jakieś inne rozwiązania?