

# Dataset Usage

## Downloading the Database

Download the compressed `dataset.ttl.bz2` file.

The compressed file *can* be used as is, but the load times seem to be slower compared to using an unzipped version.

Uncompress the `bzip2`-file.

```
bzip2 -dk dataset.ttl.bz2
```

## Reading the Database

There are multiple ways to use the unpacked RDF/TTL file. Loading the database into memory as a whole is possible and provides the fastest access, but also reserves the most resources.

For this reason, it is recommended to use a separate service to provide SPARQL access through a local network.

### Reading Manually

The `.ttl` file is now in plain text format that can be read directly with e.g. `less`. The data stored is in TTL (RDF) triple format and looks like the following.

```
@prefix wiki: <https://fi.wikipedia.org/?curid=> .
@prefix wsd: <https://example.com/> .

wiki:1000 wsd:ambiguous "PSP"@fi ;
    wsd:conllu """# text = Alun perin ohjelmaa julkaisi vuoteen 2004 asti Yhdysvaltojen Minneapolisissa sijaitseva yritys, Jasc Software.
1	Alun	alun	ADV	Adv	NER=O	4	advmod	_	_
2	perin	perin	ADV	Adv	NER=O	1	fixed	_	_
3	ohjelmaa	ohjelma	NOUN	N	Case=Par|Number=Sing|NER=O	4	obj	_	_
4	julkaisi	julkaista	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Act|NER=O	0	root	_	_
5	vuoteen	vuosi	NOUN	N	Case=Ill|Number=Sing|NER=DATE	4	obl	_	_
6	2004	2004	NUM	Num	NumType=Card|NER=DATE	5	nummod	_	_
7	asti	asti	ADP	Adp	AdpType=Post|NER=O	5	case	_	_
8	Yhdysvaltojen	Yhdysvallat	PROPN	N	Case=Gen|Number=Plur|NER=GPE	9	nmod:poss	_	_
9	Minneapolisissa	minneapolinen	PROPN	A	Case=Ine|Degree=Pos|Derivation=Inen|Number=Sing|NER=GPE	10	obl	_	_
10	sijaitseva	sijaita	VERB	V	Case=Nom|Degree=Pos|Number=Sing|PartForm=Pres|VerbForm=Part|Voice=Act|NER=O	11	acl	_	_
11	yritys	yritys	NOUN	N	Case=Nom|Number=Sing|NER=O	4	nsubj	_	SpaceAfter=No
12	,	,	PUNCT	Punct	NER=O	13	punct	_	_
13	Jasc	Jasc	PROPN	N	Case=Nom|Number=Sing|NER=ORG	11	appos	_	_
14	Software	Software	X	Foreign	Foreign=Yes|NER=ORG	13	flat:name	_	SpaceAfter=No
15	.	.	PUNCT	Punct	NER=O	4	punct	_	_

"""@fi,
        """# text = X4:ään sisältyy myös laaja versio Nik Color Efex Pron kuvanparannus- ja efektityökaluista.
1	X4:ään	X4	NUM	Num	Case=Ill|Number=Sing|NumType=Card|NER=PRODUCT	2	obl	_	_
2	sisältyy	sisältyä	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act|NER=O	0	root	_	_
3	myös	myös	ADV	Adv	NER=O	5	advmod	_	_
4	laaja	laaja	ADJ	A	Case=Nom|Degree=Pos|Number=Sing|NER=O	5	amod	_	_
5	versio	versio	NOUN	N	Case=Nom|Number=Sing|NER=O	2	nsubj	_	_
6	Nik	Nik	PROPN	N	Case=Nom|Number=Sing|NER=PRODUCT	10	nmod:poss	_	_
7	Color	Color	PROPN	N	Case=Nom|Number=Sing|NER=PRODUCT	6	flat:name	_	_
8	Efex	Efex	PROPN	N	Case=Nom|Number=Sing|NER=PRODUCT	6	flat:name	_	_
9	Pron	Pro	PROPN	N	Case=Gen|Number=Sing|NER=PRODUCT	6	flat:name	_	_
10	kuvanparannus-	kuvan#parannus	NOUN	N	Case=Nom|Number=Sing|NER=O	5	nmod	_	_
11	ja	ja	CCONJ	C	NER=O	12	cc	_	_
12	efektityökaluista	efekti#työ#kalu	NOUN	N	Case=Ela|Number=Plur|NER=O	10	conj	_	SpaceAfter=No
13	.	.	PUNCT	Punct	NER=O	2	punct	_	_

"""@fi ;
    wsd:disambiguous "PaintShop Pro"@fi .
```

### Using Apache Jena Fuseki

We used the database through [Apache Jena Fuseki SPARQL server](https://jena.apache.org/documentation/fuseki2/).

Install the software and run 

```
fuseki-server --file dataset.ttl /wsd
```

to start the server. The example command uses loads the database file into a database called `wsd`. A GUI for exploring the database can be accessed via `http://localhost:3030/#/`.

### Usage with Python


There are multiple approaches for submitting queries to an RDF database with Python. Using [rdflib](https://rdflib.readthedocs.io/en/stable/) is one possibility. However, we ended up using the package [SPARQLWrapper](https://github.com/RDFLib/sparqlwrapper) directly.

Note that one should also install [conllu](https://pypi.org/project/conllu/)-package for Python to parse the CoNLL-U formatted data from the database.

Example Python script is provided in the `examples` directory. Examples are tested with Python version 3.10.5.
