# csv-email-cleaner
Cleans a .csv file, in which only remains rows with valid e-mail domains, given a specific situation.

## How does it work?
Basically, looks for .csv files in a given directory, filters for rows with valid email domains and
then creates new .csv files with filtered rows only. 

It considers ".com" and country domains (such as ".br", ".us", ".mx") as valid domains.

## How to run
`python csv-email-cleaner.py <directory with .csv files> <destination directory of clean .csv files>`