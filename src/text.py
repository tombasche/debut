from typing import List


class Text:

    def __init__(self, text: List[str]):
        self._text = text

    def render(self) -> str:
        return '\n'.join(self._text)


class DotPointText(Text):

    def render(self) -> str:
        final_text = ""
        for dotpoint in self._text:

            if dotpoint.startswith("*"):
                final_text += f"\t\t\t {dotpoint}\n\n"
                continue

            final_text += f"\t * {dotpoint}\n\n"
        return final_text
