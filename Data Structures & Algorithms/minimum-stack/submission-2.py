class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
       

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack  or self.stack[-1]<=self.minstack[-1]:
            self.minstack.append(val)


    def pop(self) -> None:
        r=self.stack.pop()
        if r==self.minstack[-1]:
            self.minstack.pop()
        
        

    def top(self) -> int:
         return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
