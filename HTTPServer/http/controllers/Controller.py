from http.Header import Header, HeaderType
from http.Response import Response
from http.TypeOfRequest import TypeOfRequest

class Controller:
    main_headers = [
        Header(header_type=HeaderType.Server, value="PythonServer")
    ]

    def __init__(self, client, addr, type, end_points_responses) -> None:
        self.__type = type
        self.__client = client
        self.__addr = addr
        self.__end_points = end_points_responses

    @property
    def type(self):
        return self.__type

    @property
    def client(self):
        return self.__client
    
    @property
    def addr(self):
        return self.__addr

    def HandleRequest(self, request):
        for end_point in self.__end_points:
            if request.path == end_point:
                response = self.__end_points[end_point](request)
                self.__client.sendall(response.__str__().encode())
                return True
        
        return False