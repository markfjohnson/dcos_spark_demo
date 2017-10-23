from cassandra.cluster import Cluster
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql import SparkSession

cassandra_url = 'node.cassandra.l4lb.thisdcos.directory'
#cassandra_url = 'localhost'

spark = SparkSession.builder \
    .appName("PySpark Cassandra Read Write Example") \
    .config("spark.sql.crossJoin.enabled", "true") \
    .getOrCreate()


cluster = Cluster([cassandra_url])
session = cluster.connect()

session.execute("""CREATE KEYSPACE IF NOT EXISTS dcos_example WITH 
    REPLICATION = { \'class\' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }; """)

session.execute("USE dcos_example;")
session.execute("CREATE TABLE IF NOT EXISTS sample_table ( user_id timeuuid PRIMARY KEY, added_date timestamp, first_name text, last_name text, email text);")
ex_keys = cluster.metadata.keyspaces
for key in ex_keys:
    tables = ex_keys[key].tables
    for t in tables:
        print key, t
    print("------")
print "DONE"
