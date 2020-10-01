

import dash_core_components as dcc
import dash_html_components as html

from app import app


def header_link_item(link):
  return html.Li(className="nav-item ml-3", children=[
    html.A(
      className="nav-link ml-auto", 
      href=link['href'], 
      title=link['title'],
      children=[link['text']]
    )
  ])

def header_links_layout(links): 
  return html.Ul(
    className="navbar-nav rounded-left ml-auto p-2 flex-row d-none d-md-flex p-0",
    children= list(map(header_link_item, links))
  )
  
def tab_link_item(link):
  return html.Li(className="nav-item", children=[
    html.A(
      className="nav-link", 
      role="button", 
      href=link['href'], 
      title=link['title'],
      children=[link['text']]
    )
  ])

def tab_links_layout(links): 
  return html.Div(
    className="collapse navbar-collapse d-md-block bg-white",
    id="navbarSupportedContent",
    children =[ 
      html.Ul( 
        className="nav nab-tabs p-0 bg-white", 
        children = list(map(tab_link_item, links))
      )
    ]
  )

def layout(pathname='/'):
  header_links = [
    {
      'href': "",
      'title' : "",
      'text': "Github"
    }
  ]
  tab_links = [
    {
      'href': "/",
      'title' : "",
      'text': "Home"
    },
     {
      'href': "/about",
      'title' : "",
      'text': "About Magicbox Reports"
    }
  ]
  return html.Header(
    children= [
      html.A( className="skip", href="#contents", tabIndex="0", children=["Skip content"]),
      html.Nav(className="navbar navbar-expand-md flex-md-row bd-navbar p-0",
        children=[
          html.A( className="navbar-brand navbar-line mr-3", href="/", title="Go home", 
            children=[
              html.Img(className="img-fluid d-none d-lg-block", alt="", src="/assets/unicef-logo.svg")
          ]),
          html.A(className="navbar-brand mr-0", href="/", title="Go home", 
            children=[ "Magicbox Reports"
          ]),
          header_links_layout(header_links),
          html.Button(
            className='navbar-toggler',
            type="button" ,
            **{
              'data-toggle': "collapse",
              'data-target': "#navbarSupportedContent",
              'aria-controls': 'navbarSupportedContent',
              'aria-expanded': 'false',
              'aria-expanded': 'Toggle navigation'
            }, 
            children=[
              html.Span(className="navbar-toggler-icon", children=[
                html.I(className="fa fa-bars")
              ])
            ]) # Button
        ]), # Nav
        tab_links_layout(tab_links)
      ]) # Header

#<button class="navbar-toggler" type="button" data-toggle="collapse" 
# data-target="#navbarSupportedContent" 
# aria-controls="navbarSupportedContent"
#  aria-expanded="false" 
# aria-label="Toggle navigation">
#        <span class="navbar-toggler-icon"><i class="fas fa-bars"></i></span>
#    </button>