import pickle
x = -164.617
y = 44.51525
z = -103.831
t1 = -46
t2 = 4.7

tickRealiser = 200
tick = 240

for i in range(tick):
    with open(f"intro{i + tickRealiser}.mcfunction","w+") as file:
        file.write(f"tp @a {x} {y} {z} {t1} {t2}\n")
        if i < tick-1:
            file.write(f"schedule function map:intro/intro{i+1+tickRealiser} 1t")
        x += 0.16715416666
        y -= 0.076828
        z -= 0.08222916666
        t1 += 0.19166666
        t2 += 0.005