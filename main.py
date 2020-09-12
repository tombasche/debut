from src.slide import Slide
from src.slideshow import SlideShow
from src.text import Text, DotPointText


def main():
    slide_1 = Slide(
        heading="Introduction",
        text=Text(["Continuous attention to technical excellence and good design enhances agility."])
    )
    slide_2 = Slide(
        heading="What is technical excellence?",
        text=DotPointText([
            "Technical excellence, with respect to software, refers to a level of quality, maintainability and extensibility of software that is primarily expressed through a lack of defects and an abundance in business value.",
            "This means software which *works* and software that is *valuable*."
        ])
    )
    slide_3 = Slide(
        heading="What is good design?",
        text=DotPointText([
            "To design is to develop a plan or specification for the implementation of something, be it code, data or process.",
            "A good design satisfies certain goals and constraints, takes into account aesthetic and functional considerations and is expected to interact within its environment."
        ])
    )
    slide_4 = Slide(
        heading="How do these things enhance agility?",
        text=DotPointText([
            "A good design, one which adheres to software design principles, provides us with software that allows us to move fast forever.",
            "If we understand and can reason about the design of the code we can make fast decisions on the back of moving business requirements without regressing and compromising the existing speed at which we can make changes.",
            "Technical excellence means less time spent fixing bugs, and less time spent cleaning up mistakes."
        ])
    )
    slide_5 = Slide(
        heading="How do we maintain 'continuous attention'?",
        text=DotPointText([
            "Pair-programming helps us stay honest. Question the why and the how of an implementation. Play devil's advocate! 😈 ",
            "Let's talk about the code during a desk check!",
            "* What might you have done differently?",
            "* What ideas did you discard along the way and why?",
            "* What were the challenges?",
            "* Can the person reading the code understand what it does without you explaining it?",
            "How do we reach our goal in such a way that maintains our agility - is there something that might hinder us as part of a technical solution?",
            "Put yourself in the shoes of a customer or product owner - would they be happy with a 'hacky solution'? They're paying a lot of money for it."
        ])
    )
    slide_6 = Slide(
        heading="So how do we get there?",
        text=DotPointText([
            "There's resources left, right and centre about technical excellence and good design: ",
            "* Clean Code, by Robert Martin (Uncle Bob)",
            "* The Pragmatic Programmer by Andy Hunt and Dave Thomas",
            "* Test-Driven Development by Example by Kent Beck",
            "* Dozens of conference talks on YouTube!",
            "* TALK to your fellow software engineers about decisions and discuss design when writing code. You'll either be surprised by how much they have to say, or what they're willing to learn."
        ])
    )
    slide_7 = Slide(
        heading="Questions? ⁉️",
        text=Text([
            "This presentation was created by me 🤓   and is on github: github.com/tombasche/agile-manifesto-presentation",
            "The framework is something I created because ... why not. It uses 'curses' under the hood, a nearly 30-year old API that ships with UNIX/POSIX systems which efficiently writes text to the terminal."
        ])
    )
    slide_show = SlideShow([slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7],)
    slide_show.present()


if __name__ == "__main__":
    main()
