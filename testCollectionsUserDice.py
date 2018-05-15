from collections import UserDict
#https://segmentfault.com/a/1190000007757806
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key,item):
        self.data[str(key)]=item