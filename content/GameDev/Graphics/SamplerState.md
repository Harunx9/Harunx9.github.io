Title: Renderowanie 2d część 3: Sampler State
Date: 2017-06-11 08:00
Category: OpenGL
Tags: Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

Sampler to dość nowa rzecz w OpenGL, dostępna od wersji 3.3. Jest to taki kontener, który pozwala na przechowywanie parametrów potrzeb renderowania tekstur. Jego ustawienia są wykorzystywane przez fragment shader. W poprzednich wersjach OpenGL ustawienia te trzeba było ustawiać w teksturze przez funkcje glTexParameteri(), ale w momencie kiedy mamy do dyspozycji sampler, to używać będziemy właśnie jego. 
Sam interfejs klasy wygląda w następujący sposób:

	::cpp
	enum TextureWrap
	{
    	REPEAT = GL_REPEAT,
    	MIRRORED_REPEAT = GL_MIRRORED_REPEAT,
    	CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE,
    	CLAMP_TO_BORDER = GL_CLAMP_TO_BORDER
	};

	enum TextureFilter
	{
    	POINT = GL_NEAREST,
    	LINEAR = GL_LINEAR
	};

	class SamplerState
	{
	public:
    	SamplerState(TextureWrap wrap, TextureFilter filter);
    	~SamplerState();
    	void bind();
    	void unbind();

    	void changeFilter(TextureFilter filter);
    	void changeWrap(TextureWrap wrap);
	public:
    	GLuint _samplerId;
	};

Funkcje Bind i unbind służą do aktywowania i dezaktywacji samplera, dla danej tekstury i ich implementacje wyglądają w następujący sposób:

	::cpp
	void SamplerState::bind()
	{
    	glBindSampler(0, this->_samplerId);
	}

	void SamplerState::unbind()
	{
    	glBindSampler(0, 0);
	}

Do zmiany parametrów renderowania tekstur używamy natomiast poniższych funkcji:

	::cpp
	void SamplerState::changeFilter(TextureFilter filter)
	{
    	glSamplerParameteri(this->_samplerId, GL_TEXTURE_MAG_FILTER, filter);
    	glSamplerParameteri(this->_samplerId, GL_TEXTURE_MIN_FILTER, filter);
	}

	void SamplerState::changeWrap(TextureWrap wrap)
	{
    	glSamplerParameteri(this->_samplerId, GL_TEXTURE_WRAP_S, wrap);
    	glSamplerParameteri(this->_samplerId, GL_TEXTURE_WRAP_T, wrap);
	}

To tyle z elementów potrzebnych do renderowania 2D. W następnym poście zacznę od tego, że poskładamy to wszystko razem i zaimplementujemy Spritebach, który pozwoli na rysowanie 2D .


