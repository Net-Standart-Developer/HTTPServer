from enum import IntEnum

class Header:
    def __init__(self, key=None, value=None, header_type=None) -> None:
        if key != None and value != None:
            self.key = key
            self.value = value
        elif value != None and header_type != None:
            self.key = header_type.name.replace("_", "-")
            self.value = value
        else:
            raise ValueError("Неверные параметры в заголовке")

    def __str__(self) -> str:
        return f"{self.key}: {self.value}"

class HeaderType(IntEnum):
    Date = 1
    Server = 2
    Last_Modified = 3
    Content_Length = 4
    Content_Type = 5