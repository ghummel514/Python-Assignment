#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import matplotlib.pyplot as plt

"""
1. Define a function to count kmers of size k, where k is specified as an argument.
2. Define a function to create a pandas data frame containing all possible k and the associated
number of observed and expected kmers (see above table).
3. Define a function to produce a graph from the data frame of the proportion of each kmer
observed.
4. Define a function to calculate linguistic complexity.
5. Write a script to thoroughly test each of your functions.
6. Use the main function to read in your sequence data and output results.
7. Create a github repository including a README (in markdown) to submit your work. Be sure that
all your functions have appropriate docstrings.
"""


#1. count kmers

# All possible k-mers
def k_possible(k, sequence):
    l = len(sequence)
    count = 0
    if 4 ** k > l:
        count = l - k + 1
    elif 4 ** k <= l:
        count = 4 ** k
    return count

# All observed k-mers
def k_observed(k, sequence):
    observed_list = []
    l = len(sequence)
    for i in range(l - k + 1):
        kmer = ''
        for n in range(k):
            kmer = kmer + sequence[i+n]
        
        # save observed kmers in list
        if kmer not in observed_list:
            observed_list.append(kmer)
        else:
            continue
    return len(observed_list)


#2. create dataframe of all possible k, observed, and expected kmers

def create_dataframe(l, sequence):
    possible_lists = []
    observed_lists = []
    total_lists = []
    
    for k in range(1,l+1):
        observed_kmers = k_observed(k, sequence)
        possible_kmers = k_possible(k, sequence)
        possible_lists.append(possible_kmers)
        observed_lists.append(observed_kmers)
        total_lists.append(k)
        
    df = pd.DataFrame({
        'k':total_lists,
        'Possible kmers':possible_lists,
        'Observed kmers':observed_lists,
    })    
    
    return df

#3. proudce a graph from data frame

def graph(df):
    x = df.index
    y1 = df["Possible kmers"]
    y2 = df["Observed kmers"]
    plt.figure(figsize = (10,7))
    plt.plot(x,y1,'D', markerfacecolor = "purple",label = 'Possible k-mers', alpha = 0.6, markersize = 11)
    plt.plot(x,y2,'o', markerfacecolor = "yellow", label = 'Observed k-mers', alpha = 0.6, markersize = 10)
    plt.xlabel('k')
    plt.ylabel('kmers')
    plt.legend()
    plt.show()


#4. calculate linguistic complexity

def complexity(df):
    possible_sum = df["Possible kmers"].sum()
    observed_sum = df["Observed kmers"].sum()
    return observed_sum/possible_sum

#5. test script


#6. main function to read in sequence data and output results

def main():
    #define sequence
    sequence = 'ATTTGGATT'
    #create dataframe
    df = create_dataframe(9, sequence)
    #plot observed vs. possible sequences
    graph(df)
    #Plot dataframe table with observed and possible values and ling. complexity
    print("________________________________________________________________________")
    print("All Possible k and the Associated Number of Observed and Expected k-mers")
    print("________________________________________________________________________")
    print(df)
    print("________________________________________________________________________")
    print("The linguistic complexity is", complexity(df))
    print("________________________________________________________________________")
    
    
main()



# In[72]:




    


# In[ ]:




