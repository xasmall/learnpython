'''
@Description: 双端队列类，模拟入队、出队等基本操作
@version: 1.0
@Author: xasmall
@Date: 2020-03-09 11:12:15
@LastEditors: xasmall
@LastEditTime: 2020-03-09 11:20:23
'''
class myDeque:
    def __init__(self,iterable=None,maxlen=10):
        if iterable==None:
            self._content = []
            self._current = 0
        else:
            self._content=list(iterable)
            self._current=len(iterable)
        self._size = maxlen
        if self._size < self._current:
            self._size = self._current
        
    def __del__(self):
        del self._content
    
    # 修改队列大小
    def setSize(self,size):
        if size < self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def appendRight(self,y):
        if self._current < self._size:
            self._content.append(y)
            self._current = self._current + 1;
        else:
            print('The queue is full.')
    def appendLeft(self,y):
        if self._current < self._size:
            self._content.insert(0,y)
            self._current = self._current + 1;
        else:
            print('The queue is full.')
    def popLeft(self):
        if self._content:
            self._current = self._current - 1;
            return self._content.pop(0)
        else:
            print('The queue is empty')
    def popRight(self):
        if self._content:
            self._current = self._current - 1;
            return self._content.pop() 
        else:
            print('The queue is empty')

