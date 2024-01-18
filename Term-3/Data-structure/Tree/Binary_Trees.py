from random import randint



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
    
    def inorder(self) -> str:
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

    def preorder(self) -> str:
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
    pass
        
            
       

    







def main():
    my_tree = BST()
    my_tree.insert(Node(5))
    my_tree.insert(Node(3))
    my_tree.insert(Node(7))
    my_tree.insert(Node(8))
    my_tree.insert(Node(4))
    
    print(my_tree.inorder())
    

    my_tree.delete(7)
    print(my_tree.inorder())



main()