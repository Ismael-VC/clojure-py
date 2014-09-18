

cdef class PolymorphicFn(object):

    def __init__(self, Protocol proto, str name):
        self._name = name
        self._dict = {}
        self._proto = proto
        self._proto.add_method(self)
        self._default = self.__default_fn

    def __default_fn(self, *args):
        raise NotImplemented("method " + self._name + " not implemented for " + str(type(args[0])))

    cpdef extend(self, tp, f):
        self._dict[tp] = f
        self._proto.mark_satisfied(tp)


    def __call__(self, *args):
        return self._dict[type(args[0])](*args)

    cpdef set_default(self, f):
        self._default = f

cdef class Protocol(object):

    def __init__(self, name):
        self._name = name
        self._methods = {}
        self._satisfies = {}

    cpdef add_method(self, m):
        self._methods[m] = m

    cpdef satisfied_by(self, tp):
        return tp in self._satisfies

    cpdef mark_satisfied(self, tp):
        self._satisfies[tp] = tp


def extend(PolymorphicFn f, type tp):
    def extend_run(ef):
        f.extend(tp, ef)
        return f
    return extend_run