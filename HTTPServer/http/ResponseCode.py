from enum import IntEnum

class ResponseCodeType(IntEnum):
    OK = 200
    Moved_Permanently = 301
    Moved_Temporarily = 302
    Temporary_Redirect = 307
    Permanent_Redirect = 308
    Bad_Request = 400
    Unauthorized = 401
    Payment_Required = 402 
    Forbidden = 403
    Not_Found = 404
    Method_Not_Allowed = 405
    Internal_Server_Error = 500
    Not_Implemented = 501
    Bad_Gateway = 502
    Service_Unavailable = 503
    Gateway_Timeout = 504

class ResponseCode:
    def __init__(self, code=None, description=None, type=None):
        if type != None:
            self.__code = int(type)
            self.__description = type.name.replace("_", " ")
        elif code != None and description != None:
            self.__code = code
            self.__description = description
        else:
            raise ValueError("Неверные параметры в коде ответа")

    @property
    def code(self):
        return self.__code

    @property
    def description(self):
        return self.__description

    def __str__(self) -> str:
        return f"{self.__code} {self.__description}"

ResponseCode.OK = ResponseCode(type=ResponseCodeType.OK)
ResponseCode.Moved_Permanently = ResponseCode(type=ResponseCodeType.Moved_Permanently)
ResponseCode.Moved_Temporarily = ResponseCode(type=ResponseCodeType.Moved_Temporarily)
ResponseCode.Bad_Request = ResponseCode(type=ResponseCodeType.Bad_Request)
ResponseCode.Unauthorized = ResponseCode(type=ResponseCodeType.Unauthorized)
ResponseCode.Payment_Required = ResponseCode(type=ResponseCodeType.Payment_Required)
ResponseCode.Forbidden = ResponseCode(type=ResponseCodeType.Forbidden)
ResponseCode.Not_Found = ResponseCode(type=ResponseCodeType.Not_Found)