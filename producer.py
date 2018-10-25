from datetime import datetime, timezone
import config

from job_queue import JobQueue

queue = JobQueue(queue_name=config.queue_name, host=config.redis_host)
for i in range(100):
    message = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'id': i
    }
    queue.publish(message)
    
print("Queue length", queue.queue_count())