
class DancingLinks(object):

    class Node(object):
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

            if self.prev is not None:
                self.prev.next = self

            if self.next is not None:
                self.next.prev = self

        def __repr__(self):
            return 'Node(%s)' % repr(self.value)

    def __init__(self, lst=None):
        self.front = None
        self.back = None
        self.count = 0

        if lst is not None:
            for value in lst:
                self.append(value)

    def append(self, value):
        self.count += 1
        self.back = DancingLinks.Node(value, self.back)
        if self.front is None:
            self.front = self.back

    def erase(self, node):
        self.count -= 1

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node == self.front:
            self.front = node.next

        if node == self.back:
            self.back = node.prev

    def restore(self, node):
        self.count += 1

        if node.prev is not None:
            node.prev.next = node

        if node.next is not None:
            node.next.prev = node

        if node.next == self.front:
            self.front = node

        if node.prev == self.back:
            self.back = node

    def __len__(self):
        return self.count

    def __repr__(self):
        cur = self.front
        lst = []
        while cur is not None:
            lst.append(cur)
            cur = cur.next
        return 'DancingLinks([%s])' % ', '.join(map(repr, lst))


def ordered_set_partitions(lst, parts):

    dl = DancingLinks(lst)
    res = [ [ None for j in range(parts[i]) ] for i in range(len(parts)) ]

    def gen(at):

        if at == len(parts):
            yield [ [ res[i][j] for j in range(parts[i]) ] for i in range(len(parts)) ]
        else:

            def make_part(pat, cur, left):
                if pat == parts[at]:
                    yield res
                elif left >= parts[at] - pat:

                    res[at][pat] = cur.value
                    dl.erase(cur)
                    for r in make_part(pat + 1, cur.next, left - 1):
                        yield r

                    dl.restore(cur)

                    for r in make_part(pat, cur.next, left - 1):
                        yield r

            for p in make_part(0, dl.front, len(dl)):
                for g in gen(at + 1):
                    yield g

    return gen(0)

