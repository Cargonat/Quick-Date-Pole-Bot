from babel.dates import format_datetime
from emoji import emojize
import json

# start: /datepoll
# end: /datepoll or end of input_str
# input_str: list of iso 8601 formats separated by whitespace or commas
from qdpb.formatting import input_to_date_list, formatted_dates_to_out, get_indicators


class Processor(object):
    def __init__(self):
        self.formats, self.locales = self.load_config()

    def load_config(self):
        try:
            with open("config.json") as file:
                d = json.load(file)
                formats = d.get("formats")
                locales = d.get("locals")
                if not isinstance(formats, dict):
                    formats = dict()
                if not isinstance(locales, dict):
                    locales = dict()
                return formats, locales
        except OSError:
            return dict(), dict()

    def save_config(self):
        with open("config.json", "w") as file:
            json.dump({"formats": self.formats, "locales": self.locales}, file, indent=4)

    def process(self, message):
        id_str = str(message.guild.id)
        input_str = message.content
        dates = input_to_date_list(input_str)
        formatted_dates = [format_datetime(date, format=message.formats[id_str],
                                           locale=message.locales[id_str])
                           for date in dates]
        return formatted_dates_to_out(formatted_dates)

    def process_message(self, message):
        if message.content == "/datepoll help":
            await message.add_reaction(emojize(":partying_face:"))
            msg = '''You can use me to set up quick date polls.
    
        I listen to messages containing "/datepoll" followed by a list of ISO 8601 dates separated by whitespace or 
        commas. The list must be at least 1 and at most 37 dates long. The ISO 8601 format includes the YYYY-MM-DD 
        format and many simplifications of it like MM-DD. 
    
        You can set the format of the returned dates by using "/datepoll format FORMAT" where FORMAT is a format 
        using the Unicode Date Format Patterns, which can be found here: 
        https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns 
    
            You can set the locale of the returned dates by using "/datepoll locale LOCALE where LOCALE is a locale 
            such as en_US or de_DE using the ISO language and country codes. '''
            await message.channel.send(msg)
            return

        id_str = str(message.guild.id)

        format_command = "/datepoll format"
        if message.content.startswith(format_command):
            format_str = message.content[len(format_command) + 1:]
            self.formats[id_str] = format_str
            self.save_config()
            return

        locale_command = "/datepoll locale"
        if message.content.startswith(locale_command):
            locale_str = message.content[len(locale_command) + 1:]
            self.locales[id_str] = locale_str
            self.save_config()
            return

        if id_str not in self.formats.keys():
            format_str = "cccc, yyyy-MM-dd"
            self.formats[id_str] = format_str

        if id_str not in self.locales.keys():
            locale_str = message.guild.preferred_locale
            self.locales[id_str] = locale_str.replace("-", "_")

        msg, num = self.process(message)
        response = await message.channel.send(msg)

        if num != -1:
            indicators = get_indicators()
            for emoji in indicators[:num]:
                await response.add_reaction(emoji)
            await response.add_reaction(emojize(":no_entry_sign:", use_aliases=True))
