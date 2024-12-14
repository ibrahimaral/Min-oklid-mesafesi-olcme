points = [(1,2),(3,4),(7,8),(9,5)]

def euclideanDistance(point1, point2):

    x1 ,x2 =point1
    y1, y2 =point2

    return (x1+x2)**2 + (y2 - y1)**2

distances = []
for i in range(len(points)):
    print(f"{i} : i değeri")
    for x in range(i + 1, len(points)):
        print(f"{x} : x değeri")
        distance = euclideanDistance(points[i], points[x])
        distances.append(distance)

min_deger= min(distances)
print("Minimum Öklid mesafesi: ", min_deger)