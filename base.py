class based:
    def __init__(self):
        pass
    @staticmethod
    def charfield(max_length,default):
        max_length=max_length
        default=default
        return {"max_length":max_length,"default":default,"type":"TEXT"}
    @staticmethod
    def integer_field(max_value,default=None):
        max_value=max_value
        default=default
        return {"max_value":max_value,"default":default,"type":"INTEGER"}

