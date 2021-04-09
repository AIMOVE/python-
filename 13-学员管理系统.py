'''
需求：进入系统显示功能界面
1、添加学员
2、删除
3、修改学员信息
4、显示所有信息
5、退出
用户输入功能序号后执行不同的功能
'''

def sms():
    print('请选择功能---------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、显示所有学员')
    print('5、查询学员')
    print('6、退出系统')
    print('-----------------')
'''
添加学员 姓名  学号 电话
接收信息并保存
判断是否重复
对应条件成立则调用函数
'''
info = []
def add_sms():
    '''添加学员'''
    new_id = input('请输入id：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入电话：')
    global info
# 判断是否重复
    for i in info:
        if new_name == i['name']:
            print('用户已存在')
            return
# 不存在则添加
    info_dict = {}  # 准备空字典，存入
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)
    info.append(info_dict)
    print(info)
'''
删除学员
输入目标学员
判断是否存在
'''
def del_sms():
    '''删除学员'''
    del_name = input('请输入删除学员姓名：')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)
'''
修改手机号
用户输入
判断
'''
def modify_sms():
    modify_name = input('请输入修改学员姓名:')
    global info
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号:')
            break
    else:
        print('该学员不存在')
    print(info)

# 查询
def search_sms():
    search_name = input('请输入查询学员姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print(f"该学员的学号是{i['id']}, 姓名是{i['name']}, 电话是{i['tel']}")
            break
    else:
        print('用户不存在')
# 显示所有
def print_all():
    print('学号\t姓名\t电话')
    global info
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')

while True:
    sms()
    user_num = int(input('请输入序号：'))
    if user_num == 1:
        print('添加学员')
        add_sms()
    elif user_num == 2:
        print('删除学员')
        del_sms()
    elif user_num == 3:
        print('修改学员信息')
        modify_sms()
    elif user_num == 4:
        print('查询学员信息')
        search_sms()
    elif user_num == 5:
        print('显示所有学员信息')
        print_all()
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('输入有误')


