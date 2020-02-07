"""
Test script for summary.py
"""

from .summary import get_summaries, search_summaries


def test_get_summaries():
    """
    TODO: Function description
    """
    summaries = get_summaries()
    assert isinstance(summaries, list)


def test_search_summaries():
    """
    TODO: Function description
    """
    (results, count) = search_summaries("Book of", 2)
    assert isinstance(results, list) and count == 2
