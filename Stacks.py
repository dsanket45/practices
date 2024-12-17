

# STACK IN LINKED LIST-----------------------------------------------------------STACK LINKED LIST
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def isEmpty(self):
        # return self.top==None
        if self.top == None:
            return True#"yes stack is empty"
        else:
            return False#"stack  is not empty"

    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        
    def peek(self):
        if self.top == None:
            return 'stack is empty'
        else:
            print(f"peek element is :{self.top.data}")
        
    def traversal(self):
        count=0
        temp=self.top
        while temp is not None:
            count+=1
            data=temp.data
            print(data)
            temp=temp.next
        print(f"total elements in stack is {count}")
            
    def pop(self):
        temp=self.top
        if temp is None:
            print("stack is now empty you cant pop up now")
        else:
            data=self.top.data
            self.top = self.top.next
            # print(f"removed element is {temp.data}") #for printing removed element
            return data
        
    
    

s=Stack()
# s.push(1)
# s.push(2)
# s.push(30)
# s.pop()
# s.pop()
# s.pop()
# s.reverse("hello")
# s.peek()
# s.traversal()
# print(s.isEmpty())

def reverse(text):
    s1=Stack()
    for i in text:
        s1.push(i)
    res=""
    while (not s1.isEmpty()):
        res=res+s1.pop()
    print((res))
    
        
# reverse("hello")
# reverse("sanket")

def text_editer(text,pattern):
    u=Stack()
    r=Stack()
    for i in text:
        u.push(i)
    
    for i in pattern:
        if i=='u':
            if not u.isEmpty():
                data=u.pop()
                r.push(data)
            else:
                print("undo empty stack")
        else:
            if not r.isEmpty():
                data=r.pop()
                u.push(data)
            else:
                print("redo empty stack")
    res=''
    while not u.isEmpty():
        res=u.pop()+res
    
    print(res)

# print()
# pattern=input("enter pattern :")
# text_editer("sanket","ruu")  #function call-------------------------------------


# [{(a+b)}]
# BALENCED PARANTHESIS PROBLEM ------------------------------------------USING STACK-----------------
def balanced_paranthesis(text):
    Obraces={'(':')','[':']','{':'}'}
    Cbraces={')','}',']'}
    s=Stack()
    for i in text:
        if i in Obraces:
            s.push(i)
        elif i in Cbraces:
            if s.isEmpty():
                return False
            peak=s.pop()
            # print(peak,i)
            # print(Obraces[peak])
            if Obraces[peak] != i:
                return False
    return s.isEmpty()    
# print(balanced_paranthesis('[{}]'))











# STACK IN ARRAYS----------------------------------------------------------IN ARRAY
# PRE-ALLOCATED STACK MEANS NONE IS ALREDY TOOK PLACE INSTED OF  VALUE--------------------------------------------------------
class Sstack:
    def __init__(self,size):
       self.size=size
       self.stack=[None]*self.size
       self.top=-1
       
    def push(self,value):
        if self.top==self.size-1:
            print(f"stack is overflow cant insert value {value}")
        else:
            self.top+=1
            self.stack[self.top]=value
        
    def peek(self):
        if self.top==-1:
            print("stack is empty")
        else:
            peek=self.stack[self.top]
            # print(self.top)
            print(f"peak element is {peek}")
            
    def pop(self):
        if self.top==-1:
            print(f"stack is empty nothing to popup")
        else:
            removed_el=self.stack[self.top]
            self.top-=1
            print(f"removed el is {removed_el}")
            
    def display(self):
        if self.top==-1:
            print("empty stack")
        else:
            for i in range(self.top+1):
                # print(self.top+1)
                print(self.stack[i],end=' ')
            
            
a=Sstack(3)
# a.stack
a.push(2)
a.push(3)
a.push(4)
# a.pop()
a.peek()
a.display()
# print(a.stack)






# DYNAMIC STACK WHICH CAN ADD LIKE LIST----------------------------------------------------------------------------------
class Astack:
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1
        
    def isEmpty(self):
        if self.top==-1:
            print(True)
        else:
            print(False)
            
    def push(self,value):
        if self.size-1==self.top:
            print(f"stack overflow cant insert value {value}")
        else:
            self.top+=1
            self.stack.append(value)
            
    def pop(self):
        if aa.isEmpty():
            print("stack is empty can't pop now")
        else:
            removed_el=self.stack.pop()
            self.top-=1
            print(f"removed element is {removed_el}")
            
    def peek(self):
        if aa.isEmpty():
            print("there is no peak stack ")
        else:
            peek=self.stack[self.top]
            print(f"peak element is {peek}")
            
    def display(self):
        if aa.isEmpty():
            print("stack is empty")
        else:
            print(f"the elements from stack are {self.stack}")
    
aa=Astack(3) 
# aa.push(2)
# aa.push(3)
# aa.push(4)
# aa.push(5)
# print("before poping")
# print(aa.stack)
# # aa.pop()
# aa.peek()
# aa.isEmpty() 
# print("after poping")
# print(aa.stack)
# aa.display()
