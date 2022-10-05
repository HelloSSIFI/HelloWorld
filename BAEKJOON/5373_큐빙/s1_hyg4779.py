for tc in range(int(input())):
    u = ['w'] * 9
    d = ['y'] * 9
    f = ['r'] * 9
    b = ['o'] * 9
    l = ['g'] * 9
    r = ['b'] * 9
    n = int(input())

    turning = list(input().split())
    for i in range(n):
        head, p = turning[i]
        # 클
        if head == 'U':
            b1, b2, b3 = b[0], b[1], b[2]
            l1, l2, l3 = l[0], l[1], l[2]
            f1, f2, f3 = f[0], f[1], f[2]
            r1, r2, r3 = r[0], r[1], r[2]
            if p == '-':
                b[0], b[1], b[2] = r1, r2, r3
                r[0], r[1], r[2] = f1, f2, f3
                f[0], f[1], f[2] = l1, l2, l3
                l[0], l[1], l[2] = b1, b2, b3
            else:
                b[0], b[1], b[2] = l1, l2, l3
                l[0], l[1], l[2] = f1, f2, f3
                f[0], f[1], f[2] = r1, r2, r3
                r[0], r[1], r[2] = b1, b2, b3

        elif head == 'D':
            b7, b8, b9 = b[6], b[7], b[8]
            l7, l8, l9 = l[6], l[7], l[8]
            f7, f8, f9 = f[6], f[7], f[8]
            r7, r8, r9 = r[6], r[7], r[8]
            # 클
            if p == '-':
                # f -> l -> b -> r -> f
                f[6], f[7], f[8] = r7, r8, r9
                r[6], r[7], r[8] = b7, b8, b9
                b[6], b[7], b[8] = l7, l8, l9
                l[6], l[7], l[8] = f7, f8, f9
            else:
                # f -> r -> b -> l -> f
                f[6], f[7], f[8] = l7, l8, l9
                l[6], l[7], l[8] = b7, b8, b9
                b[6], b[7], b[8] = r7, r8, r9
                r[6], r[7], r[8] = f7, f8, f9

        elif head == 'F':
            u7, u8, u9 = u[6], u[7], u[8]
            l3, l6, l9 = l[2], l[5], l[8]
            d1, d2, d3 = d[0], d[1], d[2]
            r1, r4, r7 = r[0], r[3], r[6]
            if p == '-':
                u[6], u[7], u[8] = r1, r4, r7
                r[0], r[3], r[6] = d3, d2, d1
                d[0], d[1], d[2] = l3, l6, l9
                l[2], l[5], l[8] = u9, u8, u7
            # 클
            else:
                u[6], u[7], u[8] = l9, l6, l3
                l[2], l[5], l[8] = d1, d2, d3
                d[0], d[1], d[2] = r7, r4, r1
                r[0], r[3], r[6] = u7, u8, u9

        elif head == 'B':
            u1, u2, u3 = u[0], u[1], u[2]
            l1, l4, l7 = l[0], l[3], l[6]
            d7, d8, d9 = d[6], d[7], d[8]
            r3, r6, r9 = r[2], r[5], r[8]
            if p == '-':
                u[0], u[1], u[2] = l7, l4, l1
                l[0], l[3], l[6] = d7, d8, d9
                d[6], d[7], d[8] = r9, r6, r3
                r[2], r[5], r[8] = u1, u2, u3
            # 클
            else:
                u[0], u[1], u[2] = r3, r6, r9
                r[2], r[5], r[8] = d9, d8, d7
                d[6], d[7], d[8] = l7, l4, l1
                l[0], l[3], l[6] = u3, u2, u1

        # 클
        elif head == 'L':
            u1, u4, u7 = u[0], u[3], u[6]
            f1, f4, f7 = f[0], f[3], f[6]
            b3, b6, b9 = b[2], b[5], b[8]
            d1, d4, d7 = d[0], d[3], d[6]
            if p == '-':
                u[0], u[3], u[6] = f1, f4, f7
                f[0], f[3], f[6] = d1, d4, d7
                d[0], d[3], d[6] = b9, b6, b3
                b[2], b[5], b[8] = u7, u4, u1
            else:
                u[0], u[3], u[6] = b9, b6, b3
                b[2], b[5], b[8] = d7, d4, d1
                d[0], d[3], d[6] = f1, f4, f7
                f[0], f[3], f[6] = u1, u4, u7

        elif head == 'R':
            u3, u6, u9 = u[2], u[5], u[8]
            f3, f6, f9 = f[2], f[5], f[8]
            d3, d6, d9 = d[2], d[5], d[8]
            b1, b4, b7 = b[0], b[3], b[6]
            if p == '-':
                u[2], u[5], u[8] = b7, b4, b1
                f[2], f[5], f[8] = u3, u6, u9
                d[2], d[5], d[8] = f3, f6, f9
                b[0], b[3], b[6] = d9, d6, d3
            # 클
            else:
                u[2], u[5], u[8] = f3, f6, f9
                f[2], f[5], f[8] = d3, d6, d9
                d[2], d[5], d[8] = b7, b4, b1
                b[0], b[3], b[6] = u9, u6, u3

    for i in range(0, 9, 3):
        print(''.join(u[i:i + 3]))
