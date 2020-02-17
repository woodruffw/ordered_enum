import enum

from ordered_enum import OrderedEnum


def test_is_enum():
    class X(OrderedEnum):
        Foo = 1

    assert issubclass(X, enum.Enum)


def test_total_ordering():
    class X(OrderedEnum):
        Foo = 3
        Bar = 2
        Baz = 1

    for member in X:
        assert member == member

    assert X.Baz > X.Bar > X.Foo
    assert X.Baz >= X.Bar >= X.Foo
    assert X.Foo < X.Bar < X.Baz
    assert X.Foo <= X.Bar <= X.Baz
    assert X.Foo != X.Bar and X.Bar != X.Baz and X.Foo != X.Baz
