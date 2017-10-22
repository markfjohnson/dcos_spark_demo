#
# Reference the base spark image
FROM mesosphere/spark:1.1.0-2.1.1-hadoop-2.6

# Install the pip3 utility so we can install the Python package
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y python-pip build-essential python-dev
RUN pip install --upgrade pip
RUN pip install elasticsearch



