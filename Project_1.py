# Import libraries
import nash
import numpy as np


# Class implementation
class Game:
    # Constructor
    def __init__(self, Firm_1_payoffs, Firm_2_payoffs):
        # Fill Payoffs matrices
        self.__Firm_1_payoffs = Firm_1_payoffs
        self.__Firm_2_payoffs = Firm_2_payoffs

    def __find_nash_equilibrium(self):
        # set up a game
        game = nash.Game(self.__Firm_1_payoffs, self.__Firm_2_payoffs)
        # find nash equilibrium strategy
        nash_equilibrium = list(game.support_enumeration())
        # Firm 1 nash equilibrium strategy
        Firm_1_nash_equilibrium = nash_equilibrium[0][0]
        # Firm 2 nash equilibrium strategy
        Firm_2_nash_equilibrium = nash_equilibrium[0][1]
        # Get the number of nash equilibrium strategy for Firm 1
        Firm_1_ne_strategy = np.where(Firm_1_nash_equilibrium == 1)[0][0]
        # Get the number of nash equilibrium strategy for Firm 2
        Firm_2_ne_strategy = np.where(Firm_2_nash_equilibrium == 1)[0][0]
        # Determine payoffs for chosen strategies:
        Firm_1_ne_payoff = self.__Firm_1_payoffs[
                Firm_1_ne_strategy][Firm_2_ne_strategy]

        Firm_2_ne_payoff = self.__Firm_2_payoffs[
                Firm_1_ne_strategy][Firm_2_ne_strategy]

        # Print results:
        if Firm_1_ne_strategy == 0:
            print 'Nash equilibrium strategy for Firm 1 is Aggressive.\
            Payoff is', Firm_1_ne_payoff
        else:
            print 'Nash equilibrium strategy for Firm 1 is Passive.\
            Payoff is', Firm_1_ne_payoff

        if Firm_2_ne_strategy == 0:
            print 'Nash equilibrium strategy for Firm 2 is Aggressive.\
            Payoff is', Firm_2_ne_payoff
        else:
            print 'Nash equilibrium strategy for Firm 2 is Passive.\
            Payoff is', Firm_2_ne_payoff

    def __find_mixed_nash_equilibrium(self):
        # Solve system of linear equations

        # Matrix of coefficients A
        # Firm 1
        a11 = 0
        a12 = self.__Firm_1_payoffs[0][0] - self.__Firm_1_payoffs[0][1] -\
            self.__Firm_1_payoffs[1][0] + self.__Firm_1_payoffs[1][1]
        # Firm 2
        a21 = self.__Firm_2_payoffs[0][0] - self.__Firm_2_payoffs[0][1] -\
            self.__Firm_2_payoffs[1][0] + self.__Firm_2_payoffs[1][1]
        a22 = 0
        # Form matrix A in Ax = b
        A = np.array([[a11, a12], [a21, a22]])

        # Vector b
        # Firm 1
        b1 = self.__Firm_1_payoffs[1][1] - self.__Firm_1_payoffs[0][1]
        # Firm 2
        b2 = self.__Firm_2_payoffs[1][1] - self.__Firm_2_payoffs[1][0]
        b = np.array([b1, b2])

        # Ax = b
        x = np.linalg.solve(A, b)

        # The probability Firm 1 chooses Aggressive strategy
        p = x[0]
        # The probability Firm 2 chooses Aggressive strategy
        q = x[1]
        print
        if not (0 <= p <= 1 and 0 <= q <= 1):
            print 'There is no mixed strategy Nash equilibrium'
        else:
            print 'Mixed strategy Nash equilibrium:'
            print 'Firm 1: Aggressive strategy with probability', p
            print 'Firm 1: Passive strategy with probability', 1-p
            print 'Firm 2: Aggressive strategy with probability', q
            print 'Firm 2: Passive strategy with probability', 1-q

    def main(self):
        self.__find_nash_equilibrium()
        self.__find_mixed_nash_equilibrium()


Firm_1_payoffs = np.array([[25, 33], [30, 36]])
Firm_2_payoffs = np.array([[9, 10], [13, 12]])
game = Game(Firm_1_payoffs, Firm_2_payoffs)
game.main()
