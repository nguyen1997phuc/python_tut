class SwitchBase:

    def switch(self, case):
        m = getattr(self, f'case_{case}', None)
        if not m:
            return self.default
        return m

    __call__ = switch


class CustomSwitcher:

    def case_1(self):
        return 'one'

    def case_2(self):
        return 'two'

    def case_42(self):
        return 'the answer of life'

    def default(self):
        raise Exception('not a case')


switch = CustomSwitcher()
print(switch(1))
