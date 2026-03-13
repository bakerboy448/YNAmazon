"""Tests for locate_amazon_transaction_by_amount with exact and fuzzy matching."""

from datetime import date
from decimal import Decimal

from pydantic import AnyUrl

from ynamazon.amazon_transactions import (
    AmazonTransactionWithOrderInfo,
    locate_amazon_transaction_by_amount,
)


def _make_transaction(total: str) -> AmazonTransactionWithOrderInfo:
    """Create a minimal AmazonTransactionWithOrderInfo for testing.

    Note: transaction_total is inverted by the field_validator,
    so passing "-26.03" results in stored value of 26.03.
    """
    return AmazonTransactionWithOrderInfo(
        completed_date=date(2026, 3, 1),
        transaction_total=Decimal(total),
        order_total=Decimal(total).copy_negate(),
        order_number="112-0000000-0000000",
        order_link=AnyUrl(
            "https://www.amazon.com/gp/your-account/order-details?orderID=112-0000000-0000000"
        ),
        items=[],
    )


class TestExactMatch:
    def test_exact_match_returns_index_and_not_fuzzy(self):
        # transaction_total of "-26.99" → stored as 26.99 after inversion
        trans = [_make_transaction("-26.99")]
        # amount_decimal from YNAB is negative (e.g. -26.99 for a $26.99 charge)
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"))
        assert idx == 0
        assert is_fuzzy is False

    def test_exact_match_first_of_multiple(self):
        trans = [
            _make_transaction("-10.00"),
            _make_transaction("-26.99"),
            _make_transaction("-50.00"),
        ]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"))
        assert idx == 1
        assert is_fuzzy is False

    def test_no_match_returns_none(self):
        trans = [_make_transaction("-26.99")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-99.99"))
        assert idx is None
        assert is_fuzzy is False

    def test_empty_list_returns_none(self):
        idx, is_fuzzy = locate_amazon_transaction_by_amount([], Decimal("-26.99"))
        assert idx is None
        assert is_fuzzy is False


class TestIndexZeroBug:
    """Regression tests for the index-0 bug where `if not 0:` was truthy."""

    def test_match_at_index_zero(self):
        trans = [_make_transaction("-26.99"), _make_transaction("-50.00")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"))
        assert idx == 0
        assert is_fuzzy is False

    def test_match_at_index_zero_with_tolerance(self):
        trans = [_make_transaction("-26.99"), _make_transaction("-50.00")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"), tolerance=2.0)
        # Should still be exact match (not fuzzy) even with tolerance enabled
        assert idx == 0
        assert is_fuzzy is False


class TestFuzzyMatch:
    def test_fuzzy_match_within_tolerance(self):
        # Amazon charged $26.03, YNAB shows $26.99 ($0.96 diff — within $2.00 tolerance)
        trans = [_make_transaction("-26.03")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"), tolerance=2.0)
        assert idx == 0
        assert is_fuzzy is True

    def test_fuzzy_match_outside_tolerance(self):
        # Amazon charged $20.00, YNAB shows $26.99 ($6.99 diff — outside $2.00 tolerance)
        trans = [_make_transaction("-20.00")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"), tolerance=2.0)
        assert idx is None
        assert is_fuzzy is False

    def test_fuzzy_picks_closest(self):
        # Multiple candidates within tolerance — should pick closest
        trans = [
            _make_transaction("-25.00"),  # diff = 1.99
            _make_transaction("-26.50"),  # diff = 0.49 (closest)
            _make_transaction("-28.00"),  # diff = 1.01
        ]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"), tolerance=2.0)
        assert idx == 1
        assert is_fuzzy is True

    def test_exact_match_preferred_over_fuzzy(self):
        # If exact match exists, it should win even with tolerance enabled
        trans = [
            _make_transaction("-26.50"),  # fuzzy candidate
            _make_transaction("-26.99"),  # exact match
        ]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"), tolerance=2.0)
        assert idx == 1
        assert is_fuzzy is False

    def test_fuzzy_at_exact_tolerance_boundary(self):
        # Diff is exactly $2.00 — should be included (<=)
        trans = [_make_transaction("-25.00")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-27.00"), tolerance=2.0)
        assert idx == 0
        assert is_fuzzy is True

    def test_fuzzy_just_over_tolerance(self):
        # Diff is $2.01 — should NOT match
        trans = [_make_transaction("-24.99")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-27.00"), tolerance=2.0)
        assert idx is None
        assert is_fuzzy is False

    def test_zero_tolerance_disables_fuzzy(self):
        trans = [_make_transaction("-26.03")]
        idx, is_fuzzy = locate_amazon_transaction_by_amount(trans, Decimal("-26.99"), tolerance=0.0)
        assert idx is None
        assert is_fuzzy is False
