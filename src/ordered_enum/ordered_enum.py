import functools
from enum import Enum


@functools.total_ordering
class OrderedEnum(Enum):
    @classmethod
    @functools.lru_cache(None)
    def _member_list(cls):
        return list(cls)

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            member_list = self.__class__._member_list()
            return member_list.index(self) < member_list.index(other)
        return NotImplemented


@functools.total_ordering
class ValueOrderedEnum(Enum):
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
