_swap = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

visited = dict()
parent = dict()

src = list()
dst = list()


def int_to_list(ii):
    ll = list()
    while ii != 0:
        ll.append(ii % 10)
        ii = ii // 10
    ll.reverse()
    return ll


def list_to_int(ll):
    value = 0
    ii = 0
    while ii < 9:
        value = value * 10
        value = value + ll[ii]
        ii = ii + 1
    return value


def bfs():
    _blank = src.index(9)
    s = list_to_int(src)
    visited[s] = True
    parent[s] = -1
    q = list()
    q.append([s, _blank])
    while len(q) != 0:
        _from = q[0]
        del(q[0])
        _fromList = int_to_list(_from[0])
        for to in _swap[_from[1]]:
            l = _fromList[to]  # swapping
            _fromList[to] = _fromList[_from[1]]
            _fromList[_from[1]] = l
            toNum = list_to_int(_fromList)
            if toNum not in visited.keys():
                visited[toNum] = True
                parent[toNum] = _from[0]
                q.append([toNum, to])

            l = _fromList[to]  # swapping
            _fromList[to] = _fromList[_from[1]]
            _fromList[_from[1]] = l


# initial matrix
print("Give initial Matrix (represent blank by #) : \n")
for i in range(3):
    ch = input().split()
    src.extend(ch)
src[src.index('#')] = '9'

for i in range(9):
    src[i] = int(src[i])

# final matrix
print("Give final Matrix (represent blank by #) : \n")
for i in range(3):
    ch = input().split()
    dst.extend(ch)
dst[dst.index('#')] = '9'

for i in range(9):
    dst[i] = int(dst[i])

bfs()
path = list()

to = list_to_int(dst)
if to not in visited:
    print("Solve Yourself ! ")
else:
    while to != -1:
        path.append(to)
        to = parent[to]

    path.reverse()
    for i in path:
        mat = int_to_list(i)
        for ii in range(3):
            for jj in range(3):
                if mat[ii * 3 + jj] == 9:
                    print('#', end=' ')
                else:
                    print(mat[ii * 3 + jj], end=' ')
            print()
        print()
