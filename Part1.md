Unibuddy wants to build a service that allows students to search through coursebooks summaries which would make picking 
and buying a coursebook a much better experience for students.

First we need to develop a local version of the system and evaluate it. 
Our bot scraped a website with book summaries, and stored them in `data.json` in the `summaries` array. The summaries 
array is a small data example for local development. You should assume that the real service will have 100's of thousands of summaries.
   
Your goal is to code a search engine that given a search query, searches the book summaries and returns the `K` most relevant ones.
A search engine query is the set of keywords that users will type in order to find a relevant document.
You are allowed to use only basic language functionality.

The api of the search engine should be as follows:

    Input: The input should be a user query of type string
           Query example: 'Computer Science'
    Output: List of K relevant summaries. 
            A summary is a dictionary that follows the schema: {'summary': string, 'id': integer}
            Summary example:  {'summary':'Computer Science introduction coursebook', 'id':10}          
            Ouput example: [summary1, summary2, ..... summaryK] Where summaries are sorted according to order of relevance given a query
