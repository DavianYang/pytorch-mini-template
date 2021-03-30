import logging
from argparse import ArgumentParser
from pathlib import Path
from typing import Any

import ignite.distributed as idist
from ignite.engine.events import Events
from ignite.utils import manual_seed

from single_cg.engines import create_engines
from single_cg.handlers import get_handlers, get_logger
from single_cg.utils import get_default_parser