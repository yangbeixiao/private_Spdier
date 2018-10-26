#pip install wechatsogou 使用pip 下载安装第三方模块库
import wechatsogou
import requests
from pprint import pprint
from wechatsogou import WechatSogouAPI,WechatSogouConst
class Wechat():
    def __init__(self,name):
        self.name=name
        self.get_gzh=''
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        # 连接至微信搜狗搜索接口WechatSogouAPI
        self.wechat_gzh=wechatsogou.WechatSogouAPI(timeout=1,)

    # 检查输入的公众号是否存在
    def inspect_name(self):
        while True:

            #get_gzh_info获取指定公众号信息，如果不存在则返回None
            inspect=self.wechat_gzh.get_gzh_info(self.name)
            if inspect == None:
                self.name=input("搜索的公众号不存在！请重新输入:")
            else:
                self.get_gzh_info()
                break
    # 搜索所有输入名称相关的公众号信息
    def get_gzh_info(self):

    #search_gzh查找所有相关名称的公众号
    #获取到的信息参数：
    #profile_url公众号主页 headimage主页头像 wechat_name公众号名称 wechat_id微信号
    #qrcode公众号二维码 introduction公众号功能介绍 authentication账号主体
    #post_perm一个月的群发数量 view_perm一个月的阅读数量

        self.get_gzh=self.wechat_gzh.search_gzh(self.name)
        print("搜索到相关的公众号前{}个\n信息如下：".format(len(self.get_gzh)))
        #print(get_gzh)
        for key,value in enumerate(self.get_gzh):
            print("\t编号：{}\t公众号名称：{}".format(key+1,value['wechat_name']))
            for j in value.items():
                print('\t',j)
            print('\n')
        self.choice_num()
    def choice_num(self):
        while 1:
            choice_num=input("输入要进入的公众号编号：")
            if choice_num.isdigit():
                print(self.get_gzh[int(choice_num)-1]['profile_url'])
                a=requests.get(self.get_gzh[int(choice_num)-1]['profile_url'],headers=self.headers)
                text=a.text
                print(a.text)
                break
            else:
                print('输入不合法，请输入数字编号！')
    #搜索公众号文章
    def article(self):
        info = self.wechat_gzh.search_article(self.name)

        for key, value in enumerate(info):
            print("\t编号：{}".format(key + 1, ))
            # print(value)
            print("\t文章信息：")
            for i in value['article'].items():
                print('\t', i)
            print("\t公众号信息：")
            for j in value['gzh'].items():
                print('\t', j)
def choice_1():
    gzh_name = input("请输入要查找的公众号的名称：")
    wx = Wechat(gzh_name)
    wx.inspect_name()

def choice_2():
        gzh_name = input("请输入要查找文章的关键字：")
        wx = Wechat(gzh_name)
        wx.article()
if __name__=="__main__":
    num=input("1:查找公众号\n2:查找相关文章\n输入功能编号：")
    if num=='1':
        choice_1()
    elif num=='2':
        choice_2()
    else:
        print("输入不符合要求！")





#/s?timestamp=1539222137&src=3&ver=1&signature=P*FX9RjmNgAvWiE5iKZ3r