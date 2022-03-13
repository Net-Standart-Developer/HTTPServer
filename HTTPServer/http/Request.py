from .TypeOfRequest import TypeOfRequest
from .Header import Header

class Request:
    def __init__(self, type=None, path=None, version=None, headers=None, body=None, data=None) -> None:
        if data:
            data = data.split("\n")
            start_line = data[0].split()
            
            match start_line[0]:
                case "GET":
                    self.__type = TypeOfRequest.GET
                case "POST":
                    self.__type = TypeOfRequest.POST
                case "PUT":
                    self.__type = TypeOfRequest.PUT
                case "DELETE":
                    self.__type = TypeOfRequest.DELETE
                case _:
                    raise ValueError("неверный тип запроса")
            
            self.__path = start_line[1]
            self.__version = start_line[2]

            self.__headers = []

            i = 1
            isHeader = True
            while i < len(data) and isHeader:
                if data[i] == "" or data[i] == "\r":
                    isHeader = False
                else:
                    key = data[i].split(":")[0]
                    value = data[i].split(":")[1]
                    self.__headers.append(Header(key, value))
                i += 1

            if self.__type != TypeOfRequest.GET:
                self.__body = "\n".join(data[i:])
            else:
                self.__body = None

        elif type != None and path != None and version != None and headers != None and body != None:
            self.__type = type
            self.__path = path
            self.__version = version
            self.__headers = headers
            self.__body = body
        else:
            raise ValueError("неправильные параметры запроса")

    @property
    def type(self):
        return self.__type

    @property
    def path(self):
        return self.__path

    @property
    def version(self):
        return self.__version

    @property
    def headers(self):
        return self.__headers

    @property
    def body(self):
        return self.__body

    def __str__(self) -> str:
        str = f"{self.type.name} {self.path} {self.version}\r\n"
        
        for header in self.headers:
            str += header.__str__() + "\r\n"
        
        if self.body:
            str += "\r\n" + self.body
        
        return str