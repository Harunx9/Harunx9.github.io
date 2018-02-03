Title: Renderowanie 2D część 4.2: Spritebatch
Date: 2017-06-21 19:30
Category: OpenGL
Tags: Gamedev, OpenGL
Authors: Szymon Wanot
Status: published

Cześć. W poprzedniej części napisałem nieco o tym jak przebiega rysowanie a właściwie dokładanie elementów do narysowania. W tym artykule zajmiemy się dokładnie tym jak działa pipeline rysowania SpriteBatchem. Aby narysować jaką teksturę należy napisać taki oto kodzik:

	::cpp
	this->_device->clear(Colors::black);
	batch->begin(TextureWrap::REPEAT, TextureFilter::POINT_FILTER);
	
	    batch->draw(texture1, glm::vec2(200.f, 200.f), nullptr, Colors::white, 0, glm::vec2(0.f, 0.f), 2, FlipEffect::NONE_FLIP, 2);
	    batch->draw(texture2, glm::vec2(300.f, 200.f), nullptr, Colors::white, 0, glm::vec2(0.f, 0.f), 3, FlipEffect::NONE_FLIP, 2);
	
	batch->end();
	this->_device->swapBuffers();

Zacznijmy od samej góry. Aby wyczyścić backbuffer trzeba najpierw wywołać funkcje clear() z graphic device. Potem wywołujemy jedno z przeciążeń funkcji begin, która przygotowuje wszystkie elementy SpriteBatcha do rysowania. Przykładowa implementacja wygląda tak:

	::cpp
	void SpriteBatch::begin(ShaderProgram * shader, TextureWrap wrap, TextureFilter filter, glm::mat4 viewportTransform)
	{
	    if (this->_isInitialized == false && this->_isStarted) return;

	    this->_customShader = shader;
	    this->_viewport = glm::ortho(0.f,
	        static_cast<GLfloat>(this->_device->get_viewport().width),
	        static_cast<GLfloat>(this->_device->get_viewport().height),
	        0.f, -1.f, 1.f);
	    this->_viewportTransform = viewportTransform;
	    this->_isStarted = true;
	    this->_sampler->changeFilter(filter);
	    this->_sampler->changeWrap(wrap);
	}

Jak możemy zauważyć najważniejsze jest ustalenie Viewportu i samplera. Druga macierz służy do nałożenia  transformacji kamery  ale to w innym artykule napiszę na ten temat. Po wywołaniu kolejnych funkcji draw() wywołujemy funkcje end ()która wykonuje właściwe rysowanie. 

	::cpp
	void SpriteBatch::end()
	{
	    //draw to frame buffer
	    if (this->_currentTarget == nullptr)
	    {
	        this->_currentTarget->begin();
	        this->drawBatch();
	        this->_currentTarget->end();
	    }
	    else //draw to backbuffer
	    {
	        this->drawBatch();
	    }
	}

