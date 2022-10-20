from typing import Any


# dodac stos i bash

class Node:  # nody
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
        nowy.next = self.head
        self.head = nowy

    def append(self, value: Any):
        nowy = Node(value)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = nowy
        else:
            self.head = nowy

    def node(self, at: int) -> Node:
        temp = self.head
        iter = 0
        while iter < at:
            temp = temp.next
            iter += 1
        print(f'Wartosc wybraj pozycji wezla :{temp.data}')
        return temp

    def insert(self, value: Any, after: Node) -> None:
        licznik = 0
        temp = self.head
        while True:
            if licznik == value:
                node = Node(after.data)
                node.next = temp.next
                temp.next = node
                return None
            licznik += 1
            temp = temp.next

    def pop(self) -> Any:
        temp = self.head
        self.head = temp.next
        return temp


    def  remove_last(self) -> Any:
        temp = self.head
        while(temp.next):
            if(temp.next):
                temp=self.tail#nie dziala
            temp = temp.next



    def __str__(self):
        temp = self.head
        print(f'pierwszy element listy :{temp.data}')
        while (temp):
            temp = temp.next
            if temp.next is None:
                return f'ostatni element listy :{temp.data}'
            else:
                print(f'Lista:{temp.data}')


lista = LinkedList()
node1 = Node(420)
lista.append(12)
lista.push(10)
lista.append(30)
lista.append(45)
print(str(lista))
lista.node(1)
lista.insert(1, node1)
lista.pop()
print(str(lista))
