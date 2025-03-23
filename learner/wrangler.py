# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:35:49 2024
"""

from pydantic import BaseModel
from types import SimpleNamespace
from typing import Optional
import learner.utilities as util

class Wrangler(BaseModel):
    dataset: object = None
    params: Optional[dict] = dict()
    save_to: Optional[str | tuple] = None
    report: Optional[dict] = dict(explore=None)

    def model_post_init(self, __context: dict[str, any]) -> None:
        self.report = SimpleNamespace(**self.report)
        self.params = SimpleNamespace(**self.params)
        
        self()

    def __call__(self):
        util.disp("==== WRANGLE =====================================")
        
        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            import pandas as pd
            from numpy import hstack
            from sklearn.datasets import load_iris
            data = load_iris()
            self.params.classes = data.target_names
            self.params.feature_names = data.feature_names
            self.dataset = pd.DataFrame(
                hstack([data.data, data.target.reshape(-1, 1)]),
                columns=self.params.feature_names+["target"])
        #%% End example #######################################################
        
        self.shuffle()
        self.split()
        self.normalize()

    def explore(self):
        util.disp("==== Explore")

    def split(self):
        util.disp("==== Split")
        
        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            from sklearn.model_selection import train_test_split
            
            # First split: Rrain vs. the rest
            train_df, temp_df = train_test_split(
                self.dataset, test_size=1 - self.params.data_split["train"], 
                random_state=self.params.random_state)
            
            # Second split: Test and serve
            test_size = self.params.data_split["test"]
            test_size /= self.params.data_split["test"] + self.params.data_split["serve"]
            
            test_df, serve_df = train_test_split(
                temp_df, 
                test_size=1 - test_size, 
                random_state=self.params.random_state)
            
            self.dataset = SimpleNamespace(
                **dict(train=train_df, test=test_df, serve=serve_df))
        #%% End example #######################################################

    def normalize(self):
        util.disp("==== Normalize")
        
    def shuffle(self):
        util.disp("==== Shuffle")
        
        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            self.dataset = self.dataset.sample(frac=1, random_state=self.params.random_state)
        #%% End example #######################################################

class Input(BaseModel):
    index: int

class Output(BaseModel):
    index: int
    #%% Start example #########################################################
    target: str        
    #%% End example ###########################################################