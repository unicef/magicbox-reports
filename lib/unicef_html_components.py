import dash_html_components as html


def two_cols(col1, col2):
  """
  Displays two columns 50% each (responsive)
  """
  return html.Div(
    className="row",
    children=[
      html.Div(
        className="col-sm-6",
        children=col1
      ),
      html.Div(
        className="col-sm-6",
        children=col2)
    ]
  )
  
def md(text):
  return None

