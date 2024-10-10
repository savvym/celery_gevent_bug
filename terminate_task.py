from celery_app import app
from tasks import long_running_task
import time

if __name__ == '__main__':
    result = long_running_task.apply_async()
    time.sleep(5)
    res = app.control.revoke(result.id, terminate=True, reply=True)
    print(f'Task terminated request sent, res: {res}')
