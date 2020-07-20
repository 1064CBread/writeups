# Picking Up The Pieces
## Challenge Description
Can you help me? I had a flag that I bought at the store, but on the way
home, I dropped parts of it on some roads! Now some roads have strings of text,
and I can't tell which are part of my flag. I'm very smart and efficient (but
somehow not smart or efficient enough to keep my flag), so I know that I took
the fastest way from the store back to my house.

I have a map with a list of all 200000 roads between intersections, and what
strings are on them. The format of the map is <intersection 1> <intersection
2> <distance> <string on the road>. My house is at intersection 1 and the
store is at intersection 200000.

File: map.txt

## Solution

The prompt is asking for the "fastest way" ([shortest
path](https://en.wikipedia.org/wiki/Shortest_path_problem)) between two
intersections (vertices) in a map (graph) consisting of roads (edges). The
answer is usually [Dijkstra's
algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

The following Python 3 script (adapted from [this
gist](https://gist.github.com/kachayev/5990802)) finds the shortest path and
prints out the pieces collected along the way:

    from collections import defaultdict
    from heapq import *


    def dijkstra(graph, start, end):
        q = [(0, start, "", "")]
        seen = set()
        mins = {start: 0}
        while q:
            (total, a, chunk, path) = heappop(q)
            if a not in seen:
                seen.add(a)
                path += chunk
                if a == end:
                    return path
                for distance, b, chunk in graph.get(a, ()):
                    if b in seen: continue
                    prev = mins.get(b, None)
                    next = total + distance
                    if prev is None or next < prev:
                        mins[b] = next
                        heappush(q, (next, b, chunk, path))


    graph = defaultdict(list)
    with open("map.txt", "r") as fp:
      for line in fp:
        start, end, distance, chunk = line.strip().split(" ")
        graph[start].append((int(distance), end, chunk))
        graph[end].append((int(distance), start, chunk))
    print(dijkstra(graph, "1", "200000"))

This prints the following string:

    m1amJL5WAQ5Pj5mP}e1Eggs,HandSanitizer,Fruit,Soap,Pizza,IceCream,Bleach,Bread,Milk,Politicians,MacAndCheese,ToiletPaper,rgbCTF{1m_b4d_4t_sh0pp1ng},Cookies,Water,Rice,TomBrady,NewcastleUnited,YourSoul

Oh look, a flag.


## Flag

`rgbCTF{1m_b4d_4t_sh0pp1ng}`

### Author
[DeepToaster](https://github.com/deeptoaster)