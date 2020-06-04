ordered_enum
============

![license](https://raster.shields.io/badge/license-MIT%20with%20restrictions-green.png)
[![Build Status](https://img.shields.io/github/workflow/status/woodruffw/ordered_enum/CI/master)](https://github.com/woodruffw/ordered_enum/actions?query=workflow%3ACI)

**ordered_enum** is a small library for adding (total) orderings to `enum.Enum`s.

It provides two ordering behaviors:

* `ordered_enum.OrderedEnum`: total ordering by definition
* `ordered_enum.ValueOrderedEnum`: "total" ordering by member values

## Installation

**ordered_enum** requires Python 3.6 or newer.

```bash
pip3 install ordered_enum
```

## Usage

To use **ordered_enum**, just use `OrderedEnum` or `ValueOrderedEnum` as your parent class:

```python
from ordered_enum import OrderedEnum


class State(OrderedEnum):
    Disabled = 4
    Loaded = 3
    Waiting = 2
    Running = 1
    Dead = 0


assert(State.Disabled < State.Loaded)
assert(sorted([State.Dead, State.Waiting]) == [State.Waiting, State.Dead])
```

`OrderedEnum` doesn't require `@enum.unique` (or unique values at all); it uses the order of
definition to impose an ordering between members.

If you'd like to impose an ordering based on member values, you can use `ValueOrderedEnum` instead:

```python
import enum
from ordered_enum import ValueOrderedEnum


@enum.unique
class State(ValueOrderedEnum):
    Disabled = 4
    Loaded = 3
    Waiting = 2
    Running = 1
    Dead = 0


assert(State.Disabled > State.Loaded)
assert(sorted([State.Waiting, State.Dead]) == [State.Dead, State.Waiting])
```

`ValueOrderedEnum` **does** require unique values, which can be enforced via `@enum.unique`.
Failing to make a `ValueOrderedEnum`'s values unique will result in a silently broken ordering.

## Caveats

As mentioned above, `ordered_enum.OrderedEnum` provides an ordering of enum values based on their order
of definition in the class. This means that:

1. Enum values doesn't have to be unique for **ordered_enum** to work
2. Enum values can be heterogeneously typed
2. Moving enum values around changes their ordering

Therefore, you should either not depend on a specific ordering **or** ensure that your
order of definition is the order you'd like.
