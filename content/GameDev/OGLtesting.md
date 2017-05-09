Title: OpenGL a Unit Testy
Date: 2017-04-17 18:00
Category: Gamedev
Tags: DSP2017, Gamedev, Tools
Authors: Szymon Wanot
Status: published

Cześć. Wiem, że powinienem w pierwszej kolejności napisać o C++ i testowaniu, ale zeszło mi na to jakieś 3 godziny, więc może ktoś skorzysta z mojej wiedzy. Chciałem napisać prosty test sprawdzający czy klasa programu Shadera działa tak jak tego oczekuję. Napisałem więc prosty test, odpaliłem go i od tego  momentu nastąpiła moja mocna konsternacja, która później przerodziła się w nieco większe zdenerwowanie. W projekcie używam GLEW, aby mieć dostęp do funkcji OpenGL i okazuje się, że aby działało kompilowanie shaderów muszę pomyślenie inicjalizować tą bibliotekę, bo inaczej dostane na twarz wyjątek. Po kilu próbach udało mi się pomyślnie skompilować shader w moim głównym projekcie, ale testy wymagały więcej pracy. Musiałem dodać do testów SDL i GLEW dodatkowo testowanie, które wymaga zainicjalizowania okienka i kontekstu OpenGL - robię to za pomocą takiego fixture:
 
    ::cpp
    class ShaderTestFixture : public ::testing::Test
    {
    protected:
        virtual void SetUp()
        {
            SDL_Init(SDL_INIT_VIDEO);

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);

            SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
            SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 2);

            SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
            auto _window = SDL_CreateWindow("Game Window",
                SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                640,
                360,
                SDL_WINDOW_OPENGL);

            auto ctx = SDL_GL_CreateContext(_window);

            GLenum glewError = glewInit();

        }

        virtual void TearDown()
        {
            SDL_Quit();
        }
    };

Sam przykładowy test wygląda tak:

    ::cpp
    TEST_F(ShaderTestFixture, shader_can_be_load_from_inline_source)
    {
        //Arrange
        const char *vertexSource =
            "#version 330 core\n"
            "layout (location = 0) in vec4 position;\n"
            "layout (location = 1) in vec4 in_tint;\n"
            "out vec2 tex_pos;\n"
            "out vec4 tint;\n"
            "uniform mat4 projection;\n"
            "void main(void)\n"
            "{\n"
            "gl_Position = projection * vec4(position.x, position.y, 0.0f, 1.0f);\n"
            "tex_pos = vec2(position.z, position.w);\n"
            "tint = in_tint;\n"
            "}\n";

        const char *fragmentSource =
            "#version 330 core\n"
            "in vec2 tex_pos;\n"
            "in vec4 tint;\n"
            "out vec4 color;\n"
            "uniform sampler2D tex;\n"
            "uniform float global_alpha;\n"
            "void main(void)\n"
            "{\n"
            "color = vec4(tint.x, tint.y, tint.z, global_alpha * tint.w) * texture(tex, tex_pos);\n"
            "}";

        auto shader = new ShaderProgram(vertexSource, fragmentSource);
   
        //Act    
        auto result = shader->compile();
 
        //Assert
        ASSERT_EQ(ShaderCompileResult::COMPILATION_SUCESS, result);
    }

Dobrze, że ten problem wyszedł teraz, ponieważ mogłem w łatwy sposób zmodyfikować kod. Cała sytuacja nauczyła mnie, żeby pisać testy mimo wszystko, ponieważ jak bym miał zaimplementowane więcej to musiałbym naprawdę mocno się napracować, aby znaleźć źródło problemu. Postaram się napisać inne testy dla elementów używających OpenGL i zobaczymy, czy nie mam większej ilości błędów. Nauka z tej sytuacji jest dość oczywista  - piszemy testy nawet w bardzo ograniczonym zakresie. To na razie tyle mam nadzieję, że komuś przyda się to co w tym miejscu napisałem. Można dodać możliwość konfiguracji wersji OpenGL i inne rzeczy, ale to już później. Mam nadzieję, że w następnym wpisie opisze więcej o testowaniu kodu w C++.