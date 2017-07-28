# vivo-hackathon
UMD Libraries VIVO Hackathon Scripts

## vivoquery and vivoload scripts

These are wrappers around VIVO SPARQL query and update endpoints.

```
# set your VIVO server URL, root email, and password
export VIVO_SERVER=http://...
export VIVO_EMAIL=...
export VIVO_PASSWORD=...

# upload some triples stored in 1 or more files
# files must be in N-Triples format
./vivoload data.nt moredata.nt

# default query gets 10 triples
./vivoquery

# pass in a SPARQL query as the first argument
./vivoquery "SELECT ?o WHERE { ?s <http://purl.org/dc/terms/title> ?o }"

# add additional curl options after the query
# e.g., select a different response type
./vivoquery "SELECT ?o WHERE { ?s <http://purl.org/dc/terms/title> ?o }" \
    -H "Accept: text/csv"

# use an empty query to use the default query with extra curl options
./vivoquery "" -H "Accept: text/csv"
```
