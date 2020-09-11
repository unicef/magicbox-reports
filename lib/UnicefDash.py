import dash
import dash_html_components as html


class UnicefDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        # Inspect the arguments by printing them
        print(kwargs)
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>My App</title>
                {metas}
                {css}
            </head>
            <body>
              <nav class="navbar navbar-expand-md flex-column flex-md-row bd-navbar p-0">
  <a class="navbar-brand navbar-line d-none d-md-block d-lg-block my-2 ml-3"
    href="/" aria-label="Unicef">
    <img class="img-fluid" alt="unicef-logo"
      src="assets/unicef-logo.svg">
  </a>
  <a class="navbar-brand" href="/">Magicbox reports</a>
</nav>
          <div class="doc container">
                {app_entry}
                {config}
                {scripts}
                {renderer}
                </div>
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'],
            metas=kwargs['metas'],
            css=kwargs['css'])