class Vertex:
  def __init__(self, line):
    args = line.split(',')
    index = int(args[1])
    pos = self.parsef3(args, 2)
    normal = self.parsef3(args, 5)
    edge_pow = int(args[8])
    uv = self.parsef2(args, 9)
    