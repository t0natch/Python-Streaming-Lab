"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():

    # Create a shared queue
    q = Queue()
    producer = CSVProducer("transactions.csv", q, delay=1.0)
    consumer = Consumer(q)
    thread_producer = threading.Thread(target=producer.start)
    thread_consumer = threading.Thread(target=consumer.start)
    thread_producer.start()
    thread_consumer.start()
#Optionally join them so the program runs continuously
    """
    TODO:
    - Create the shared queue.
    - Instantiate the producer and consumer.
    - Create a thread for each.
    - Start both threads.
    - Optionally join them so the program runs continuously.

    The students should run:
        python pipeline.py
    and observe live streaming behavior.
    """


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
