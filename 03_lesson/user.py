class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def say_f_name(self):
        print(self.f_name)

    def say_l_name(self):
        print(self.l_name)

    def say_f_l_name(self):
        print(self.f_name, self.l_name)
