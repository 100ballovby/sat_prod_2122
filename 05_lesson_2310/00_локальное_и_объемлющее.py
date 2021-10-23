def say():
    # enclosing
    print('Говорю....')
    def hello():
        # enclosing name
        print('привет')
        def tbd():
            # local name
            print('')
    hello()

say()


