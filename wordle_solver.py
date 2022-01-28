import collections, gzip, re


class WordleSolver:

  def __init__(self, fn='words.txt.gz', verbose=True):
    self._load_words(fn)
    if verbose:
      print('loaded', len(self._words), 'words with char freqs:', sorted(self._cf(self._words).items()))
    self._gray = set()
    self._yellow_at = set()
    self._green_at = set()
    
  def _load_words(self, fn):
    self._words = set()
    pattern = re.compile(r'^[a-z]{5}$')
    with gzip.open(fn) as f:
      for line in f.readlines():
        for word in line.split():
          word = word.decode().strip().lower()
          if pattern.match(word):
            self._words.add(word)
    
  def _cf(self, words):
    cf = collections.defaultdict(int)
    for word in words:
      for c in word:
        cf[c] += 1
    return cf
  
  def gray(self, chars):
    for c in chars.lower():
      self._gray.add(c)
    
  def green(self, c, i):
    self._green_at.add((c, i-1))
    
  def yellow(self, c, i):
    self._yellow_at.add((c, i-1))
  
  def _seen_chars(self):
    return set([c for c,i in self._yellow_at] + [c for c,i in self._green_at])
    
  def candidates(self):
    for word in self._words:
      if any((c not in word for c in self._seen_chars())): continue
      if any((c in word for c in self._gray)): continue
      if any((word[i] == c for c,i in self._yellow_at)): continue
      if any((word[i] != c for c,i in self._green_at)): continue
      yield word

  def igs(self):
    igs = {}
    seen = self._seen_chars()
    candidates = list(self.candidates())
    cf = self._cf(candidates)
    for word in candidates:
      ig = 0
      for c in set(word):
        if c in seen: continue
        ig += cf[c]
      igs[word] = ig
    return igs
  
  def suggest(self, n=4):
    return sorted(self.igs().items(), key=lambda x: (x[1], x[0]), reverse=True)[:n]


