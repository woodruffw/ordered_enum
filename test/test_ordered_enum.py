import enum

import pytest

from ordered_enum import OrderedEnum, ValueOrderedEnum


def test_is_enum():
    class X(OrderedEnum):
        Foo = 1

    class Y(ValueOrderedEnum):
        Foo = 1

    assert issubclass(X, enum.Enum)
    assert issubclass(Y, enum.Enum)


def test_total_ordering():
    class X(OrderedEnum):
        Foo = 3
        Bar = 2
        Baz = 1

    @enum.unique
    class Y(ValueOrderedEnum):
        Foo = 1
        Bar = 2
        Baz = 3

    for member in X:
        assert member == member

    assert X.Baz > X.Bar > X.Foo
    assert X.Baz >= X.Bar >= X.Foo
    assert X.Foo < X.Bar < X.Baz
    assert X.Foo <= X.Bar <= X.Baz
    assert X.Foo != X.Bar and X.Bar != X.Baz and X.Foo != X.Baz

    for member in Y:
        assert member == member

    assert Y.Baz > Y.Bar > Y.Foo
    assert Y.Baz >= Y.Bar >= Y.Foo
    assert Y.Foo < Y.Bar < Y.Baz
    assert Y.Foo <= Y.Bar <= Y.Baz
    assert Y.Foo != Y.Bar and Y.Bar != Y.Baz and Y.Foo != Y.Baz


def test_total_ordering_typesafe():
    class X(OrderedEnum):
        Foo = "a"
        Bar = "b"
        Baz = "c"

    with pytest.raises(TypeError):
        "a" < X.Baz

    @enum.unique
    class Y(ValueOrderedEnum):
        Foo = "a"
        Bar = "b"
        Baz = "c"

    with pytest.raises(TypeError):
        "a" < Y.Baz


def test_total_value_ordering_unsound():
    class X(ValueOrderedEnum):
        Foo = 1
        Bar = 1
        Baz = 2

    assert not (X.Foo < X.Bar)
    assert not (X.Foo > X.Bar)
