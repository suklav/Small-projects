#send + more =money
#cryptarithmetic

for s in range(10):
 for e in range(10):
  for n in range(10):
   for d in range(10):
    for m in range(10):
     for o in range(10):
      for r in range(10):
       for y in range(10):
        send = 1000*s + 100*e + 10*n + d
        more = 1000*m + 100*o + 10*r + e
        more = 10000*m + 1000*o + 100*n + 10*e + y
        
        if send + more == money :
         if s!=e and s!=n and s!=d and s!=m and s!=o and s!=r and s!=y and e!=n and e!=d and e!=m and e!=o and e!=r and e!=y and n!=d and n!=m and n!=o and n!=r and n!=y and d!=m and d!=o and d!=r and d!=y and m!=o and m!=r and m!=y and o!=r and o!=y and r!=y :
         print(send," + ", more," = ",money)
