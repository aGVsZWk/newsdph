

# 创建连接
# File Name：db.py
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
#
# engine = create_engine('mysql://root@localhost/study?charset=utf8')
# Base = declarative_base(engine)
#
#
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True, nullable=False)
#     email = Column(String(64), unique=True)
#
#     def __repr__(self):
#         return '<User: {}>'.format(self.name)
#
#
# class Course(Base):
#     __tablename__ = 'course'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64))
#     user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
#     user = relationship('User',
#             backref=backref('course', cascade='all, delete-orphan'))
#
#     def __repr__(self):
#         return '<Course: {}>'.format(self.name)
#
#
# if __name__ == '__main__':
#     # 使用声明基类的 metadata 对象的 create_all 方法创建数据表：
#     Base.metadata.create_all()



# session maker
# File Name: create_data.py
# from sqlalchemy.orm import sessionmaker
# from faker import Faker
# from db import Base, engine, User, Course
#
# session = sessionmaker(engine)()
# fake = Faker('zh-cn')
#
# def create_users():
#     for i in range(10):
#         # 创建 10 个 User 类实例，伪造 name 和 email
#         user = User(name=fake.name(), email=fake.email())
#         # 将实例添加到 session 会话中，以备提交到数据库
#         # 注意，此时的 user 对象没有 id 属性值
#         # 映射类的主键字段默认从 1 开始自增，在传入 session 时自动添加该属性值
#         session.add(user)
#
# def create_courses():
#     # session 有个 query 方法用来查询数据，参数为映射类的类名
#     # all 方法表示查询全部，这里也可以省略不写
#     # user 就是上一个函数 create_users 中的 user 对象
#     for user in session.query(User).all():
#         # 两次循环，对每个作者创建两个课程
#         for i in range(2):
#             # 创建课程实例，name 的值为 8 个随机汉字
#             course = Course(name=''.join(fake.words(4)), user_id=user.id)
#             session.add(course)
#
# def main():
#     # 执行两个创建实例的函数，session 会话内就有了这些实例
#     create_users()
#     create_courses()
#     # 执行 session 的 commit 方法将全部数据提交到对应的数据表中
#     session.commit()
#
# if __name__ == '__main__':
#     main()



# v2
# File Name: db.py

# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
#
# engine = create_engine('mysql://root@localhost/study?charset=utf8')
# Base = declarative_base(engine)
#
#
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True, nullable=False)
#     email = Column(String(64), unique=True)
#
#     def __repr__(self):
#         return '<User: {}>'.format(self.name)
#
#
# class Course(Base):
#     __tablename__ = 'course'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64))
#     user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
#     user = relationship('User',
#             backref=backref('course', cascade='all, delete-orphan'))
#
#     def __repr__(self):
#         return '<Course: {}>'.format(self.name)
#
#
# class Lab(Base):
#     __tablename__ = 'lab'
#     id = Column(Integer, ForeignKey('course.id'), primary_key=True)
#     name = Column(String(128))
#     course = relationship('Course', backref=backref('lab', uselist=False))
#
#     def __repr__(self):
#         return '<Lab: {}>'.format(self.name)
#
#
# Rela = Table('rela', Base.metadata,
#         Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
#         Column('course_id', Integer, ForeignKey('course.id'), primary_key=True)
# )
#
#
# class Tag(Base):
#     __tablename__ = 'tag'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True)
#     course = relationship('Course', secondary=Rela, backref='tag')
#
#     def __repr__(self):
#         return '<Tag: {}>'.format(self.name)
#
#
# if __name__ == '__main__':
#     Base.metadata.create_all()
#
#
# # File Name: db.py
#
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
#
# engine = create_engine('mysql://root@localhost/study?charset=utf8')
# Base = declarative_base(engine)
#
#
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True, nullable=False)
#     email = Column(String(64), unique=True)
#
#     def __repr__(self):
#         return '<User: {}>'.format(self.name)
#
#
# class Course(Base):
#     __tablename__ = 'course'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64))
#     user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
#     user = relationship('User',
#             backref=backref('course', cascade='all, delete-orphan'))
#
#     def __repr__(self):
#         return '<Course: {}>'.format(self.name)
#
#
# class Lab(Base):
#     __tablename__ = 'lab'
#     id = Column(Integer, ForeignKey('course.id'), primary_key=True)
#     name = Column(String(128))
#     course = relationship('Course', backref=backref('lab', uselist=False))
#
#     def __repr__(self):
#         return '<Lab: {}>'.format(self.name)
#
#
# Rela = Table('rela', Base.metadata,
#         Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
#         Column('course_id', Integer, ForeignKey('course.id'), primary_key=True)
# )
#
#
# class Tag(Base):
#     __tablename__ = 'tag'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True)
#     course = relationship('Course', secondary=Rela, backref='tag')
#
#     def __repr__(self):
#         return '<Tag: {}>'.format(self.name)
#
#
# if __name__ == '__main__':
#     Base.metadata.create_all()





################
################
################
# import importlib
# import pkgutil
#
#
# def import_submodules(package, recursive=True):
#     """ Import all submodules of a module, recursively, including subpackages
#
#     :param package: package (name or actual module)
#     :type package: str | module
#     :rtype: dict[str, types.ModuleType]
#     """
#     if isinstance(package, str):
#         package = importlib.import_module(package)
#     results = {}
#     for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
#         full_name = package.__name__ + '.' + name
#         results[full_name] = importlib.import_module(full_name)
#         if recursive and is_pkg:
#             results.update(import_submodules(full_name))
#     return results
#
# print(import_submodules(__name__).keys())
# __all__ = import_submodules(__name__).keys()

#
# def import_submodules(package_name):
#     """ Import all submodules of a module, recursively
#
#     :param package_name: Package name
#     :type package_name: str
#     :rtype: dict[types.ModuleType]
#     """
#     package = sys.modules[package_name]
#     return {
#         name: importlib.import_module(package_name + '.' + name)
#         for loader, name, is_pkg in pkgutil.walk_packages(package.__path__)
#     }
#
# import imp
# import sys
# #----------------------------------------------------------------------
# def dynamic_importer(name, class_name):
#     """
#     Dynamically imports modules / classes
#     """
#     try:
#         fp, pathname, description = imp.find_module(name)
#     except ImportError:
#         print("unable to locate module: " + name)
#         return (None, None)
#
#     try:
#         example_package = imp.load_module(name, fp, pathname, description)
#     except Exception, e:
#         print(e)
#
#     try:
#         myclass = imp.load_module("%s.%s" % (name, class_name), fp, pathname, description)
#         print(myclass)
#     except Exception, e:
#         print(e)
#
#     return example_package, myclass
