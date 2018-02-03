Title: Renderowanie 2D część 1: Tekstury
Date: 2017-05-17 17:30
Category: OpenGL
Tags: DSP2017, Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

Ostatnio udało mi się skończyć renderowanie w 2DXngine, chciałbym opisać jak działa zaimplementowane przeze mnie rozwiązanie. Zaczniemy od struktur danych, które są nam potrzebne aby działało renderowanie 2D. Jako pierwsze przyjrzymy się jak zaimplementować teksturę oraz jak ją wczytać z dysku, co nie do końca może być takie oczywiste w C++. W mojej implementacji separuje dane wczytane od tekstury za pomocą klasy bitmapy, a jej interfejs prezentuje się następująco:

	::cpp
	class Bitmap 
	{
	public:
    
    	Bitmap(unsigned char * data, GLuint width, GLuint height);
    	Bitmap();
    	~Bitmap();
    
    	static Bitmap* load(AssetPath assetPath);
    	static Bitmap empty(GLuint width, GLuint height)
    	{
        	return Bitmap(0, width, height);
    	}

    	void remove();

    	READONLY_PROPERTY(GLfloat, texelWidth)
    	READONLY_PROPERTY(GLfloat, texelHeight)
    	READONLY_PROPERTY(GLuint, width)
    	READONLY_PROPERTY(GLuint, height)
    	READONLY_PROPERTY(unsigned char *, data)
	};

W implementacji zastosowałem macro READONLY_PROPERTY, generuje ono publiczny getter i prywatne pole. Obiekty typu Bitmap służą tylko za kontenery danych, stąd też ciekawa w nich tylko jest metoda load, i jej implementacja wygląda następująco:

	::cpp
	Bitmap* Bitmap::load(AssetPath assetPath)
	{
    	int width, height;
    	auto path = assetPath.toCStr();
    	auto imageData = SOIL_load_image(path, &width, &height, 0, SOIL_LOAD_RGBA);
    
    	return new Bitmap(imageData, width, height);
	}

Do wczytywania obrazków wykorzystuję bibliotekę SOIL, którą można znaleźć -> [TU](http://www.lonesock.net/soil.html) pobieramy kompilujemy i działamy. Generalnie mógłbym użyć samego stb_image, ale nie wiem czy nie będę korzystał z jakiś innych funkcji tej biblioteki, więc na razie zostawiam ją w całości. Jeżeli chodzi o teksturę to jej interfejs wygląda w taki sposób:

	::cpp
	class Texture : public Asset
	{
	public:
    	static Texture * load(AssetPath assetPath);

    	Texture(AssetPath assetPath, Bitmap* bitmap);
    	~Texture();

    	void bind() const;

    	READONLY_PROPERTY(GLuint, textureId)
    	READONLY_PROPERTY(Bitmap*, bitmap)
	protected:
    	virtual void generate();
	};

Ze względu na to, że wymaga tego konwencja każda klasa asset będzie posiadać statyczną metodę load. W przyszłości może zrobię osobno loadery, żeby się tego pozbyć i lepiej pilnować konwencji, ale na razie tak to zostanie. Metoda generate powstała natomiast ze względu na klasy potomne, ale o tym później. Sama metoda ma za zadanie tworzyć teksturę w kontekście OpenGl i jej implementacja wygląda następująco:

	::cpp
	void Texture::generate()
	{
    	glGenTextures(1, &this->_textureId);
    	glBindTexture(GL_TEXTURE_2D, this->_textureId);

    	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, this->_bitmap->get_width(), this->_bitmap->get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, this->_bitmap->get_data());

    	glBindTexture(GL_TEXTURE_2D, 0);
	}

Ostatnią rzeczą związaną z teksturami jest RenderTarget. Reprezentuje on pustą teksturę na której renderowane są inne obiekty. Jest to przydatne kiedy chcemy wprowadzić postprocessing czy warstwowość renderowania. Dodatkowo w mojej implementacji zastępuję on FrameBufferObject, w tym momencie przydaje się wydzielenie bindowania tekstury do metody generate, ponieważ jej nadpisanie w RenderTarget wygląda następująco:
 
	::cpp
	void RenderTarget::generate()
	{
   		glBindFramebuffer(GL_FRAMEBUFFER, this->_fbo);
    	Texture::generate();
    	this->bind();
    	glFramebufferTexture(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, this->get_textureId(), 0);
    	GLenum drawBuffers[1] = { GL_COLOR_ATTACHMENT0 };
    	glDrawBuffers(1, drawBuffers);

    	if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE)
        	std::terminate();
    	glBindFramebuffer(GL_FRAMEBUFFER, 0);
	}

To chyba na tyle. Całość kodu jest na GitHubie, więc nie będę omawiał dokładnie wszystkiego, w razie potrzeby można tam zajrzeć. W razie pytań czy uwag jak zawsze zapraszam do sekcji komentarzy.

