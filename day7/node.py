import typing
from abc import ABC, abstractclassmethod


class Node(ABC):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    @property
    @abstractclassmethod
    def size(self) -> int:
        pass

    @property
    @abstractclassmethod
    def children(self) -> typing.List['Node']:
        pass

    @abstractclassmethod
    def add_child(self, child: 'Node'):
        pass

    def get_named_child(self, child_name: str) -> typing.Optional['Node']:
        matching = [
            child for child in self.children if child.name == child_name]

        return matching[0] if matching else None


class FileNode(Node):
    _size: int

    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self._size = size

    @property
    def size(self) -> int:
        return self._size

    @property
    def children(self):
        return []

    def add_child(self, child: 'Node'):
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f'{self.name} ({self.size})'

    def __str__(self) -> str:
        return self.__str__()


class DirectoryNode(Node):
    _children: typing.List[Node]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children = []

    @property
    def size(self) -> int:
        return sum([child.size for child in self._children])

    @property
    def children(self) -> typing.List[Node]:
        return [*self._children]

    def add_child(self, child: Node):
        if self.get_named_child(child.name):
            raise Exception('File already exists.')

        self._children.append(child)

    def __repr__(self) -> str:
        return f'{self.name} ({self.size}) ({len(self.children)})'

    def __str__(self) -> str:
        return self.__str__()
