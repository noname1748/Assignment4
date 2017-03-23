import numpy as np
import random


class Krylov:

    def __init__(self, No_State, Prob_Penalty):
        self.No_State = No_State
        self.Prob_Penalty = Prob_Penalty

    def Environment(self, alpha):
        return random.random() < self.Prob_Penalty[alpha]

    def Krylov_Action(self, cur_state):
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
            if random.random() < 0.5:
                if cur_state == self.No_State - 1:
                    cur_state = 2 * self.No_State - 1
                elif cur_state == 2 * self.No_State - 1:
                    cur_state = self.No_State - 1
                else:
                    cur_state = cur_state + 1
            else:
                if cur_state == self.No_State:
                    cur_state = self.No_State
                elif cur_state == 0:
                    cur_state == 0
                else:
                    cur_state = cur_state - 1
        return cur_state

    def Krylov_Sim(self, cur_state, no_sims):
        no_state = self.No_State
        token = np.zeros(2 * no_state)
        for idx_sim in range(0, no_sims):
            cur_state = self.Krylov_Action(cur_state)
            token[cur_state] = token[cur_state] + 1
        return sum(token[range(0, no_state)]) / no_sims, sum(token[range(no_state, 2 * no_state)]) / no_sims
