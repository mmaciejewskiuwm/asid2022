from typing import Any


class Node: #podstawa listy
    value: Any
    next: 'Node'

    def __init__(self, data=None):
        self.data = data
        self.next = None
        return

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any):
        nowy = Node(value)
        if (self.head):
            temp = self.head
            while(temp.next):
                a = temp
                temp = nowy
                temp.next = a





    def append(self, value: Any):
        nowy = Node(value)
        if (self.head):
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = nowy
        else:
            self.head = nowy


    def __str__(self):
        temp = self.head
        print(f'pierwszy element listy :{temp.data}')
        while(temp):
            temp = temp.next
            if(temp.next==None):
                return f'ostatni element listy :{temp.data}'
            else:
                print(f'Lista:{temp.data}')
lista = LinkedList()
lista.append(12)
lista.push(10)
lista.append(30)
lista.append(45)
print(str(lista))




