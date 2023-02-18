class Article:
  def __init__(self, url, sentences):
    self.url = url
    self.sentences = sentences

  def __str__(self):
    return f'''url:{self.url}
    sentences:{self.sentences}
    '''
