import dateutil.parser
from emoji import emojize
import re


def get_indicators():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    letters = ["regional_indicator_" + letter for letter in alphabet]
    return [emojize(":" + emoji_str + ":", use_aliases=True) for emoji_str in letters]


def formatted_dates_to_out(formatted_dates):
    num = len(formatted_dates)
    if 0 == num:
        return "Error: No date entered.", -1
    if num >= 20:
        return "Error: Too many dates entered. Maximum is 19", -1

    lines = []
    indicators = get_indicators()
    for i in range(num):
        lines.append(indicators[i] + " " + formatted_dates[i])
    lines.append(emojize(":no_entry_sign:") + " None of the above")
    return "\n".join(lines), num


def input_to_date_list(input_str):
    dates = []
    command = "/datepoll"
    separators = "\\s|,"

    start_command_pos = input_str.find(command)
    if start_command_pos != -1:
        list_start = start_command_pos + len(command)
        input_str = input_str[list_start:]
        end_command_pos = input_str.find(command)
        if end_command_pos != -1:
            input_str = input_str[:end_command_pos]

        date_str_list = re.split(separators, input_str)
        date_str_list = [s for s in date_str_list if s != ""]

        for date in date_str_list:
            dates.append(dateutil.parser.parse(date))

    return dates
