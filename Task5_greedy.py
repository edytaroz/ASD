
from queue import PriorityQueue

#Deklarujemy kolejke priorytetową. Wkładamy do niej te indeksy i ich wartości,
#kóre są w naszym zasięgu i których wartości nie są równe 0. Wtedy zdejmujemy
#największą wartość z kolejki i dodajemy ją do zasięgu. Powtarzamy aż zasięg
#będzie większy od tablicy albo przejdziemy przez całą tablicę. Sortujemy wynikową
#tablicę. Złożoność pamięciowa to O(n) a czasowa O(n log n )


def pq_frog(T):
    n =len(T)
    lilie = PriorityQueue()
    skok = T[0]
    l = [0]
    for i in range(1,n):
        if skok < n - 1:
            if T[i] != 0:
                lilie.put((-T[i],i))
            if i == skok:
                maks = lilie.get()[1]
                l.append(maks)
                skok += T[maks]
    l.sort()
    return l
