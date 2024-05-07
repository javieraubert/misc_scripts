def busqueda_lineal(A,X):
    j=0
    n=len(A)
    while (j<n)and(X!=A[j]):
        j+=1
    if j<n:
        return 1
    else:
        return 0
def busqueda_pos(A,X):
    j=0
    n=len(A)
    while (j<n)and(X!=A[j]):
        j+=1
    if j<n:
        return j
    else:
        return 0

nodos = ('1', '2', '3', '4', '5', '6')
dist = {'1': {'2': 1, '3': 12},
        '2': {'1': 1, '3': 9, '4': 3},
        '3': {'1': 12, '2': 9, '4': 4, '5': 5},
        '4': {'2': 3, '3': 4, '5': 13, '6':15},
        '5': {'3': 5, '4': 13, '6': 14},
        '6': {'4':15, '5':14}}
nodos = ('1', '2', '3', '4', '5', '6')
dist = {'1': {'2': 1, '3': 12},
        '2': {'1': 1, '3': 3, '4': 3},
        '3': {'1': 12, '2': 3, '4': 4, '5': 0},
        '4': {'2': 3, '3': 4, '5': 13, '6':15},
        '5': {'3': 0, '4': 13, '6': 14},
        '6': {'4':15, '5':14}}

def dijkstra(nodos,dist,A,B):
    visitado=[]
    camino=[]
    distsum=0
    i=0
    n=0
    visto=0
    current=A
    while i==0:
        j=0
        f=[None for x in range(len(dist[current].items()))]
        g=[None for x in range(len(dist[current].items()))]
        for neighb, distan in dist[current].items(): 
            f[n]=neighb
            g[n]=distan
            n=n+1
        if busqueda_lineal(f,B):
            ind=busqueda_pos(f,B)
            camino.append(current)
            camino.append(f[ind])
            distsum=distsum+g[ind]
            print ("El path es {} y la suma de los tramos es {}".format(camino,distsum))
            i=1
            return 1
        else:
            i=0
        n=0
        camino.append(current)
        visitado.append(current)
        f=[x for x in f if x is not None]
        g=[x for x in g if x is not None]
        while j==0:
            gmin=min(g)
            ind=g.index(gmin)
            visto=busqueda_lineal(visitado,f[ind])
            if visto:
                f.pop(ind)
                g.pop(ind)
            else:
                current=f[ind]
                print ("El siguiente salto es {}".format(current))
                print ("Los saltos actuales son {}".format(visitado))
                distsum=distsum+g[ind]
                j=1