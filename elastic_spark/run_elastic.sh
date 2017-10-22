#!/usr/bin/env bash

#!/usr/bin/env bash
dcos spark run --docker-image=markfjohnson/spark_elastic --submit-args="https://raw.githubusercontent.com/markfjohnson/dcos_spark_demo/master/cassandra_spark/Cassandra_rw.py" --verbose