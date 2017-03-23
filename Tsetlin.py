import numpy as np
import random


class Tsetlin:

    def __init__(self, No_State, Prob_Penalty):
        self.No_State = No_State
        self.Prob_Penalty = Prob_Penalty
        self.P = self.Tsetlin_Theoretical()

    def Environment(self, alpha):
        return random.random() < self.Prob_Penalty[alpha]

    def Tsetlin_Action(self, cur_state):
        if 0 <= cur_state < self.No_State:
            alpha = 0
        else:
            alpha = 1

        beta = self.Environment(alpha)

        if beta == 0:
            if cur_state == self.No_State:
                cur_state = self.No_State
            elif cur_state == 0:
                cur_state = 0
            else:
                cur_state = cur_state - 1
        else:
            if cur_state == self.No_State - 1:
                cur_state = 2 * self.No_State - 1
            elif cur_state == 2 * self.No_State - 1:
                cur_state = self.No_State - 1
            else:
                cur_state = cur_state + 1
        return cur_state

    def Tsetlin_Sim(self, cur_state, no_sims):
        no_state = self.No_State
        token = np.zeros(2 * no_state)
        for idx_sim in range(0, no_sims):
            cur_state = self.Tsetlin_Action(cur_state)
            token[cur_state] = token[cur_state] + 1
        return sum(token[range(0, no_state)]) / no_sims, sum(token[range(no_state, 2 * no_state)]) / no_sims

    def Tsetlin_Theoretical(self):
        d1 = 1 - self.Prob_Penalty[0]
        d2 = 1 - self.Prob_Penalty[1]
        c1 = self.Prob_Penalty[0]
        c2 = self.Prob_Penalty[1]
        N = self.No_State
        return 1 / (1 + (c1 / c2)**N * (c1 - d1) / (c2 - d2) * (c2**N - d2**N) / (c1**N - d1**N)), 1 / (1 + (c2 / c1)**N * (c2 - d2) / (c1 - d1) * (c1**N - d1**N) / (c2**N - d2**N))
