from .aggregator import get_author_from_api, get_author, multi_search

def test_get_author_from_api():
  author_name = get_author_from_api('0')
  if author_name == '':
    assert True
  else:
    assert False

def test_get_author():
  author_name = get_author('0')
  if author_name == '':
    assert True
  else:
    assert False

def test_multi_search():
  search_strings = [
    "Book of",
    "Book in"
  ]

  (results, count) = multi_search(search_strings, 4)
  if type(results) == list and count == 8:
    assert True
  else:
    assert False
