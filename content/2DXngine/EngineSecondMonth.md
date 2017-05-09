Title: 2DXngine: Renderowanie 2D i inne informacje
Date: 2017-05-06 10:00
Category: Gamedev
Tags: DSP2017, 2DXngine
Authors: Szymon Wanot
Status: published

Cześć wszystkim. Wiem, że ostatnio było mało postów na temat progresu silnika - no niestety stworzenie sensownego renderowania pochłonęło masę czasu na research i implementacje. Mimo tego i tak będę miał sporo refactoringu, ale o tym napiszę później. Podczas implementacji chciałem, aby mój system renderowania był wzorowany na tym co znamy z Monogame, czyli spritebatchu. Technika ta pozwala na optymalizowane draw call', a dodatkowo opakowana pozwala używać wspomnianego spritebatcha do rysowania 2D oraz dodatkowych metod z graphic device do renderowania 3D. Nie mam jeszcze implementacji graphic device, ale zakładam ją w przyszłości, ponieważ chciałbym, aby silnik potrafił również obsługiwać renderowanie 3D. Jeśli chodzi o spriteach założyłem, że chciałbym go używać w następujący sposób:

Batch.begin() -> rozpoczynam wkładanie tego co chce renderować do batch
Batch.draw(params) -> odkładanie kolejnych obrazków do batcha
Batch.draw(params) -> odkładanie kolejnych obrazków do batcha
Batch.draw(params) -> odkładanie kolejnych obrazków do batcha
Batch.draw(params)-> odkładanie kolejnych obrazków do batcha
Batch.end() -> rysowanie batcha

Kto kiedyś używał Monogame lub LibGDX, to na pewno zna powyższy pattern. Ja swojego batcha dodatkowo wzbogaciłem o sampler object(dostępny od OpenGL 3.3) tak, żeby nie trzeba podczas bindowania tekstury ustawiać filtrowania i zawijania tekstury, a można to zrobić przy każdym stracie batchowania. Całość działa całkiem dobrze i dokładnie opiszę wszystko w osobnych artykułach, ponieważ tu nie ma na to miejsca. Dodatkowo zaimplementowałem asset shadera i asset textury2D oraz render target. Ten ostatni będzie służył mi do właściwego renderowania scen, ponieważ standartowo OpenGL renderuje wszytko na back buffer, a mi chodzi żeby rendnerował do tekstury, ponieważ otwiera to możliwości postprocessingu i pozwala mi operować tylko na elementach sceny, a nie na UI. O postporcessingu też pewnie kiedyś napiszę, bo to temat dość ciekawy i mocno przydatny. Co do dalszego rozwoju to jak mam już renderowanie  2D, to mogę zająć się inputem i muzyką a to myślę, że nie będą już tak skomplikowane tematy jak samo ryzowanie. Zanim to jednak nastąpi daje sobie jeszcze tydzień na uporządkowanie kodu i dokończenie renderowania opartego o warstwy. Dodatkowo przydałoby się napisać trochę testów do tego co już zrobiłem, ponieważ nie miałem na to czasu. Myślę, że testy pozwolą mi spojrzeć na całość z nowej pespektywy i nieco zoptymalizować kod, plus sprawdzać czy wszystko działa na pewno tak jak to planowałem. Myślę, że to na razie tyle w przyszłych postach opisze dokładnie poszczególne elementy potrzebne do stworzenie renderowania 2D w OpenGL.