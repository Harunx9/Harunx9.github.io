Title: Pimp your commandline
Date: 2016-11-06 00:00
Category: Inne, tools
Tags: inne, tools
Authors: Szymon Wanot
Status: published

Cześć, dziś chciałem nieco odejść od tematu programowania na rzecz pokazania możliwości modyfikacji narzędzi pracy programisty. Oprócz ulubionego IDE na podorędziu każdego developera powinna znajdować się konsola czy też tzw. commandline. Systemy Uniksopodobne (Linux, OSX, FreeBSD, itp) mogą poszczycić się masą dodatków do swoich terminali tak Windowsy od zawsze miały w na tym polu nieco gorzej. Od pewnego czasu sytuacja ta zaczęła się zmieniać za pomocą ciekawych alternatyw dla cmd.exe czy niebieskiego powershella. 


Pierwsza i chyba najstarszą alternatywą jest emulator basha z gita. Ja sam trochę z tego korzystałem, ale jakoś nie do końca mi ta alternatywa odpowiadała, mimo wszystko należy o niej z obowiązku wspomnieć. Po wielu bojach i próbach ucywilizowania windowsowego cmd poddałem się i obecnie korzystam z cmder’a (zbudowany na emulatorze ConEmu w tandemie z powershellem). Teminal można znaleźć pod adresem: http://cmder.net/.
Efekt po przeróbkach powinien prezentować się w taki oto sposób:

![Alt posh](/images/posh.gif)

Dodatkowo aby poprawić wygląd tak jak jest to pokazane powyżej korzystać z następujących dodatków powershella: 

- posh-git - czyli dodatek do gita w powershell dostępny pod: [https://github.com/dahlbyk/posh-git](https://github.com/dahlbyk/posh-git)
- oh-my-posh - czyli powerline dla powershella plus parę innych udogodnień: [https://github.com/JanJoris/oh-my-posh](https://github.com/JanJoris/oh-my-posh)
- font - fira code: [https://github.com/tonsky/FiraCode](https://github.com/tonsky/FiraCode)


Po instalacji wszystkiego należy ustawić oh my posh jako skrypt startowy cmder’a. Aby tego dokonać należy wejść do {instalacja cmder}\config i do pliku user-profile.ps1 oddać linie:

    ::powershell
    Import-Module oh-my-posh


Jeżeli wszystko poszło ok to pozostaje tylko dostosować kolory i tyle.
