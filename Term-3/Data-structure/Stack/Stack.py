from datetime import datetime
from time import sleep 

MESSAGE_1 = (
    "\n### Page 1 ###\n\n"
    "Enter 0 to stop the program\n"
    "Enter 1 for creating stack\n"
    "Enter 2 for watching all stacks\n"
    "Enter 3 for selecting one stack\n"
    "Enter 4 to push to the selected stack\n"
    "Enter 5 to pop from the selected stack\n"
    "Enter 6 to delete the selected stack\n"
    "Enter 7 to see the selected stack\n"
    "Enter 8 to go to the next page"
)

MESSAGE_2 = (
    "\n### Page 2 ###\n"
    "\nWarning: Do not use spaces"
    "\n\nEnter 0 to stop the program\n"
    "Enter 1 to turn infix to postfix\n"
    "Enter 2 to turn postfix to infix\n"
    "Enter 3 to turn infix to prefix\n"
    "Enter 4 to turn preix to infix\n"
    "Enter 5 to turn prefix to postfix\n"
    "Enter 6 to turn postfix to prefix\n"
    "Enter 7 to check paranties\n"
    "Enter 8 to go to the next page\n"
    "Enter 9 to go to the previous page\n"
)   

MESSAGE_3 = (
    "\n### Page 3 ###\n"
    "\nWarning: Do not use spaces"
    "\n\nEnter 0 to stop the program\n"
    "Enter 1 to evaluate postfix expression\n"
    "Enter 2 to evaluate prefix expression\n"
    "Enter 3 to go to the previous page\n"
)





class Node:
    
    def __init__(self,data) -> None:
        self.data = data
        self.bottom = None
    
    def __str__(self) -> str:
        return str(self.data)
    
class Stack:

    def __init__(self,top=None) -> None:
        self.top = top
        self.depth = 0
        self.created_at = datetime.now().strftime("%H:%M:%S")

    def pop(self) -> Node:
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

    def display(self,node)->str:
        if node.bottom == None:
            return str(node.data)
        return str(node.data) + "\n" + self.display(node.bottom)

    def is_empty(self) -> bool:
        return self.depth == 0 
    
    def whats_top(self):
        return self.top
    
    def __str__(self) ->str:
        return f"a stack created at {self.created_at} with the top of {self.top}"

    




class ToolsMixin:
    
    """
    the "mixin" means that this class 
    should be mixed with other classes
    in order to function .
    """

    def associativity(self,c):
        if c == '^':
            return 'R'
        return 'L'
    
    def precedence(self,a):
        precedence_dict = {'^':3,'/': 2, '*': 2, '+': 1, '-': 1}
        return precedence_dict[a]

    def is_operand(self,c):
        return c.isalnum()    

    def is_operator(self,c):
        return c in {'^','+', '-', '*', '/'}

    def is_opening_Bracket(self,c):
        return c in ["(","{","["]
    def is_closing_Bracket(self,c):
        return c in [")","}","]"]
    def match_Brackets(self,a,b):
        match_dict = {"(":")","{":"}","[":"]"}
        return match_dict[a] == b

