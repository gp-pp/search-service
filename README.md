Run the following commands to after cloning the repository:

1. ```docker-compose build```
2. ```docker-compose up```


The active endpoints are at ports 7700 and 3003:

> - localhost:7700/
> - localhost/3003/profiles
> - localhost/3003/papers

Send search queries using query parameters, for example:

> localhost/3003/profiles?q=something
> localhost/3003/papers?q=something
It will query the results with prof. Debdeep Mukhopadhyay at the top.
