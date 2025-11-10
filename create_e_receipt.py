from PIL import Image, ImageFont, ImageDraw
from config import *
import datetime


def create_receipt(_from: str, _for: str, amount: int, payment_type: str, date: datetime.date, receipt_no):
    template = Image.open(BACKGROUND)
    draw = ImageDraw.Draw(template)

    check_true = 466 * (300/100)
    cash_true = 639 * (300/100)

    font_size = 24 * (300/100)
    font = ImageFont.truetype(font=POPPINS_LIGHT, size=font_size)

    draw.text((455 * (300/100), 313 * (300/100)), str(_from),
              fill="black", font=font)

    draw.text((455 * (300/100), 353 * (300/100)), str(_for),
              fill="black", font=font)

    draw.text((455 * (300/100), 395 * (300/100)), f"Rs. {str(amount)}",
              fill="black", font=font)

    if payment_type.lower() == "check":
        draw.text((check_true, 469 * (300/100)), "X",
                  fill="black", font=font)
    elif payment_type.lower() == "cash":
        draw.text((cash_true, 469 * (300/100)), "X",
                  fill="black", font=font)

    draw.text((1070 * (300/100), 78 * (300/100)), str(receipt_no),
              fill="black", font=font)

    draw.text((70 * (300/100), 78 * (300/100)), str(date),
              fill="black", font=font)

    template.save(SAVE_PATH + receipt_no + ".jpg")