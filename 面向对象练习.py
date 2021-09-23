class cup:
    height = ''  #杯子多高
    volume = ''  #杯子能装多少毫升水
    color = ''  #杯子颜色
    texture = ''  #杯子什么材料做的

    def loaded(self):
        print(self.color,'能存放液体的杯子')

c = cup()

c.height = 25
c.volume = 650
c.color = '克莱因蓝'
c.texture = '闪瞎狗眼的钛合金'
c.loaded()

class Notebookcomputer:
    Screensize = ''  #屏幕大小
    Price = '' #价格
    cpu = ''  #cpu型号
    Memmorysize = ''  #内存大小
    Standbytime = ''  #待机时长

    def playgame(self):
        print(self.Price,'块钱买的肯德基原神联名全家桶')

N = Notebookcomputer

N.Screensize = '24英寸'
N.Price = '7800'
N.cpu = 'intel i9 处理器'
N.Memmorysize = '800 GB'
N.Standbytime = '8小时'
N.playgame ()
