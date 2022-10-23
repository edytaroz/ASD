from egz1btesty import runtests
#Edyta Rozczypała
#Najpierw uzupełniamy wartości x w drzewie. Będzie to tablica z poziomami, na których
#znajdują się liście w poddrzewie danego wierzchołka. Następnie sortujemy niemalejąco
#tablice z poziomami w korzeniu, a potem tworzymy inną tablicę bez powtórzonych
#poziomów. Następnie dla każdego poziomu z tablicy uruchamiamy algorytm szukający
#minimalnej liczby uciętych krawędzi do otrzymania ładnego drzewa. Złożoność O(n*n)



class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = []         # pole do wykorzystania przez studentow

def is_leaf(T,h):
    if T.left is None and T.right is None and T is not None:
        T.x.append(h)
    elif T.left is None and T.right is not None:
        is_leaf(T.right,h+1)
        T.x.extend(T.right.x)
    elif T.right is None and T.left is not None:
        is_leaf(T.left,h+1)
        T.x.extend(T.left.x)
    elif T.right is not None and T.left is not None and T is not None:
        is_leaf(T.left,h+1)
        is_leaf(T.right,h+1)
        T.x.extend(T.right.x)
        T.x.extend(T.left.x)


def change(T,d,counter,h):
    c = 0
    if T.left is None and T.right is not None:
        if d not in T.right.x and max(T.right.x) < d:
            counter += 1
        elif d not in T.right.x and max(T.right.x) > d:
            if h == d:
                counter += 1
            else:
                c = change(T.right,d,counter,h+1)
        else:
            c = change(T.right,d,counter,h+1)
    elif T.right is None and T.left is not None:
        if d not in T.left.x and max(T.left.x) < d:
            counter += 1
            c = change(T.left,d,counter,h+1)
        elif d not in T.left.x and max(T.left.x) > d:
            if h == d:
                counter += 1
            else:
                c = change(T.left,d,counter,h+1)
        else:
            c = change(T.left,d,counter,h+1)
    elif T.right is not None and T.left is not None:
        if d not in T.right.x and d not in T.left.x:
            if max(T.right.x) < d and max(T.left.x) < d:
                counter += 2
            elif max(T.right.x) < d and max(T.left.x) > d:
                c = change(T.left,d,counter,h+1)
                counter += 1
            elif max(T.right.x) > d and max(T.left.x) < d:
                c = change(T.right, d, counter, h + 1)
                counter += 1
            else:
                if h == d:
                    counter += 2
                else:
                    a = change(T.right, d, counter, h + 1)
                    b = change(T.left, d, counter, h + 1)
                    c = a + b
        elif d not in T.right.x and d in T.left.x:
            if max(T.right.x) < d:
                c = change(T.left,d,counter,h+1)
                counter += 1
            else:
                a = change(T.left,d,counter,h+1)
                b = change(T.right,d,counter,h+1)
                c = a + b
        elif d in T.right.x and d not in T.left.x:
            if max(T.left.x) < d:
                c = change(T.right, d, counter, h + 1)
                counter += 1
            else:
                a = change(T.left, d, counter, h + 1)
                b = change(T.right, d, counter, h + 1)
                c = a + b
        else:
            if h == d:
                counter += 2
            else:
                a = change(T.right,d,counter,h+1)
                b = change(T.left,d,counter,h+1)
                c = a + b
    return counter + c


def wideentall( T ):
    # tu prosze wpisac wlasna implementacje
    is_leaf(T,0)
    T.x.sort()
    n = len(T.x)
    heights = [T.x[0]]
    for i in range(n-1):
        if T.x[i] != T.x[i+1]:
            heights.append(T.x[i+1])
    mins = 10**10
    for i in range(len(heights)):
        a = change(T,heights[i],0,0)
        if a <= mins:
            mins = a
    return mins

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )