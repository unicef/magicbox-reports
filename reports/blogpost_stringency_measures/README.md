# Blogpost on measures enacted by governments
 

# Description of files

The present folder contains the code to manipulate, calculate and save the relevant datasets for creating the interactive plots as in the blogpost.

* [blogpost-stringency-measures_save-data.ipynb](blogpost-stringency-measures_save-data.ipynb)  

    Code to download datasets on COVID-19 statistics, government stringency index and maps. It does several calculations in order to save output files the information needed to reproduce the plots in the blogpost in an interactive way.

    For the geographical boundaries of the map, a dataset from geopandas is used, not the official UN since it's not clear the copyright restriction.

    See [README.md](../data/README.md) in the `data` folder for more info about the files. Below a summary on which files and values must be used to reproduce the plots in the blogpost.

* [blogpost-stringency-measures.ipynb](blogpost-stringency-measures.ipynb)

    Code to download datasets on COVID-19 statistics (version from ECDC no longer updated daily), government stringency index and maps. Same version used to produce the static figures in the blogpost, not optmized as several functions do the same calculations.

# Files and variables to use for interactive plots

See [README.md](../data/README.md) in `data` folder.


