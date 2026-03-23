V = int(input())
edge = int(input())
edges = []
for _ in range(edge):
    u, v = map(int, input().split())
    edges.append([u, v])



lst = []

for x in edges:
    x1 = x[0]
    x2 = x[1]
    su = 1
    rep = ""
    for i in range(len(edges)):
        for j in edges:

            if j[0] == x2:
                if j[1] == x1:
                    su = su+1
                    rep = "stop"
                    break


                su += 1
                x2 = j[1]
                continue
        if rep == "stop":
            break
    if su < len(edges):

        lst.append(su)
        
        

print(max(lst))
