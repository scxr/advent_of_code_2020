with open('pwords.txt','r') as f:
    pwords = f.read().split('\n')
allowed = 0

for i in pwords:
    tmp = i.split()
    print(tmp)
    min = tmp[0].split('-')[0]
    max = tmp[0].split('-')[1]
    letter = tmp[1][0]
    cnt = 0
    for i in tmp[2]:
        if i == letter:
            cnt += 1
       
    if cnt <= int(max) and cnt >= int(min):
        allowed += 1
            
print(allowed)


def find(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
allowed = 0
for i in pwords:
    tmp = i.split()
    min = tmp[0].split('-')[0]
    max = tmp[0].split('-')[1]
    letter = tmp[1][0]
    indexes = find(tmp[2], letter)
    shifted_indexes = [str(i+1) for i in indexes]
    if min in shifted_indexes and max in shifted_indexes:
        pass
    elif min in shifted_indexes:
        allowed += 1
    elif max in shifted_indexes:
        allowed += 1
    else:
        pass
print(allowed)