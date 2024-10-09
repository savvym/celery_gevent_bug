from celery_app import app
import time

@app.task(bind=True)
def long_running_task(self):
    try:
        for i in range(100):
            # 模拟长时间运行任务
            print(f'Working on {i}...')
            time.sleep(1)
            # 检查是否收到终止信号
            if self.request.called_directly:
                print('Task terminated by user request.')
                return 'Task terminated'
    except Exception as e:
        return str(e)
    return 'Task completed'

