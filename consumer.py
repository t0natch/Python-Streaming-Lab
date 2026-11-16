"""
consumer.py
----------------
This file contains the logic for a Consumer that continuously reads messages
from the queue and processes them.

The Consumer runs forever, just like a streaming system.
"""

import time
from queue import Queue

class Consumer:
    def __init__(self, q):
        self.q = q
        self.running_total = 0.0
        """
        PARAMETERS:
        - q : the shared queue (simulated topic)

        TODO:
        - Store the queue.
        - Initialize any state variables you may want later,
          e.g. a running total for stateful computations.
        """
        

    def start(self):
        while True:
            
            event = self.q.get()
            try:
                print(f"Received event: {event}")
                self.process(event)
            finally:
                self.q.task_done()
        """
        Main loop of the consumer.

        TODO:
        - Continuously call q.get() to receive events.
        - Print the event received.
        - Pass it to the process() function.
        """
    

    def process(self, event):
        time.sleep(0.1)
        amount = float(event["amount"])
        self.running_total += amount
        print(
            f"Processed transaction {event['transaction_id']} | "
            f"amount: {amount:.2f} | total: {self.running_total:.2f}"
        )
        """
        TODO:
        - Simulate some processing time using time.sleep().
        - Transform fields (e.g., convert amount to float).
        - Implement optional filtering conditions.
        - Update any state (example: running total).
        """
   

# Debugging test

if __name__ == "__main__":
    """
    Run this alone to see consumer behavior.

    Note: It will block waiting for messages since no producer is running.
    """
    q = Queue()
    consumer = Consumer(q)
    consumer.start()
