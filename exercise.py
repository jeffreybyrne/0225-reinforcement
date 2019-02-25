def draw_shape(options):
  shape = ""

  for r in range(options['rows']):
    for c in range(options['cols']):
      shape += options['char']

    shape += "\n"


  return shape


my_input = {'cols': 4, 'rows': 4, 'char': '*'}
print(draw_shape(my_input))

my_next_input = {'cols': 9, 'rows': 3, 'char': '0'}
print(draw_shape(my_next_input))
