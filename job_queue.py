import json
import redis
import signal

class JobQueue():
    def __init__(self, queue_name, host):
        self.queue_name = queue_name
        self.queue_name_error = queue_name + '_error'
        self.redis_conn = redis.Redis(host)

    
    def start_consume(self, job_func):
        signal.signal(signal.SIGINT, self.terminate_signal)
        signal.signal(signal.SIGTERM, self.terminate_signal)
        self.running = True
        while self.running:
            _, body = self.redis_conn.blpop(self.queue_name, timeout=1)
            if body is None:
                continue
            try:
                print(body)
                job_func(body)
            except KeyboardInterrupt as e:
                self.redis_conn.lpush(self.queue_name, body)
                break
            except Exception as e:
                print(e)
                self.redis_conn.lpush(self.queue_name_error, body)

        print("Done")            
    
    def queue_count(self):
        return self.redis_conn.llen(self.queue_name)

    def publish(self, body):
        self.redis_conn.rpush(self.queue_name, json.dumps(body))

    def terminate_signal(self, signum, frame):
        self.running = False
