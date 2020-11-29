# SF Crime Statistics with Spark Streaming

## Overview

In this project, we provide a statistical analyses of the data using Apache Spark Structured Streaming. We created a Kafka server to produce data, a test Kafka Consumer to consume data and ingest data through Spark Structured Streaming. Then we applied Spark Streaming windowing and filtering to aggregate the data and extract count on hourly basis.

## Environment

- Java 1.8.x
- Python 3.6 or above
- Zookeeper
- Kafka
- Scala 2.11.x
- Spark 2.4.x

## How to Run?

### Start Zookeeper and Kafka Server

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

### Run Kafka Producer server

```bash
python kafka_server.py
```

### Run the kafka Consumer server

```bash
python kafka_consumer.py
```

### Submit Spark Streaming Job

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py
```

## Screenshots

### Kafka Consumer

<img src="https://github.com/Waelson/SF-Crime-Statistics-with-Spark-Streaming/blob/main/images/messages_produced.png">

### Output Spark

### Batch 1

<img src="https://github.com/Waelson/SF-Crime-Statistics-with-Spark-Streaming/blob/main/images/batch1.png">

### Batch 2

<img src="https://github.com/Waelson/SF-Crime-Statistics-with-Spark-Streaming/blob/main/images/batch2.png">
