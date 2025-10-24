def change_to_binary(num: int): 
    #تبدیل مبنا از دسیمال به باینری 
    
    binary_saver = []
    one_zero_saver = []
    finish_sign = -1 
    result=""
       
    if num == 0:
        return 0
    elif num < 0:
        
        num*=-1
        binary_saver.append(num) 
           
        while True :
            num = num // 2
            binary_saver.append(num)
            if num == 0:
                break
        
        for i in binary_saver:
            if i == 0 :
                continue
            x = i%2
            one_zero_saver.append(x)

        result+="-0b"
        while True:
            try:
                result += str(one_zero_saver[finish_sign])
                finish_sign -= 1
            except:
                break
        
        return result 
        
    else:
        
        binary_saver.append(num)  
          
        while True :
            num = num // 2
            binary_saver.append(num)
            if num == 0:
                break
        
        for i in binary_saver:
            if i == 0 :
                continue
            x = i%2
            one_zero_saver.append(x)
            
        result+="0b"
        
        while True:
            try:
                result += str(one_zero_saver[finish_sign])
                finish_sign -= 1
            except:
                break
            
        return result        
   
        
while True:
    
    menu_number = int(input("Welcome change to binary menu \n1)Change to binary\n2)exit\nselect your number :: "))
    
    if menu_number == 1:
        num = int(input("Enter your number:: "))
        show_result = f"Answer is :: {change_to_binary(num)}"
        print(show_result)
        
    elif menu_number == 2:
        break
    else:
        continue
    
    
    