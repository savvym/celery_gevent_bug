from celery import Celery

# 创建 Celery 应用
app = Celery('tasks', 
             broker='pyamqp://guest:guest@127.0.0.1:5672//')  # 使用 RPC 后端

# 配置 Celery 相关设置
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
    
