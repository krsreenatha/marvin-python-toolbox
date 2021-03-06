#!/usr/bin/env python
# coding=utf-8

# Copyright [2017] [B2W Digital]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta
from .._compatibility import six
from .._logging import get_logger

from .engine_base_action import EngineBaseOnlineAction


__all__ = ['EngineBasePrediction']
logger = get_logger('engine_base_prediction')


class EngineBasePrediction(EngineBaseOnlineAction):
    __metaclass__ = ABCMeta

    _model = None
    _metrics = None

    def __init__(self, **kwargs):
        self._model = self._get_arg(kwargs=kwargs, arg='model')
        self._metrics = self._get_arg(kwargs=kwargs, arg='metrics')

        super(EngineBasePrediction, self).__init__(**kwargs)

    @property
    def model(self):
        return self._load_obj(object_reference='_model')

    @model.setter
    def model(self, model):
        self._save_obj(object_reference='_model', obj=model)

    @property
    def metrics(self):
        return self._load_obj(object_reference='_metrics')

    @metrics.setter
    def metrics(self, metrics):
        self._save_obj(object_reference='_metrics', obj=metrics)

