# Debut

## Have a play first

```
python examples/main.py
```

The slideshow will pause for input after the headers and each paragraph of text after it animates.

Once the nav indicator appears in the bottom left corner then you can choose to go back or forward.

Note that this will only work in supported terminals ... the IntelliJ terminal isn't one of them.


### Make your own slideshow: 

Clone this repo and install it with `python3 setup.py install`

```python
from debut import SlideShow, Slide, TitleSlide, Text

title_slide = TitleSlide(
    title="Dagon",
    author="H.P. Lovecraft"
)
slide_1 = Slide(
    heading="Spooky things",
    text=Text([
        "First a spooky thing happened",
        "Then another"
    ])
)
slideshow = SlideShow([title_slide, slide_1])
slideshow.present()
```

* A `Text()` object accepts a list of strings to render as individual paragraphs.
* A `DotPointText()` object can also be used which will render them as individual paragraphs indented with an asterisk.