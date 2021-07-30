def mergeSort(A):
    print('begin, A =', A)
    if len(A) > 1:
        L, R = A[:len(A) // 2], A[len(A) // 2:]
        print('if len(A) > 1:')
        print('A =', A, ', L =', L, ', R =', R)
        mergeSort(L)
        print('mergeSort(L)')
        print('A =', A, ', L =', L, ', R =', R)
        mergeSort(R)
        print('mergeSort(R)')
        print('A =', A, ', L =', L, ', R =', R)
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            print('while i < len(L) and j < len(R):')
            print('A =', A, ', L =', L, ', R =', R)
            if L[i] <= R[j]:
              A[k] = L[i]
              i += 1
              print('if L[i] <= R[j]:')
              print('A =', A, ', L =', L, ', R =', R, ', i =', i)
            else:
                A[k] = R[j]
                j += 1
                print('else:')
                print('A =', A, ', L =', L, ', R =', R, ', j =', j)
            k += 1
            print('k = ', k)
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
            print('while i < len(L)')
            print('A=', A, ', L =', L, ', R =', R, ', i =', i, ', k =', k)
        while j < len(R):
            A[k]=R[j]
            j += 1
            k += 1
            print('while j < len(R)')
            print('A=', A, ', L =', L, ', R =', R, ', j =', j, ', k =', k)
A = [8,7,6,5]
mergeSort(A)
print(A)
