class Face(UnitBase):
  def __init__(self, line):
    args = line.split(',')
    self.material = args[1]
    self.index = int(args[2])
    self.vtx_indices = [int(args[3]), int(args[4]), int(args[5])]

  def to_line(self):
    args = ["Face"]
    args.append(self.material)
    args.extend(self.vtx_indices)
    return ",".join(args)