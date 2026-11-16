"""
producer.py
----------------
This file contains the logic for a Producer that simulates a real-time data
stream by reading events from a CSV file and sending them one by one into a queue.

"""

import csv
import time
import random
from queue import Queue

class CSVProducer:
    def __init__(self, csv_path, q, delay=1.0):
        """Initialize a CSV producer.

        Args:
            csv_path: Path to the CSV file to stream.
            q: Queue used to send rows to the consumer.
            delay: Base delay, in seconds, between rows.
        """
        self.csv_path = csv_path
        self.q = q
        self.delay = delay

    def read_csv(self):
        return csv.DictReader(open(self.csv_path, 'r'))

    """
    PARAMETERS:
    - csv_path : path to the CSV file (str)
        - q        : queue acting as our 'topic'
        - delay    : time to wait between sending each row (float)

       TODO : Implement the __init__ method to initialize the producer.
       
       """
        
    def start(self):
        opened_csv = self.read_csv()
        while True:
            for row in opened_csv:
                print(f"Sending row: {row}")
                self.q.put(row)
                time.sleep(self.delay + random.uniform(0, 0.5))
        """
        This method should:
        1. Open the CSV file.
        2. Loop through each row 
        3. Print the row being sent.
        4. Push it into the queue 
        5. Sleep for 'delay' seconds to simulate streaming.

        TODO:
        - Implement the streaming behavior.
        - Optional: Add random jitter to simulate irregular network delays.
        """
      


# Debugging test

if __name__ == "__main__":
    q = Queue()
    producer = CSVProducer("transactions.csv", q, delay=1.0)
    producer.start()
    """
    Run this file alone to test your producer.

    Expected behavior:
    - It should print rows from the CSV file every 'delay' seconds.
    """
   

