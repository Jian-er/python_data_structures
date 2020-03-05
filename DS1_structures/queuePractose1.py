class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)






# 打印机

class Printer:
    # 初始化参数：设置打印机的速率
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None     # 空闲状态
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <=0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages()*60/self.pagerate



import random
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

from pythonds.basic.queue import Queue

# newPrintTask 决定是否创建一个新的打印任务
def stmulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute) # 初始化打印机
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)

    print("平均等待时间为：%6.2f"%averageWait)


def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    stmulation(3600, 5)