Jeżeli mamy nałożony render target to cały batch jest rysowany to niego jeżeli nie to rysujemy na backbuffer. Funkcja drawBatch() która rysuje cały bufor ma następującą implementację: 

	::cpp
	void SpriteBatch::drawBatch()
	{
	
	    switch (this->_sortMode)
	    {
	    case SortMode::FRONT_TO_BACK:
	        std::sort(this->_items.begin(), this->_items.end(),
	            [=](SpriteBatchItem* item1, SpriteBatchItem* item2) { return item1->drawOrder < item2->drawOrder; });
	        break;
	    case SortMode::BACK_TO_FRONT:
	        std::sort(this->_items.begin(), this->_items.end(),
	            [=](SpriteBatchItem* item1, SpriteBatchItem* item2) { return item1->drawOrder > item2->drawOrder; });
	        break;
	    }
	
	    if (this->_viewport == glm::mat4())
	    {
	        GLint display[4];
	        glGetIntegerv(GL_VIEWPORT, display);
	        this->_viewport = glm::ortho(0.f, (float)display[2],
	            (float)display[3], 0.f);
	    }
	
	    GLuint currentProgram;
	    if (this->_customShader != nullptr)
	    {
	        this->_customShader->use();
	        currentProgram = this->_customShader->get_programId();
	    }
	    else
	    {
	        this->_defaultShader->use();
	        currentProgram = this->_defaultShader->get_programId();
	    }
	
	    glm::mat4  full_viewProj =  this->_viewport * this->_viewportTransform;
	    auto viewport = glm::value_ptr(full_viewProj);
	    glUniformMatrix4fv(glGetUniformLocation(currentProgram, "projection"), 1, GL_FALSE, viewport);
	
	    glBindVertexArray(this->_vao);
	
	    glBindBuffer(GL_ARRAY_BUFFER, this->_vbo);
	    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, this->_ebo);
	
	    size_t spritesCount = this->_items.size();
	    size_t batchesToDraw = spritesCount / MAX_BATCH_ITEMS;
	
	    this->_sampler->bind();
	    for (size_t batchNumber = 0; batchNumber < batchesToDraw + 1; ++batchNumber)
	    {
	        size_t spriteNumber = spritesCount - (batchNumber * MAX_BATCH_ITEMS);
	        if (spriteNumber > MAX_BATCH_ITEMS)
	            spriteNumber = MAX_BATCH_ITEMS;
			
	        for (size_t i = batchNumber * MAX_BATCH_ITEMS; i < batchNumber * MAX_BATCH_ITEMS + spriteNumber; ++i)
	        {
	            auto item = this->_items[i];
			
	            size_t newI = (i - (i / MAX_BATCH_ITEMS * MAX_BATCH_ITEMS)) * 32;
			
	            //top left
	            this->_vertexBuffer[newI + 0] = item->postions[0].x;
	            this->_vertexBuffer[newI + 1] = item->postions[0].y;
	            this->_vertexBuffer[newI + 2] = item->texcoords[0].x;
	            this->_vertexBuffer[newI + 3] = item->texcoords[0].y;
	            this->_vertexBuffer[newI + 4] = item->color.x;
	            this->_vertexBuffer[newI + 5] = item->color.y;
	            this->_vertexBuffer[newI + 6] = item->color.z;
	            this->_vertexBuffer[newI + 7] = item->color.w;
	            //top right
	            this->_vertexBuffer[newI + 8] = item->postions[1].x;
	            this->_vertexBuffer[newI + 9] = item->postions[1].y;
	            this->_vertexBuffer[newI + 10] = item->texcoords[1].x;
	            this->_vertexBuffer[newI + 11] = item->texcoords[1].y;
	            this->_vertexBuffer[newI + 12] = item->color.x;
	            this->_vertexBuffer[newI + 13] = item->color.y;
	            this->_vertexBuffer[newI + 14] = item->color.z;
	            this->_vertexBuffer[newI + 15] = item->color.w;
	            //top left
	            this->_vertexBuffer[newI + 16] = item->postions[2].x;
	            this->_vertexBuffer[newI + 17] = item->postions[2].y;
	            this->_vertexBuffer[newI + 18] = item->texcoords[2].x;
	            this->_vertexBuffer[newI + 19] = item->texcoords[2].y;
	            this->_vertexBuffer[newI + 20] = item->color.x;
	            this->_vertexBuffer[newI + 21] = item->color.y;
	            this->_vertexBuffer[newI + 22] = item->color.z;
	            this->_vertexBuffer[newI + 23] = item->color.w;
	            //top right
	            this->_vertexBuffer[newI + 24] = item->postions[3].x;
	            this->_vertexBuffer[newI + 25] = item->postions[3].y;
	            this->_vertexBuffer[newI + 26] = item->texcoords[3].x;
	            this->_vertexBuffer[newI + 27] = item->texcoords[3].y;
	            this->_vertexBuffer[newI + 28] = item->color.x;
	            this->_vertexBuffer[newI + 29] = item->color.y;
	            this->_vertexBuffer[newI + 30] = item->color.z;
	            this->_vertexBuffer[newI + 31] = item->color.w;
	        }
		
	        size_t fullSize = spritesCount - batchNumber * MAX_BATCH_ITEMS;
		
	        if (fullSize > MAX_BATCH_ITEMS)
	            fullSize = MAX_BATCH_ITEMS;
			
	        glBufferSubData(GL_ARRAY_BUFFER, 0, fullSize* (32 * sizeof(GLfloat)),
	            &this->_vertexBuffer[0]);
			
	        auto lastTex = this->_items[batchNumber * MAX_BATCH_ITEMS]->texture;
	        int offset = 0;
		
	        SpriteBatchItem* spriteItem;
	        for (size_t i = 0; i < spriteNumber; ++i)
	        {
	            spriteItem = this->_items[batchNumber * MAX_BATCH_ITEMS + i];
	            if (spriteItem->texture->get_textureId() != lastTex->get_textureId())
	            {
	                lastTex->bind();
	                glDrawElements(GL_TRIANGLES, (i - offset) * 6,
	                    GL_UNSIGNED_INT, (GLvoid*)(offset * 6 * sizeof(GLuint)));
	                offset = i;
	                lastTex = spriteItem->texture;
	            }
	        }
		
	        lastTex->bind();
	        glDrawElements(GL_TRIANGLES, (spriteNumber - offset) * 6,
	            GL_UNSIGNED_INT, (GLvoid*)(offset * 6 * sizeof(GLuint)));
	    }
	
	    glBindTexture(GL_TEXTURE_2D, 0);
	    glBindBuffer(GL_ARRAY_BUFFER, 0);
	    this->_sampler->bind();
	
	    glBindVertexArray(0);
	    glUseProgram(0);
	
	    this->_isStarted = false;
	    this->clearBatchItems();
	}

Metoda drawBatch na początku sortuje tekstury, oblicza viewport włącza customowy shader jeżeli  jest on ustawiony. Następnie obliczana jest macierz projekcji i wszystkie dane pakowane są do bufora oraz wysyłane są one do rysowania. Po wszystkim batch jest czyszczony i cały proces zaczyna się od nowa. To chyba na tyle jeżeli chodzi o samego batcha z grafiki została nam jeszcze kamera, którą opiszę w następnym artykule.