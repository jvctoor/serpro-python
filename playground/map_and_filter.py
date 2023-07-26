

arrayJoao = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mp = map(lambda x: x*2, arrayJoao)
filtrado = filter(lambda x: x % 2 == 0, arrayJoao)

print(list(mp))
print(list(filtrado))




