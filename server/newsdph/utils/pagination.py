

class Pagination(object):
    """
    自定义分页
    """
    def __init__(self, current, pageSize, totalCount):
        try:
            current = int(current)
        except Exception as e:
            current = 1
        if current <=0:
            current = 1
        self.current = current
        # 数据总条数
        self.totalCount = totalCount

        # 每页显示10条数据
        try:
            pageSize = int(pageSize)
        except Exception as e:
            pageSize = 9
        if pageSize <=0:
            pageSize = 9
        self.pageSize = pageSize

        # 页面上应该显示的最大页码
        pageCount, div = divmod(totalCount, pageSize)
        if div:
            pageCount += 1
        self.pageCount = pageCount


    @property
    def start(self):
        return (self.current - 1) * self.pageSize

    @property
    def end(self):
        return self.current * self.pageSize
