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
