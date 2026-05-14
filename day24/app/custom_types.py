from typing import TypedDict, Literal, TypeAlias

class RawUserDict(TypedDict):
    name: str
    age: str
    city: str
    email: str

class UserDict(TypedDict):
    name: str
    age: int
    city: str
    email: str    

ValidationError : TypeAlias = str


MenuChoice = Literal['1','2','3','4','5','6','0']
