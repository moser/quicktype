from dataclasses import dataclass
from typing import Any, Union, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Foo:
    name: str
    size: float

    @staticmethod
    def from_dict(obj: Any) -> 'Foo':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        size = from_float(obj.get("size"))
        return Foo(name, size)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["size"] = to_float(self.size)
        return result


@dataclass
class Bar:
    address: str
    size: str

    @staticmethod
    def from_dict(obj: Any) -> 'Bar':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        size = from_str(obj.get("size"))
        return Bar(address, size)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["size"] = from_str(self.size)
        return result


@dataclass
class Baz:
    foo_or_bar: Union[Foo, Bar]

    @staticmethod
    def from_dict(obj: Any) -> 'Baz':
        assert isinstance(obj, dict)
        foo_or_bar = from_union([Foo.from_dict, Bar.from_dict], obj.get("fooOrBar"))
        return Baz(foo_or_bar)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fooOrBar"] = from_union([lambda x: to_class(Foo, x), lambda x: to_class(Bar, x)], self.foo_or_bar)
        return result


def foo_from_dict(s: Any) -> Foo:
    return Foo.from_dict(s)


def foo_to_dict(x: Foo) -> Any:
    return to_class(Foo, x)


def bar_from_dict(s: Any) -> Bar:
    return Bar.from_dict(s)


def bar_to_dict(x: Bar) -> Any:
    return to_class(Bar, x)


def baz_from_dict(s: Any) -> Baz:
    return Baz.from_dict(s)


def baz_to_dict(x: Baz) -> Any:
    return to_class(Baz, x)
