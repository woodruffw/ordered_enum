import functools
from enum import Enum


@functools.total_ordering
class OrderedEnum(Enum):
    @classmethod
    @functools.lru_cache(None)
    def _member_list(cls):
        return list(cls)

    def __lt__(self, other):
        member_list = self.__class__._member_list()
        return member_list.index(self) < member_list.index(other)
