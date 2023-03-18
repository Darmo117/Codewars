import math


class PaginationHelper:
    def __init__(self, collection: list, items_per_page: int):
        self._items = collection
        self._items_per_page = items_per_page

    def item_count(self) -> int:
        return len(self._items)

    def page_count(self) -> int:
        return math.ceil(self.item_count() / self._items_per_page)

    def page_item_count(self, page_index: int) -> int:
        start_i = page_index * self._items_per_page
        if start_i < 0 or start_i > self.item_count():
            return -1
        end_i = min((page_index + 1) * self._items_per_page, self.item_count())
        return end_i - start_i

    def page_index(self, item_index: int) -> int:
        if item_index < 0 or item_index >= self.item_count():
            return -1
        return item_index // self._items_per_page
