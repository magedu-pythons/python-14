#实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】

class SingleNode:
    """
    代表单个节点
    """
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return repr(self.item)            #能够将这个类打印出来


class Stack:
    """
    容器类，某种方式存储一个个节点
    """
    def __init__(self):
        self.top = None
        self.bottom = None
        self.nodes=[]

    def append(self, item):
        node = SingleNode(item)
        if self.bottom == None:           #空栈
            self.bottom = node
        else:
            node.next = self.top
        self.top = node
        self.nodes.append(item)              #追加

    def pop(self):
        if self.top is None:
            raise Exception('Empty')
        node=self.top
        if node.next is None:             #只有一个node
            self.top=None
            self.bottom=None
        else:
            self.top=node.next
        self.nodes.pop()
        return node.item            #返回删除的node的item


ll = Stack()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.top,ll.bottom,ll.nodes)
ll.pop()
print(ll.top,ll.bottom,ll.nodes)
ll.pop()
print(ll.top,ll.bottom,ll.nodes)
ll.pop()
print(ll.top,ll.bottom,ll.nodes)
ll.pop()
print(ll.top,ll.bottom,ll.nodes)