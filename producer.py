from datetime import datetime, timezone
import config

from job_queue import JobQueue

queue = JobQueue(queue_name=config.queue_name, host=config.redis_host)

message = {
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'task': 'run'
}

queue.publish(message)
print('Published')