from PIL import Image, ImageDraw, ImageFont
from vkbot import config


def split_lines(text, line_size):
    split_text = text.split(" ")
    lines = []
    line = ""
    word_count = 0

    while True:  # Бесконечный цикл, так как мы не знаем количество строк.
        line += split_text[word_count]+" "

        if len(line) > line_size:
            lines.append(line)
            line = ""

        word_count += 1

        # Останавливаем цикл, когда доходим до последнего слова
        if word_count+1 == len(split_text):
            line += split_text[word_count] + " "
            lines.append(line)
            break

    return lines


def split_text_into_lines(text, width, height, font_size):
    letters_count_in_line = int(width / (font_size/2))
    split_lines_text = \
        "\n".join(split_lines(text, line_size=letters_count_in_line))

    return split_lines_text


def write_in_image(image: Image,
                   text: str,
                   xy: list,
                   width: int,
                   height: int,
                   font_size: int = 50,
                   font: ImageFont or None = None) -> Image:
    if not font:
        font = ImageFont.truetype(
            (config.MEDIA_DIR / "sans-serif.ttf").__str__(),
            size=font_size
        )

    split_text = split_text_into_lines(
        text=text,
        width=width,
        height=height,
        font_size=font_size,
    )

    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        xy=xy,
        text=split_text,
        font=font,
        fill='#1C0606'
    )

    return image