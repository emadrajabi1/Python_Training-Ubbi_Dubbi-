def Ubbi_Dubbi(text):
    
    vowels =['a','e','i','o','u']
    output = []

    for char in text:
        if char.lower() in vowels:
            output.append('ub')
            output.append(char)
        else:
            output.append(char)
            
    return ''.join(output)

if __name__ =='__main__':
    while True:
        user_input = input("Tell your word: ")
        
        if user_input.lower() in ("exit", "quit","Esc",""):
            print("Bye!")
            break
        print(Ubbi_Dubbi(user_input))
 
        