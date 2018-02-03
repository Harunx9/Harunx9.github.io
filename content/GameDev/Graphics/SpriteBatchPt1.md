Title: Renderowanie 2D część 4.1: Spritebatch
Date: 2017-06-18 17:00
Category: OpenGL
Tags: Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

W poprzednich postach opisałem składowe potrzebne do napisania właściwego renderowania, dziś zajmiemy się właśnie Spritebatchem, który będzie służył w silniku 2DXngine do renderowania 2D. Zacznijmy jak zawsze od  interfejsu klasy, którą będziemy omawiać:

	::cpp
	enum FlipEffect
	{
	    NONE_FLIP,
	    FLIP_HORIZONTAL,
	    FLIP_VERTICAL,
	};
	
	enum SortMode
	{
	    NONE_SORT,
	    FRONT_TO_BACK,
	    BACK_TO_FRONT,
	};
	
	class SpriteBatch
	{
	public:
	    SpriteBatch(GraphicDevice* device);
	    ~SpriteBatch();
	
	    bool initialize();
	
	    void set_renderTarget(RenderTarget* target);
	    void begin();
	    void begin(TextureWrap wrap, TextureFilter filter);
	    void begin(ShaderProgram * shader, TextureWrap wrap, TextureFilter filter, glm::mat4 viewportTransform);
	    void end();
	
	    void draw(Texture* texture, glm::vec2 position, Color color, float drawOrder);
	    void draw(Texture* texture, RectangleI destinationRectangle, Color color, float drawOrder);
	    void draw(Texture* texture, glm::vec2 position, RectangleI* sourceRectangle, Color color, float drawOrder);
	    void draw(Texture* texture, RectangleI destinationRectangle, RectangleI* sourceRectangle, Color color, float drawOrder);
	    void draw(Texture* texture, RectangleI destinationRectangle, RectangleI* sourceRectangle, Color color, float rotation, glm::vec2 origin, FlipEffect flip, float drawOrder);
	    void draw(Texture* texture, glm::vec2 position, RectangleI* sourceRectangle, Color color, float rotation, glm::vec2 origin, glm::vec2 scale, FlipEffect flip, float drawOrder);
	    void draw(Texture* texture, glm::vec2 position, RectangleI* sourceRectangle, Color color, float rotation, glm::vec2 origin, float scale, FlipEffect flip, float drawOrder);
	
	private:
	    struct SpriteBatchItem
	    {
	        Texture * texture;
	        glm::vec2 postions[4];
	        glm::vec2 texcoords[4];
	        glm::vec4 color;
	        glm::vec2 origin;
	        GLfloat rot;
	        float drawOrder;
	    };
	
	    void drawBatch();
	
	    void clearBatchItems();
	    SpriteBatchItem * createNewItem();
	
	    glm::mat4 _viewport;
	    glm::mat4 _viewportTransform;
	    bool initializeDefaultShader();
	    bool isRenderTargetSet();
	    size_t _currentSpriteCount;
	    std::vector<SpriteBatchItem*>  _items;
	    RenderTarget * _currentTarget;
	    ShaderProgram * _defaultShader;
	    ShaderProgram * _customShader;
	    bool _isInitialized;
	    bool _isStarted;
	    SortMode _sortMode;
	    SamplerState* _sampler;
	    GLuint _vao;
	    GLuint _vbo;
	    GLuint _ebo;
	    GraphicDevice* _device;
	    GLfloat _vertexBuffer[MAX_BATCH_ITEMS * 32];
	};

