Title: Ogólna architektura silnika - pętla gry
Date: 2017-03-04 18:00
Category: Gamedev
Tags: DSP2017, Gamedev
Authors: Szymon Wanot
Status: published

Elementem, który posiada każdy silnik do gier jest pętla gry. W skrócie jest to element, który cyklicznie wykonuje całą logikę naszej gry. Wszystkie gry posiadają pewne stałe elementy, które muszą być wykonane, aby całość systemu działała.

W największym uproszczeniu gra co klatkę powinna:

- sprawdzić sygnały z urządzeń wejścia,
- na podstawie tych sygnałów wykonać logikę wszystkich obiektów uczestniczących w grze,
- po wykonaniu logiki narysować wszystko oraz wyświetlić to użytkownikowi.

W najprostszym ujęciu pseudokodu (wiem miało być bez kodu, ale się nie da) powinno to wygląd tak:
    
    ::csharp
    loop{
	    HandleInput();
	    Update();
	    Draw();
	
        If(exitCondition == true){
		    Exit()
	    }
    }

W takim ujęciu pętla wykona się tyle razy ile pozwoli na to procesor. Takiej sytuacji chcemy uniknąć, ponieważ w grze wiele rzeczy opiera się o upływ czasu musimy, więc obliczyć ile czasu upłynęło nam pomiędzy kolejnymi klatkami. Gry najczęściej działają w 60 fps lub w 30 fps, czyli na klatkę mamy 16 ms lub 30 ms. Aby zmierzyć czas powinniśmy zaimplementować timer, który zmierzy nam czas pomiędzy kolejnymi klatkami. 

    ::csharp
    timeStep = 1 / 30f [30fps] or 1/ 60 [60fps]
    accumulator  = 0;
    timer.Start()
    
    loop{
	    deltaTime = timer.ElapsedTime();
	    accumulator = accumulator + deltaTime;
	
        HandleInput();
	
        while (accumulator >= _timeStep)
        {
            Update(deltaTime);
            accumulator = accumulator - deltaTime;
        }
	
        Draw(deltaTime);
	
        If(exitCondition == true){
		    Exit()
	    }
    }

Dzięki zastosowaniu timera w powyższym kodzie update wykona się tylko przy zdefiniowanym kroku czasu. Aby mieć  pewność, że czas płynie bardzo dokładnie stosuje się inne sztuczki. Mnie jednak nie było to nigdy potrzebne, gdyby jednak kogoś to mega interesowało to polecam artykuł [TU](http://gafferongames.com/game-physics/fix-your-timestep/) tam znajdziecie jeszcze więcej sposobów odmierzania czasu w pentli gry. Dodam jeszcze, że często nie będziecie musieli pisać kodu pętli gry, ponieważ większość frameworków czy bibliotek (Monogame, LibGDX, Phaser.js, itp.) posiada już własną implementacje. Mimo to warto wiedzieć co znajduje się w bebechach, żeby zrozumieć wysokopoziomową logikę. To tyle, kolejny wpis przejdzie na nieco wyższy poziom abstrakcji w implementowaniu własnego silnika.
