# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:16:03 2024
"""

from pydantic import BaseModel
import time
from types import SimpleNamespace
from typing import Optional
import learner.utilities as util
import learner.wrangler as wra


class Learner(BaseModel):
    data: wra.Wrangler = None
    params: Optional[dict] = dict()
    hyperparams: Optional[dict] = dict()  # Model hyperparameters
    model: object = None
    report: dict = {
        k: dict(runtime=None)
        for k in "wrangle explore design train test serve".split()}
    save_to: Optional[str | tuple] = None

    def model_post_init(self, __context: dict[str, any]) -> None:
        self.report = SimpleNamespace(**self.report)
        self.params = SimpleNamespace(**self.params)
        self.hyperparams = SimpleNamespace(**self.hyperparams)

    def __call__(self, tasks: str):
        tasks = tasks.split()
        if "wrangle" in tasks:
            self.wrangle()
        if "train" in tasks:
            self.design()
            self.train()
        if "test" in tasks:
            self.test()
        if "serve" in tasks:
            self.serve()

    def explore(self, data: wra.Wrangler = None):
        util.disp("==== EXPLORE =====================================")

    def design(self):
        util.disp("==== DESIGN ======================================")

        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            from sklearn.linear_model import LogisticRegression
            self.model = LogisticRegression(C=self.hyperparams.C)
        #%% End example #######################################################

    def train(self, data: wra.Wrangler = None):
        util.disp("==== TRAIN =======================================")

        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            if data is None:
                data = self.data
                dataset = self.data.dataset.train
            else:
                dataset = self.data.dataset

            runtime = time.time()
    
            self.model.fit(
                dataset[data.params.feature_names],
                dataset[data.params.target_names],
            )
    
            self.report.train["score"] = self.model.score(
                dataset[data.params.feature_names],
                dataset[data.params.target_names]
                )
    
            self.report.train["runtime"] = time.time() - runtime

    def test(self, data: wra.Wrangler = None):
        util.disp("==== TEST ========================================")

        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            if data is None:
                data = self.data
                dataset = self.data.dataset.test
            else:
                dataset = self.data.dataset
            
            runtime = time.time()
                
            self.report.test["score"] = self.model.score(
                dataset[data.params.feature_names],
                dataset[data.params.target_names]
                )
                
            self.report.test["runtime"] = time.time() - runtime
        #%% End example #######################################################

    def serve(self, data: wra.Wrangler = None):
        util.disp("==== SERVE =======================================")

        #%% Start example #####################################################
        import pandas as pd
        
        if self.params.RUN_EXAMPLE:
            if data is None:
                data = self.data
                dataset = self.data.dataset.serve
            else:
                dataset = self.data.dataset
            
            runtime = time.time()
                
            prediction = self.model.predict(
                dataset[data.params.feature_names]
                )
            
            prediction = pd.DataFrame(
                prediction,
                columns=['target'],
                index=dataset[data.params.feature_names].index)
            
            prediction.target = prediction.target.apply(
                lambda x: str(data.params.classes[int(x)]))
            
            self.report.serve["prediction"] = prediction
            self.report.serve["runtime"] = time.time() - runtime
        #%% End example #######################################################


    def save(self):
        util.disp("==== SAVE ========================================")
        
        #%% Start example #####################################################
        if self.params.RUN_EXAMPLE:
            import dill
            import os
            
            util.create_directory(os.path.join(*self.save_to))
            with open(os.path.join(*self.save_to+('learner.dill',)), 'wb') as f:
                dill.dump(self, f)
        #%% End example #######################################################
        
        