from datetime import datetime
from random import randint
from time import sleep


MESSAGE_1 = (
    "\n### BST ###\n\n"
    "Enter 0 to stop the program\n"
    "Enter 1 for creating bst tree\n"
    "Enter 2 for watching all bst trees\n"
    "Enter 3 for selecting one bst tree\n"
    "Enter 4 to insert to the selected tree\n"
    "Enter 5 to delete from the selected tree\n"
    "Enter 6 to delete the selected tree\n"
    "Enter 7 to see the selected tree\n"
    "Enter 8 to go to the next page\n"
)

MESSAGE_2 = (
    "\n### HEAP ###\n"
    
    "\n\nEnter 0 to stop the program\n"    
    "Enter 1 for creating heap tree\n"
    "Enter 2 for watching all heap trees\n"
    "Enter 3 for selecting one heap tree\n"
    "Enter 4 to insert to the selected tree\n"
    "Enter 5 to delete from the selected tree\n"
    "Enter 6 to delete the selected tree\n"
    "Enter 7 to see the selected tree\n"
    "Enter 8 to go to the previous page\n"
)  

MESSAGE_ORDER = (
    
    
       
    "\nEnter 1 for preorder\n"
    "Enter 2 for inorder\n"
    "Enter 3 for postorder\n"
    
)  


MESSAGE_HEAP =(

    "\n Enter 1 to create Max heap"
    "\n Enter 2 to create Min heap\n"

)



class Stack_Node:
    
    def __init__(self,data) -> None:
        self.data = data
        self.bottom = None
    
    def __str__(self) -> str:
        return str(self.data)


class Stack:

    def __init__(self,top=None) -> None:
        self.top = top
        self.depth = 0
        

    def pop(self) -> Stack_Node:
        if self.depth == 0:
            raise IndexError("pop from an empty stack")
        else:
            temp = self.top
            self.top = self.top.bottom
            temp.bottom = None
            self.depth -= 1
            return temp 
        
    def push(self,newTop) -> None:
        
            newTop.bottom = self.top
            self.top = newTop
            self.depth+=1

    def is_empty(self) -> bool:
        return self.depth == 0 



class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.data)



class Tree:
    
    def __init__(self) -> None:
        self.root = None
        self.created_at = datetime.now().strftime("%H:%M:%S")


    def inorder(self) -> list:
        answer = list()
        temp = self.root
        stack = Stack()
        while (temp != None or not(stack.is_empty())):
            if (temp != None):
                stack.push((Stack_Node(temp)))
                temp = temp.left
            else:
                temp = stack.pop().data
                answer.append(temp.data)
                temp = temp.right
        return answer

    def preorder(self) -> list:
        answer = list()
        temp = self.root
        stack = Stack()
        while (temp != None or not(stack.is_empty())):
            if (temp != None):
                answer.append(temp.data)
                stack.push((Stack_Node(temp)))
                temp = temp.left
            else:
                temp = stack.pop().data                
                temp = temp.right
        return answer

    def postorder(self) -> list:
        pass

    def __str__(self) -> str:
        return f"a tree created at {self.created_at} with the root of {self.root}"

class BST(Tree):
    
    

    def insert(self,node) ->None:
        
        if self.root == None:
            self.root = node
            return
        leaf = self.leaf_finder_for_insertion(new=node,node=self.root)
        if node.data > leaf.data:
            leaf.right = node
        elif node.data < leaf.data:
            leaf.left = node

    def leaf_finder_for_insertion(self,new,node=None,prev=None):
               
        
        if node == None:
            return prev
        elif new.data > node.data:
            return self.leaf_finder_for_insertion(new=new,prev=node,node=node.right)
        elif new.data < node.data:
            return self.leaf_finder_for_insertion(new=new,prev=node,node=node.left)

    def Search(self,key):
        
        def ssearch(key,node=self.root,prev=None):
            if node == None:
                return (False,node,prev)
            if key == node.data:
                return (True,node,prev)
            elif key > node.data:
                return ssearch(key,node=node.right,prev=node)
            elif key < node.data:
                return ssearch(key,node=node.left,prev=node)
        
        return ssearch(key)
    

    def delete(self,key):
        answer,node,prev = self.Search(key)
        
        if node.right and node.left:
            return self.Two_children_deletion(node,prev)        
        elif node.right or node.left :
            return self.one_child_deletion(node,prev)
        else:
            return self.leaf_deletion(node,prev)

    def leaf_deletion(self,node,prev):
        if node == prev.right:
            prev.right = None
        elif node == prev.left:
            prev.left = None
        return node    


    def one_child_deletion(self,node,prev):
        if node.right :
            child = node.right
        elif node.left :
            child = node.left

        if node == prev.right:
            prev.right = child
            del node
        elif node == prev.left:
            prev.left = child
            del node


    
    
    def max_or_min_replacment(self,node,inorder):
        for index,item in enumerate(inorder):
            if node.data == item:
                if randint(1,2) == 1 :
                    return ("Min",inorder[index+1])
                else:
                    return ("Max",inorder[index-1])
            

    def Two_children_deletion(self,node,prev):
        inorder = self.inorder()
        
        side,replacment = self.max_or_min_replacment(node,inorder)
        new_node = self.delete(replacment)

        new_node.left = node.left
        new_node.right = node.right

        if prev:
            if node == prev.left:
                prev.left = new_node
            elif node == prev.right:
                prev.right = new_node
        else:
            self.root = new_node
        
        return node


