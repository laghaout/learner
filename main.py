# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:47:49 2024
"""

import json
import learner.learner as lea
import learner.utilities as util
import learner.wrangler as wra
import sys


def main(task: str = None, kwargs: dict = dict(config='config.json')) -> object:

    with open(kwargs["config"]) as file:
        kwargs = json.load(file)

    match task:
        case 'oneoffwrangle':
            pass  # TODO
        case 'wrangle':
            return wra.Wrangler(**kwargs['wrangler'])
        case 'train':
            wrangler = wra.Wrangler(**kwargs["wrangler"])
            if isinstance(kwargs["learner"], dict):
                learner = lea.Learner(data=wrangler, **kwargs['learner'])
                learner.design()
            elif isinstance(kwargs["learner"], lea.Learner):
                learner = kwargs["learner"]
                learner.data = wrangler
            learner.train()
            if hasattr(learner.data.dataset, 'test'):
                learner.test()
            return learner
        case 'test':
            wrangler = wra.Wrangler(**kwargs["wrangler"])
            assert isinstance(kwargs["learner"], lea.Learner), "No learner specified!"
            learner = kwargs["learner"]
            learner.data = wrangler
            learner.test()
            return learner.report.test
        case 'serve':
            wrangler = wra.Wrangler(**kwargs["wrangler"])
            assert isinstance(kwargs["learner"], lea.Learner), "No learner specified!"
            learner = kwargs["learner"]
            learner.data = wrangler
            return learner.serve()
        case _:
            wrangler = wra.Wrangler(**kwargs['wrangler'])
            learner = lea.Learner(data=wrangler, **kwargs['learner'])
            learner.explore()
            learner.design()
            learner.train()
            learner.test()
            learner.serve()
            learner.save()
            return learner


if __name__ == "__main__":

    match len(sys.argv):
        # CLI call with default arguments
        case 2:
            output = main(sys.argv[1])
        # CLI call with specified arguments
        case 3:
            pass  # TODO
        # Default run
        case _:
            output = main()

#%% Experiment

pass