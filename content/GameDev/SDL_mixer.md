Title: SDL_mixer,  czyli szybka implementacja audio
Date: 2017-07-09 21:20
Category: Gamedev
Tags: Gamedev
Authors: Szymon Wanot
Status: published

Prawdopodobnie każdy twórca gier chce, by jego gra powodowała większą immersję, dlatego też należałoby do niej dodać oprócz grafiki takżę dźwięk oraz muzykę. 
Ze względu na to, że 2DXngine używa SDL2 postanowiłem iść dalej tą drogą i do odczytywania wykorzystać plugin SDL_mixer. Jest to mała wtyczka do SDL2, która pozwala odczytywać muzykę i dźwięki w różnych formatach. Moje rozwiązanie jest oparte o klasy i przyjrzymy się mu w perspektywie plików MP3 i WAV. 
Muzyka i dźwięki posiadają swoje klasy bazowe Sound i Music, które wyglądają w następujący sposób:

	::cpp
	enum SoundState {
	    STOPPED,
	    PLAYING,
	    PAUSED
	};

	class Sound : public Asset
	{
	protected:
	    SoundState _currentState;
	    Sound(AssetPath path, const AssetType* type) : Asset(path, type) {}
	public:
	    virtual ~Sound() {}
	    virtual void play(bool repeat = false) = 0;
	    virtual void pause() = 0;
	    virtual void resume() = 0;
	    virtual void stop() = 0;
	    SoundState get_soundState()
	    {
	        return this->_currentState;
	    }
	};

	class Music : public Asset
	{
	protected:
	    SoundState _currentState;
	    Music(AssetPath path, const AssetType* type) : Asset(path, type) {}
	public:
	    virtual ~Music() {}
	    virtual void play(bool repeat = false) = 0;
	    virtual void pause() = 0;
	    virtual void resume() = 0;
	    virtual void stop() = 0;
	    SoundState get_musicState()
	    {
	        return this->_currentState;
	    }
	};

W przypadku pliku MP3 ładowanie pliku odbywa się w następujący sposób:

	::cpp
	Mp3Sound::Mp3Sound(AssetPath path) : Music(path, DefaultAssetType::MP3_TYPE)
	{
	    std::string fPathStr = path.get_fullPath();
	    const char* soundPath = fPathStr.c_str();
	    this->_musicData = Mix_LoadMUS(soundPath);
	    this->_currentState = SoundState::STOPPED;
	}

W przypadku Wav wygląda to podobnie tylko funkcja Mix_LoadMUS(const char* path) zamienia się na Mix_LoadWAV(const char* path). Różnice występują natomiast w odtwarzaniu, aby odegrać muzykę używam serwisu MusicService, który trzyma referencje na odgrywany kawałek. Za jego pomocą mogę również zatrzymywać, wznawiać lub zakończyć odrywanie danej muzyki.
W przypadku dźwięku sprawa ma się nieco inaczej, o ile muzyka odpaloną jedną ścieżkę na raz to dźwięki można ze sobą mixować i odpalać je kilka w jednym czasie. W tym przypadku w SoundService inicjalizuję kanały dla dźwięku zanim zacznę serwisu używać:

	::cpp
	Mix_AllocateChannels(256);

Jest to o tyle ważne, ponieważ podczas odtwarzania dźwięku pobieramy pierwszy wolny kanał i na nim odtwarzamy dźwięk, jeżeli chcemy potem zatrzymać dźwięk to musimy podać kanał na którym odgrywany jest dźwięk. W mojej implementacji wygląda to następująco:

	::cpp
	void WavSound::play(bool repeat)
	{
	    int loop = 1;
	    if (repeat)
	    {
	        loop = -1;
	    }

	    this->_channel = Mix_PlayChannel(-1, this->_soundData, loop);
	
	    if (this->_channel != -1)
	    {
	        this->_currentState = SoundState::PLAYING;
	    }
	}

	void WavSound::pause()
	{
	    Mix_Pause(this->_channel);
	    this->_currentState = SoundState::PAUSED;
	}

	void WavSound::stop()
	{
	    Mix_HaltChannel(this->_channel);
	    this->_channel = -1;
	    this->_currentState = SoundState::STOPPED;
	}

Oprócz MP3 zaimplementowałem jeszcze format OGG. Zobaczymy czy go będę używał, ale jakby ktoś potrzebował to jest. Zobaczymy jak muzyka będzie się sprawowała podczas implementacji gry, ale na razie z testów wynika, że powinno być ok. To chyba wszystko w temacie SDL_mixer w razie gdybym czegoś się jeszcze w tym temacie dowiedział, to opiszę na blogu.