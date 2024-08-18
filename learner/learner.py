# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:16:03 2024

@author: amine
"""

from pydantic import BaseModel
from types import SimpleNamespace
from typing import Optional
import learner.utilities as util
import learner.wrangler as wra


class Learner(BaseModel):
    data: wra.Wrangler = None
    params: Optional[dict] = None
    model: object = None
    report: dict = {
        k: dict(delta_tau=None)
        for k in "wrangle explore design train test serve".split()}
    save_to: Optional[str | tuple] = None

    def model_post_init(self, __context: dict[str, any]) -> None:
        if self.report is not None:
            self.report = SimpleNamespace(**self.report)
        if self.params is not None:
            self.params = SimpleNamespace(**self.params)

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

    def train(self, data: wra.Wrangler = None):
        util.disp("==== TRAIN =======================================")

    def test(self, data: wra.Wrangler = None):
        util.disp("==== TEST ========================================")

    def serve(self, data: wra.Wrangler = None):
        util.disp("==== SERVE =======================================")

    def save(self):
        util.disp("==== SAVE ========================================")
