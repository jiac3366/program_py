def howlong(a=None, **kw):

    print(kw)


if __name__ == '__main__':
    howlong('/web/view/edit_custom', type='json', auth="user")
