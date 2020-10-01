import dash
import dash_html_components as html


class UnicefDash(dash.Dash):
    
    
    def interpolate_index(self, **kwargs):
        # Inspect the arguments by printing them
        #print(kwargs)
        kwargs['app_entry'] = """
    <div id="react-entry-point">
                    <div class="_dash_loading d-flex justify-content-center align-items-center">
                        <div class="d-flex justify-content-center align-items-center">
                          <div class="spinner-border" role="status" aria-hidden="true"></div>
                            <strong class='ml-2'>Loading...</strong>
                          </div>
                    </div>
                </div>"""

        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>UNICEF Magicbox reports</title>
                {metas}
                {css}
            </head>
            <body>
                {app_entry}
                {config}
                {scripts}
                {renderer}
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'],
            metas=kwargs['metas'],
            css=kwargs['css'])