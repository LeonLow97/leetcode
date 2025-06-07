from collections import deque

def bfs_traversal(graph, start_node):
	visited = set()

	q = deque()
	q.append(start_node)
	visited.add(start_node)

	while q:
		parent = q.popleft()

		if parent in graph:
			for child in graph[parent]:
				if child not in visited:
					q.append(child)
					visited.add(child)

	return sorted(list(visited))

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
			"expected": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		},
		{
			"title": "disconnected graph",
			"input_graph": {
				0: [1],
				2: [3],
				4: []
			},
			"input_start_node": 0,
			"expected": [0, 1]
		},
		{
			"title": "single node graph",
			"input_graph": {},
			"input_start_node": 42,
			"expected": [42]
		},
		{
			"title": "self loop",
			"input_graph": {
				1: [1]
			},
			"input_start_node": 1,
			"expected": [1]
		},
		{
			"title": "start from isolated node",
			"input_graph": {
				0: [1],
				2: [],
				3: [4],
			},
			"input_start_node": 2,
			"expected": [2]
		},
		{
			"title": "undirected graph (bidirectional edges)",
			"input_graph": {
				0: [1],
				1: [0, 2],
				2: [1]
			},
			"input_start_node": 0,
			"expected": [0, 1, 2]
		}
	]

	all_tests_pass = True
	for test in test_cases:
		actual = bfs_traversal(test["input_graph"], test["input_start_node"])
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
