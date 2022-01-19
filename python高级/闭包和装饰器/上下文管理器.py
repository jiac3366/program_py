if __name__ == '__main__':
    from contextlib import contextmanager


    @contextmanager
    def myopen(name, state):
        try:
            f = open(name, state)
            yield f
            print('yes')
        except:
            print('error')
        finally:
            print('close()')
            f.close()
