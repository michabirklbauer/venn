#!/usr/bin/env python3

# VENN - TESTS
# 2023 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

set_1 = \
{'AKVTSAMQTMLFTMLR2-ANSAVKLQ6',
 'AKVTSAMQTMLFTMLR2-KLDNDALNNIINNAR1',
 'AKVTSAMQTMLFTMLR2-MADQAMTQMYKQAR11',
 'AKVTSAMQTMLFTMLR2-SEDKR4',
 'AKVTSAMQTMLFTMLR4-MADQAMTQMYKQAR11',
 'AKVTSAMQTMLFTMLR5-ANSAVKLQ6',
 'AKVTSAMQTMLFTMLR5-KLDNDALNNIINNAR1',
 'AKVTSAMQTMLFTMLR5-MADQAMTQMYKQAR11',
 'AKVTSAMQTMLFTMLR9-ANSAVKLQ6',
 'AKVTSAMQTMLFTMLR9-KLDNDALNNIINNAR1',
 'AKVTSAMQTMLFTMLR9-MADQAMTQMYKQAR11',
 'ANSAVKLQ6-DGCVPLNIIPLTTAAKLMVVIPDYNTYK13',
 'ANSAVKLQ6-DGCVPLNIIPLTTAAKLMVVIPDYNTYK16',
 'ANSAVKLQ6-KLDNDALNNIINNAR1',
 'ANSAVKLQ6-KLEKMADQAMTQMYK1',
 'ANSAVKLQ6-KLEKMADQAMTQMYK4',
 'ANSAVKLQ6-SLNVAKSEFDRDAAMQR6',
 'DGCVPLNIIPLTTAAKLMVVIPDYNTYK13-SEDKR4',
 'DGCVPLNIIPLTTAAKLMVVIPDYNTYK16-KLDNDALNNIINNAR1',
 'DGCVPLNIIPLTTAAKLMVVIPDYNTYK16-SEDKR4',
 'KLDNDALNNIINNAR1-KLDNDALNNIINNAR1',
 'KLDNDALNNIINNAR1-KLEKMADQAMTQMYK4',
 'KLDNDALNNIINNAR1-KSLNVAK1',
 'KLDNDALNNIINNAR1-MADQAMTQMYKQAR11',
 'KLDNDALNNIINNAR1-MADQAMTQMYKQAR7',
 'KLDNDALNNIINNAR1-SEDKR4',
 'KLDNDALNNIINNAR1-SLNVAKSEFDRDAAMQR6',
 'KLEKMADQAMTQMYK1-SEDKR4',
 'KLEKMADQAMTQMYK4-SEDKR4',
 'KSLNVAK1-SEDKR4',
 'MADQAMTQMYKQAR10-SEDKR4',
 'MADQAMTQMYKQAR11-SEDKR4',
 'SEDKR4-SLNVAKSEFDRDAAMQR6'}

set_2 = \
{'AKVTSAMQTMLFTMLR2-ANSAVKLQ6',
 'AKVTSAMQTMLFTMLR2-KLDNDALNNIINNAR1',
 'AKVTSAMQTMLFTMLR2-MADQAMTQMYKQAR11',
 'AKVTSAMQTMLFTMLR2-MADQAMTQMYKQAR7',
 'AKVTSAMQTMLFTMLR4-MADQAMTQMYKQAR7',
 'ANSAVKLQ6-DGCVPLNIIPLTTAAKLMVVIPDYNTYK16',
 'ANSAVKLQ6-KLDNDALNNIINNAR1',
 'ANSAVKLQ6-KLEKMADQAMTQMYK1',
 'ANSAVKLQ6-SLNVAKSEFDRDAAMQR6',
 'DGCVPLNIIPLTTAAKLMVVIPDYNTYK16-KLDNDALNNIINNAR1',
 'DGCVPLNIIPLTTAAKLMVVIPDYNTYK16-SEDKR4',
 'KLDNDALNNIINNAR1-KLEKMADQAMTQMYK4',
 'KLDNDALNNIINNAR1-MADQAMTQMYKQAR10',
 'KLDNDALNNIINNAR1-MADQAMTQMYKQAR11',
 'KLDNDALNNIINNAR1-SLNVAKSEFDRDAAMQR6',
 'KLEKMADQAMTQMYK1-SEDKR4',
 'KSLNVAK1-SEDKR4',
 'MADQAMTQMYKQAR11-SEDKR4',
 'SEDKR4-SLNVAKSEFDRDAAMQR6'}

set_3 = \
{'AKVTSAMQTMLFTMLR2-KLDNDALNNIINNAR1',
 'AKVTSAMQTMLFTMLR2-MADQAMTQMYKQAR11',
 'DGCVPLNIIPLTTAAKLMVVIPDYNTYK16-KLDNDALNNIINNAR1',
 'KLDNDALNNIINNAR1-KLDNDALNNIINNAR1',
 'KLDNDALNNIINNAR1-KLEKMADQAMTQMYK4',
 'KLDNDALNNIINNAR1-KSLNVAK1',
 'KLDNDALNNIINNAR1-MADQAMTQMYKQAR11',
 'KLDNDALNNIINNAR1-SLNVAKSEFDRDAAMQR6',
 'KLEKMADQAMTQMYK1-SEDKR4',
 'KLEKMADQAMTQMYK4-SEDKR4',
 'KSLNVAK1-SEDKR4',
 'MADQAMTQMYKQAR11-SEDKR4',
 'SEDKR4-SLNVAKSEFDRDAAMQR6'}

from venn import venn

def test_venn2():
    assert venn(set_1,
                set_2,
                label = ["Set 1", "Set 2"],
                colors = ["#4361EE", "#4CC9F0"]) is not None

def test_venn3():
    assert venn(set_1,
                set_2,
                set_3) is not None