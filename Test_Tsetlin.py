
def binary_search(low, high, ci, Acc):
    if low > high:
        return -1
    if high == low:
        return high
    mid_idx = int((high + low) / 2)
    # print mid_idx
    T_mid = Tsetlin.Tsetlin(mid_idx, ci)
    p1 = T_mid.Tsetlin_Theoretical()
    if p1[0] > Acc:
        return binary_search(low, mid_idx, ci, Acc)
    else:
        return binary_search(mid_idx + 1, high, ci, Acc)
    return mid_idx


def Q1a(chosen_state):
    no_sims = 10000
    init_state = 2
    c1 = np.arange(0.05, 0.7, 0.1)

    for idx_c1 in range(0, len(c1)):
        ci = [c1[idx_c1], 0.7]
        T = Tsetlin.Tsetlin(chosen_state[idx_c1], ci)
        P1 = T.Tsetlin_Sim(init_state, no_sims)
        P1_close = T.Tsetlin_Theoretical()
        print "Probability in Environment of [%.3f,%.3f] with N = %.0f is %.3f by simulation, %.3f using formula." % (ci[0], ci[1], chosen_state[idx_c1], P1[0], P1_close[0])


def Q1b():
    min_state = 3  # one side
    max_state = 21  # one side
    init_state = 2
    Accuracy = 0.95
    c1 = np.arange(0.05, 0.7, 0.1)
    best_state = np.zeros(len(c1))

    for idx_c1 in range(0, len(c1)):
        ci = [c1[idx_c1], 0.7]
        low = min_state
        high = max_state
        best_state[idx_c1] = binary_search(min_state, max_state, ci, Accuracy)
        T = Tsetlin.Tsetlin(best_state[idx_c1], ci)
        P1 = T.P
        print "In Environment [%.3f,%.3f], the minimum states to obtain 95%% Accuracy is %.0f with probability of %.3f." % (ci[0], ci[1], best_state[idx_c1], P1[0])

    return best_state


if __name__ == "__main__":
    import numpy as np
    import Tsetlin

    print "###########################################################################"
    print "Q1a"
    print "###########################################################################"
    chosen_state = np.full((7), 3, dtype=int)

    Q1a(chosen_state)

    print "###########################################################################"
    print "Q1b"
    print "###########################################################################"

    best_state = Q1b()

    print "###########################################################################"
    print "Q1c"
    print "###########################################################################"
    print best_state
    Q1a(best_state.astype(int))
