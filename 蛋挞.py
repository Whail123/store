from threading import Thread
import time

lanzi = 0
class cook(Thread):
    def run(self) -> None:
        global lanzi
        while True:
         if lanzi < 500:
             lanzi = lanzi + 1
             print('篮子里还剩',lanzi,'个蛋挞')
         if lanzi == 500:
             time.sleep(3)
             print('篮子已满')
             break

danta = 2  #蛋挞一个2块
class guke(Thread):
    user = '张三'
    user = '李四'
    user = '王五'
    user = '易一'
    user = '钱七'
    user = '赵八'
    money = 3000
    def run(self) -> None:
        global danta
        global lanzi
        while True:
          if self.money > 2:
              self.money = self.money -2
              lanzi = lanzi -1
              print('还剩',self.money,'块钱','蛋挞还剩',lanzi,'个')
          if lanzi == 0:
              time.sleep(2)
          if self.money == 0:
              break


g1 = guke()
g2 = guke()
g3 = guke()
g4 = guke()
g5 = guke()
g6 = guke()




c1 = cook()
c2 = cook()
c3 = cook()

c1.start()
c2.start()
c3.start()

g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
g6.start()
