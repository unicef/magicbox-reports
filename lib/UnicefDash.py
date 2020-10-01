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