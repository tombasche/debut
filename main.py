from src.slide import Slide
from src.slideshow import SlideShow


def main():
    first_slide = Slide(
        heading="Introduction",
        text="Continuous attention to technical excellence and good design enhances agility."
    )
    next_slide = Slide(
        heading="What is technical excellence?",
        text="""
* Technical excellence, with respect to software, refers to a level  of quality, maintainability and extensibility of software that is     primarily expressed through a lack of defects and an abundance in     business value."""
    )
    slideshow = SlideShow(
        [first_slide, next_slide],
    )
    slideshow.present()


if __name__ == "__main__":
    main()
