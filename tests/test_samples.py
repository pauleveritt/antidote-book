"""Test each of the sections in the book.

The book is organized into sections which point at the working
code in the package. The working code "exports" a function that
the tests standardize on."""
import pytest

from antidote_book import manual_injection


@pytest.mark.parametrize(
    'target',
    [
        manual_injection
    ]
)
def test_each_sample(target):
    """Get the test function, run it, ensure results match."""
    test_function = getattr(target, 'test')
    actual, expected = test_function()
    assert actual == expected
