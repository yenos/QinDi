QinDi
=====

Quick n' Dirty scripts Repositories
- mtgx2txt: extract domains, subdomains and IP from a Paterva Casefile file (*.mtgx)
- ioc2txt: extract IP and domains from a Mandiant IOC file (*.ioc)

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

## ioc2txt (Python)

### What are you doing?
Script to extract the value of domainsand IPv4 in Mandiant IOC (*.ioc) file. The output is stdout and a txt file.

### What's may come next?
- Better arguments and options handling
- Output in a database
- Snort rules as output

### Usage
$ python3 ioc2txt.py [ioc file]

### Example 
$ python3 ioc2txt.py Alienvault-RedOctober.ioc
> [IP] 141.101.239.225 <br />
> [IP] 178.162.129.237 <br />
> [IP] 178.162.182.42 <br />
> [IP] 178.63.208.49 <br />
> [... troncated ...] <br />
> [DO] winupdateos.com<br />
> [DO] world-mobile-congress.com<br />
> [DO] xponlineupdate.com<br />
>  <br />
> result-Alienvault-RedOctober-ioc.txt seccessfully created! 
