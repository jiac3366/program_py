def howlong(*a, **kw):
    print(a)
    print(kw)


if __name__ == '__main__':
    howlong('/web/view/edit_custom', 'gg', type='json', auth="users")
