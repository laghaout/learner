# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:49:39 2024

@author: amine
"""

from pydantic import BaseModel

class MyModel(BaseModel):
    x: int
    y: int
    z: int = None  # Default value will be overridden in model_post_init

    def model_post_init(self, __context: dict[str, any]) -> None:
        # Perform post-initialization logic here
        self.z = self.x + self.y
        # object.__setattr__(self, 'z', self.x + self.y)

# Example usage
model = MyModel(x=1, y=2)
print(model.z)  # Output: 3
