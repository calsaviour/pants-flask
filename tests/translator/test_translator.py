from translator import Translator

def test_translator():
  t = Translator()
  t.translate("Hello World", "zh")
  assert t.counter == 1
