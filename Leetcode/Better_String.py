def count_distinct_subsequences(s, index, memo):
    if index == -1:
        return 1  
    
    if index in memo:
        return memo[index]  
    
    include = count_distinct_subsequences(s, index - 1, memo)
    
    exclude = 0
    last_occurrence = {}
    
    for j in range(index):
        last_occurrence[s[j]] = j 
    
    if s[index] in last_occurrence:
        exclude = count_distinct_subsequences(s, last_occurrence[s[index]] - 1, memo)
    
    memo[index] = include + (include - exclude)
    return memo[index]

def better_string(str1, str2):
    count1 = count_distinct_subsequences(str1, len(str1) - 1, {})
    count2 = count_distinct_subsequences(str2, len(str2) - 1, {})
    
    return str1 if count1 >= count2 else str2

# Example usage
str1 = "gfg"
str2 = "ggg"
print(better_string(str1, str2))  # Output: "gfg"
