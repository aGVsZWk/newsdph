from newsdph.extensions import db


def fetch_to_dict(sql, params={}, fetch='all', bind=None):
    '''
    dict的方式返回数据
    :param sql: select * from xxx where name=:name
    :param params:{'name':'zhangsan'}
    :param fetch:默认返回全部数据，返回格式为[{},{}],如果fetch='one',返回单条数据，格式为dict
    :param bind:连接的数据，默认取配置的SQLALCHEMY_DATABASE_URL，
    :return:
    '''
    resultProxy = db.session.execute(sql, params, bind=db.get_engine(bind=bind))
    if fetch == 'one':
        result_tuple = resultProxy.fetchone()
        if result_tuple:
            result = dict(zip(resultProxy.keys(), list(result_tuple)))
        else:
            return {}
    else:
        result_tuple_list = resultProxy.fetchall()
        if result_tuple_list:
            result = []
            keys = resultProxy.keys()
            for row in result_tuple_list:
                result_row = dict(zip(keys, row))
                result.append(result_row)
        else:
            return []
    return result


# 分页
def fetch_to_dict_pagetion(sql, params={}, page=1, page_size=15, bind=None):
    sql_count = """select count(*) as count from (%s) _count""" % sql
    total_count = get_count(sql_count, params, bind=bind)
    sql_page = '%s limit %s,%s' % (sql, (page - 1) * page_size, page_size)
    print('sql_page:', sql_page)
    result = fetch_to_dict(sql_page, params, 'all', bind=bind)
    result_dict = {'data': result, 'count': total_count}
    return result_dict


# 执行单条语句（update,insert）
def execute(sql, params={}, bind=None):
    print('sql', sql)
    db.session.execute(sql, params, bind=db.get_engine(bind=bind))
    db.session.commit()


def get_count(sql, params={}, bind=None):
    return int(fetch_to_dict(sql, params, fetch='one', bind=bind).get('count'))



# 执行多条语句，失败自动回滚
def execute_many(sqls):
    print(sqls)
    if not isinstance(sqls, (list, tuple)):
        raise Exception('type of the parameters must be list or tuple')
    if len(sqls) == 0:
        raise Exception("parameters's length can't be 0")
    for statement in sqls:
        if not isinstance(statement, dict):
            raise Exception("parameters erro")
    try:
        for s in sqls:
            db.session.execute(s.get('sql'), s.get('params'), bind=db.get_engine(bind=s.get('bind', None)))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception("execute sql fail ,is rollback")


# 创建连接
# File Name：db.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://root@localhost/study?charset=utf8')
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',
            backref=backref('course', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Course: {}>'.format(self.name)


if __name__ == '__main__':
    # 使用声明基类的 metadata 对象的 create_all 方法创建数据表：
    Base.metadata.create_all()



# session maker
# File Name: create_data.py
from sqlalchemy.orm import sessionmaker
from faker import Faker
from db import Base, engine, User, Course

session = sessionmaker(engine)()
fake = Faker('zh-cn')

def create_users():
    for i in range(10):
        # 创建 10 个 User 类实例，伪造 name 和 email
        user = User(name=fake.name(), email=fake.email())
        # 将实例添加到 session 会话中，以备提交到数据库
        # 注意，此时的 user 对象没有 id 属性值
        # 映射类的主键字段默认从 1 开始自增，在传入 session 时自动添加该属性值
        session.add(user)

def create_courses():
    # session 有个 query 方法用来查询数据，参数为映射类的类名
    # all 方法表示查询全部，这里也可以省略不写
    # user 就是上一个函数 create_users 中的 user 对象
    for user in session.query(User).all():
        # 两次循环，对每个作者创建两个课程
        for i in range(2):
            # 创建课程实例，name 的值为 8 个随机汉字
            course = Course(name=''.join(fake.words(4)), user_id=user.id)
            session.add(course)

def main():
    # 执行两个创建实例的函数，session 会话内就有了这些实例
    create_users()
    create_courses()
    # 执行 session 的 commit 方法将全部数据提交到对应的数据表中
    session.commit()

if __name__ == '__main__':
    main()



# v2
# File Name: db.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://root@localhost/study?charset=utf8')
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',
            backref=backref('course', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Course: {}>'.format(self.name)


class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer, ForeignKey('course.id'), primary_key=True)
    name = Column(String(128))
    course = relationship('Course', backref=backref('lab', uselist=False))

    def __repr__(self):
        return '<Lab: {}>'.format(self.name)


Rela = Table('rela', Base.metadata,
        Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('course.id'), primary_key=True)
)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    course = relationship('Course', secondary=Rela, backref='tag')

    def __repr__(self):
        return '<Tag: {}>'.format(self.name)


if __name__ == '__main__':
    Base.metadata.create_all()


# File Name: db.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://root@localhost/study?charset=utf8')
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',
            backref=backref('course', cascade='all, delete-orphan'))

    def __repr__(self):
        return '<Course: {}>'.format(self.name)


class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer, ForeignKey('course.id'), primary_key=True)
    name = Column(String(128))
    course = relationship('Course', backref=backref('lab', uselist=False))

    def __repr__(self):
        return '<Lab: {}>'.format(self.name)


Rela = Table('rela', Base.metadata,
        Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('course.id'), primary_key=True)
)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    course = relationship('Course', secondary=Rela, backref='tag')

    def __repr__(self):
        return '<Tag: {}>'.format(self.name)


if __name__ == '__main__':
    Base.metadata.create_all()
