ordered_enum
============

**ordered_enum** is a small class for adding (total) orderings to `enum.Enum`s.

## Installation

**ordered_enum** requires Python 3.6 or newer.

```bash
pip3 install ordered_enum
```

## Usage

To use **ordered_enum**, just use `OrderedEnum` as your parent class:

```python
from ordered_enum import OrderedEnum


class State(OrderedEnum):
    Disabled = 0
    Loaded = 1
    Waiting = 2
    Running = 3
    Dead = 4


assert(State.Disabled < State.Loaded)
assert(sorted([State.Dead, State.Waiting]) == [State.Waiting, State.Dead])
```

**ordered_enum** doesn't require `@enum.unique` (or unique values at all); it uses the order of
definition to impose an ordering between members.

## Caveats

As mentioned above, **ordered_enum** provides an ordering of enum values based on their order
of definition in the class. This means that:

1. Enum values doesn't have to be unique for **ordered_enum** to work
2. Moving enum values around changes their ordering

Therefore, you should either not depend on a specific ordering **or** ensure that your
order of definition is the order you'd like.
