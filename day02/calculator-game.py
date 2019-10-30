# coding: utf-8
import random

def reset():
    name = "Clara"
    questions = 0
    points = 0
    return [name, questions, points]

def scoreUp(score, correct=True):
	if correct:
		score[1] += 1
		score[2] += 1
	else:
		score[1] += 1
	return score

def frage(score):
    a = random.randint(1,100)
    b = random.randint(1,100)
    ops = ['+', '-', '-', '-']
    z = random.choice(ops)
    print("Wieviel ist {} {} {}?".format(a, z, b))
    ergebnis = eval(str(a) + str(z) + str(b))
    antwort = input("Was ist Deine Antwort?")
    print("Du sagst, die Antwort ist:")
    print(antwort)
    print("Das ist.......")
    if int(antwort) == ergebnis:
        print("richtig")
        score = scoreUp(score, correct=True)
    else:
        print("falsch")
        score = scoreUp(score, correct=False)
    return score

def run(name, x):
    name = name
    questions = 0
    points = 0

    score = [name, questions, points]
    
    n = 0
    while n < x:
        frage(score)
        n += 1

    print('{}, Du hast {} Runden gespielt und dafür {} Punkte erhalten'.format(score[0],score[1],score[2]))

if __name__ == '__main__':
    run('Clara', 3)
