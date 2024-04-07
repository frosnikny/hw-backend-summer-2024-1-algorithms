from queue import LifoQueue, Queue
from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        stack = LifoQueue()
        stack.put(self._root)
        lst = []
        while not stack.empty():
            a = stack.get()
            if a not in lst:
                lst.append(a)
                for i in reversed(a.outbound):
                    stack.put(i)
        return lst

    def bfs(self) -> list[Node]:
        queue = Queue()
        queue.put(self._root)
        lst = []
        while not queue.empty():
            a = queue.get()
            if a not in lst:
                lst.append(a)
                for i in a.outbound:
                    queue.put(i)
        return lst
