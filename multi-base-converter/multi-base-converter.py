def change_to_binary(num: int) -> str: 
    #Convert a decimal number to a binary number.
    
    binary_saver = []
    one_zero_saver = []
    finish_sign = -1 
    result=""
       
    if num == 0:
        return "0b0"
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

def change_to_decimal(num: int):
   
    """
    Convert a binary number to a decimal number.
    
    Note:
        This function currently only supports positive numbers.
        
        Negative numbers are not handled in this script. 
        Implementation of the following numeric systems will be done in a separate repository:
            - One's Complement
            - Two's Complement
            - Unsigned (no sign)
        Addition and subtraction operations in these systems will also be implemented there.
    """
    
  
    save_binary = []
    sum_bit_value = 0
    
    if num == 0 :
        return 0
    elif num < 0 :
          raise NotImplementedError(
            "Negative numbers are not supported in this function. "
            "This feature will be implemented in the separate complement systems repository."
        )
    
    else:
        
        str_num = str(num)
        for i in str_num:
            save_binary.append(i)
            
        bit_value = len(save_binary)-1
        for i in save_binary:
            if int(i) == 1:  
                    z=int(i)
                    z =  2**bit_value
                    sum_bit_value +=z
                    bit_value -= 1 
                    if bit_value < 0:
                        break
            else:
                bit_value -= 1
                if bit_value < 0:
                        break 
        return sum_bit_value 
          
while True:
    print("\n" + "="*40)
    menu_number = int(input("Welcome change to binary menu \n1)Change to binary\n2)Change to decimal\n3)exit\nselect your number :: "))
    print("="*40)
    if menu_number == 1:
        num = int(input("Enter your number:: "))
        show_result = f"Answer is :: {change_to_binary(num)}"
        print(show_result)
    elif menu_number == 2:
        num = int(input("Enter your number:: "))
        show_result = f"Answer is :: {change_to_decimal(num)}"
        print(show_result)
    elif menu_number == 3:
       break
    else:
        continue
    
