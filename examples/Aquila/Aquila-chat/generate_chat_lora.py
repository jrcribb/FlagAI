# Copyright © 2023 BAAI. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
import os
import torch
from flagai.auto_model.auto_loader import AutoLoader
from flagai.model.predictor.predictor import Predictor
from flagai.data.tokenizer import Tokenizer
import torch.nn as nn
from flagai.model.tools.lora.prepare_lora import lora_transfer
state_dict = "./checkpoints_in/"
model_name = 'aquila-7b'


loader = AutoLoader("lm",
                    model_dir=state_dict,
                    model_name=model_name,
                    use_cache=True,
                    fp16=True,
                    adapter_dir='./output')
model = loader.get_model()

tokenizer = loader.get_tokenizer()

model.eval()
mode.half()
model.cuda()

predictor = Predictor(model, tokenizer)

texts = [
    "Find the product of the numbers: 5 and 8",
    "Provide five tips for effectively using tape measures",
    "Create a resume for a job in web development.",
]

for text in texts:
    print('-' * 80)
    text = f'{text}'
    print(f"text is {text}")
    with torch.no_grad():
        out = predictor.predict_generate_randomsample(text,
                                                      out_max_length=200,
                                                      top_p=0.95)
        print(f"pred is {out}")
