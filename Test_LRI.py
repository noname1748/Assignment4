def Test_Stability(LRI, cur_Prob):
    no_test = 100
    max_Sim = 10000
    no_pos = 0
    ave_Step = 0
    for idx_test in range(0, no_test):
        (no_sim, p1) = LRI.LRI_Sim(cur_Prob, max_Sim)
        if p1[0] > 0.9:
            no_pos = no_pos + 1
            ave_Step = ave_Step + no_sim
    if no_pos / no_test > 0.95:
        return (True, ave_Step / no_pos)
    else:
        return (False, ave_Step / no_pos)


def binary_search(low, high, ci, cur_Prob, Acc):
    no_sim = 10000
    if low > high:
        return -1
    if high == low:
        return high
    mid = (high + low) / 2
    LRI_mid = LRI.LRI(mid, ci)
    (flag, ave_Step) = Test_Stability(LRI_mid, cur_Prob)
    if flag:
        (no_step, p1) = LRI_mid.LRI_Sim(cur_Prob, no_sim)
        if p1[0] > Acc:
            return binary_search(low, mid, ci, cur_Prob, Acc)
        else:
            return binary_search(mid, high, ci, cur_Prob, Acc)
        return mid
    else:
        return binary_search(mid, high, ci, cur_Prob, Acc)


def Q3b(KR_min, KR_max, c1_range, Accuracy):
    print "**************************************************************"
    print "Q3(b)"
    print "**************************************************************"

    for idx_c1 in range(0, len(c1_range)):
        init_Prob = [0.5, 0.5]
        ci = [c1_range[idx_c1], 0.7]
        KR = binary_search(KR_min, KR_max, ci, init_Prob, Accuracy)
        LRI_cur = LRI.LRI(KR, ci)
        (flag, ave_Step) = Test_Stability(LRI_cur, [0.5, 0.5])
        print("With Environment of [%.3f,%.3f], the best KR is %.5f which takes %.0f steps to converge to 95%% accuracy." % (
            ci[0], ci[1], KR, ave_Step))


def Q3a(KR, no_sim):
    print "**************************************************************"
    print "Q3(a)"
    print "**************************************************************"

    c1 = np.arange(0.05, 0.7, 0.1)
    for idx_c1 in range(0, len(c1)):
        init_Prob = [0.5, 0.5]
        ci = [c1[idx_c1], 0.7]
        L_RI = LRI.LRI(KR, ci)
        (no_step, P) = L_RI.LRI_Sim(init_Prob, no_sim)
        print("Given KR = %.3f in Environment of [%.3f,%.3f], it takes %.0f times to converge." % (
            KR, ci[0], ci[1], no_step))

if __name__ == "__main__":
    import numpy as np
    import LRI

    Q3a(0.99, 10000)

    KR_min = 0.0001
    KR_max = 0.9999
    Accuracy = 0.95
    ci = np.arange(0.05, 0.7, 0.1)

    Q3b(KR_min, KR_max, ci, Accuracy)
