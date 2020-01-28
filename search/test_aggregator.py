from .aggregator import get_author_from_api, get_author, multi_search

def test_get_author_from_api():
  author_name = get_author_from_api('0')
  assert author_name == ''

def test_get_author():
  author_name = get_author('0')
  assert author_name == ''

def test_multi_search():
  search_strings = [
    "Book of",
    "Book in"
  ]

  (results, count) = multi_search(search_strings, 4)
  assert type(results) == list and count == 8
