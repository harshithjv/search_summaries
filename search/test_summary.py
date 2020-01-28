from .summary import getSummaries, search_summaries

def test_getSummaries():
  summaries = getSummaries()
  assert type(summaries) == list

def test_search_summaries():
  (results, count) = search_summaries("Book of", 2)
  assert type(results) == list and count == 2 
