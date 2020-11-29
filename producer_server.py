from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        """
        Read input JSON file from disk and produce individual serialized rows to Kafka
        """
        print("generate_data - init")
        with open(self.input_file, "r") as f:

            # read JSON data from input file
            data = json.loads(f.read())

            for idx, row in enumerate(data):                
                # serialize Python dict to string
                msg = self.serialize_json(row)
                #print(f"Linha: {row}")
                self.send(self.topic, msg)
                self.flush()
                #print("Sleeping")
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return 
        
        
    @staticmethod
    def serialize_json(json_data):
        """
        Serialize Python dict to JSON-formatted, UTF-8 encoded string
        """
        return json.dumps(json_data).encode("utf-8")        