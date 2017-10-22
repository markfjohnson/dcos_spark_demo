import elasticsearch

elastic_url = 'coordinator-0-node.elastic.autoip.dcos.thisdcos.directory'
elastic_url = 'localhost'
elastic_port = 1025

print('Connecting to Elastic Search url={}, port={}'.format(elastic_url,elastic_port))
es = elasticsearch.Elasticsearch([{'host':elastic_url,'port':elastic_port}])
es.index(index='posts', doc_type='blog', id=1, body={
    'author': 'Santa Clause',
    'blog': 'Slave Based Shippers of the North',
    'title': 'Using Celery for distributing gift dispatch',
    'topics': ['slave labor', 'elves', 'python',
               'celery', 'antigravity reindeer'],
    'awesomeness': 0.2
})