class Expressions:
    
    """
    The methods of this class need "Tools" class
    to function .
    use them together.
    """

    def infix_to_postfix(self,sentence=None):
        
        stack = Stack()
        postfix_expression = []
        if not sentence:
            sentence = input("Enter your infix sentence here:")
        else:
            sentence = sentence

        for c in sentence:
            if self.is_operand(c):
                postfix_expression.append(c)
            elif c == '(':
                stack.push(Node(c))
            elif c == ')':
                while not stack.is_empty() and stack.whats_top().data != '(':
                    postfix_expression.append(stack.pop().data)
                stack.pop()  # Pop the '('
            elif self.is_operator(c):
                while not stack.is_empty() and self.is_operator(stack.whats_top().data):
                    
                    if (self.precedence(stack.whats_top().data)>self.precedence(c) or 
                        self.precedence(stack.whats_top().data)==self.precedence(c) and self.associativity(c)=="L"):
                        postfix_expression.append(stack.pop().data)
                    else:
                        stack.push(Node(c))
                        break
                else:
                    stack.push(Node(c))
            
        while not stack.is_empty():
            postfix_expression.append(stack.pop().data)

        return(''.join(postfix_expression))
        

    def prefix_to_infix(self):
        stack = Stack()
        reversed_stack = Stack()
        prefix_expression = input("Enter your prefix in here :")

        reverse_prefix = prefix_expression[::-1]

        for c in reverse_prefix:
            if self.is_operand(c):
                stack.push(Node(c))
            elif self.is_operator(c):
                a = stack.pop()
                b = stack.pop()

                new = "(" + b.data + c + a.data + ")"
                new = Node(new)
                
                stack.push(new)

        reversed_answer = stack.whats_top().data
        for c in reversed_answer:
            reversed_stack.push(Node(c))
        answer = ""
        while not reversed_stack.is_empty():
            answer+=reversed_stack.pop().data

        answer = answer.replace("(","Temp").replace(")","(").replace("Temp",")")

        return answer

    def prefex_to_postfix(self):
        stack = Stack()
        
        prefix_expression = input("Enter your sentence in here :")

        for c in reversed(prefix_expression):
            if self.is_operand(c):
                stack.push(Node(c))
            elif self.is_operator(c):
                a = stack.pop()
                b = stack.pop()
                
                temp = a.data + b.data + c 
                stack.push(Node(temp))

        return stack.whats_top().data

    def postfix_to_prefix(self):
        
        stack = Stack()
        postfix_expression = input("Enter your postfix in here :")

        for c in postfix_expression:
            if self.is_operand(c):
                stack.push(Node(c))
            elif self.is_operator(c):
                a = stack.pop()
                b = stack.pop()
                
                temp = c + b.data + a.data 
                stack.push(Node(temp))

        return stack.whats_top().data
    
    def postfix_to_infix(self):

        stack = Stack()
        postfix_expression = input("Enter your postfix in here :")

        for c in postfix_expression:
            if self.is_operand(c):
                stack.push(Node(c))
            elif self.is_operator(c):
                a = stack.pop()
                b = stack.pop()
                
                temp = "(" + b.data + c + a.data + ")"
                stack.push(Node(temp))

        return stack.whats_top().data


    def infix_to_prefix(self):
        infix = input("Enter your infix in here :")  
        output=""
        stack = Stack()
        infix = infix[::-1]

        for c in infix:
            if c == '(':
                c = ')'
            elif c == ')':
                c = '('
        
        
        for c in infix:
            
            
            if self.is_operand(c):
                output += c
                
            
            elif c == '(':
                stack.push(Node(c))
            
            
            elif c == ')':
                while stack.whats_top().data != '(':
                    output += stack.pop().data
                stack.pop()
            
            
            elif self.is_operator(c):
                if not stack.is_empty() and self.is_operator(stack.whats_top().data):
                    if c == '^':
                        while self.precedence(c) <= self.precedence(stack.whats_top().data):
                            output += stack.pop().data
                    else:
                        while self.precedence(c) < self.precedence(stack.whats_top().data):
                            output += stack.pop().data
                    stack.push(Node(c))
                else:
                    stack.push(Node(c))

        while not stack.is_empty():
            output+=(stack.pop().data)

        prefix = output[::-1]

        return prefix
        

class Evaluate:
    def evaluate_Postfix(self, exp=None):
        stack = Stack()
        if not exp:
            exp = input("Enter your expression in here:")

        for c in exp:   
            if self.is_operand(c):
                stack.push(Node(c))
            else:
                val1 = stack.pop().data
                val2 = stack.pop().data
                stack.push(Node(str(eval(val2 + c + val1))))
 
        return stack.pop().data

    def evaluate_Prefix(self,exp=None):
        if not exp:
            exp = input("Enter your expression in here:")
        stack = Stack()
        for c in reversed(exp):
            if self.is_operand(c):
                stack.push(Node(c))
            else:
                val1 = stack.pop().data
                val2 = stack.pop().data
                stack.push(Node(str(eval(val1 + c + val2))))

        return stack.pop().data

class Brackets:
    def are_Brackets_Balanced(self,expr=None):
        stack = Stack()

        if not expr:
            expr = input("Enter ypur expression in here:")

        for c in expr:
            if self.is_opening_Bracket(c): 
                stack.push(Node(c))

            elif self.is_closing_Bracket(c):
    
                if stack.is_empty():
                    return False
                current_char = stack.pop().data
                if self.match_Brackets(current_char,c):
                    continue
                else:
                    return False

        
        if stack.is_empty():
            return True
        return False

