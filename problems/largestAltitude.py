def largestAltitude(gain):
    altitudes = []
    altitudes.append(0)
    for i in range(len(gain)):
        altitude = 0
        for j in range(0, i + 1):
            altitude += gain[j]
        altitudes.append(altitude)
    print(altitudes)
    return max(altitudes)


