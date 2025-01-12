class ProductIterator:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = 0

    def __iter__(self):
        # self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.iter_obj.products):
            prod_iter = self.iter_obj.products[self.index]
            self.index += 1
            return str(prod_iter)
        else:
            raise StopIteration


# for i in ProductIterator(category1):
#     next(i)
