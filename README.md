# Magicbox reports
 

# How to create a new report

1. Clone/Install the repo.
  
    ```bash
      git clone repo.url/magicbox-reports
      cd magicbox-reports
      source venv/bin/activate # use the virtualenv
      pip install
    ```
    If using conda instead of venv:
    ```bash
      conda create -n myenv python=3.8
      conda activate myenv
      pip install -r requirements.txt
    ```

2. Create a new branch and switch to it:
    ```bash
      git branch report/my-report
      git checkout report/my-report
    ```

3. Run the app
    ```bash
      python index.py
    ```

    Open a browser in `http://localhost:8050`

3. Create a subfolder in the reports folder following this convention `YYYY-MM-name-of-the-report`
    ```bash
      cd reports
      mkdir 2020-08-10-my-report
    ```

4. Create a file __init__.py in the new report folder
    ```bash
      cd 2020-08-10-my-report
      touch __init__.py
    ```
5. Add a method called `layout` tha
  
    ```python
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output

    from app import app

    # Contents of the report
    def layout():
      layout = html.H3('Hello world')
      return layout

    ## For callbacks use @app
    # @app.callback(...)
    # def mycallback(...):  
    ```

6. Add the metadata. Within the reports folder create the file `metadata.py`. This file contains the metadata of the report that is used to list it on the homepage.
   
  ```python
    # Report title
    title = "Report 3 title "
    # Meta keywords
    keywords = "keyword1, keyword2, keyword3"
    # Meta description
    description = "description description 3"
    # Summary displayed in homepage
    summary = "Summary Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc mollis pulvinar tellus vel vulputate. Integer ac massa efficitur, sagittis turpis ullamcorper, vehicula velit. Donec placerat cursus leo eu ultrices. In porttitor varius nisl. In iaculis arcu non massa ullamcorper, ac blandit dolor pulvinar. Etiam tempus urna id sapien vulputate, a congue nunc condimentum. Proin pellen "

    # thumbnail displayed on the homepage
    thumb = 'report3.png'
    # Alt
    thumb_alt = 'description for accessibility 3'
  ```
  The `thumb` file must be in `/assets` within the root folder of the project.    

7. Create a PR in github.

# Deployment to test environment

```
   git push heroku master   
```

Open [https://magicbox-reports.herokuapp.com](https://magicbox-reports.herokuapp.com)



Useful links

* https://dash.plotly.com/deployment
