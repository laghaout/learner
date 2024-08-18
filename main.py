# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:47:49 2024

@author: amine
"""

import json
import learner.learner as lea
import learner.utilities as util
import learner.wrangler as wra
import sys


def assemble_kwargs(task: str = None, kwargs: dict = None):

    envars = util.get_env_variables()

    with open(envars.DEFAULT_CONFIG, 'r') as file:
        default_config = json.load(file)
        for k, v in default_config.items():
            default_config[k] = dict(params=dict(envars=envars)) | v

    if kwargs is not None:
        return default_config | kwargs
    else:
        return default_config


def main(task: str, kwargs: dict = dict()) -> object:

    kwargs = assemble_kwargs(task, kwargs)

    match task.lower():
        case 'oneoffwrangle':
            pass  # TODO
        case 'wrangle':
            return wra.Wrangler(**kwargs['wrangler'])
        case 'train':
            wrangler = wra.Wrangler(**kwargs['wrangler'])
            learner = lea.Learner(data=wrangler, **kwargs['learner'])
            learner.design()
            learner.train()
            if hasattr(learner.data.dataset, 'test'):
                learner.test()
            return learner
        case 'test':
            learner = kwargs['learner']
            learner.data = wra.Wrangler(**kwargs['wrangler'])
            learner.test()
            return learner.report.test
        case 'serve':
            learner = kwargs['learner']
            learner.data = wra.Wrangler(**kwargs['wrangler'])
            return learner.serve()
        case 'all':
            wrangler = wra.Wrangler(**kwargs['wrangler'])
            learner = lea.Learner(data=wrangler, **kwargs['learner'])
            learner.explore()
            learner.design()
            learner.train()
            learner.test()
            learner.serve()
            learner.save()
            return learner
        case _:
            assert False, f"There is no such task as task = `{task}`."


if __name__ == "__main__":

    match len(sys.argv):
        # CLI call with default arguments
        case 2:
            output = main(sys.argv[1])
        # CLI call with specified arguments
        case 3:
            kwargs = assemble_kwargs(sys.argv[1], sys.argv[2])
            output = main(sys.argv[1], **kwargs)
        # Default run
        case _:
            task = 'all'
            if False:
                kwargs = assemble_kwargs(
                    task, dict(
                        learner=dict(params=dict(a=7))))
                output = main(task, kwargs)
            else:
                output = main(task)
            print(output)
