from PIL import Image
from random import shuffle, randrange


def generate_maze(width, height):
    visited = [[0] * width + [1] for _ in range(height)] + [[1] * (width + 1)]
    vertical = [["#.."] * width + ['#'] for _ in range(height)] + [[]]
    horizental = [["###"] * width + ['#'] for _ in range(height + 1)]
 
    def generate(x, y):
        visited[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (ii, jj) in d:
            if visited[jj][ii]:
                continue
            if ii == x:
                horizental[max(y, jj)][x] = "#.."
            if jj == y:
                vertical[y][max(x, ii)] = "..."
            generate(ii, jj)
 
    generate(randrange(width), randrange(height))
 
    s = ""
    for (a, b) in zip(horizental, vertical):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

 
if __name__ == '__main__':
    print(generate_maze(40,40))
    
