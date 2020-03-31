import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# UDP data
list=['0110011001100000','0101010101010101','1000111100001100']

length=len(list)

values=[]
for num in list:
    values.append(int(num,2))

sum1=0
for j in values:
    sum1= sum1+ j

# wraparound
ov=int('1'+'0'*16,2)
if(sum1>=ov):
    sum=bin(sum1%ov+1)[2:]
else:
    sum=bin(sum1)[2:]

# fill 0
if(len(sum)<16):
    sum='0'*(16-len(sum))+ sum
print("sum:",sum)

# sum → checksum
checksum=''
for char in sum:
    if (char=='0'):
        checksum=checksum+'1'
    else:
        checksum=checksum+'0'
print("checksum:",checksum)

check_value=int(checksum,2)
if (sum1 >= ov):
    result = bin( (sum1 + check_value)% ov + 1)[2:]
else:
    result = bin(sum1 + check_value)[2:]
print("result:",result)

# check if result equals 111111111111111
if(result=='1'*16):
    print("check success!")


# plot
axbox=[]
text_box=[]
for ii in range(length):
    axbox.append(plt.axes([0.4, 0.75-ii*0.1, 0.25, 0.06]))
    text_box.append(TextBox(axbox[ii], '16-bit data'+str(ii+1)+' ', initial=list[ii]))
axbox1 = plt.axes([0.4, 0.75-length*0.1, 0.25, 0.06])
text_box1 = TextBox(axbox1, 'sum:', sum)
axbox2 = plt.axes([0.4, 0.65-length*0.1, 0.25, 0.06])
text_box2 = TextBox(axbox2, 'checksum:', checksum)

plt.show()