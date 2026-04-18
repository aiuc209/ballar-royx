def normallashtirish(ballar):
    normallangan_ballar = []
    for ball in ballar:
        normallangan_ball = (ball / 1000) * 100
        normallangan_ballar.append(normallangan_ball)
    return normallangan_ballar

ballar = [10, 200, 500, 800, 1000]
normallangan_ballar = normallashtirish(ballar)
print(normallangan_ballar)
