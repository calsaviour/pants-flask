python_library(
  name = "all",
  dependencies = [
    ":class_vis",
    ":prep_terrain_data",
    ":ClassifyNB"
  ]
)

python_library(
  name = "class_vis",
  sources = ['class_vis.py'],
  dependencies = [
    'src/python/3rdparty/python:matplotlib',
    'src/python/3rdparty/python:pylab',
    'src/python/3rdparty/python:numpy'
  ],
)

python_library(
  name = "prep_terrain_data",
  sources = ['prep_terrain_data.py']
)

python_library(
  name = "ClassifyNB",
  dependencies = [
    'src/python/3rdparty/python:sklearn'
  ],
  sources = ['ClassifyNB.py']
)


python_binary(name='naivebayes',
  dependencies=[
    ":all"
  ],
  source='naivebayes.py'
)
