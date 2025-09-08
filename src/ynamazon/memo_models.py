import abc
from typing import Any, ClassVar, override

from loguru import logger

from ynamazon.base import MultiLineText
from ynamazon.memo_utils import (
    extract_order_url,
    normalize_memo,
    remove_markdown_bold,
    remove_markdown_links,
)


class MemoBase(MultiLineText, abc.ABC):
    max_length: ClassVar[int] = 500

    _original_lines: list[str] | None = None
    _line_ending: ClassVar[str] = "\n"

    @override
    def model_post_init(self, context: Any, /) -> None:
        self._original_lines = self.lines.copy()

    def reset(self) -> None:
        if self._original_lines is not None:
            self.lines: list[str] = self._original_lines.copy()

    def __len__(self) -> int:
        """Returns the length of the memo when rendered as a string."""
        return len(self._render_lines())

    @property
    def length_exceeded_by(self) -> int:
        """Returns the number of characters by which the memo exceeds the maximum length."""
        return max(0, len(self) - self.max_length)

    def extract_order_url(self) -> str | None:
        return extract_order_url(self._render_lines())

    def _render_lines(self) -> str:
        return self._line_ending.join(self.lines)

    def remove_markdown_links(self) -> None:
        """Removes markdown links from the memo."""
        self.lines = [remove_markdown_links(line) for line in self.lines]

    def remove_markdown_bold(self) -> None:
        """Removes markdown bold formatting from the memo."""
        self.lines = [remove_markdown_bold(line) for line in self.lines]

    def remove_markdown_formatting(self) -> None:
        """Removes all markdown formatting from the memo."""
        self.remove_markdown_links()
        self.remove_markdown_bold()

    @staticmethod
    def is_item_line(line: str) -> bool:
        """Check if a line is an item line (starts with a digit and contains '. ')."""
        return line[0].isdigit() and ". " in line

    def get_item_line_indexes(self) -> list[int]:
        """Extracts indexes of item lines from the memo."""
        return [i for i, line in enumerate(self.lines) if self.is_item_line(line)]

    def get_item_lines(self) -> list[str]:
        """Extracts item lines from the memo."""
        return [line for line in self.lines if self.is_item_line(line)]

    def get_non_blank_lines(self) -> list[str]:
        """Extracts non-blank lines from the memo."""
        return [line for line in self.lines if line.strip()]

    def get_multi_order_line(self) -> str | None:
        """Extracts the multi-order line from the memo."""
        return next((line for line in self.lines if line.startswith("-This transaction")), None)

    def get_items_header(self) -> str | None:
        """Extracts the items header line from the memo."""
        return next((line for line in self.lines if line == "Items"), None)

    @abc.abstractmethod
    def truncate(self) -> None:
        """Truncates the memo to fit within the maximum length."""
        pass

    @abc.abstractmethod
    def truncate_item_lines(self) -> None:
        """Truncates item lines to fit within the maximum length."""
        pass


class StandardMemo(MemoBase):
    @override
    def truncate_item_lines(self) -> None:
        """Removes item lines until the memo fits within the maximum length."""
        exceeded_len_by = self.length_exceeded_by
        if exceeded_len_by <= 0:
            return

        item_indexes = self.get_item_line_indexes()
        if not item_indexes:
            return

        # TODO: OK, I forgot that I need to calculate how much space I'm allowed for item lines
        #       and then remove item lines until I'm within that space.

    @override
    def truncate(self) -> None:
        """Truncates the memo to fit within the maximum length."""
        current_length = len(self)
        if current_length <= self.max_length:
            return

        url_line = self.extract_order_url()

        self.remove_markdown_formatting()

        extra_length = len(self) - self.max_length
        if extra_length <= 0:
            logger.debug("Removing markdown formatting was sufficient to fit memo within limit.")
            return

        logger.debug(f"Memo exceeds max length by {extra_length} characters.")

        truncated_lines: list[str] = []
        total_length = 0
        for line in self.lines:
            line_length = len(line) + 1
