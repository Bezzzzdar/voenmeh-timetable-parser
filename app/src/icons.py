# icons.py - icons in base64 for app
# Copyright (C) 2024 Ivan Rastegaev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import base64
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage

base64_update_button_icon_black = """
    iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAC3ElEQVR4nO2ayW
    tUQRCHv0SDcUNNRAVxxaOCXhVR8CgiKJi4BsE9wYOXBBVEDKIGFf8NRfAiQfCiBCWKxqteAgpBEuNCosSMsaWhRoZH
    90wcp/vNUh/UYQbe1Hs11V31un6gKIqiKIoSliZgF3AdeAQMAO+B78BP4BPwDugFeoBWoJkKZy5wDOgHfgPmH20KeA
    6cAuZTQSwG7gDfinhon41JZuTLiuQ10ZkBnAE+l/DBk/YVOAfUl1sAVgEv89z4L+AFcBvYA2wEVgCzgVnAEmA90CL7
    xECBQPQB68olANuAYc+NfgAuAcuL+N3VQDcw4vltm2k70g5AGzDpSdWzwMwS+JgDnAfGHX4ywJG0ArBbUjvp+C6wNI
    A/u2Qee5ZXa+wAbAV+OMpWJ1AXeKO97CirmZgBWOZYl5OSEbE4IQHPt1EG40HCkf03DhGf42kE4LDDURfp0RMzAI3A
    kKMeu5qSUlJs01Ry2hMOxh3NSNUGoAEYTDiwuzG1EoAFwC1gNOflpLmWApC7D9jOq+PvN4qiKIqiKIqiKIqipEiHvK
    rbV/bqP5hwTKSzk6NRObyxhzg1E4DuhM9BOcariQCskSO6XJ+nQzgyZRgAeyT/NOFvKNQ+YDx2kfS44Lif/aGcGY/Z
    0dgB4tPmGJLeD+nQ5LGMjM1isdcxER4WpUkwjOOhcz9PSUqGHJXViVgiORm2crvNBMYkrMUjkOgtUhIznbH8PYc/O5
    rfSQSMY3c/6JHIjIlYwoqg/pcGUYa5ZHcTog6JgvGUt+2i9HTtDSPSpKwtwt9K4IpjIp21j8AWImLy1HfbjDwpsFG+
    AW5ImdogKd0oIiir/9kE7BOR5SvP8spav1wTFVOgwakXZVhIoaTNtJMRNAlOptvhLQKulVgq+wW4KaLrimGe6Hj6Cq
    Szz2ypewYclWVS0TTJ+rYy2IfAW2lcJqSGW+n8aymhV6WsLUz7phVFURRFoar5AxszMxxqWUcYAAAAAElFTkSuQmCC
"""
base64_update_button_icon_white = """
    iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAADAElEQVR4nO3a3Y
    tVVRjH8e2UNJphOqGBaBleGtitEgVdiggJY/kWQeYrc+FNkYIMSVSS0b+hCN2IBN0UYpik3tZNoCDRNFr4gq99Yo1r
    4rjP3jPTaa8zb+t7uTnn/J79nGetZ+39/Ioik8lkMplMJiFYjA34DN/gIi7jFu7iD/yC0ziKt9BXTGfwNN7DOfztv/
    MQP2A3nimmC3gOX+EvzXEjVkZtVZS/0N27LkYCeAJ7cU06/sQB9EypBOAFnB8j8Af4EV/iTazBcszDU1iC1dgc94mw
    R4zFGayaEgnAa/i9JtArOIxlHfzuiziCoZrfDpX2xqQmAO/gXk2pDuDJBjTm4yPcrNC5jx2TkgBsjKVd5jiWJtALS+
    bbCr0HsW12LwF4Fbcr2tYHmJN4ox2saKv3u5YAPF+xLsMy2JhMtD2G92PCa0kp/nVJK/wb25IJ1sexs+sJwPYKrQ+T
    iE0snqNdSwB6cbWiH7cdShrW7YgUgewradwsH0ZmbAIwF7+WNAYbFZniCViIYxhueTjpmzUJKO0DO7D/34uZTCaTyW
    QymUwmk8lkJovwiB4f1Xtn/ouJ6on06ORoOL68WVjMogQcKcmG13dzZ0UCsDK+omtlTwqhjmg8kMdj6sH3JcmrSfYB
    9RxqXGziMR2siOftVGJ1hNHYliSi44/my0PSkykFxyJMZ7cnE2+PZVPFRDiYNJakFC1TDuBhLMlko7Iweo9mifJkON
    jt1qbSHaHt9h/5eaoMEqc7scRMcCx/okIvjObXN63XRlk1XttaY5G5Ec0S84pmxnIHamx3d4I75P9qdJyAeP316PSs
    YigeUl7qQG8FPq6YSI/yG9YV3UJNAloOI98Zm0v4PLQpvBxLujeaoIL/5xX0R5PlTzXLa5TgPl3etZsfLwEth5KBxE
    bJUGm7UnsSOkpAy+cW4dOGrbLX8UUwXRfTBSyIPp4z45RzHaHVncW7YZkUM8Au3x9tsKfwczy43Ik9PFjnL8QW+klo
    a3h2suPOZDKZTCZTzGj+AQZFI5wzXlijAAAAAElFTkSuQmCC
"""

base64_edit_button_icon_black = """
    iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA6UlEQVR4nO3bwQ
    2DMAAEQfff9KaEPFAE5GYkFwDr48c5AAAAz9eXgwD/LQsQYFoWIMC0LECAaVmAANOyAAGmZQECTMsCBJiWBQgwLQsQ
    YFoWIMC0LECAaVmAANOyAAGmZQECTMsCBJiWBQgwLQsQ4FE3zjm//WfNCz6X3oEA595LJMARYPozdtndD9DLjwBHgN
    tvYW9ewNO09sBPkwACTMsCBJiWBQgwLQsQYFoWIMC0LECAaVmAANOyAAGmZQECTMsCBJiWBQgwLQsQYFoWIMC0LECA
    aVmAANOyAAGmZQECTMsCAACA82Ifl4a7fTTQpbcAAAAASUVORK5CYII=
"""
base64_edit_button_icon_white = """
    iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA2UlEQVR4nO3TwR
    ECQQwEsc0/6SYD7rlwI0VgV9ecAwAA8ON6cPu+10sAAaZlAQJMywIEmJYFCDAtCxBgWhYgwLQsQIBpWYAA07IAAaZl
    AQJMywIEmJYFCDAtCxBgWhYgwLQsQIBpWYAA07IAAaa1toCnh/lOgMsEuEyAywS4TIDLBLhMgMvO27T28K9JAAGmZQ
    ECTMsCBJiWBQgwLQsQYFoWIMC0LECAaVmAANOyAAGmZQECTMsCBJiWBQgwLQsQYFoWIMC0LECAaVmAANOyAAGmZQEA
    AMD5bx8SK+4PlrKiPQAAAABJRU5ErkJggg==
"""

base64_app_icon = """
    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
"""

def _get_icon_from_base64(base64_icon: str, width: int, height: int):
    """Function for decode image from base64 code"""
    image_data = base64.b64decode(base64_icon)
    image = QImage()
    image.loadFromData(image_data)
    pixmap = QPixmap.fromImage(image)
    icon_size = QSize(width, height)
    scaled_pixmap = pixmap.scaled(icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    icon = QIcon(scaled_pixmap)

    return icon, icon_size