class Program(ToolsMixin,Expressions,Evaluate,Brackets):
    def __init__(self) -> None:
        self.all_stacks =[]
        self.selected = None
    
    def repeat(self,a,time=1):
        sleep(time)
        if a == 1:
            self.page_one()
        elif a ==2:
            self.page_two()
        elif a ==3:
            self.page_three()

    def page_one(self):
        print(MESSAGE_1)
        command = int(input())
        if command in [0,1,2,3,4,5,6,7,8]:
            if command == 0 :
                return 
            elif command == 1:
                self.create()
                self.repeat(1,0.5)
            elif command == 2:
                self.display()
                self.repeat(1)
            elif command == 3:
                self.select()
                self.repeat(1)
            elif command ==4:
               self.push()
               self.repeat(1)
            elif command == 5:
                self.pop()
                self.repeat(1)
            elif command == 6:
               self.delete()
               self.repeat(1)
            elif command == 7:
                self.show_me()
                self.repeat(1)
            elif command == 8:
                self.page_two()
        else:
            print("Bad command")
            self.repeat(1)

    def page_two(self):
        command = int(input(MESSAGE_2))
        if command in [0,1,2,3,4,5,6,7,8,9]:
            if command == 0:
                return
            elif command == 1:
                print(self.infix_to_postfix())
                self.repeat(2)
            elif command == 2:
                print(self.postfix_to_infix())
                self.repeat(2)
            elif command == 3:
                print(self.infix_to_prefix())
                self.repeat(2)
            elif command == 4:
                print(self.prefix_to_infix())
                self.repeat(2)
            elif command == 5:
                print(self.prefex_to_postfix())
                self.repeat(2)
            elif command ==6:
                print(self.postfix_to_prefix())
                self.repeat(2)

            elif command == 7:
                if (self.are_Brackets_Balanced()):
                    print("Balanced")
                else:
                    print("they are not balanced")
                self.repeat(2)
            elif command == 8:
                self.page_three()
            elif command == 9:
                self.page_one()

        else:
            print("bad command")
            sleep(1)
            self.page_two()
    
    def page_three(self):
        command = int(input(MESSAGE_3))
        if command in [0,1,2,3]:
            if command == 0:
                return
            elif command == 1:
                print(self.evaluate_Postfix())
                self.repeat(3)
            elif command == 2:
                print(self.evaluate_Prefix())
                self.repeat(3)
            elif command == 3:
                self.page_two()

    def create(self):
        x = Stack()
        print("stack created succusfuly\n")
        self.all_stacks.append(x)
        
    
    def display(self):
        
        if len(self.all_stacks) == 0:
            print("you dont have any stack , create one\n")
            sleep(1)
            self.page_one()
        else:
            for stack in self.all_stacks:
                print(stack)
            print("\n")
            

    def select(self):
        if len(self.all_stacks) == 0 :
            print("you dont have stack to choose")
            
        else:
            dictt = dict()
            for index,object in enumerate(self.all_stacks):
                print(object,"\t",index+1)
                dictt[index+1]=object
            command = int(input("Enter the number to select stack: "))
            try :
                self.selected = dictt[command]
            except :
                print("bad command")
                
            else:
                print(f"you selected : {self.selected}")
                

    def push(self):
        if self.selected == None:
            print("first select one stack to work with")
            
        else:
            new_node = Node(input("Enter the data for new node:"))
            self.selected.push(new_node)
            print("you pushed new node succesfully")
            
    
    


    def pop(self):
        if self.selected == None:
            print("first select one stack to work with")
            
        else:
            try :
                print(self.selected.pop())
                
            except:
                print("the stack is empty")
                
        
    def delete(self):
        if self.selected == None:
            print("first select one stack to work with")
            
        else:
            for stack in self.all_stacks:
                if stack == self.selected:
                    self.all_stacks.remove(stack)
        
            del self.selected
            print("deleted succusfuly")
            self.selected = None
            

    def show_me(self):
        if self.selected == None:
            print("first select one stack to work with")
            
        else:
            print(self.selected)
            

   

def main():
    my_program = Program()
    my_program.page_one()


if __name__ == "__main__":
    main()

    

        
