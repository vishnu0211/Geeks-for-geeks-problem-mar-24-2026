"""You are given n courses, labeled from 0 to n - 1 and a 2d array prerequisites[][] where prerequisites[i] = [x, y] indicates that we need to take course y first if we want to take course x.

Find if it is possible to complete all tasks. Return true if all tasks can be completed, or false if it is impossible.

Examples:

Input n = 4, prerequisites[] = [[2, 0], [2, 1], [3, 2]]
Output: true
Explanation: 
To take course 2, you must first finish courses 0 and 1.
To take course 3, you must first finish course 2.
All courses can be completed, for example in the order [0, 1, 2, 3] or [1, 0, 2, 3].

Change your code to your input or add input line

"""
n = 3
pre_req = [[0,1] , [1,2] , [2,0]]

course_complete = []

course_list = [i for i in range(n)]

for x in pre_req:
    x1 = x[-1]
    su = 0
    for y in pre_req:
        if y[0] == x1:
            break
        else:
            su += 1
            continue
    if su == len(pre_req):
        course_complete.append(x1)

print(course_complete)

rem_courses = []
for course in course_list:
    if course not in course_complete:
        rem_courses.append(course)


for x in rem_courses:
    s = 0
    for y in pre_req:
        if y[0] == x:
            su = su+1
            if su == len(course_complete):
                course_complete.append(x)

print(course_complete)

is_complete = len(course_complete) == n
print(is_complete)


