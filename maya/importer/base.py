class ImporterBase
  def __init__(self):
    pass

  def parsef4(self, args, start_ind):
    return [int(args[start_ind]), int(args[start_ind+1]), int(args[start_ind+2]), int(args[start_ind+3])]

  def parsef3(self, args, start_ind):
    return [int(args[start_ind]), int(args[start_ind+1]), int(args[start_ind+2])]

  def parsef2(self, args, start_ind):
    return [int(args[start_ind]), int(args[start_ind+1])]