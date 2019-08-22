def factorial(n): 
      f = 1
    if (n == 0 or n == 1): 
        return 1
    for i in range(2, n + 1): 
        f = f * i 
    return f 
  def getSum(arr, n): 
      fact = factorial(n) 
         digitsum = 0
    for i in range(n): 
        digitsum += arr[i] 
    digitsum *= (fact // n) 
       res = 0
    i = 1
    k = 1
    while i <= n : 
        res += (k * digitsum) 
        k = k * 10
        i += 1
      return res 
  if __name__ == "__main__": 
      arr = [1, 2, 3] 
    n = len(arr) 
          print(getSum(arr, n)) 
  
