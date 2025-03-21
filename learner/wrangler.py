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
        import pandas as pd
        from numpy import hstack
        from sklearn.datasets import load_iris
        data = load_iris()
        self.params.target_names = data.target_names
        self.params.feature_names = data.feature_names
        self.dataset = pd.DataFrame(
            hstack([data.data, data.target.reshape(-1, 1)]),
            columns=self.params.feature_names+["target"])
        #%% End example #######################################################
        
        self.shuffle()
        self.split()
        self.normalize()

    def explore(self):
        util.disp("==== EXPLORE")

    def split(self):
        util.disp("==== Split")
        
        #%% Start example #####################################################
        from sklearn.model_selection import train_test_split
        
        # First split: Train (70%) and Temp (30% for test+serve)
        train_df, temp_df = train_test_split(
            self.dataset, test_size=0.3, random_state=42)
        
        # Second split: Test (15%) and Serve (15%)
        test_df, serve_df = train_test_split(
            temp_df, test_size=0.5, random_state=42)
        
        self.dataset = SimpleNamespace(
            **dict(train=train_df, test=test_df, serve=serve_df))
        #%% End example #######################################################

    def normalize(self):
        util.disp("==== Normalize")
        
    def shuffle(self):
        util.disp("==== Shuffle")
        
        #%% Start example #####################################################
        self.dataset = self.dataset.sample(frac=1)
        #%% End example #######################################################