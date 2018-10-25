# Redis job queue

This project implements a job queue in python using a (local running) Redis database. The consumer is fault tolerant in the way if the it receives SIGTERM or SIGINT the the message back on the queue and therefore not lost. Also if an exception is raised within the handler function, the message is moved to a dedicated error queue for later investigation.

## Start Redis locally
`docker-compose start`

## Publish
```
from job_queue import JobQueue
queue = JobQueue(queue_name='test_queue', host='0.0.0.0')
queue.publish(message)
```

## Consume
```
from job_queue import JobQueue

def handle_message(body):
    print(body)
    # Do some work

queue = JobQueue(queue_name='test_queue', host='0.0.0.0')
queue.start_consume(job_func=handle_message)
```
