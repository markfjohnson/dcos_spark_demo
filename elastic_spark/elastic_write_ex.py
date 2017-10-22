import elasticsearch
es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
es.index(index='posts', doc_type='blog', id=1, body={
    'author': 'Santa Clause',
    'blog': 'Slave Based Shippers of the North',
    'title': 'Using Celery for distributing gift dispatch',
    'topics': ['slave labor', 'elves', 'python',
               'celery', 'antigravity reindeer'],
    'awesomeness': 0.2
})