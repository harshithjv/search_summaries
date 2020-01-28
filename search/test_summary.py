from .summary import getSummaries, search_summaries

def test_getSummaries():
  summaries = getSummaries()
  if type(summaries) == list:
    assert True
  else:
    assert False

def test_search_summaries():
  (results, count) = search_summaries("Book of", 2)
  if type(results) == list and count == 2:
    assert True
  else:
    assert False