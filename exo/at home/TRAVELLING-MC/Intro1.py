import pickle
x = -166.851    
y = 60.51357
z = -61.61
t1 = -120.2
t2 = 32.7

tickRealiser = 0
tick = 100

for i in range(tick):
    with open(f"intro{i + tickRealiser}.mcfunction","w+") as file:
        file.write(f"tp @a {x} {y} {z} {t1} {t2}\n")
        if i < tick-1:
            file.write(f"schedule function map:intro/intro{i+1+tickRealiser} 1t")
        x -= 0.07298
        y -= 0.078804
        z -= 0.18048
        t1 += 0.295
        t2 -= 0.138