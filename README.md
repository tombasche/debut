## Usage

```
python main.py
```

The slideshow will pause for input after the headers and each paragraph of text after it animates.

Once the nav indicator appears in the bottom left corner then you can choose to go back or forward.

Note that this will only work in supported terminals ... the IntelliJ terminal isn't one of them.


## The SlideShow framework

* Probably should think of a name for it and make it a separate library!

### Make your own slideshow: 

```python
from slideshow import SlideShow
from slide import Slide
from text import Text

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