# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:35:49 2024

@author: amine
"""

from pydantic import BaseModel
from types import SimpleNamespace
from typing import Optional
import learner.utilities as util


class Wrangler(BaseModel):
    dataset: object = None
    params: Optional[dict] = None
    save_to: Optional[str | tuple] = None
    report: Optional[dict] = dict(explore=None)
    nrows: Optional[int] = None

    def model_post_init(self, __context: dict[str, any]) -> None:
        if self.report is not None:
            self.report = SimpleNamespace(**self.report)
        if self.params is not None:
            self.params = SimpleNamespace(**self.params)
            
        self()

    def __call__(self):
        util.disp("==== WRANGLE =====================================")
        self.split()
        self.normalize()

    def explore(self):
        util.disp("==== EXPLORE")

    def split(self):
        util.disp("==== Split")

    def normalize(self):
        util.disp("==== Normalize")