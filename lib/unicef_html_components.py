import dash_html_components as html

def two_cols(col1, col2):
  """
  displays two columns 50% each
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
  