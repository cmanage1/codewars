def persistence(n):
    count =0 
    num_arr= [int(j) for j in str(n) ] #putting digits in array
    
    while (len(num_arr)) > 1:
        product= 1
        for i in range (0, len(num_arr) ):
            product *= num_arr[i] #multiplying indexes of array
        count += 1
        num_arr= [int(j) for j in str(product) ] 
    return count
