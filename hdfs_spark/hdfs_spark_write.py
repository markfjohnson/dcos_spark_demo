from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql import SparkSession

warehouseLocation="/"
spark = SparkSession.builder.appName("SparkSessionHDFSExample").config("spark.sql.warehouse.dir", warehouseLocation).enableHiveSupport().getOrCreate()

sc = spark.sparkContext()
values = sc.parallelize(range(1,1000))
spark.saveAsTextFile("/testfile")