Web VPython 3.2
import random
b = box(make_trail = True)

while True : 
    rate(100)
    k = keysdown()
    if ' ' in k :
        b.color = vec(random.random(),random.random(),random.random())
        b.pos.x = random.uniform(-10,10)
        b.pos.y = random.uniform(-10,10)
        b.trail_color = b.color
        
