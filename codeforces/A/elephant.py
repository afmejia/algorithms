#617A math

def min_steps_edit(coordinate):
    return (coordinate + 4) // 5

def min_steps(coordinate):
    steps = 0
    elephant_steps = [1, 2, 3, 4, 5]
    while coordinate > 0:
        if coordinate in elephant_steps:
            steps += 1
            coordinate = 0
        else:
            steps += coordinate // 5
            coordinate = coordinate % 5
    
    return steps

coordinate = int(input())

print(min_steps_edit(coordinate))