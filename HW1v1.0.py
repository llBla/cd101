print("Enter number of composers:")
n = int(input())
m = int(5)
mid = float(0.0)
composers = []
words = ['Name:', 'Last Name:', 'Birth:', 'Death:']
print('Enter composers information')
for i in range(n):
    composers.append([0]*m)
    print(f'\nComposer {i+1}')
    for j in range(m-1):
        print(f'{words[j]}')
        composers[i][j] = input()
    composers[i][m-1] = int(int(composers[i][m-2]) - int(composers[i][m-3]))
    mid = mid + composers[i][m-1]

    print('\nIn result:')
for i in range(n):
    print(f'\nComposer {i+1} \nName: {composers[i][0]} Last name: {composers[i][1]} Age: {composers[i][-1]}\n')

print('Middle age: %.0f' % (mid/n))