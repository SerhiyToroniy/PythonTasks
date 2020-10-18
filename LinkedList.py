class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=node()

    def append(self,data):#add data to list
        new_node=node(data)#create new node with "data"
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=new_node#if list was empty

    def length(self):#return integer value of list's length
        cur=self.head
        total=0 #counter
        while cur.next is not None:
            total+=1
            cur=cur.next
        return total

    def display(self): #the same as print(list)
        elems=[]
        cur_node=self.head
        while cur_node.next is not None:
            cur_node=cur_node.next
            elems.append(cur_node.data) #append every node to empty list
        print(elems) #print list

    def get(self,index): #return data by index
        if index>=self.length() or index<0: #index is out of range
            raise None
        cur_idx=0 #counter
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data #we found it
            cur_idx+=1

    def __getitem__(self,index): #acsess by index (arr[])
        return self.get(index) #call get method

    def insert(self, index, data):
        if index >= self.length() or index < 0:
            return self.append(data)
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = node(data)
                prior_node.next = new_node
                new_node.next = cur_node
                return
            prior_node = cur_node
            cur_idx += 1

    def erase(self, index):
        if index >= self.length() or index < 0:  # added 'index<0' post-video
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def cut(self, start, end):
        if start >= end:
            start, end = end, start
        for i in range(end+1):
            if i >= start:
                self.erase(start)