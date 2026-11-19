class GameLog:
    """
    게임의 행동 및 결과를 보여주는 로그

    다음 입력이 시작되기 전까지 로그를 모아놓다가 플러시함

    싱글톤으로 관리됨.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("GameLog 생성")
            cls._instance = super().__new__(cls)
            cls._instance.__buffer = []
            cls._instance.__history = []
        return cls._instance

    def add(self, msg: str):
        self.__buffer.append(msg)

    def flush(self):
        for msg in self.__buffer:
            print(msg)

        self.log_history()
        self.__buffer.clear()

    def log_history(self):
        self.__history.extend(self.__buffer)

    @property
    def history(self):
        return self.__buffer

    @property
    def history(self):
        return self.__history
