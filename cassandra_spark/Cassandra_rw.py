from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import *

from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql import SQLContext

cassandra_url = 'node-0.cassandra.mesos'
cassandra_url = 'localhost'
KEYSPACE="dcos_example"
TABLE_NAME="sample_table"

sc = SparkContext(appName="PySpark Cassandra File Write Example")

spark = SparkSession.builder \
    .appName("PySpark Cassandra Read Write Example") \
    .config("spark.sql.crossJoin.enabled", "true") \
    .getOrCreate()


cluster = Cluster([cassandra_url])  # provide contact points and port

# Verify Tables and Keyspaces exist for data if not then create it
session = cluster.connect()

session.execute("CREATE KEYSPACE IF NOT EXISTS {} WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }; ".format(KEYSPACE))

session.execute("USE {};".format(KEYSPACE))
session.execute("CREATE TABLE IF NOT EXISTS {} ( user_id timeuuid PRIMARY KEY, added_date timestamp, first_name text, last_name text, email text);".format(TABLE_NAME))
session.execute("DESCRIBE TABLES;")
