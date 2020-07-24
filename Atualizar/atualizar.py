import os
import subprocess
import pathlib

from errbot import BotPlugin, botcmd

class Atualizar(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def atualizar(self, msg, args):
        """Say hello to the world"""
        cmd = "cd " + str(pathlib.Path(__file__).parent.absolute().parent) + " && git pull"
        proc = subprocess.run(cmd, shell=True, text=True)
        return proc.stdout