def convert_to_binary(n:int)->str:
    res=""
    while n>0:
        if n%2==1:
            res+="1"
        else:
            res+="0"
        n = n//2
    return res[::-1]

#print(convert_to_binary(13))

def convert_to_decimal(s:str):
    n=len(s)
    pow=1
    num=0
    for i in range(n-1,-1,-1):
        if s[i]=="1":
            num = num+pow
        pow=pow*2
    return num


def is_kth_bit_set(n: int, k: int) -> bool:
    return(n&(1<<k))!=0

#print(is_kth_bit_set(4, 0))
#print(is_kth_bit_set(4, 2))

def set_kth_bit(n: int, k: int) -> bool:
    return(n|(1<<k))!=0

def clear_kth_bit(n: int, k: int) -> bool:
    return(n&~(1<<k))

def remove_last_set_bit(n:int):
    return n & n-1
