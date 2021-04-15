import math
import inkex.extensions


class Scalefit(EffectExtension):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "-x", "--width", type=float, default=32,
            help="The canvas width")
#        self.arg_parser.add_argument(
#            "-y", "--height", type=float, default=32,
#            help="The canvas height")
#        self.arg_parser.add_argument(
#            "-u", "--units", type=str, default="px",
#            help="The unit of the canvas dimensions")
#        self.arg_parser.add_argument(
#            "-m", "--margin_width", type=float, default=0,
#            help="The margin width")
#        self.arg_parser.add_argument(
#            "-m", "--margin_height", type=float, default=0,
#            help="The margin height")

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
    e.run()
