def main(h, a, b):
    answer_eg = (h - a + b) % 24
    answer = (h - a) + b if (h - a) + b > 0 else (h - a) + b + 24
    return answer_eg, answer


def test_case(main):
    err_log = []
    for h in range(0, 24):
        for a in range(-11, 13):
            for b in range(-11, 13):
                if main(h, a, b)[0] != main(h, a, b)[1]:
                    err_log.append('False: %d %d %d = %d \n' % (h, a, b, main(h, a, b)[0]))
    return ''.join(err_log)


print(test_case(main))