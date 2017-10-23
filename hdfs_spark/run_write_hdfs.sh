#!/usr/bin/env bash
dcos spark run  --submit-args="https://raw.githubusercontent.com/markfjohnson/dcos_spark_demo/6269cb5f50527c7adf2dc212ee7c9f145fe9738e/hdfs_spark/hdfs_spark_write.py" --verbose
