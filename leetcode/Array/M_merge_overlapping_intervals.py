'''
[
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]->
[ [1,2], [3,8], [9,10]]
'''
def mergeOverlappingIntervals(intervals):
	intervals.sort()
	prev = intervals[0]
	r=[]
	
	print(intervals)
	for i in range(1, len(intervals)):
		if intervals[i][0]<=prev[1]:
			prev[1]=intervals[i][1] if intervals[i][1]>prev[1] else prev[1]
		else:
			r.append(prev)
			prev=intervals[i]
			
	r.append(prev)    
	return r
