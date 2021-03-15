#Summations: Tasks
#1+2+3....+98+99

sum = 0
for i in range(1, 100, 1) :
    sum = sum + i
print(sum)


#2+4+6+.....+48+50
s = 0
for i in range(2, 51, 2) :
    s = s + i
print(s)

# 3(1)^2 + 3(2)^2 +.....+3(500)^2
sumsq = 0
for i in range(1, 501) :
    sumsq += i**2

print(3*sumsq)

#(3k-2) for k in (-50, 100)
newSum = 0
for i in range(-50, 100, 1) :
    newSum += 3*i-2
print(newSum)

#100(j+1)^2 for j in (-50, 100)
nSum = 0
for i in range(-50, 100) :
    nSum += 100*(i+1)**2
print(nSum)

#Calculate sum of the areas of circles whose radii are 1, 2, 3, ….. 100 cm. 
sumArea = 0
for radii in range(1, 101) :
    sumArea += 3.14*radii**2
print(sumArea)

#Calculate sum of the areas of a rectangle whose sides are (1,0.5), (2,1), (3,1.5) ….. (100,50) cm. 
sumRect = 0
for i in range(1, 101) :
    b = 0.5*i
    sumRect += i*b
print(sumRect)

#I change the question: calculate sum of the areas of a rectangle whose sides are (1,0.001), (2,0.001),(3,0.00.1) ….. (100,0.001) cm. 
sumrec = 0
for i in range(1, 101) :
    sumrec += i*0.001
print(sumrec)
#Once you finish these code: write a code in such a way that it should ask you to enter ranges of a series summation. You can use any of these series for example. 
begin = int(input('Enter the first term: '))
end = int(input('Enter the last term: '))

#Series: (3k - 2)
kSum = 0
for k in range(begin, end+1) :
    kSum += 3*k - 2
print(kSum)







