rap2.taobao.org

https://cnodejs.org/api

# 登录

url: `/auth/login`

POST

```json
{
    "username": "askhdqwe",
    "password": "asdasdasd",
    "remember": 1
}
```

```json
{
    "code": 200,
    "msg":"铁憨憨!登录成功",
    "msg_type": "s",
    "payload":{
        "id": 1,
        "confirmed": 1,
        "locked" :1,
        "active": 1,
        "token":"eyasdasd.asdasdasd.asdasd",
        "status":1
    }
}
```


`curl 127.0.0.1:8000/auth/login -X POST -d '{"email": "2571117816@qq.com", "password": "123456", "remember":1}' --header "Content-Type: application/json"`
# 获取用户信息

url: `/user/profile?id=`

need token

id 可接收数组

GET

```json
{
  "code": 200,
  "msg": "铁憨憨!获取用户信息成功!!!",
  "msg_type": "s",
  "payload": {
    "count": 1,
    "data": [
      {
        "active": 1,
        "age": 18,
        "avatar": "",
        "birthday": "Wed, 08 Apr 2020 17:38:48 GMT",
        "confirmed": 1,
        "email": "2571117816@qq.com",
        "hobby": "足球,睡觉",
        "id": 1,
        "locked": 0,
        "name": "何磊",
        "phone": "13838381234",
        "role_id": 4,
        "sex": "man",
        "username": "aGVsZWk"
      }
    ],
    "status": 1
  }
}
```

# 注册

url: `/auth/register`

POST

```json
{
    "email":"qqqq@qq.com",
    "username":"xxxxx",
    "password":"xxxxx",
    "code": "123456"
}
```

```json
{
    "code": 200,
    "msg":"铁憨憨!注册成功，请点击邮件进行激活！",
    "msg_type": "s",
    "payload":{
        "status":1
    }
}
```

# 注册发--短信--邮箱验证码

url: `/auth/verify`

POST

```json
{
    "email": "2571117816@qq.com"
}
```

```json
{
    "code": 200,
    "msg":"铁憨憨!验证码已发送至邮箱，有效期3分钟！",
    "msg_type": "s",
    "payload":{
        "status":1
    }
}
```


# 激活

url: `/auth/confirm?id=?token=`

GET
```json
{
    "code": 200,
    "msg":"铁憨憨!请完善个人信息!",
    "payload":{
        "id": 1,
        "token":"xxx",
        "confirmed": 1,
        "active": 0,
        "locked": 0,
        "status":1
    }
}
```

# 上传头像  (是否可由前端处理)
url: `/user/settings/avatar/upload`

need token

POST
```json
"avatar": "xxx"
```

表单提交文件，返回文件名，文件地址

```json
{
    "code": 200,
    "msg":"铁憨憨!上传头像成功，请进行修剪!",
    "payload":{
        "id": 1,
        "name": "avatar1",
        "href":"xxxxx",
        "status": 1
    }
}
```

# 修剪头像 (是否可由前端处理)
url: `/user/settings/avatar/crop`

POST

need token

```json
{
    "code": 200,
    "msg": "铁憨憨!头像修剪成功，请继续完善个人信息!",
    "payload":{
        "id": 1,
        "name": "avatar1",
        "href":"xxxxx",
        "status": 1
    }
}
```


# 设置个人信息
url: `/user/settings/profile`

need token

POST
```json
{
    "id": 1,
    "name":"xxx",
    "age":19,
    "birthday": "2020-04-05 18:40:20",
    "avatar": "xxx"
}
```

```json
{
    "code": 200,
    "msg": "铁憨憨!个人信息设置成功!",
    "payload":{
        "status": 1
    }
}
```
