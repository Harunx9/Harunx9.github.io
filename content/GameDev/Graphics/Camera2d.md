Title: Renderowanie 2D cześć 5: Kamera
Date: 2017-07-02 14:00
Category: OpenGL
Tags: Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

Cześć. W poprzednich artykułach opisałem jak zaimplementowałem renderowanie 2D, dziś jeszcze jeden element dotyczący grafiki, czyli kamera 2D. Kamera jest elementem za pomocą, którego możemy manipulować viewport'em.
Sam interfejs klasy kamery jest dość prosty:

	::cpp
	class Camera
	{
	public:
	    Camera(int viewportWidth, int viewportHeight);
	    ~Camera();

	    inline float get_rotation() const
	    {
	        return this->_rotation;
	    }

	    inline void set_rotation(float rotation)
	    {
	        if (MIN_ROT < rotation && rotation < MAX_ROT)
	            this->_rotation = rotation;
	    }

	    inline float get_zoom()const
	    {
	        return this->_zoom;
	    }

	    inline void set_zoom(float zoom)
	    {
	        if (MIN_ZOOM < zoom && zoom < MAX_ZOOM)
	            this->_zoom = zoom;
	    }


	    glm::mat4 get_viewMatrix();

	    PROPERTY(int ,viewportWidth)
	    PROPERTY(int ,viewportHeight)
	    PROPERTY(glm::vec2, position)
	    PROPERTY(glm::vec2, origin)

	private:
	    float _zoom;
	    float _rotation;

	    const float MAX_ROT = std::numeric_limits<float>::max();
	    const float MIN_ROT = std::numeric_limits<float>::lowest();

	    const float MAX_ZOOM = std::numeric_limits<float>::max();
	    const float MIN_ZOOM = std::numeric_limits<float>::lowest();
	};

Z implementacyjnej części to najciekawsza jest funkcja  get_viewMatrix()  ma ona dość prostą implementacje.

	::cpp
	glm::mat4 Camera::get_viewMatrix()
	{
	    glm::mat4 vm = glm::mat4();
	    vm = glm::translate(vm, glm::vec3(this->_origin, 0.f));
	    vm = glm::rotate(vm, -this->_rotation, glm::vec3(0.f, 0.f, 1.f));
	    vm = glm::scale(vm, glm::vec3(this->_zoom, this->_zoom, 1.f));
	    vm = glm::translate(vm, glm::vec3(-this->_origin, 0.f));
	    vm = glm::translate(vm, glm::vec3(-this->_position, 0.f));
	    return vm;
	}

Po obliczeniu nowej macierzy można ją podać w metodzie begin spritebatcha i za jej pomocą transformować standardowy viewport. Z rzeczy brakujących to można by było napisać funkcję project i unproject, aby można było przeliczać koordynaty muszy z okienka do świata gry i ze świata gry do koordynatów okienka. Na razie nie potrzebuje takiej funkcjonalności, ale pewnie w przyszłości dodam taką funkcje. 



