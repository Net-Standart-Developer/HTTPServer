class Response:
    def __init__(self, version, code, headers, body=None):
        self.__version = version
        self.__code = code
        self.__headers = headers
        self.__body = body

    @property
    def version(self):
        return self.__version

    @property
    def code(self):
        return self.__code

    @property
    def headers(self):
        return self.__code

    @property
    def body(self):
        return self.__body

    def __str__(self) -> str:
        resp = f"{self.__version} {self.__code}\r\n"
        for header in self.__headers:
            resp += header.__str__() + "\r\n"
        
        if self.__body != None:
            resp += "\r\n"
            resp += self.__body
        
        return resp