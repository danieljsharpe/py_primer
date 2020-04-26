debugbool = False
openmpbool = False

with open('formattestfile.out', 'w') as f:
    f.write('''
DEF DEBUG = {debug}
DEF OPENMP = {openmp}
    '''.format(openmp=openmpbool, debug=debugbool))
