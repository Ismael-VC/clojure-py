


cdef class Protocol(object):
    cdef dict _satisfies
    cdef dict _methods
    cdef str _name
    cpdef add_method(self, m)
    cpdef satisfied_by(self, tp)
    cpdef mark_satisfied(self, tp)

cdef class PolymorphicFn(object):
    cdef dict _dict
    cdef str _name
    cdef Protocol _proto
    cdef _default
    cpdef extend(self, tp, fn)
    cpdef set_default(self, f)

cdef inline satisfied_by(Protocol proto, type tp):
    return proto.satisfied_by(tp)

