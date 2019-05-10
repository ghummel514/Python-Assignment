#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from assignment4 import *


def test_observed():
    sequence = 'ATTTGGATT'
    k = 1
    observed = k_observed(seq, k)
    expected = 3
    assert expected == observed

def test_possible():
    sequence = 'ATTTGGATT'
    k = 1
    expected = 4
    observed = k_possible(seq, k)
    assert expected == observed
    
def test_ling_complexity():
    complx = .875
    assert complx == complexity(observed,possible)
    sequence = 'ATTTGGATT'
    df = create_dataframe(9, sequence)
    expected = complexity(df)
    assert expected == complx
    
def test_df():
    sequence = 'ATTTGGATT'
    df = create_dataframe(9, sequence)
    obs_obs = df["Observed kmers"].tolist()
    obs_poss = df["Possible kmers"].tolist()
    exp_obs = [3,5,6,6,5,4,3,2,1]
    exp_poss = [4,8,7,6,5,4,3,2,1]
    assert obs_obs == exp_obs
    assert obs_poss == exp_poss

    

