# pipenv 虚拟环境激活报错

使用命令：
"""
pipenv --three --python=`which python3`
"""

# celery 启动：

先切换到 server 目录下，然后参考以下命令：
前台启动：`celery worker -A newsdph.proj -l info`
后台启动：`celery multi start 2 -A newsdph.proj -l info`

后台停止：`celery multi stop 1 -A newsdph.proj -l info`

其中的数字为节点数，可指定范围
