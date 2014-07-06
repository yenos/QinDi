QinDi
=====

Quick n' Dirty scripts Repositories

=====
# List

## mtgx2text (Python)

### What are you doing?
Script to extract the value of domains, subdomains and IPv4 adresses entities from a Paterva Casefile (*.mtgx) file. The output is stdout and a txt file.

### What's may come next?
- More supported entities
- Modularize the thing
- Better arguments and options handling
- Output in a database
- Snort rules as output

### Usage
$ python3 mtgx2txt.py [casefile file]

### Example 
$ python3 mtgx2txt.py example.mtgx
> [IP] 74.207.243.1 <br />
> [IP] 74.207.243.2 <br />
> [IP] 74.207.243.3 <br />
> [IP] 74.207.243.4 <br />
> [DO] domaine.com <br />
> [SD] sub.domaine.com <br />
>  <br />
> result-example-mtgx.txt successfully created! <br /> 
