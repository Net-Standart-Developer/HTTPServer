from http.Header import Header, HeaderType
from http.Response import Response
from http.TypeOfRequest import TypeOfRequest

class Controller:
    main_headers = [
        Header(header_type=HeaderType.Server, value="PythonServer")
    ]

    def __init__(self, reader, writer, addr, type, end_points_responses) -> None:
        self.__type = type
        self.__reader = reader
        self.__writer = writer
        self.__addr = addr
        self.__end_points = end_points_responses

    @property
    def type(self):
        return self.__type

    @property
    def reader(self):
        return self.__reader

    @property
    def writer(self):
        return self.__writer
    
    @property
    def addr(self):
        return self.__addr

    async def HandleRequest(self, request):
        for end_point in self.__end_points:
            if request.path == end_point:
                response = self.__end_points[end_point](request)
                self.__writer.write(response.__str__().encode())
                await self.__writer.drain()
                return True
        
        return False