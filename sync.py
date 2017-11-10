import pynipap
from pynipap import Prefix
a = pynipap.AuthOptions({
    'authoritative_source': 'NIPAP-Sync/1.0'
})
pynipap.xmlrpc_uri = "{nipapurl}"

query = {
    'operator': 'equals',
    'val1': 'type',
    'val2': 'host'
}

search_options = {
    'max_result': 1000
}

search_result = Prefix.search(query, search_options)

file = open("/tmp/nipap.hosts", "w")

for p in search_result['result']:
    ip = p.prefix.split('/')[0]
    host = p.description.replace(" ", "_")
    file.write(ip + " " + host + "\n")

file.close()
