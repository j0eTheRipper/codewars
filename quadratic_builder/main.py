class Monomial:
    def __init__(self, monomial: str):
        self.monomial = monomial
        self.__format_monomial()

    def __get_variable(self):
        pass

    def __format_monomial(self):
        self.monomial.replace(' ', '')
        self.monomial.replace('(', '')
        self.monomial.replace(')', '')
