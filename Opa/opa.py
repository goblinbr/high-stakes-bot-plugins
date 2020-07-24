import re

from errbot import BotPlugin, re_botcmd

class Opa(BotPlugin):
    """'Opa' plugin for Errbot"""

    @re_botcmd(pattern=r"^opa$", flags=re.IGNORECASE)
    def opa(self, msg, match):
        """Say Opa"""
        return "Opa <@{}>".format(msg.frm.id)