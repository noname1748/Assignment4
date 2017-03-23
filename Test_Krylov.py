

if __name__ == "__main__":
    import numpy as np
    import Krylov
    import Tsetlin

    no_state = 8
    ci = [0.55, 0.7]

    no_sims = 1000000
    init_state = 2
    token = np.zeros(2 * no_state)

    T1 = Tsetlin.Tsetlin(no_state, np.divide(ci, 2))
    P1_T1_Sim = T1.Tsetlin_Sim(init_state, no_sims)
    P1_T1_Theo = T1.Tsetlin_Theoretical()

    K = Krylov.Krylov(no_state, ci)
    P1_Krylov = K.Krylov_Sim(init_state, no_sims)

    print "*****************************************************************"
    print "Q2"
    print "*****************************************************************"

    print "Tsetlin: E = [%.3f/2,%.3f/2], N = 16, P1 from simulation = %.5f, P1 from closed form equation = %.5f." % (ci[0], ci[1], P1_T1_Sim[0], P1_T1_Theo[0])
    print "Krylov: E = [%.3f,%.3f], N = 16, P1 from simulation = %.5f." % (ci[0], ci[1], P1_Krylov[0])