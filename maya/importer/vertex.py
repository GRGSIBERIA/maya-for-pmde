class Vertex(UnitBase):
  def __init__(self, line):
    args = line.split(',')
    self.index    = int(args[1])
    self.pos      = UnitBase.parsef3(self, args, 2)
    self.normal   = UnitBase.parsef3(self, args, 5)
    self.edge_pow = int(args[8])
    self.uv       = UnitBase.parsef2(self, args, 9)
    self.add_uv   = [
      UnitBase.parsef4(self, args, 11), UnitBase.parsef4(self, args, 15), 
      UnitBase.parsef4(self, args, 19), UnitBase.parsef4(self, args, 23)
    ]
    self.weight_type  = int(args[27])
    self.bone_names   = [args[28], args[30], args[32], args[34]]
    self.bone_weights = [args[29], args[31], args[33], args[35]]
    self.sdef_c = UnitBase.parsef3(self, args, 36)
    self.sdef_r0 = UnitBase.parsef3(self, args, 39)
    self.sdef_r1 = UnitBase.parsef3(self, args, 42)

  def to_line(self):
    args = []
    