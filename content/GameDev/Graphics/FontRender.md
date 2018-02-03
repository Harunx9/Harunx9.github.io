Title: Renderowanie 2D cześć 6: Tekst True Type Font
Date: 2017-08-06 13:00
Category: OpenGL
Tags: Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

Renderowanie tekstu jest nieco bardziej skomplikowane od wyświetlania prostych obrazków. Wyświetlanie tekstu możemy zrealizować na dwa sposoby:

- renderowanie SpriteFontów,
- renderowanie True Type Font. 

Pierwszy sposób polega na wygenerowaniu sobie z pliku czcionki tekstury oraz pliku opisującego układ znaków na teksturze. Potem podczas renderowania wycinamy za pomocą tych danych odpowiednie obszary z tekstury i w ten sposób konstruujemy napisy. Ten sposób jest oczywiście jak najbardziej ok i wiele z silników z niego korzysta. Ja w 2DXngine postanowiłem pójść drugą drogą, czyli zaimplementować renderowanie bezpośrednio z plików czcionek True Type Font. Podejście to wymaga zainstalowanie dodatkowo biblioteki [freetype](https://www.freetype.org), ponieważ będzie ona nam potrzebna do wygenerowania glifów, które później będziemy wyświetlali. Dodatkowo potrzeba jest jeszcze biblioteka [zlib1](https://www.zlib.net/). Jako pierwsze przyjrzymy się implementacji tworzenia elementów do wyświetlenia. Podstawowe metryki fonta reprezentuje poniższy rysunek: 

![Alt metrics](/images/metrics.png)

Dodatkowe informacje można znaleźć na stronie [free type project](https://www.freetype.org/freetype2/docs/glyphs/index.html). Jak już się zaznajomimy z metrykami to możemy stworzyć strukturę reprezentująca glif:

	::cpp
	struct Glyph
	{
	    Texture* tex;
	    glm::ivec2 bearing;
	    glm::ivec2 advance;
	    GlyphState state;
	
	    static Glyph empty() 
	    {
	        Glyph glyph = {
	            nullptr,
	            glm::ivec2(0,0),
	            glm::ivec2(0,0),
	            EMPTY_GLYPH
	        };
	
	        return glyph;
	    }
	};

Samo generowanie czcionek dla podsawowych znaków ASCII wygląda w następujący sposób:

	::cpp
	 glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

	    FT_Library ft;
	    if (FT_Init_FreeType(&ft))
	        std::exit(1);

	    auto strPath = path.get_fullPath();
	    auto charPath = strPath.c_str();

	    FT_Face face;
	    if (FT_New_Face(ft, charPath, 0, &face))
	        std::cout << "ERROR::FREETYPE: Failed to load font" << std::endl;

	    FT_Set_Pixel_Sizes(face, 0, 48);

	    for (GLubyte letter = 0; letter < 128; letter++)
	    {
	        if (FT_Load_Char(face, letter, FT_LOAD_RENDER))
	        {
	            std::cout << "ERROR::FREETYTPE: Failed to load Glyph" << std::endl;
	            continue;
	        }

	        Bitmap* bmp = new Bitmap(face->glyph->bitmap.buffer, face->glyph->bitmap.width, face->glyph->bitmap.rows);
	        Texture* texture = new Texture(AssetPath::empty(), bmp, GL_RED);

	        Glyph character = {
	            texture,
	            glm::ivec2(face->glyph->bitmap_left, face->glyph->bitmap_top),
	            glm::ivec2(face->glyph->advance.x,face->glyph->advance.y),
	            GlyphState::FILL_GLYPH
	        };
	        this->_characterMap.insert(std::pair<GLchar, Glyph>(letter, character));
	    }
	    FT_Done_Face(face);
	    FT_Done_FreeType(ft);

Powyższy kod generuje kolekcje bitmap, które przechowują obrazek każdego glifu w grayscale - aby poprawnie wyświetlić taką czcionkę potrzebujemy podmienić standardowy fragment shader, na taki jak poniżej:

	::cpp
	#version 330 core
	layout (location = 0) out vec4 color;
	in vec2 fragmentTexCoord;
	in vec4 fragmentColor;
	uniform sampler2D tex;
	uniform float global_alpha;
	void main(void)
	{
	     color = vec4(1, 1, 1, texture(tex, fragmentTexCoord).r) * fragmentColor;
	}

Do samego rysowania użyłem spritebatcha, który już zaimplementowałem w silniku:

	::cpp
	 batch->begin(this->_fontShader, TextureWrap::CLAMP_TO_EDGE, TextureFilter::LINEAR_FILTER, camera);

	    for (auto c : text)
	    {
	        Glyph g = this->_characterMap[c];
	        if (g.state != GlyphState::EMPTY_GLYPH)
	        {
	            //compute base pos variables
	            float x = position.x + g.bearing.x * scale.x;
	            float y = position.y - g.bearing.y * scale.y;

	            float width = g.tex->get_bitmap()->get_width() * scale.x;
	            float height = g.tex->get_bitmap()->get_height() * scale.y;

	            batch->draw(g.tex, RectangleI(x, y, width, height), color, 0);

	            position.x += (g.advance.x >> 6) * scale.x;
	            position.y += (g.advance.y >> 6) * scale.y;
	        }
	    }

	    batch->end();

I to w sumie tyle jeśli chodzi o renderowanie czcionek. Całość implementacji znajduje się już w repozytorium, więc ciekawskich zapraszam na githuba. 



