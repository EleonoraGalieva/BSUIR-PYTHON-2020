import collections


class Memoized:
    def __init__(self, func, cache_size=8):
        self.func = func
        self.cache = {}
        self.cache_size = cache_size

    def __call__(self, args):
        if isinstance(args, collections.Hashable):
            if args in self.cache:
                return self.cache[args]
            else:
                value = self.func(args)
                if len(self.cache) < self.cache_size:
                    self.cache[args] = value
                return value
        else:
            return self.func(args)
