import json
import time
from job_queue import JobQueue
import config


def handle_message(body):
    message = json.loads(body)
    print(message)
    # Do some work

queue = JobQueue(queue_name=config.queue_name, host=config.redis_host)
queue.start_consume(job_func=handle_message)
