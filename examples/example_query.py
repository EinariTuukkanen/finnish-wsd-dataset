import collections

import conllu
from SPARQLWrapper import SPARQLWrapper, JSON


db = SPARQLWrapper("http://localhost:3030/wsd/query")
db.setReturnFormat(JSON)

prefix = """
    PREFIX wiki: <https://fi.wikipedia.org/?curid=> 
    PREFIX wsd: <https://example.com/>
"""


def run_query(query: str) -> dict:
    db.setQuery(f"{prefix}\n{query}")
    return db.query().convert()["results"]["bindings"]


def sanitize_sparql(text: str) -> str:
    return text.replace('"', r"\"")


"""
Example: Get senses by ambiguous word
"""


def get_glossary_by_ambiguous_word(word: str) -> list:
    """Returns mapping with senses as the keys and sense definitions as the values"""
    query = f"""
        SELECT ?id ?dis ?conllu
        WHERE {{
            ?id wsd:ambiguous    "{sanitize_sparql(word)}"@fi ;
                wsd:conllu    	 ?conllu ;
                wsd:disambiguous ?dis .
        }}
    """
    bindings = run_query(query)

    senses = collections.defaultdict(list)
    for b in bindings:
        # Also possible to first join the strings and then parse
        senses[b["dis"]["value"]].append(conllu.parse(b["conllu"]["value"])[0])

    return senses


ambiguous_word = "Finlandia"
glossary = get_glossary_by_ambiguous_word(ambiguous_word)
print(f"Sense options for {ambiguous_word}: {', '.join(glossary.keys())}")

"""
Example: Get CoNLL-U's by disambiguous word 
"""


def get_conllus_by_disambiguous_word(word: str) -> list:
    query = f"""
        SELECT ?id ?dis ?conllu
        WHERE {{
            ?id wsd:disambiguous    "{sanitize_sparql(word)}"@fi ;
                wsd:conllu    	 ?conllu .
        }}
    """
    bindings = run_query(query)

    # Also possible to first join the strings and then parse
    return [conllu.parse(b["conllu"]["value"])[0] for b in bindings]


disambiguous_word = "Finlandia (makeinen)"
conllus = get_conllus_by_disambiguous_word(disambiguous_word)

# Print the list of tokenlists
print(conllus)

# Print the first tokenlist
sentence = conllus[0]
print(sentence)

# Print the first token
token = sentence[0]
print(token.items())

# Print the POS and NER tags
print(f"POS: {token['upos']}, NER: {token['feats']['NER']}")
