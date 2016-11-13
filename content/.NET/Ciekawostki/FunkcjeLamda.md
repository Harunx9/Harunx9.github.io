Title: Czy wiesz co robi za Ciebie kompilator?: Funkcje lambda
Date: 2016-10-24 00:00
Category: .NET
Tags: blog, .net, programming, c#
Authors: Szymon Wanot
Status: published

Cześć, kiedyś ludzie mówili mi, że nie należy wkładać palców między drzwi, bo może zaboleć. Niestety jakoś tak wychodzi, że jestem ciekawy jak
działa to z czym pracuję, więc zacząłem się nieco przyglądać jak wygląda .NET pod maską i nawet mi się spodobało.
Na pierwszy ogień pójdą dziś funkcje lambda w C# i to co kompilator sprytnie dodaje za programistę. Rozpatrzmy zatem oto taki prosty kodzik: 

    ::csharp
    class Person
    {
        public string Name { get; set; }
        public string Surname { get; set; }
    }
 
    class Program
    {
        static void Main(string[] args)
        {
            var list = new List<Person>();
            list.Add(new Person { Name = "John", Surname = "Doe" });
 
            var result = list.Where(x => x.Surname == "Doe");
        }
    }

Po skompilowaniu w konfiguracji Debug zdekompilowaniu ILSpy otrzymamy coś takiego:

    ::c#
    class Program
    {
        [CompilerGenerated]
        [Serializable]
        private sealed class <>c
        {
            public static readonly Program.<>c <>9 = new Program.<>c();

            public static Func<Person, bool> <>9__0_0;

            internal bool <Main>b__0_0(Person x)
            {
                return x.Surname == "Doe";
            }
        }

        private static void Main(string[] args)
        {
            IEnumerable<Person> arg_4B_0 = new List<Person>
            {
                new Person
                {
                    Name = "John",
                    Surname = "Doe"
                }
            };
            Func<Person, bool> arg_4B_1;
            if ((arg_4B_1 = Program.<>c.<>9__0_0) == null)
            {
                arg_4B_1 = (Program.<>c.<>9__0_0 = new Func<Person, bool>(Program.<>c.<>9.<Main>b__0_0));
            }
            IEnumerable<Person> result = arg_4B_0.Where(arg_4B_1);
        }
    }

Jak można zauważyć funktory w C# generują dodatkowe klasy, które implementują funkcję lambda zapisaną przez nas w listingu pierwszym. Do tego odkrycia doszedłem w sumie przez przypadek. Pewnie taka
implementacja jest jak najbardziej ok, nie mniej jednak warto wiedzieć jak kod wygląda po kompilacji. W powyższym przypadku kod skompilowany w konfiguracji Release niewiele się różni, więc nie ma sensu
pokazywanie go. Powyższy przykład zmotywował mnie do poszukania większej ilości przykładów, więc jeśli coś znajdę to niezwłocznie opublikuję. A tym czasem życzę miłej lektury i do następnego razu. 