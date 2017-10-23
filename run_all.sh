#!/usr/bin/env bash
set -x
bash cassandra_spark/run_cassandra_rw.sh
bash elastic_spark/run_elastic.sh
bash kafka_spark/run_kafka_test.sh
cd postgresQL_Spark
bash run_postgresql.sh
cd ..