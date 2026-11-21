from typing import Any, Iterator, TypeVar, Generic, Self
 
# restrict generic type T to only accept given types
T = TypeVar('T', str, int, 'Collection[int]', 'Collection[str]')
 
class Collection(Generic[T]):
    """
    Generic collection class of type T with basic collection operations.
    See: https://sgra64.github.io/py-fun.github.io/src.collections.html.
    """
 
    def __init__(self, *args, asSet=False):
        """
        Constructor of a Collection.
 
        Args:
            args: elements added to the Collection including
            number or string literals, sets and lists.
        """
        self._items = set() if asSet else list()
        for arg in args:
            self.add(arg)
 
    def _norm(self, item):
        """Normalise an item the same way add() stores it."""
        item = item if not isinstance(item, set | dict) else frozenset(item)
        if isinstance(self._items, set) and isinstance(item, list):
            item = tuple(item)
        return item
 
    def add(self, item: T) -> Self:
        """
        Add an element of type T to the collection.
 
        Args:
            item: element to add to the collection.
 
        Returns:
            Chainable self-reference to the collection with the element added.
        """
        item = item if not isinstance(item, set | dict) else frozenset(item)
        if isinstance(self._items, list):
            self._items.append(item)
        else:
            # list cannot be added to a set since lists are mutable and therefore unhashable.
            self._items.add(item if not isinstance(item, list) else tuple(item))
        return self
 
    def contains(self, item: Any) -> bool:
        """
        Test that an item or subset exists in the collection.
 
        Args:
            item: element to test that it is in the collection.
 
        Returns:
            True if element is in the collection, False otherwise.
        """
        try:
            return self._norm(item) in self._items
        except TypeError:   # unhashable item cannot be in a set
            return False
 
    def size(self) -> int:
        """
        Returns the number of items in the collection.
 
        Returns:
            the number of items in the collection.
        """
        return len(self._items)
 
    @classmethod
    def zip(cls, l1: 'Collection[list]', l2: 'Collection[list]') -> 'Collection[tuple]':
        """
        Return a new collection of two-item tuples zipped from the input collections.
 
        Args:
            c1: input Collection from which the left element is taken.
            c2: input Collection from which the right element is taken
 
        Returns:
            Collection of pairs zipped from each input Collection.
        """
        result = cls()
        for left, right in zip(l1, l2):
            result.add((left, right))
        return result
 
    def _unique_items(self) -> list:
        """Distinct values in first-seen order (equality based, lists become tuples)."""
        unique = []
        for item in self._items:
            item = tuple(item) if isinstance(item, list) else item
            if item not in unique:
                unique.append(item)
        return unique
 
    def pset(self) -> list[set[T]]:
        """
        Return the power set of this Collection using backtracking.
 
        Duplicate values are ignored. Sets cannot contain mutable sets, hence
        the power set is returned as a list of sets.
 
        Returns:
            The power set of this Collection.
        """
        return list(self.pset_gen())
 
    def pset_gen(self) -> Iterator['set[T]']:
        """
        Generator that yields each subset using backtracking.
 
        Returns:
            Generator object for the power set of this Collection.
        """
        items = self._unique_items()
 
        def backtrack(i: int, current: list):
            if i == len(items):
                yield set(current)              # leaf: one decision per item taken
                return
            yield from backtrack(i + 1, current)    # item i excluded
            current.append(items[i])                # item i included (choose)
            yield from backtrack(i + 1, current)
            current.pop()                           # un-choose (backtrack)
 
        return backtrack(0, [])
 
    def perm(self) -> list[list[T]]:
        """
        Return all permutations of this Collection.
 
        Permutations are taken over item positions, so equal items at different
        positions yield distinct (but equal-looking) permutations.
 
        Returns:
            The list of permutations of this Collection.
        """
        return list(self.perm_gen())
 
    def perm_gen(self) -> Iterator[list[T]]:
        """
        Generator that yields permutations using backtracking.
 
        Returns:
            Generator object for the list of permutations of this Collection.
        """
        items = list(self._items)
        used = [False] * len(items)
        current = []
 
        def backtrack():
            if len(current) == len(items):
                yield list(current)             # copy: 'current' keeps changing
                return
            for i in range(len(items)):
                if used[i]:
                    continue
                used[i] = True                  # choose item at position i
                current.append(items[i])
                yield from backtrack()
                current.pop()                   # un-choose (backtrack)
                used[i] = False
 
        return backtrack()
 
    def __contains__(self, item: Any) -> bool:
        """Checks if an item or subset exists in the collection (in-operator)."""
        return item in self._items
 
    def __len__(self) -> int:
        """Returns the number of items in the collection, invoked by len()."""
        return len(self._items)
 
    def __iter__(self) -> Iterator[Any]:
        """Returns an iterator over the items in the collection, invoked in loops."""
        return iter(self._items)
 
    def __repr__(self):
        """Custom representation for str() that formats inner frozenSets as { }."""
        elements = []
        for item in self._items:
            if isinstance(item, set | frozenset):
                elements.append(f"{{{", ".join(repr(e) for e in item)}}}")
            else:
                elements.append(repr(item))
        # 
        r = f"{', '.join(elements)}"
        return f"[{r}]" if isinstance(self._items, list) else f"{{{r}}}"
 
