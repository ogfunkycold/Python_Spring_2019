print('')
a = int(input('Enter Integer 1: '))
b = int(input('Enter Integer 2: '))
c = int(input('Enter Integer 3: '))

amod = a%2
bmod = b%2
cmod = c%2

num_odd = amod+bmod+cmod
num_even = 3-num_odd

all_sum = a+b+c
odd_sum = a*amod+b*bmod+c*cmod
even_sum = all_sum - odd_sum

odd_string = str(a)*amod + ' ' + str(b)*bmod + ' '+str(c)*cmod
even_string = str(a)*(1-amod) + ' ' + str(b)*(1-bmod) + ' '+str(c)*(1-cmod)

print('')
print('You supplied the numbers: ', a,b,c)
print('Their sum is ',all_sum,'.',sep='')
print('')
print('There are',num_odd,'odd numbers.')
print('They are: ',odd_string)
print("Their sum is ",odd_sum,'.',sep='')
print('')
print('There are',num_even,'even numbers.')
print('They are: ',even_string)
print("Their sum is ",even_sum,'.',sep='')
print('')


