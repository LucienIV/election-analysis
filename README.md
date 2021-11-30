# election-analysis

## Overview of Election Audit

The purpose of this election audit analysis is to take the earlier results which determined the number and percentage of votes obtained by each candidate and add to that an analysis of the number of votes in each county involved in the election as well as which county had the most votes cast within it.

## Election-Audit Results

The results output by the script display the results as follows:

![image](https://user-images.githubusercontent.com/92831138/144114565-39498d4c-c04b-4e59-91db-8fdb45893715.png)

* There were a total of 369,711 votes cast in the election
* Arapahoe County had 24,801 votes cast, equalling 6.7% of the total votes cast.
* Jefferson County had 38,855 votes cast, equalling 10.5% of the total votes cast.
* Denver County had the most votes cast of the analyzed counties with 306,055 votes cast, equalling 82.8% of the total votes cast.
* Raymon Anthony Doane received 11,606 votes, equalling 3.1% of the total votes cast.
* Charles Casper Stockham received 85,213 votes, equalling 23% of the total votes cast.
* Diane Degette was the winner of the election, receiving 272,892 votes. This is equal to 73.8% of the total votes cast.

## Election-Audit Summary

The script used for this audit could easily be used for any other election audit. Rather than typing a list of candidates or counties into the script, it dynamically populates dictionaries and lists based on the information present in the csv the data is pulled from. As long as the csv file has the required information it would be easy to make the minor modificaitons necessary to reuse this script. One obvious change necessary to the script would be changing the file paths in lines 9 and 11 to pull from and write to the correct locations. Case in point, the current code `file_to_load = os.path.join("Resources", "election_results.csv")` will not pull from the correct document if reused. Lines 47 and 50 could potentially need to be changed as well depending on how the csv that data is being pulled from is formatted. The code `candidate_name = row[2]` expects the candidate name to be in the third column of the csv for example. This code would not work without modificaiton were the data in a different column in another csv. 
