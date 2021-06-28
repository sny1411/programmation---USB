import pickle
x = -174.076
y = 52.71197
z = -79.478
t1 = -91
t2 = 19

tickRealiser = 100
tick = 100

for i in range(tick):
    with open(f"intro{i + tickRealiser}.mcfunction","w+") as file:
        file.write(f"tp @a {x} {y} {z} {t1} {t2}\n")
        if i < tick-1:
            file.write(f"schedule function map:intro/intro{i+1+tickRealiser} 1t")
        x += 0.09555
        y -= 0.0827952
        z -= 0.24599
        t1 += 0.455
        t2 -= 0.144