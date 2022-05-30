def SortH(p,k):
    def merge_sort(p):
        def merge_div(p):
            if p.next is not None:
                f = p
                fast = f.next
                count = 1
                while fast.next is not None and fast.next.next is not None:
                    count += 1
                    f = f.next
                    fast = fast.next.next
                prev = f
                new = Node()
                new.next = f.next
                prev.next = None
                new = new.next
                tuple = (p, new)
                return tuple

        def merge(first, first2):
            if first is None:
                return first2
            if first2 is None:
                return first
            if first.next is None and first2.next is None:
                if first.val > first2.val:
                    first2.next = first
                    return first2
                else:
                    first.next = first2
                    return first
            g = Node()
            g.next = first
            prev = g
            a = g
            while first is not None and first2 is not None:
                if first.val < first2.val:
                    prev = first
                    first = first.next
                elif first.val == first2.val:
                    tmp = first.next
                    prev = first
                    first.next = first2
                    tmp2 = first2.next
                    first2.next = tmp
                    first2 = tmp2
                    first = first.next
                else:
                    tmp = first
                    prev.next = first2
                    tmp2 = first2.next
                    first2.next = tmp
                    prev = prev.next
                    first = prev.next
                    first2 = tmp2
            if first2 is not None:
                prev.next = first2
            return a.next

        def mergesort(p):
            if p is not None and p.next is not None and p.next.next is not None:
                tup = merge_div(p)
                a = tup[0]
                b = tup[1]
                c = mergesort(a)
                d = mergesort(b)
                e = merge(c, d)
                return e
            else:
                if p is None:
                    return p
                elif p is not None and p.next is None:
                    return p
                elif p is not None and p.next is not None:
                    if p.val > p.next.val:
                        tmp = p
                        p.next.next = tmp
                        tmp2 = p.next
                        p.next = None
                        return tmp2
                return p

        return mergesort(p)

    def bubble(p, k):
        g = Node()
        temp = p.next
        p.next = g.next
        g.next = p
        g.next.next = temp
        prev = g
        f = prev.next
        flag = False
        n = 0
        while flag is not True and n < k:
            n += 1
            flag = True
            prev = g
            f = prev.next
            while f.next is not None:
                if f.val > f.next.val:
                    flag = False
                    tmp = f
                    prev.next = f.next
                    f = prev.next
                    tmp2 = f.next
                    f.next = tmp
                    f.next.next = tmp2
                prev = f
                f = f.next
        return g.next
    if k <= 10:
        return bubble(p,k)
    else:
        return merge_sort(p)
