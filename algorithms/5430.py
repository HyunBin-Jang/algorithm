from sys import stdin, stdout
T = int(input())

for _ in range(T):
    operations = input()
    n = int(input())
    if n == 0:
        input()
        sequence = []
    elif n == 1:
        sequence = [int(stdin.readline().lstrip('[').rstrip().rstrip(']'))]
    else:
        sequence = list(map(int, stdin.readline().lstrip('[').rstrip().rstrip(']').split(',')))
    R_count = 0
    error = False
    for p in operations:
        if p == 'R':
            R_count += 1
        else:
            if n == 0:
                error = True
                break
            if R_count % 2 == 0:
                sequence.pop(0)
                n -= 1
            else:
                sequence.pop()
                n -= 1
    if error:
        stdout.write("error\n")
    elif n == 0:
        stdout.write("[]\n")
    else:
        if R_count % 2 == 0:
            stdout.write('[')
            stdout.write(str(sequence[0]))
            for i in range(1, n):
                stdout.write(',')
                stdout.write(str(sequence[i]))
            stdout.write(']\n')
        else:
            sequence.reverse()
            stdout.write('[')
            stdout.write(str(sequence[0]))
            for i in range(1, n):
                stdout.write(',')
                stdout.write(str(sequence[i]))
            stdout.write(']\n')