from structshape import structshape
t = [1,2,3]
structshape(t)
list of 3 int

t2 = [[1,2]], [3,4], [5,6]]
structshape(t2)
'list of 3 list of 2 int'

>>> t3 = [1,2,3, 4.0, '5', '6', [7], [8], 9]
structshape(t3)
'list of (3 int, float, 2 str, 2 list of int, int)'

