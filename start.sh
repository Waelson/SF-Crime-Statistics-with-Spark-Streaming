conda install --file requirements.txt
#/usr/bin/kafka-topics --create --topic com.udacity.crime.police-event --zookeeper localhost:2181 --partitions 1 --replication-factor 1
#/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.crime.police-event --from-beginning
#/usr/bin/kafka-topics --delete --topic com.udacity.crime.police-event --zookeeper localhost:2181