class Heap(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = None
        self.size = 0
        self.created_at = datetime.now().strftime("%H:%M:%S")

    def insert(self, obj) -> None:
        
        

        if self.size == 0:
            super().append(obj)
            self.size += 1
        else:
            super().append(obj)
            self.size += 1
            for i in range((self.size//2)-1, -1, -1):
                self.heapify(i)

    
    def delete(self):
        last = self.pop()
        self[0] = last
        
        for i in range((self.size//2)-1, -1, -1):
            self.heapify(i)

    def __str__(self) -> str:
        return super().__str__()
    
    @property
    def whois(self):
        return f"a heap created at {self.created_at}"


class Max_Heap(Heap):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = "Max"
        

    def heapify(self, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < self.size and self[i] < self[l]:
            largest = l

        if r < self.size and self[largest] < self[r]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.heapify(largest)


class Min_Heap(Heap):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = "Min"
    
    
    def heapify(self,i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < self.size and self[i] > self[l]:
            smallest = l

        if r < self.size and self[smallest] > self[r]:
            smallest = r

        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.heapify(smallest)


                
       

    







class Program:
    def __init__(self) -> None:
        self.all_bst_trees =[]
        self.all_heap_trees = []
        self.bst_selected = None
        self.heap_selected = None
    
    def repeat(self,a,time=1):
        sleep(time)
        if a == 1:
            self.page_one()
        elif a ==2:
            self.page_two()
        

    def page_one(self):
        print(MESSAGE_1)
        command = int(input())
        if command in [0,1,2,3,4,5,6,7,8]:
            if command == 0 :
                return 
            elif command == 1:
                self.create_bst()
                self.repeat(1,0.5)
            elif command == 2:
                self.display_bst()
                self.repeat(1)
            elif command == 3:
                self.select_bst()
                self.repeat(1)
            elif command ==4:
               self.insert_bst()
               self.repeat(1)
            elif command == 5:
                self.delete_from_bst()
                self.repeat(1)
            elif command == 6:
               self.delete_bst()
               self.repeat(1)
            elif command == 7:
                self.show_me_bst()
                self.repeat(1)
            elif command == 8:
                self.page_two()

        else:
            print("Bad command")
            self.repeat(1)

    def page_two(self):
        command = int(input(MESSAGE_2))
        if command in [0,1,2,3,4,5,6,7,8]:
            if command == 0:
                return
            elif command == 1:
                self.create_heap()
                self.repeat(2)
            elif command == 2:
                self.display_heap()
                self.repeat(2)
            elif command == 3:
                self.select_heap()
                self.repeat(2)
            elif command == 4:
                self.insert_heap()
                self.repeat(2)
            elif command == 5:
                self.delete_from_heap()
                self.repeat(2)
            elif command ==6:
                self.delete_heap()
                self.repeat(2)

            elif command == 7:
                self.show_me_heap()
            elif command == 8:
                self.page_one()
            

        else:
            print("bad command")
            sleep(1)
            self.page_two()
    
    

    def create_bst(self):
        x = BST()
        print("Bst created succusfuly\n")
        self.all_bst_trees.append(x)
        
    
    def display_bst(self):
        
        if len(self.all_bst_trees) == 0:
            print("you dont have any tree , create one\n")
            sleep(1)
            self.page_one()
        else:
            for tree in self.all_bst_trees:
                print(tree)
            print("\n")
            

    def select_bst(self):
        if len(self.all_bst_trees) == 0 :
            print("you dont have bst to choose")
            
        else:
            dictt = dict()
            for index,object in enumerate(self.all_bst_trees):
                print(object,"\t",index+1)
                dictt[index+1]=object
            command = int(input("Enter the number to select the bst: "))
            try :
                self.bst_selected = dictt[command]
            except :
                print("bad command")
                
            else:
                print(f"you selected : {self.bst_selected}")
                

    def insert_bst(self):
        if self.bst_selected == None:
            print("first select one tree to work with")
            
        else:
            new_node = Node(int(input("Enter the data for new node:")))
            self.bst_selected.insert(new_node)
            print("you inserted new node succesfully")
            
    
    


    def delete_from_bst(self):
        if self.bst_selected == None:
            print("first select one tree to work with")
            
        else:
            try :
                data = int(input("which node you want to be deleted(enter its data):"))
                print(self.bst_selected.delete(data))
                
            except:
                print("this node is not in the tree")
                
        
    def delete_bst(self):
        if self.bst_selected == None:
            print("first select one stack to work with")
            
        else:
            for tree in self.all_bst_trees:
                if tree == self.bst_selected:
                    self.all_bst_trees.remove(tree)
        
            del self.bst_selected
            print("deleted succusfuly")
            self.bst_selected = None
            

    def show_me_bst(self):
        if self.bst_selected == None:
            print("first select one tree to work with")
            
        else:
            print(self.bst_selected)
            command = int(input(MESSAGE_ORDER))
            if command in [1,2,3]:
                if command == 1:
                    print(self.bst_selected.preorder())
                elif command ==2:
                    print(self.bst_selected.inorder())
                elif command == 3:
                    print(self.bst_selected.postorder())
            else:
                print("bad command")

   #heap####################################################################################33
                
    def create_heap(self):
        command = int(input(MESSAGE_HEAP))
        if command in [1,2]:
            if command == 1:
                 x = Max_Heap()
            elif command ==2:
                x = Min_Heap()
        else:
            print("bad command")

        self.all_heap_trees.append(x)
        print("Heap created succusfuly\n")
        
        
    
    def display_heap(self):
        
        if len(self.all_heap_trees) == 0:
            print("you dont have any tree , create one\n")
            sleep(1)
            self.page_one()
        else:
            for tree in self.all_heap_trees:
                print(tree.whois)
            print("\n")
            

    def select_heap(self):
        if len(self.all_heap_trees) == 0 :
            print("you dont have heap to choose")
            
        else:
            dictt = dict()
            for index,object in enumerate(self.all_heap_trees):
                print(object,"\t",index+1)
                dictt[index+1]=object
            command = int(input("Enter the number to select the heap: "))
            try :
                self.heap_selected = dictt[command]
            except :
                print("bad command")
                
            else:
                print(f"you selected : {self.heap_selected}    {self.heap_selected.whois} ")
                

    def insert_heap(self):
        if self.heap_selected == None:
            print("first select one heap to work with")
            
        else:
            new_node = (int(input("Enter the data for new node:")))
            self.heap_selected.insert(new_node)
            print("you inserted new node succesfully")
            
    
    


    def delete_from_heap(self):
        if self.heap_selected == None:
            print("first select one tree to work with")
            
        else:
            try :
                data = int(input("which node you want to be deleted(enter its data):"))
                print(self.heap_selected.delete(data))
                
            except:
                print("this node is not in the tree")
                
        
    def delete_heap(self):
        if self.heap_selected == None:
            print("first select one stack to work with")
            
        else:
            for tree in self.all_bst_trees:
                if tree == self.heap_selected:
                    self.all_heap_trees.remove(tree)
        
            del self.heap_selected
            print("deleted succusfuly")
            self.heap_selected = None
            

    def show_me_heap(self):
        if self.heap_selected == None:
            print("first select one tree to work with")
            
        else:
            print(self.heap_selected)
            
            


def main():
    my_program = Program()
    my_program.page_one()


if __name__ == "__main__":
    main()

    