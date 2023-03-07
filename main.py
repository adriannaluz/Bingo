import random

string = "BINGO"
bingo = [x for x in string]

ball = random.sample(range(1,76), 75)

def random_ball():
    for i in range(75):
        if ball[i] <= 15:
            rand_ball = 'B', ball[i]

        if 15 < ball[i] <= 30:
            rand_ball = 'I', ball[i]

        if 30 < ball[i] <= 45:
            rand_ball = 'N', ball[i]

        if 45 < ball[i] <= 60:
            rand_ball = 'G', ball[i]

        if 60 < ball[i] <= 75:
            rand_ball = 'O', ball[i]

        return rand_ball

print(random_ball())
