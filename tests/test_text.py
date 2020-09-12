from src.text import Text, DotPointText


class TestTextRender:

    def test_text(self):
        t = Text(
            text=["hello", "there"]
        )
        assert '\n' in t.render()

    def test_dotpoint_text(self):
        t = DotPointText(
            text=["hello", "second_point", "third_point"]
        )
        rendered = t.render()
        assert "\t * hello\n" in rendered

    def test_subdotpoint_text(self):
        t = DotPointText(
            text=["hello", "second_point", "* indented_point"]
        )
        rendered = t.render()
        split_up = rendered.split("\n\n")
        assert "\t\t\t * indented_point" in split_up[2]
