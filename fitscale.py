import math
import inkex


class Scalefit(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option(
            "-x", "--width", type=float, default=32,
            help="The canvas width")
        self.OptionParser.add_option(
            "-y", "--height", type=float, default=32,
            help="The canvas height")
        self.OptionParser.add_option(
            "-u", "--units", type=str, default="px",
            help="The unit of the canvas dimensions")
        self.OptionParser.add_option(
            "-m", "--margin_width", type=float, default=0,
            help="The margin width")
        self.OptionParser.add_option(
            "-n", "--margin_height", type=float, default=0,
            help="The margin height")

    def effect(self):
        # Get the documents dimensions
        docW = self.svg.unittouu(self.document.getroot().get('width'))
        docH = self.svg.unittouu(self.document.getroot().get('height'))

        # Extract fields from UI
        self.width = self.svg.unittouu(
            str(self.options.width + self.options.units))
        self.height = self.svg.unittouu(
            str(self.options.height + self.options.units))
        self.margin = self.svg.unittouu(
            str(self.options.margin + self.options.margin_units))
        CloseDebugFile()

if __name__ == '__main__':
    e = Scalefit()
    e.affect()
