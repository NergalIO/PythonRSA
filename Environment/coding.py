class coding: 
    dictionary = {
        '!':b'\x01','"':b'\x02','#':b'\x03','$':b'\x04','%':b'\x05','&':b'\x06','\'':b'\x07','(':b'\x08',')':b'\x09','*':b'\x0a','+':b'\x0b',',':b'\x0c','-':b'\x0d','.':b'\x0e','/':b'\x0f',':':b'\x10',';':b'\x11','<':b'\x12','=':b'\x13','>':b'\x14','?':b'\x15','@':b'\x16','[':b'\x17','\\':b'\x18',']':b'\x19','^':b'\x1a','_':b'\x1b','`':b'\x1c','{':b'\x1d','|':b'\x1e','}':b'\x1f','~':b'\x20','a':b'\x21','b':b'\x22','c':b'\x23','d':b'\x24','e':b'\x25','f':b'\x26','g':b"\x27",'h':b'\x28','i':b'\x29','j':b'\x2a','k':b'\x2b','l':b'\x2c','m':b'\x2d','n':b'\x2e','o':b'\x2f','p':b'\x31','q':b'\x32','r':b'\x33','s':b'\x34','t':b'\x35','u':b'\x36','v':b'\x37','w':b'\x38','x':b'\x39','y':b'\x3a','z':b'\x3b','A':b'\x3c','B':b'\x3d','C':b'\x3e','D':b'\x3f','E':b'\x41','F':b'\x42','G':b'\x43','H':b'\x44','I':b'\x45','J':b'\x46','K':b'\x47','L':b'\x48','M':b'\x49','N':b'\x4a','O':b'\x4b','P':b'\x4c','Q':b'\x4d','R':b'\x4e','S':b'\x4f','T':b'\x51','U':b'\x52','V':b'\x53','W':b'\x54','X':b'\x55','Y':b'\x56','Z':b'\x57','0':b'\x58','1':b'\x59','2':b'\x5a','3':b'\x5b','4':b'\x5c','5':b'\x5d','6':b'\x5e','7':b'\x5f','8':b'\x61','9':b'\x62','й':b'\x63','ё':b'\x64','ц':b'\x65','у':b'\x66','к':b'\x67','е':b'\x68','н':b'\x69','г':b'\x6a','ш':b'\x6b','щ':b'\x6c','з':b'\x6d','ф':b'\x6e','ы':b'\x6f','в':b'\x70','а':b'\x71','п':b'\x72','р':b'\x73','о':b'\x74','л':b'\x75','д':b'\x76','я':b'\x77','ч':b'\x78','с':b'\x79','м':b'\x7a','и':b'\x7b','т':b'\x7c','ь':b'\x7d','б':b'\x7e','ю':b'\x7f','ж':b'\x80','э':b'\x81','х':b'\x82','ъ':b'\x83','Й':b'\x84','Ц':b'\x85','У':b'\x86','К':b'\x87','Е':b'\x88','Н':b'\x89','Г':b'\x8a','Ш':b'\x8b','Щ':b'\x8c','З':b'\x8d','Х':b'\x8e','Ъ':b'\x8f','Ф':b'\x90','Ы':b'\x91','В':b'\x92','А':b'\x93','П':b'\x94','Р':b'\x95','О':b'\x96','Л':b'\x97','Д':b'\x98','Ж':b'\x99','Э':b'\x9a','Я':b'\x9b','Ч':b'\x9c','С':b'\x9d','М':b'\x9e','И':b'\x9f','Т':b'\xa0','Ь':b'\xa1','Б':b'\xa2','Ю':b'\xa3','№':b'\xa4','\n':'\xa5',' ':b'\xa6','':b'\xa7',
}
    
    def __init__(self) -> None:
        pass

    def __call__(self, value: str | bytes) -> str | bytes:
        if type(value) is str:
            return self.encode(value)
        elif type(value) is bytes:
            return self.decode(value)
        raise TypeError(f"In class ''coding', argument 'value' can't get {type(value)} type")

    def encode(self, value: str) -> bytes:
        result = b""
        for val in value:
            if not val in self.dictionary:
                raise ValueError(f"Value '{val}' not founded in dictionary.")
            result += self.dictionary.get(val)
        return result

    def decode(self, value: bytes) -> str:
        result = ""
        for i in range(len(value)):
            result += self.get_key_by_value(value[i])
        return result
        
    def get_key_by_value(self, val: int) -> str:
        for key, value in self.dictionary.items():
            if value == val.to_bytes(1, "little"):
                return key
        raise ValueError(f"Value '{val}' not founded in dictionary.")