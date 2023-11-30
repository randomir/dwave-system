# Copyright 2018 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

__all__ = ['__version__', '__author__', '__authoremail__', '__description__']

__version__ = '1.22.0'
__author__ = 'D-Wave Systems Inc.'
__authoremail__ = 'tools@dwavesys.com'
__description__ = 'All things D-Wave System.'


# register the non-open-source packages required for dwave-drivers to work
contrib = [{
    'name': 'drivers',
    'title': 'D-Wave Drivers',
    'description': 'These drivers enable some automated performance-tuning features.',
    'license': {
        'name': 'D-Wave EULA',
        'url': 'https://docs.ocean.dwavesys.com/eula',
    },
    'requirements': [
        'dwave-drivers>=0.4.4',
    ]
}]
