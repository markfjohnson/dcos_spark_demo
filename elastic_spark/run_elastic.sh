#!/usr/bin/env bash

#!/usr/bin/env bash
dcos spark run --docker-image=markfjohnson/elastic_spark --submit-args="https://raw.githubusercontent.com/markfjohnson/dcos_spark_demo/master/elastic_spark/elastic_write_ex.py" --verbose