Zacznijmy od GraphicDevice, który przyjmuje konstruktor spritebatch. Na razie jest to proste opakowanie na OpenGL z SDL, może w przyszłości rozwinę ten koncept, ale na razie taka implementacja mi wystarczy, więc tak zostanie. Dalej jest inicjalizacja, funkcje rozpoczynające i  kończące rysowanie. Jeżeli chodzi o samo rysowanie to jak widzimy funkcja draw ma sporo przeciążeń, więc powinno wystarczyć dla zastosowań prostego rysowania 2D, ale po kolei jak odbywa się rysowanie. Tak na prawdę prawdziwe rysowanie następuje podczas działania funkcji end. Kolejne  wywołania draw mają za zadanie dodanie nowego SpriteBatchItem do kolejki rysowania. Sam SpriteBatchItem  jest zbiorem pewnych danych, które potrzebne są do narysowania tekstury na ekranie. Przykładowa implementacja funkcji draw wygląda w następujący sposób:

	::cpp
	void SpriteBatch::draw(Texture * texture, glm::vec2 position, RectangleI * sourceRectangle, Color color, float rotation, glm::vec2 origin, glm::vec2 scale, FlipEffect flip, float 	drawOrder)
	{
	    auto batchItem = createNewItem();
	    if (batchItem == nullptr)
	        return;
		
	    auto size = glm::vec2(texture->get_bitmap()->get_width(), texture->get_bitmap()->get_height()) * scale;
	
	    batchItem->texture = texture;
	
	    if (rotation == 0.f)
	    {
	        batchItem->postions[0] = glm::vec2(
	            position.x - origin.x,
	            position.y - origin.y);
			
	        batchItem->postions[1] = glm::vec2(
	            (position.x - origin.x) + size.x,
	            position.y - origin.y);
			
	        batchItem->postions[2] = glm::vec2(
	            position.x - origin.x,
	            (position.y - origin.y) + size.y);
			
	        batchItem->postions[3] = glm::vec2(
	            position.x - origin.x + size.x,
	            (position.y - origin.y) + size.y);
	    }
	    else
	    {
	        float cosRot = glm::cos(rotation);
	        float sinRot = glm::sin(rotation);
		
	        batchItem->postions[0] = glm::vec2(
	            position.x + (-origin.x * cosRot) - (-origin.y * sinRot),
	            position.y + (-origin.x * sinRot) - (-origin.y * cosRot));
			
	        batchItem->postions[1] = glm::vec2(
	            position.x + (-origin.x + size.x) * cosRot - (-origin.y)* sinRot,
	            position.y + (-origin.x + size.x) * sinRot - (-origin.y)* cosRot);
			
	        batchItem->postions[2] = glm::vec2(
	            position.x + (-origin.x * cosRot) - (-origin.y + size.y)* sinRot,
	            position.y + (-origin.x * sinRot) - (-origin.y + size.y)* cosRot);
			
	        batchItem->postions[3] = glm::vec2(
	            position.x + (-origin.x + size.x) * cosRot - (-origin.y + size.y)* sinRot,
	            position.y + (-origin.x + size.x) * sinRot - (-origin.y + size.y)* cosRot);
	    }
	
	    //set color
	    batchItem->color.x = color.r;
	    batchItem->color.y = color.g;
	    batchItem->color.z = color.b;
	    batchItem->color.w = color.a;
	
	    //origin
	    batchItem->origin = glm::vec2(0.f, 0.f);
	
	    //rotation
	    batchItem->rot = 0.f;
	
	    batchItem->drawOrder = drawOrder;
	
	    //texCoord
	    if (sourceRectangle != nullptr)
	    {
	        batchItem->texcoords[0] = glm::vec2(
	            sourceRectangle->get_x() * texture->get_bitmap()->get_texelWidth(),
	            sourceRectangle->get_y() * texture->get_bitmap()->get_texelHeight());
			
	        batchItem->texcoords[1] = glm::vec2(
	            (sourceRectangle->get_x() + sourceRectangle->get_width()) * texture->get_bitmap()->get_texelWidth(),
	            sourceRectangle->get_y() * texture->get_bitmap()->get_texelHeight());
			
	        batchItem->texcoords[2] = glm::vec2(
	            sourceRectangle->get_x() * texture->get_bitmap()->get_texelWidth(),
	            (sourceRectangle->get_y() + texture->get_bitmap()->get_height()) * texture->get_bitmap()->get_texelHeight());
			
	        batchItem->texcoords[3] = glm::vec2(
	            (sourceRectangle->get_x() + sourceRectangle->get_width()) * texture->get_bitmap()->get_texelWidth(),
	            (sourceRectangle->get_y() + texture->get_bitmap()->get_height()) * texture->get_bitmap()->get_texelHeight());
	    }
	    else
	    {
	        batchItem->texcoords[0] = glm::vec2(0.f, 0.f);
	        batchItem->texcoords[1] = glm::vec2(1.f, 0.f);
	        batchItem->texcoords[2] = glm::vec2(0.f, 1.f);
	        batchItem->texcoords[3] = glm::vec2(1.f, 1.f);
	    }
	
	    switch (flip)
	    {
	    case FLIP_HORIZONTAL:
	    {
	        auto tltmp1 = batchItem->texcoords[0];
	        auto trtmp = batchItem->texcoords[1];
	        batchItem->texcoords[0] = batchItem->texcoords[2];
	        batchItem->texcoords[1] = batchItem->texcoords[3];
	        batchItem->texcoords[2] = tltmp1;
	        batchItem->texcoords[3] = trtmp;
	    }
	    break;
	    case FLIP_VERTICAL:
	    {
	        auto tltmp2 = batchItem->texcoords[0];
	        auto bltmp = batchItem->texcoords[2];
	        batchItem->texcoords[0] = batchItem->texcoords[1];
	        batchItem->texcoords[2] = batchItem->texcoords[3];
	        batchItem->texcoords[1] = tltmp2;
	        batchItem->texcoords[3] = bltmp;
	    }
	    break;
	    }
	}

Za przykład wziąłem najbardziej rozbudowaną implementacje, żeby dokładnie prześledzić, to w jaki sposób potrzebujemy zapisać dane, aby potem mogły one zostać wyświetlone. Na początku tworzymy nowy SpritebatchItem, a nastepnie określamy wymiray tekstury przy zeskalowaniu. Kolejnym krokiem jest przypisanie wskaźnika na teksturę, jest to potrzebne, by potem pobrać z niego id tekstury.  Następnie w zależności od tego czy nasza tekstura jest obrócona czy nie, musimy przypisać pozycje do 4 vertexów w taki sposób:

	[ tl ]---------[ tr ]
	  |             / |
	  |          /    |
	  |        /      |
	  |      /        |
	  |   /           |
	[ bl ]--------[ br ]

Jak widać na schemacie każda tekstura składa się z połączonych 2 trójkątów, więc na logikę vertexów powinno być 6. Każdy vertex to jednak alokacja pamięci, więc tworzymy 4 vertexy i 6 indexów, czyli wskaźników na vertex. Dzięki temu unikamy dodatkowej alokacji pamięci, a efekt jest ten sam. W kolejnych krokach przypisane zostają kolor, origin (środek obiektu) oraz rotacja. Kolejną sprawą jest przypisanie koordynatów tekstury. Ostatnim etapem jest ewentualne odwrócenie tekstury, jeżeli jest ona w jakiś sposób odwrócona. Mniej więcej inne przeciążenia robią to samo. To w tej części na tyle, w następnym artykule prześledzimy jak wygląda samo rysowanie i jak używać naszego SpriteBatcha.


