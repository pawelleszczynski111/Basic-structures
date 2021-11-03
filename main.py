from typing import Any

class Node:
    def __init__(self, vale: Any=None, next = None):
        self.value: Any= value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head: Node=None
        self.tail: Node=None


    def __len__(self):
        a=self.head
        i=0
        while a!= None:
            i+=1
            a=a.next
        return i

    def push(self, value:Any):
        if self.head==None:
            a=Node(value)
            self.head=a
            self.tail=a
        else:
            self.push(value)


    def append(self,value: Any):
        if self.head is None:
            self.push(value)
        else:
            a = self.tail
            a.next = Node(value)
            self.tail = a.next


    def node(self, at: int):
        if len(self) >= at:
            a = self.head
            for x in range(at):
                a = a.next
            return a
        else:
            raise ValueError("Error")


    def insert(self, value: Any,after: Node):
        if after==None:
            raise ValueError("Error")
        else:
            a=Node(value)
            a.next=after.next
            after.next=a


    def pop(self)->Any:
        if self.head==None:
            raise ValueError("Error")
        else:
         a=self.head
         self.head=a.next
         return a


    def remove_last(self):
        a=self.head
        a=self.node(len(self)-1)
        self.tail=a
        a=a.next
        dlt=a.next
        a.next=None
        return dlt


    def remove(self, after:Node):
        a=self.head
        if after.next==self.tail:
            self.remove_last()
        else:
            while a.next!=after:
                a=a.next
                a.next=after.next

    def __str__(self):
        strng= ''
        a=self.head
        for i in range(len(self)):
            strng+=str(a.value)+'->'
            a=a.next
            return strng


class Stack:
    def __init__(self):
        self._storage=LinkedList()


    def __len__(self):
        return len(self._storage)

    def __str__(self):
        strng=''
        for i in range(len(self)):
            strng+='/'+str(self._storage.node(x).value+'/\n\n')
            return strng

    def push(self,a:Any):
        self._storage.push(a)

    def pop(self):
        if len(self._storage) !=0:
            return self._storage.pop().value
        else:
            raise ValueError('Error')


class Queue:

    def __init__(self):
        self._storage=LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        strng=''
        for i in range(len(self._storage)):
            strng+=str(self._storage.node(i).value)+'  '
            return strng

    def peek(self):
        if len(self._storage) !=0:
            return self._storage.tail.value
        else:
            raise ValueError('Error')

    def enqueue(self,a:Any):
        self._storage.push(a)

    def dequeue(self):
        if len(self._storage)==0:
            raise ValueError('Error')
        else:
            return self._storage.remove_last().value