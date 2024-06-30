#dfs algorithm
graph = {
    '0':['1', '2'], '1':['2'],'2':['3'],'3':['1', '2']
}
visited =set()
def dfs(visited,graph,root):
    if root not in visited:
       print(root)
       visited.add(root)
       for neighbour in graph[root]:
          dfs(visited,graph,neighbour)
print("the following is depth first search:")
dfs(visited,graph,'0')
