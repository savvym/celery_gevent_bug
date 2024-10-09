from celery_app import app
from tasks import long_running_task
import time

if __name__ == '__main__':
    # 启动长时间运行任务
    result = long_running_task.apply_async()

    # 等待一段时间然后发送终止信号
    time.sleep(5)
    result.revoke(terminate=True, signal='SIGTERM')

    print('Task terminated request sent.')

