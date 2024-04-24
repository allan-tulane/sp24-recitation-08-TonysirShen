from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):

  def dijkstra_helper(visited, frontier):
    while frontier:
      distance, edges, node = heappop(frontier)  ### get current
      if node not in visited:
        visited[node] = (distance, edges)
        for neighbor, weight in graph[node]:  ### visting neighbours
          edges += 1
          distance += weight
          heappush(frontier, (distance, edges, neighbor))
    return visited

  frontier = []
  heappush(frontier, (0, 0, source))
  visited = {}
  return dijkstra_helper(visited, frontier)


def bfs_path(graph, source):

  def bfs_helper(visited, frontier, parents):
    while frontier:
      current = frontier.pop()
      visited.add(current)
      children = graph[current]
      for node in children:
        if node not in parent:
          parents[node] = current
        if node not in visited:
          frontier.append(node)
    return parents

  visited = set()
  frontier = deque()
  parent = {}
  frontier.append(source)
  return bfs_helper(visited, frontier, parent)


graph = {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}
print(bfs_path(graph, 's'))


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
  if destination not in parents:
    return ''
  else:
    parent = parents[destination]
    return get_path(parents, parent) + parent


print(get_path(bfs_path(graph, 's'), 'd'))

graph = {
    's': {('a', 1), ('c', 4)},
    'a': {('b', 2)},  # 'a': {'b'},
    'b': {('c', 1), ('d', 4)},
    'c': {('d', 3)},
    'd': {},
    'e': {('d', 0)}
}

result = shortest_shortest_path(graph, 's')
print(result)
