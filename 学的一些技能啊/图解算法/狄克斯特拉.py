"""
广度优先适用于非加权图中搜索最短路径
狄克斯特拉用于在加权图中搜索最短路径
权重为负数时不能使用狄克斯特拉，使用贝尔曼-福德算法
"""
graph={}

#存储边节点
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2

graph["a"]={}
graph["a"]["fin"]=1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5

graph["fin"]={}

#开销表
infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

#存储父节点
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

#处理过的结点
processed=[]

#开销最小的结点
def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=costs[node]
            lowest_cost_node=node
    return lowest_cost_node

#实现狄克斯特拉算法
node=find_lowest_cost_node(costs)
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if new_cost<costs[n]:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)
    node=find_lowest_cost_node(costs)

print(costs)
