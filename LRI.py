import random


class LRI:

    def __init__(self, K_R, Prob_Penalty):
        self.Prob_Penalty = Prob_Penalty
        self.K_R = K_R

    def Environment(self, alpha):
        return random.random() < self.Prob_Penalty[alpha]

    def LRI_Action(self, cur_Prob):
        alpha = random.random()
        if alpha <= cur_Prob[0]:
            Action = 0
        else:
            Action = 1

        beta = self.Environment(Action)

        if beta == 0:
            if Action == 0:
                P1 = 1 - self.K_R * cur_Prob[1]
                cur_Prob = [P1, 1 - P1]
            else:
                P1 = self.K_R * cur_Prob[0]
                cur_Prob = [P1, 1 - P1]
        return cur_Prob

    def LRI_Sim(self, cur_Prob, No_Sim):
        for idx_sim in range(0, No_Sim):
            cur_Prob = self.LRI_Action(cur_Prob)
            if cur_Prob[0] >= 0.95:
            	return (idx_sim, cur_Prob)
        return (No_Sim, cur_Prob)
