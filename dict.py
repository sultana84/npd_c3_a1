class Yourdict(dict):

  def __getattr__(self, attr):
    return self.get(attr)

  def __setattr__(self, attr, value):
    self[attr] = value    
