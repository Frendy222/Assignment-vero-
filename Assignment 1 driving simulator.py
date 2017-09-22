t = int(input('Time spend on road :'))+1
a = int(input('Acceleration :'))
d = int(input('Distance :'))
speedlimit = 60
iv = 0
v = 0
s = 0

for i in range (t) :
    v = iv*a
    s = a/2*iv*iv
    star=s/10
    print('Duration:',i,'Distance:','*'*int(star))
    iv+=1
if (v>speedlimit):
    print('\nThis person went over the speed limit( Max speed :',v,' )')
else :
    print('\nThis person does not went over the speed limit( Max speed :',v,' )')
if (s>d):
    print('This person reach the destination( Max distance :',s,' )')
else:
    print('This peron does not reach the destination( Max distance :',s,' )')
