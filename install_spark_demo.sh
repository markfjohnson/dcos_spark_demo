#
# Setup Spark Demo Environment
#


# Create users and Roles
dcos package install --cli dcos-enterprise-cli
dcos security org groups create data_sci
dcos security org groups create fin_analytics

dcos security org users create -d Frank -p frank frank
dcos security org users create -d Berta -p berta berta
dcos security org users create -d Federica -p federica federica
dcos security org users create -d Bobby -p bobby bobby
dcos security org users create -d Emily -p emily emily
dcos security org users create -d Edward -p edward edward

dcos security org groups add_user data_sci bobby
dcos security org groups add_user data_sci berta
dcos security org groups add_user data_sci federica
dcos security org groups add_user fin_analytics frank
dcos security org groups add_user fin_analytics emily
dcos security org groups add_user fin_analytics edward


# 
dcos package install --yes spark --options=spark-dispatcher-options.json
dcos package install --yes marathon-lb
dcos package install --yes hdfs
dcos package install --yes cassandra
dcos package install --yes kafka
dcos package install --yes elastic

# Setup HDFS for Spark-history
# spark run --submit-args="XXX GitHub reference for spark setup HDFS history options"

# Install Spark History
dcos package install --yes spark-history --options=files/spark-history-options.json