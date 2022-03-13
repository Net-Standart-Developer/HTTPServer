import os
from datetime import datetime
from http.Header import Header, HeaderType
from .Controller import Controller
from http.TypeOfRequest import TypeOfRequest
from http.Response import Response
from http.ResponseCode import ResponseCode, ResponseCodeType
import managers
from main import resources

class GetController(Controller):
    main_headers = Controller.main_headers

    def __init__(self, reader, writer, addr):
        super().__init__(reader, writer, addr, TypeOfRequest.GET, get_end_points)

    async def HandleRequest(self, request):
        if await super().HandleRequest(request) == True:
            return True

        if managers.FileManager.file_is_exist(resources + request.path.replace("/", "\\")):
            response = getResource(request)
            self.writer.write(response.__str__().encode())
            await self.writer.drain()
            return True

        response = get_end_points["/notfound.html"](request)
        self.writer.write(response.__str__().encode())
        await self.writer.drain()
        
        return False

GetController.main_headers.append(Header(header_type=HeaderType.Content_Type, value="text/html"))

def getIndex(request):
    index = managers.FileManager.read_file(resources + "\\index.html")

    headers = GetController.main_headers.copy()
    headers.append(Header(header_type=HeaderType.Date, value=datetime.now().__str__()))
    headers.append(Header(header_type=HeaderType.Content_Length, value=len(index.encode())))

    response = Response(request.version, ResponseCode.OK, headers, index)
    return response

def getResource(request):
    index = managers.FileManager.read_file(resources + request.path.replace("/", "\\"))

    headers = GetController.main_headers.copy()
    headers.append(Header(header_type=HeaderType.Date, value=datetime.now().__str__()))
    headers.append(Header(header_type=HeaderType.Content_Length, value=len(index.encode())))

    response = Response(request.version, ResponseCode.OK, headers, index)
    return response

def getNotFound(request):
    index = managers.FileManager.read_file(resources + "\\notfound.html")

    headers = GetController.main_headers.copy()
    headers.append(Header(header_type=HeaderType.Date, value=datetime.now().__str__()))
    headers.append(Header(header_type=HeaderType.Content_Length, value=len(index.encode())))

    response = Response(request.version, ResponseCode.Not_Found, headers, index)
    return response

get_end_points = {
    "/":getIndex,
    "/notfound.html":getNotFound
}