import sys
INT_MAX = sys.maxint

def find_minRow(cost_matrix, n):
	_min = [];
	for i in range(n):
		_min.append(min(cost_matrix[i]))
	return _min

def find_minCol(cost_matrix, n):
	_min = [];
	for i in range(n):
		min_ = INT_MAX
		for j in range(n):
			min_ = min(min_, cost_matrix[j][i])
		_min.append(min(cost_matrix[i]))
	return _min

def subtractMinRow(cost_matrix, minEachRow, n):
	for i in range(n):
		to_sub = minEachRow[i]
		cost_matrix[i][:] = [x-to_sub for x in cost_matrix[i]]
	return cost_matrix	


def subtractMinCol(cost_matrix, minEachCol, n):
	for i in range(n):
		to_sub = minEachCol[i];
		for j in range(n):
			cost_matrix[j][i] = cost_matrix[j][i] - to_sub;
	return cost_matrix	

def zeroExists(row_matrix):
	if 0 in row_matrix:
		return True;
	return False;

def zeroExistsCol(cost_matrix, row, col, n):
	for i in range(n):
		if i==row:
			continue
		elif cost_matrix[i][col]==0:
			return True
	return False

def findLines(cost_matrix, n):
	global_min = []
	for i in range(n):#iterate each row
		if not zeroExists(cost_matrix[i]):
			continue
		else:
			temp_min = []
			temp_min.append(i);
			for j in range(n):
				if zeroExistsCol(cost_matrix, i,j,n):
					temp_min.append(j);
				else:
					continue;
			if len(global_min) == 0:
				global_min = temp_min
			elif len(global_min) > len(temp_min):
				global_min = temp_min
			else:
				continue
	return global_min

def modifyMatrix(cost_matrix, lines, n):
	overall_min = INT_MAX
	for i in range(n):
		if i==lines[0]:
			continue
		else:
			for j in range(n):
				if j not in lines[1:]:
					overall_min = min(overall_min, cost_matrix[i][j])
	
	for i in range(n):
		for j in range(n):
			if j in lines[1:] and i==lines[0]:
				cost_matrix[i][j] = cost_matrix[i][j] + overall_min
			elif j not in lines[1:] and i!=lines[0]:
				cost_matrix[i][j] = cost_matrix[i][j] - overall_min

	return cost_matrix

def findIndex(cost_matrix, row, n):
	for i in range(n):
		if cost_matrix[row][i]==0:
			return i
	return -1

def findAllocation(cost_matrix, n):
	allocation = {}
	while(1):
		for i in range(n):
			if cost_matrix[i].count(0) == 1:
				index = findIndex(cost_matrix, i, n)
				allocation.update({i : index})
				for j in range(n):
					cost_matrix[j][index] = INT_MAX
		if len(allocation)==n:
			break;

	return allocation

def hungarianAllocation(cost_matrix, n):
	minEachRow = find_minRow(cost_matrix, n)
	#print minEachRow
	cost_matrix = subtractMinRow(cost_matrix, minEachRow, n)
	
	minEachCol = find_minCol(cost_matrix, n)
	cost_matrix = subtractMinCol(cost_matrix, minEachCol, n)
	
	while 1:
		#print cost_matrix
		lines = []
		lines = findLines(cost_matrix, n)
		#print lines
		cost_matrix = modifyMatrix(cost_matrix, lines, n)

		if len(lines) == n:
			#print cost_matrix
			allocation = {}
			allocation = findAllocation(cost_matrix, n)
			#print allocation
			for each in allocation:
				print each, "\t----->\t", allocation[each]+1 
			break;
		else:
			#print cost_matrix
			continue

#n = int(raw_input())
n = 5
cost_matrix = [
	[10,3,3,2,8],
	[9,7,8,2,7],
	[7,5,6,2,4],
	[3,5,8,2,4],
	[9,10,9,6,10]
]

#print cost_matrix
allocation = {}
allocation = hungarianAllocation(cost_matrix, n)