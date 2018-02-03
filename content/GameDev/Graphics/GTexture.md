Title: Renderowanie 2D część 2: Shadery
Date: 2017-05-20 18:50
Category: OpenGL
Tags: DSP2017, Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

Shadery to programy wykonywane podczas procesu renderowania OpenGL. Nie będę tu opisywał całego pipeline, ponieważ to byłby temat na cały osobny artykuł, więc wspomnę tylko, że dla renderowania 2D istotne jest wipięcie się w fazę vertex shadera i fragment shadera. Ten pierwszy opowiada za umiejscowienie naszego spritea w przestrzeni, jego transformacje itp. Drugi shader włącza się już po rasteryzacji obrazu i odpowiada za kolorowanie poszczególnych pixeli. Pogramy shadera w przypadku OpenGL pisze się w języku GLSL. Przypomina on bardzo składnią C i jest językiem strukturalnym. Możemy w programie pisanym np. w C++ przesyłać do niego dane itp. Dodatkowo składnie wzbogacają wszystkie potrzebne typy matematyczne takie jak wektory, macierze i quaterniony oraz niezbędne funkcje matematyczne. Jeżeli nie chcecie babrać się z pisaniem w C++ lub chcecie tylko potestować shadery to zapraszam na [shadertoy](https://www.shadertoy.com/). Jako, że GLSL jest osobnym językiem musi on zostać wczytany skompilowany i uruchomiony podczas działania programu. W tym celu zrobiłem parę rzeczy, aby to ułatwić i zamknąć w jedną całość za pomocą klas. Jako pierwszą zaimplementowałem klasę dla pojedynczego programu shadera. Jej interfejs wygląda w następujący sposób:

	::cpp
	enum ShaderType
	{
    	VERTEX_SHADER = GL_VERTEX_SHADER,
    	FRAGMENT_SHADER = GL_FRAGMENT_SHADER,
    	GEOMERTY_SHADER = GL_GEOMETRY_SHADER
	};

	enum ShaderCompileResult
	{
    	COMPILATION_ERROR,
    	COMPILATION_SUCESS
	};

	class Shader
	{
	public:
    	Shader(const char * path, ShaderType type);
    	Shader(std::string source, ShaderType type);
    	~Shader();
    
    	bool tryLoad();
    	ShaderCompileResult compile();
    	READONLY_PROPERTY(GLuint, shaderId)
    	READONLY_PROPERTY(ShaderType, type)
	private:
    	bool _compiled;
    	std::string _source;
    	std::string _path;
	};

Jak widać zmapowałem stałe OpenGl na enum ShaderType, dodatkowo zrobiłem enum określający to czy kompilacja się powiodła. Wynika to z tego względu, że stosowanie wyjątków jest bardzo kosztowne w C++, dlatego zamieniłem je na takie oto rezultaty operacji. Będę to musiał jakoś spłaszczyć tak, aby rezultaty były bardziej uniwersalne. Przejdźmy do  implementacji. Funkcja try load próbuje wczytać z podanego pliku kod shadera:

	::cpp
	bool Shader::tryLoad()
	{
    	if (this->_source.empty() == false)
        	return true;

    	if (File::exist(this->_path))
    	{
        	this->_source = File::readFileToEnd(this->_path);
        	return true;
    	}

    	return false;
	}

Funkcja compile wczytany kod kompiluje oraz zwraca czy proces ten się powiódł czy nie:

	::cpp
	ShaderCompileResult Shader::compile()
	{
    	this->_shaderId = glCreateShader(this->_type);
    	const GLchar* src = this->_source.c_str();
    
    	glShaderSource(this->_shaderId, 1, &src, nullptr);
    	glCompileShader(this->_shaderId);
    
    	_compiled = true;

    	GLint success;
    	glGetShaderiv(this->_shaderId, GL_COMPILE_STATUS, &success);

	    if (success == GL_FALSE)
    	    return ShaderCompileResult::COMPILATION_ERROR;

    	return ShaderCompileResult::COMPILATION_SUCESS;
	}

Zdaję sobie sprawę, że powinineim na początku kompilacji sprawdzić czy mam wczytane pliki, ale tym zajmuje się klasa Shader Program, która posiada taki oto interfejs:

	::cpp
	enum ProgramCompilationResult
	{
    	COMPILE_ERROR,
    	COMPILE_SUCCESS
	};

	class ShaderProgram : public Asset
	{
	public:
    	static ShaderProgram* load(AssetPath assetPath);
    	ShaderProgram(AssetPath assetPat);
    	ShaderProgram(std::string vertexProgram, std::string fragmentProgram, std::string geometryProgram = "");
    	~ShaderProgram();

    	ShaderProgram & use();

    	ProgramCompilationResult compile();

    	void setFloatParam(const char* paramName, float value);
    	void setIntParam(const char* paramName, int value);
    	void setVec2fParam(const char* paramName, float x, float y);
    	void setVec2fParam(const char* paramName, const glm::vec2 &value);
    	void setVec3fParam(const char* paramName, float x, float y, float z);
    	void setVec3fParam(const char* paramName, const glm::vec3 &value);
    	void setVec4fParam(const char* paramName, float x, float y, float z, float w);
    	void setVec4fParam(const char* paramName, const glm::vec4 &value);
    	void setMatrix4Param(const char* paramName, const glm::mat4 &value);
   
   		READONLY_PROPERTY(GLuint, programId)
	private:
    	void loadShadersFromFile();
    	void loadShadersFromSource(std::string vertexProgram, std::string fragmentProgram, std::string geometryProgram);
    	std::string _programName;
    	std::string _vertexPath;
    	std::string _fragmentPath;
    	std::string _geometryPath;
    	Shader * _vertexShader;
    	Shader * _fragmentShader;
    	Shader * _geometryShader;
	};

Jest to klasa, która wczytuje właściwy program shadera z kilku podprogramów i linkuje je razem tak, aby działały w jednym pipelinie. W tym momencie jest możliwość wpięcia się w fazę vertex, geometry i fragment, choć jak na razie nie jest to silnik 3D. Funkcja compile wygląda w następujący sposób:

	::cpp
	ProgramCompilationResult ShaderProgram::compile()
	{
    	ShaderCompileResult vertexCompileResult, fragmentCompileResult, geometryCompileResult = ShaderCompileResult::COMPILATION_ERROR;

    	if (this->_vertexShader->tryLoad())
    	{
        	vertexCompileResult = this->_vertexShader->compile();
        	if (vertexCompileResult == ShaderCompileResult::COMPILATION_ERROR)
            	return ProgramCompilationResult::COMPILE_ERROR;
    	}

    	if (this->_fragmentShader->tryLoad())
    	{
        	fragmentCompileResult = this->_fragmentShader->compile();
        	if (fragmentCompileResult == ShaderCompileResult::COMPILATION_ERROR)
            	return ProgramCompilationResult::COMPILE_ERROR;
    	}

    	if (this->_geometryShader->tryLoad())
    	{
        	geometryCompileResult = this->_geometryShader->compile();
        	if (geometryCompileResult == ShaderCompileResult::COMPILATION_ERROR) 
            	return ProgramCompilationResult::COMPILE_ERROR;
    	}

    	this->_programId = glCreateProgram();

    	if (vertexCompileResult == ShaderCompileResult::COMPILATION_SUCESS)
    	{
       		glAttachShader(this->_programId, this->_vertexShader->get_shaderId());
   	 	}

    	if (fragmentCompileResult == ShaderCompileResult::COMPILATION_SUCESS)
    	{
        	glAttachShader(this->_programId, this->_fragmentShader->get_shaderId());
    	}

    	if (geometryCompileResult == ShaderCompileResult::COMPILATION_SUCESS)
    	{
        	glAttachShader(this->_programId, this->_geometryShader->get_shaderId());
    	}

    	glLinkProgram(this->_programId);

    	GLint success;
    	glGetProgramiv(this->_programId, GL_LINK_STATUS, &success);

    	delete this->_vertexShader;
    	delete this->_fragmentShader;
    	delete this->_geometryShader;

    	if (success == GL_FALSE)
        	return ProgramCompilationResult::COMPILE_ERROR;

    	return ProgramCompilationResult::COMPILE_SUCCESS;
	}

Generalnie próbuje ona skompilować i zlinkować shadery vertex, geometry i fragment. Jak to się uda to zwracany jest sukces, jeżeli nie to zwracany jest błąd, który trzeba obsłużyć. Generalnie jak już pisałem, nad obsługą błędów będę musiał jeszcze popracować, ale to już coś na przyszłość. To na razie było by na tyle w następnym poście przyjrzymy się samplerom tekstur.

