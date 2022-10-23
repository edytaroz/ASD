from egz1atesty import runtests
from queue import PriorityQueue
#Edyta Rozczypała
#Algorytm polega na dodaniu wszystkich elementów do kolejki priorytetowej, następnie
#wchodzimy do pętli z iteratorem d oznaczającym ilość dni, podczas których będziemy
#mogli zbierać śnieg. Każdego dnia wyciągana jest kolejna największa liczba z
#kolejki i dodawana do sumy. Obliczamy też sumę stopioneko śniego w trakcie d dni
#i odejmujemy je od naszej sumy. Sprawdzamy czy suma jest większa od dnia poprzedniego
#i jeśli jest to ją zamieniamy. Kończymy pętle jeśli suma stopionego śniegu jest
#większa od maksymalnej sumy zebranego śniegu.Złożoność algorytmnu to O(n log n)
#Uwaga techniczna, u mnie w testach tablica S była przedstawiona jako [[liczby]]
#dlatego na początku kodu robię S=S[0], gdyby tablica była przedstawiona [liczby]
#ta linijka byłaby zbędna i nie zostałaby wpisana do kodu.


def frog(S):
    #S = S[0]
    n = len(S)
    maks = 0
    sum = 0
    st_snieg = 0
    Q = PriorityQueue()
    for i in range(n):
        Q.put(-S[i])
    for d in range(1,n+1):
        st_snieg += (d-1)
        a = abs(Q.get())
        sum += a
        sum -= st_snieg
        if sum > maks:
            maks = sum
        sum += st_snieg
        if st_snieg > maks:
            break
    return maks

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    return frog(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
