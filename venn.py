#!/usr/bin/env python3

# VENN
# 2023 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
from typing import List

def venn(set_1: set,
         set_2: set,
         set_3: set = None,
         labels: List[str] = ["1", "2", "3"],
         colors: List[str] = ["#4361EE", "#4CC9F0", "#F72585"],
         alpha: float = 0.6,
         contour: bool = False,
         linewidth: float = 0.5,
         filename: str = None) -> plt.figure:

    if set_3 is None:

        if len(labels) > 2:
