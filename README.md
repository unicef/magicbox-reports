# 

# How to create a new report

1. Clone the repo
  
    ```bash
      git clone repo.url/magicbox-reports
      cd magicbox-reports
    ```

2. Create a new branch
    ```bash
      git branch report/my-report
    ```

3. Create a subfolder in the reports folder following this convention `YYYY-MM-name-of-the-report`
    ```bash
      cd reports
      mkdir 2020-08-my-report
    ```

4. Create a file __init__.py in the new folder
    ```bash
      cd 2020-08-my-report
      touch __init__.py
    ```
5. Add a method called `page` that receives an argument app
  
    ```python
      def page(app):
        # Add here your code
    ```

6. Adding the metadata
    

7. 