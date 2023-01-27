# Quick Venn Diagrams

A wrapper to create venn diagrams quickly with [matplotlib-venn](https://github.com/konstantint/matplotlib-venn) in python using sets as input and some pre-configured aesthetics that I commonly use.

## Requirements

Requires [matplotlib](https://matplotlib.org/) and [matplotlib-venn](https://github.com/konstantint/matplotlib-venn).

```
pip install -r requirements.txt
```

## Usage

```python
from venn import venn

set_1 = {"A", "B", "C", "D"}
set_2 = {"C", "D", "E", "F"}
set_3 = {"D", "G", "H", "I"}

# 2 set venn diagram
fig_1 = venn(set_1, set_2)
# 3 set venn diagram
fig_2 = venn(set_1, set_2, set_3)
```

Function `venn` documentation:
```python
def venn(set_1: set,
         set_2: set,
         set_3: set = None,
         labels: List[str] = ["Set 1", "Set 2", "Set 3"],
         colors: List[str] = ["#4361EE", "#4CC9F0", "#F72585"],
         alpha: float = 0.6,
         contour: bool = False,
         linewidth: float = 0.5,
         title: str = "Venn Diagram",
         filename: str = None) -> plt.figure:

    """
    DESCRIPTION
    Wrapper with some defaults that I use for creating venn diagrams with the
    matplotlib-venn package (https://github.com/konstantint/matplotlib-venn).

    PARAMETERS:
        set_1: set
            first set of the venn diagram
        set_2: set
            second set of the venn diagram
        set_3: set
            [Optional]
            if specified a three set venn diagram will be drawn, if not specified
            the two set venn diagram of set_1 and set_2 will be drawn
            DEFAULT: None
        labels: List[str]
            [Optional]
            list of labels for the sets
            DEFAULT: ["Set 1", "Set 2", "Set 3"]
        colors: List[str]
            [Optional]
            list of valid matplotlib colors to use for the venn circles
            DEFAULT: ["#4361EE", "#4CC9F0", "#F72585"]
        alpha: float
            [Optional]
            color opacity
            DEFAULT: 0.6
        contour: bool
            [Optional]
            if contour should be drawn around venn circles
            DEFAULT: False
        linewidth: float
            [Optional]
            linewidth of the contour
            DEFAULT: 0.5
        title: str
            [Optional]
            title of the figure
            DEFAULT: "Venn Diagram"
        filename: str
            [Optional]
            if given the venn diagram will be saved at the specified location in
            .png and .svg format with and without title
            DEFAULT: None

    RETURNS:
        plt.figure
            matplotlib figure object of the created venn diagram
    """
```

## License

- [MIT](https://github.com/michabirklbauer/venn/blob/master/LICENSE)

## Contact

- [micha.birklbauer@gmail.com](mailto:micha.birklbauer@gmail.com)
