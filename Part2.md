# Write an API to find books
##### Code  - 45 min

We need to make that functionality available remotely as a service, so users can find coursebook summaries anywhere in the world.

Assuming you are given summaries of all books, 
use the previously built search engine to offer an API that given a `list` of queries and an integer `K`, 
it will return the top K matched book as list, for every query in the list, so the result will be a list of lists.

    Egs input: [query1, query2]
        results: [[book1 ... bookK], [book1 .... bookK]]

If you did not manage to complete the previous exercise use a mock of the search API instead.

A `book` object is defined as follows: 
```
{ id: “string”, author: “string”, summary: “string”, query: “string”} 
```
The information about the book author is provided by another 
microservice which you can call `https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding`. The api accepts POST
`application/json` content as such `{'book_id: integer}` and return the book author `{'author': string}`. (NOTE: `book_id` here is the same as `id` in summaries list)

Keep in mind that the list of queries can be large or that K can be a big integer.

Write the code using engineering best practices. Use the framework of your choice to serve that endpoint
