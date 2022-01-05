#!/usr/bin/env python3


def calc_areas(vp, cv):
    areas = []
    for i in range(len(cv)):
        area = 0
        for j in range(1, len(cv[i]) + 1):
            # fixed the following line for the exercise (original didn't contain the if expression)
            v1 = cv[i][j] if j < len(cv[i]) else cv[i][0]
            v0 = cv[i][j - 1]
            area += 0.5 * (vp[v1][0] * vp[v0][1] - vp[v1][1] * vp[v0][0])
        areas.append(area)
    return areas


if __name__ == "__main__":
    cv = [[0, 1, 2, 5, 6], [2, 3, 4, 7, 5]]  # vertex numbers per cell
    vp = [
        [0.8, 5.5],
        [2.4, 7.0],
        [4.1, 6.4],
        [6.3, 7.0],
        [7.6, 4.8],
        [3.9, 4.0],
        [1.9, 3.4],
        [6.3, 3.3],
    ]  # x and y positions per vertex

    print(calc_areas(vp, cv))
