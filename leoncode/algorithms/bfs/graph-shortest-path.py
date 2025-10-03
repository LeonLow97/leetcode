from collections import deque

def bfs_shortest_path(graph, start_node, end_node):
	# start node same as end node
	if start_node == end_node:
		return [start_node]

	visited = set()
	childToParent = {}

	q = deque()
	q.append(start_node)
	visited.add(start_node)

	while q:
		parent = q.popleft()

		if parent == end_node:
			break
		
		if parent in graph:
			for child in graph[parent]:
				if child not in visited:
					q.append(child)
					childToParent[child] = parent
					visited.add(child)

	# No path found, return None
	if end_node not in childToParent:
		return None

	path = [end_node]
	current = end_node
	while current != start_node:
		current = childToParent[current] # assume a child node only has 1 parent node
		path.append(current)

	path.reverse()
	return path

def tests():
	test_cases = [
		{
			"title": "multiple nodes",
			"input_graph": {
				0: [3, 5, 9],
				1: [6, 7, 4],
				2: [10, 5],
				3: [0],
				4: [1, 5, 8],
				5: [2, 0, 4],
				6: [1],
				7: [1],
				8: [4],
				9: [0],
				10: [2]
			},
			"input_start_node": 0,
			"input_end_node": 1,
			"expected": [0, 5, 4, 1]
		},
		{
			"title": "parent start node connected directly to child",
			"input_graph": {
				1: [2, 3],
				2: [1, 3],
				3: [1, 2]
			},
			"input_start_node": 1,
			"input_end_node": 3,
			"expected": [1, 3]
		},
		{
			"title": "start equals end node",
			"input_graph": {
				1: [2],
				2: [3],
				3: []
			},
			"input_start_node": 2,
			"input_end_node": 2,
			"expected": [2]
		},
		{
			"title": "no path between nodes",
			"input_graph": {
				1: [2],
				2: [],
				3: [4],
				4: []
			},
			"input_start_node": 1,
			"input_end_node": 4,
			"expected": None  # You should return None if path doesn't exist
		},
		{
			"title": "cyclic graph",
			"input_graph": {
				1: [2],
				2: [3],
				3: [1]
			},
			"input_start_node": 1,
			"input_end_node": 3,
			"expected": [1, 2, 3]
		},
		{
			"title": "disconnected graph",
			"input_graph": {
				1: [2],
				2: [],
				3: [],
				4: []
			},
			"input_start_node": 1,
			"input_end_node": 3,
			"expected": None
		}
	]

	all_tests_pass = True
	for test in test_cases:
		actual = bfs_shortest_path(test["input_graph"], test["input_start_node"], test["input_end_node"])
		if actual != test["expected"]:
			print("FAIL:", test["title"])
			all_tests_pass = False
		else:
			print("PASS:", test["title"])
	
	return all_tests_pass

if tests():
	print("✅ All tests passed!")
else:
	print("❌ Some test(s) failed!")
