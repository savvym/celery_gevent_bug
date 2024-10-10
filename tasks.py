from celery_app import app
import time

@app.task(bind=True)
def long_running_task(self):
    try:
        i = 0
        while True:
            # 模拟长时间运行任务
            print(f'Working on {i}...')
            time.sleep(1)
            i += 1
    except Exception as e:
        return str(e)
    return 'Task completed'

