""" flexx.ui

GUI toolkit based on web technology with a Pythonic API.
"""

from ..app import run, stop, call_later, make_app
from ..app import Pair, get_instance_by_id

from .widget import Widget  #, Window
from .button import Label, Button
from .layout import Layout, Box, HBox, VBox
from .layout import BaseTableLayout, FormLayout, GridLayout
from .layout import Splitter, HSplitter, VSplitter
from .layout import PinboardLayout
from .progressbar import ProgressBar
from .layout2 import Panel, PlotWidget, PlotLayout
