import dash
import dash_html_components as html


class UnicefDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        # Inspect the arguments by printing them
        #print(kwargs)
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>UNICEF Magicbox reports</title>
                {metas}
                {css}
            </head>
            <body>
            <header>
  <a class="skip" href="#contents" tabindex="0">Skip Navigation</a>
  <nav class="navbar navbar-expand-md flex-md-row bd-navbar p-0">
    <a class="navbar-brand navbar-line mr-3" href="./" title="Go home" aria-label="Go Home">
      <img class="img-fluid d-none d-lg-block" alt="" src="/assets/unicef-logo.svg">
    </a>
    <a class="navbar-brand mr-0" href="./">Magicbox reports</a>
    <ul class="navbar-nav rounded-left ml-auto p-2 flex-row d-none d-md-flex p-0">
				<li class="nav-item ml-3">
            <a class="nav-link ml-auto" href="https://github.com/unicef/design-system/"><i class="fab fa-github"></i> Github</a>
				</li>
			</ul>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"><i class="fas fa-bars"></i></span>
    </button>
  </nav>

<div class="collapse navbar-collapse d-md-block bg-white" id="navbarSupportedContent">
  <ul class="nav nav-tabs p-0"><li class="nav-item">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link " role="button" href="/about">About UNICEF Magicbox</a>
      </li>
  </ul>
</div>
</header>
          <div class="doc container mt-4">
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