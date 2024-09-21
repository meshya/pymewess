class BaseProtocol:
    def __init__ (self): ...
class BaseConnection:
    ...
class BaseEncrypt:
    ...

class Config:
    protocol: BaseProtocol

    def __init__ ( self,
            protocol=None,
            address=None,
            connection=None,
            encrypt=None,
            name=None,
            ):
        ...
    def url(self):
        ...
    
            
