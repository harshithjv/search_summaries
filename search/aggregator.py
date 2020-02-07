"""
aggregator.py
"""

from .summary import search_summaries

# Below will variable and get_author func is dummy as there is
# no API to fetch actual data. Only adding reference/pseudo
# code for the problem statement.
book_author_ids = {}


def get_author_from_api(id=None):
    """
    TODO: Function description
    """
    return ''


def get_author(id=None):
    """
    TODO: Function description
    """
    author = ''
    try:
        author = book_author_ids[id]
    except KeyError:
        book_author_ids[id] = get_author_from_api(id)
    return author


def multi_search(search_strings, k):
    """
    TODO: Function description
    """
    results = []
    total_count = 0
    for search_string in search_strings:
        (subresults, count) = search_summaries(search_string, k)
        for sresult in subresults:
            sresult["author"] = get_author(sresult['id'])
            sresult["query"] = search_string
        results.append(subresults)
        total_count += count
    return (results, total_count)
