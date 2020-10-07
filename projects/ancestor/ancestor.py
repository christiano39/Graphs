class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def get_parents(child, ancestors):
    parents = []

    for pair in ancestors:
        if pair[1] == child:
            parents.append(pair[0])
    
    if len(parents) == 0: return None

    return parents
        

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    paths = []

    q.enqueue([starting_node])

    # bfs that gets all paths of parents
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if get_parents(v, ancestors) is None:
            paths.append(path)
        else:
            for p in get_parents(v, ancestors):
                path_copy = path + [p]
                q.enqueue(path_copy)

    # filter out only the longest paths
    longest_paths = []
    longest = paths[0]
    for path in paths:
        if len(path) == len(longest):
            longest_paths.append(path)
        elif len(path) > len(longest):
            longest = path
            longest_paths = [path]

    #if there is a tie for longest path, grab the smallest numeric ID
    smallest_id = longest_paths[0][-1]
    for path in longest_paths:
        if path[-1] < smallest_id:
            smallest_id = path[-1]

    if smallest_id == starting_node:
        return -1

    return smallest_id