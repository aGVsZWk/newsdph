import itchat

itchat.auto_login(hotReload=True)
users = itchat.search_friends(name=u'安欣')
userName = users[0]['UserName']

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg)
    itchat.send(msg, toUserName = userName)

if __name__ == '__main__':
    print_content('aaa')
