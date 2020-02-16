def perfect_number(x):
  divisors = []
  running_total = 0
  
  #determines what the numbers divisors are
  #note: the list of divisors doesn't include the number itself
  for i in range(1,x):
    if x%i==0:
      divisors.append(i)
      
  #sums the divisors
  for number in divisors:
    running_total += number
  
  #checks whether the number is equal to the sum of its divisors
  if x == running_total:
    print(str(x) + " is a perfect number.")
  else:
    print(str(x) + " is not a perfect number.")

