class WrapMe(object):
    def __init__(self,obj):
        self.__data=obj

    def get(self):
        return self.__data

    def __repr__(self):
        return repr('self.__data')

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data,attr)

# wrappedComplex=WrapMe(3.5+4.2j)
# print (wrappedComplex)
# print (wrappedComplex.imag)
# print (wrappedComplex.real)
# print (wrappedComplex.conjugate())
# print (wrappedComplex.get())

wrappedList=WrapMe([123,'foo',45.67])
print(wrappedList.append('bar'))