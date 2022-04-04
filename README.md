## A Look Into Music Mood Patterns Jan 2020 - Jan 2022

# Contributors: Isa de Luis and Lukas Milroy

This project was created as a way of taking a deeper look into popular music over the course of the pandemic. We used the [Billboard API](https://rapidapi.com/LDVIN/api/billboard-api/) to gather data on the top 10 songs each month from January 2020 to January 2022. We then analyzed the key words in each song through sentiment analysis.

The Billboard API is an API offered by [rapidAPI](https://rapidapi.com/hub) and created by the user [LDVIN](https://rapidapi.com/user/LDVIN). In order to use this API, you will need to create an account through rapid API and follow thr instructions on the [Billboard API](https://rapidapi.com/LDVIN/api/billboard-api/) page. The API provides the Billboard chart rankings for each week, along with information on song titles, artists, and previous chart rankings. To use the API, you must sign up for an API key on its homepage. Then, you can use Requests to get the Billboard Top 100 data for any day. We called the API for the last day of each month from January 31, 2020 through January 31, 2022. After gathering data, we saved it in a dictionary so we could access it later without having to do pull requests each time we revisited the project.

To ensure that your  plots will display correctly, you will need to run the following code:

      import matplitlib.pyplot at plt
      import numpy as np
      import pandas as pd
