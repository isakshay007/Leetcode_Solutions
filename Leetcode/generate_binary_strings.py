def generate_binary_strings(n,output="",last_digit="0"):
    if n == 0:
        print(output)
        return 
    
    generate_binary_strings(n-1,output+"0","0")

    if last_digit == "0":
        generate_binary_strings(n-1,output+"1","1")

k = 3
generate_binary_strings(k)