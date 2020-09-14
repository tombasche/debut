from src.slide import Slide, TitleSlide
from src.slideshow import SlideShow
from src.text import Text, DotPointText


def main():
    title_slide = TitleSlide(
        title="Agile Principle #9",
        author="Thomas Basche 🤓  "
    )
    slide_1 = Slide(
        heading="Introduction",
        text=Text(["Continuous attention to technical excellence and good design enhances agility."])
    )
    slide_2 = Slide(
        heading="What is technical excellence?",
        text=DotPointText([
            "A level of quality, maintainability and extensibility of software expressed through a lack of defects and an abundance in business value.",
            "This means software which works and software that is valuable.",
            "It means software that's easy to change at the drop of a hat!"
        ])
    )
    slide_3 = Slide(
        heading="What is good design?",
        text=DotPointText([
            "A good design: ",
            "* Satisfies certain goals within a set of constraints, ",
            "* takes into account aesthetic and functional considerations, ",
            "* and interacts efficiently within its environment."
        ])
    )
    slide_4 = Slide(
        heading="How do these things enhance agility?",
        text=DotPointText([
            "Software that's well-designed is software that allows us to maintain a constant pace indefinitely.",
            "Good design reduces the amount of mental overhead spent reasoning about code.",
            "Highly-cohesive and loosely-coupled components mean faster delivery.",
            "... which also means better and more thorough testing.",
            "Less time spent fixing bugs and mistakes.",
            "More time spent adding features and value."
        ])
    )
    slide_5 = Slide(
        heading="How do we maintain 'continuous attention' to these things?",
        text=DotPointText([
            "Pair-programming helps us stay honest. Question the why and the how of an implementation. Play devil's advocate! 😈 ",
            "Let's talk about the code during a desk check!",
            "* What might you have done differently?",
            "* What ideas did you discard along the way and why?",
            "* What were the challenges?",
            "* Can the person reading the code understand what it does without you explaining it?",
            "* Is there something in this solution that might hinder us in future?"
        ])
    )
    slide_6 = Slide(
        heading="How do we maintain 'continuous attention' to these things?",
        text=DotPointText([
            "Put yourself in the shoes of a customer or product owner",
            "* Would they be happy with a 'hacky solution'? ",
            "* They're paying a lot of money for it!"
        ])
    )
    slide_7 = Slide(
        heading="So how do we get there?",
        text=DotPointText([
            "Come to the software engineering chapter!",
            "There's resources left, right and centre about technical excellence and good design: ",
            "* 📖   Clean Code, by Robert C. Martin (Uncle Bob)",
            "* 📖   The Pragmatic Programmer by Andy Hunt and Dave Thomas",
            "* 📖   Test-Driven Development by Example by Kent Beck",
            "* 📺   Dozens of conference talks on YouTube!",
            "* 💬   TALK to your fellow software engineers about your code. You'll either be surprised by how much they have to say, or what they're willing to learn."
        ])
    )
    slide_8 = Slide(
        heading="Questions? ⁉️",
        text=Text([
            "This presentation was created by me and is on github: ",
            "* github.com/tombasche/agile-manifesto-presentation",
            "The framework is something I created because ... why not. It uses 'curses' under the hood, a nearly 30-year old API that ships with UNIX/POSIX systems which efficiently writes text to the terminal.",
            "You could pull the code down and create your own 'slideshow' with it if you were so inclined...\n",
            "slide_show = SlideShow([title_slide, slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8],)",
            "slide_show.present()"
        ])
    )
    slide_show = SlideShow(
        slides=[title_slide, slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8],
        show_page_numbers=True
    )
    slide_show.present()


if __name__ == "__main__":
    main()
