# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:16:03 2024
"""

from pydantic import BaseModel
from types import SimpleNamespace
from typing import Optional
import learner.utilities as util
import learner.wrangler as wra


class Learner(BaseModel):
    data: wra.Wrangler = None
    params: Optional[dict] = dict()
    model: object = None
    report: dict = {
        k: dict(delta_tau=None)
        for k in "wrangle explore design train test serve".split()}
    save_to: Optional[str | tuple] = None

    def model_post_init(self, __context: dict[str, any]) -> None:
        self.report = SimpleNamespace(**self.report)
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

        #%% Start example #####################################################
        import os
        import tensorflow as tf

        early_stopping_threshold = self.params.early_stopping_threshold
        metric = self.params.metrics[0]
        
        class EarlyStopping(tf.keras.callbacks.Callback):
            def on_epoch_end(
                self,
                epoch,
                logs={},
                early_stopping_threshold=early_stopping_threshold,
            ):
                if logs.get(f"val_{metric}") > early_stopping_threshold:
                    print(
                        f"\nReached {early_stopping_threshold*100}%",
                        "validation accuracy so cancelling training!",
                    )
                    self.model.stop_training = True

        model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(*self.save_to+("checkpoints.keras",)),
            save_weights_only=False,
            verbose=0,
            monitor=f"val_{self.params.metrics[0]}",
            mode="max",
            save_best_only=True,
        )

        self.params.callbacks = [
            EarlyStopping(),
            model_checkpoint_callback,
            tf.keras.callbacks.TensorBoard(
                log_dir=self.save_to,
                histogram_freq=1,
                profile_batch=0,
                write_images=True,
            ),
        ]

        # Model
        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(
                    self.params.hidden_units[0],
                    input_dim=len(self.data.params.feature_names),
                    activation=self.params.activation,
                )
            ]
            + [
                tf.keras.layers.Dense(
                    hidden_units, activation=self.params.activation
                )
                for hidden_units in self.params.hidden_units[1:]
            ]
            + [
                tf.keras.layers.Dense(
                    self.params.output_units,
                    activation=self.params.output_activation,
                )
            ]
        )

        self.model.compile(
            loss=self.params.loss,
            optimizer=self.params.optimizer,
            metrics=self.params.metrics,
        )
        #%% End example #######################################################

    def train(self, data: wra.Wrangler = None):
        util.disp("==== TRAIN =======================================")

    def test(self, data: wra.Wrangler = None):
        util.disp("==== TEST ========================================")

    def serve(self, data: wra.Wrangler = None):
        util.disp("==== SERVE =======================================")

    def save(self):
        util.disp("==== SAVE ========================================")