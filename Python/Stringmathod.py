if __name__ == '__main__':
    N = int(input())
    arr= []
    
    while inLoop == True:
        command = list (input().partition(' '))
        
        if command[0] == 'insert':
           indexValue= list(int(command[1].partition(' ')))
           arr.insert(indexValue[0],indexValue[1])
        
        if command[0] == 'print':
            print(arr)
            
        if command[0] == 'remove':
            removeValue= int(command[1])
            arr.remove(removeValue)
        
        if command[0] == 'append' :
           indexValue= int(command[1])
           arr.append(indexValue)
               
        if command[0] == 'sort':
            arr.sort()
            
        if command[0] =='pop':
            arr.pop()
            
        if command[0] =='reverse':
            arr.reverse()
            