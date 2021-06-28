import pickle
x = -124.667
y = 26.15336
z = -123.484
t1 = -0.2
t2 = 5.9

tickRealiser = 440
tick = 160

for i in range(tick):
    with open(f"intro{i + tickRealiser}.mcfunction","w+") as file:
        file.write(f"tp @a {x} {y} {z} {t1} {t2}\n")
        if i < tick-1:
            file.write(f"schedule function map:intro/intro{i+1+tickRealiser} 1t")
        x += 0.00104375
        y += 0.0240415
        z += 0.20643125
        t1 += 0.00125
        t2 += 0.275625