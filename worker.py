from job_queue import JobQueue
import config


def handle_message(body):
    print(body)
    # Do some work


queue = JobQueue(queue_name=config.queue_name, host=config.redis_host)
queue.start_consume(job_func=handle_message)
