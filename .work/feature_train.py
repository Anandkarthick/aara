class feature_train(object):

    def __init__(self, ft_name):
        self.ft_name=ft_name

    def selection(self):
        return(self.ft_name, "Feature selected")