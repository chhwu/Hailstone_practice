count = 0

print('This program computes Hailstone sequences.')
old_num = int(input('Enter a number: '))
while old_num != 1:
    if old_num % 2 == 0:
        new_num = old_num / 2
        count += 1
        print('%d is even, so I take half: %d' % (old_num, new_num))
        old_num = new_num
    else:
        new_num = old_num * 3 + 1
        count += 1
        print('%d is odd, so I make 3n + 1: %d' % (old_num, new_num))
        old_num = new_num

print('It took %d steps to reach 1.' % count)