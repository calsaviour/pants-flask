python_tests(
  name = 'all',
  dependencies = [
    ':translator',
  ]
)

python_tests(
  name = 'translator',
  dependencies = [
    ':test_translator',
  ]
)

python_tests(
  name = 'test_translator',
  sources = ['test_translator.py'],
  dependencies = [
    'src/python/translator:translator'
  ]
)
