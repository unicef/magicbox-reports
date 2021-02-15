import dash_core_components as dcc

'''
Simple wrappers of the dash_core_components by applying some values
'''

def graph(fig, id):
  """ 
  Wraps dash_core_component.Graph with some default values 
  """

  return dcc.Graph(
      id=id,
      config={'displaylogo': False},
      figure=fig
  )  
