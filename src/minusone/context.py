from math import *
import sys

class GCodeContext:
    def __init__(self, xy_feedrate, z_feedrate, start_delay, stop_delay, pen_up_angle, pen_down_angle, z_height, z_active, z_safe, finished_height, x_home, y_home, register_pen, num_pages, continuous, file):
      self.xy_feedrate = xy_feedrate
      self.z_feedrate = z_feedrate
      self.start_delay = start_delay
      self.stop_delay = stop_delay
      self.pen_up_angle = pen_up_angle
      self.pen_down_angle = pen_down_angle
      self.z_height = z_height
      self.z_safe = z_safe
      self.z_active = z_active
      self.finished_height = finished_height
      self.x_home = x_home
      self.y_home = y_home
      self.register_pen = register_pen
      self.num_pages = num_pages
      self.continuous = continuous
      self.file = file

      self.drawing = False
      self.last = None

      self.preamble = [
        "(Scribbled version of %s @ %.2f)" % (self.file, self.xy_feedrate),
        "( %s )" % " ".join(sys.argv),
		"M73 P0 R22",
		"M73 Q0 S23",
		"M201 X9000 Y9000 Z500 E10000 ; sets maximum accelerations, mm/sec^2",
		"M203 X500 Y500 Z12 E120 ; sets maximum feedrates, mm/sec",
		"M204 P1500 R1500 T1500 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2",
		"M205 X10.00 Y10.00 Z0.20 E2.50 ; sets the jerk limits, mm/sec",
		"M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec",
		"",
		";TYPE:Custom",
		"G91; relative movements",
		"G1 Z5 F9000; Z up 5mm",
		"G90; back to absolute",
		"",
		"G28; home all axes",
		"M420 S1; load leveling mesh",
		"G0 Z5 F9000; lift nozzle",
		"",
		"G21 ; set units to millimeters",
		"G90 ; use absolute coordinates",

        "G0 X0 Y0 Z0",
        "G92 X%.2f Y%.2f Z%.2f (you are here)" % (self.x_home, self.y_home, self.z_height),
        ""
      ]

      self.postscript = [
        "",
		"(end of print job)",
		"G91; relative movements",
		"G1 Z15 F9000; Z up 15mm",
		"G90; back to absolute",
        "G92.1; back to real coordinates",
		"G0 X200 Y220 F9000; hot end toward park;",
		"G0 Y230; Park nozzle",
		"M84; disable motors",
		"",
		"",
		";Pacman",
		"M300 S987 P100",
		"M300 S1975 P100",
		"M300 S2959 P100",
		"M300 S2489 P100",
		"M300 S1975 P100",
		"M300 S2959 P100",
		"M300 S0 P133",
		"M300 S2489 P133",
		"M300 S2093 P100",
		"M300 S4186 P100",
		"M300 S3135 P100",
		"M300 S2637 P100",
		"M300 S4186 P100",
		"M300 S3135 P100",
		"M300 S0 P133",
		"M300 S2637 P133",
		"M300 S987 P100",
		"M300 S1975 P100",
		"M300 S2959 P100",
		"M300 S2489 P100",
		"M300 S1975 P100",
		"M300 S2959 P100",
		"M300 S0 P133",
		"",
		"",
		"M73 P100 R0",
		"M73 Q100 S0",
        ""

#				"M300 S%0.2F (pen up)" % self.pen_up_angle,
#				"G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay),
#				"M300 S255 (turn off servo)",
#				"G1 X0 Y0 F%0.2F" % self.xy_feedrate,
#				"G1 Z%0.2F F%0.2F (go up to finished level)" % (self.finished_height, self.z_feedrate),
#				"G1 X%0.2F Y%0.2F F%0.2F (go home)" % (self.x_home, self.y_home, self.xy_feedrate),
#				"M18 (drives off)",
      ]

      self.registration = [
        "M300 S%d (pen down)" % (self.pen_down_angle),
        "G4 P%d (wait %dms)" % (self.start_delay, self.start_delay),
        "M300 S%d (pen up)" % (self.pen_up_angle),
        "G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay),
        "M18 (disengage drives)",
        "M01 (Was registration test successful?)",
        "M17 (engage drives if YES, and continue)",
        ""
      ]

      self.sheet_header = [
        "(start of sheet header)",
        "G92 X%.2f Y%.2f Z%.2f (you are here)" % (self.x_home, self.y_home, self.z_height),
      ]
      if self.register_pen == 'true':
        self.sheet_header.extend(self.registration)
      self.sheet_header.append("(end of sheet header)")

      self.sheet_footer = [
        "(Start of sheet footer.)",
        "M300 S%d (pen up)" % (self.pen_up_angle),
        "G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay),
        "G91 (relative mode)",
        "G0 Z15 F%0.2f" % (self.z_feedrate),
        "G90 (absolute mode)",
        "G0 X%0.2f Y%0.2f F%0.2f" % (self.x_home, self.y_home, self.xy_feedrate),
        "M01 (Have you retrieved the print?)",
        "(machine halts until 'okay')",
        "G4 P%d (wait %dms)" % (self.start_delay, self.start_delay),
        "G91 (relative mode)",
        "G0 Z-15 F%0.2f (return to start position of current sheet)" % (self.z_feedrate),
        "G0 Z-0.01 F%0.2f (move down one sheet)" % (self.z_feedrate),
        "G90 (absolute mode)",
        "M18 (disengage drives)",
        "(End of sheet footer)",
      ]

      self.loop_forever = [ "M30 (Plot again?)" ]

      self.codes = []

    def generate(self):
      if self.continuous == 'true':
        self.num_pages = 1

      codesets = [self.preamble]
      if (self.continuous == 'true' or self.num_pages > 1):
        codesets.append(self.sheet_header)
      elif self.register_pen == 'true':
        codesets.append(self.registration)
      codesets.append(self.codes)
      if (self.continuous == 'true' or self.num_pages > 1):
        codesets.append(self.sheet_footer)

      if self.continuous == 'true':
        codesets.append(self.loop_forever)
        for codeset in codesets:
          for line in codeset:
            print line
      else:
        for p in range(0,self.num_pages):
          for codeset in codesets:
            for line in codeset:
              print line
          for line in self.postscript:
            print line

    def start(self):
      self.codes.append("G1 Z%.2f F%.2f (pen down)" % (self.z_active, self.z_feedrate))
      # self.codes.append("G4 P%d (wait %dms)" % (self.start_delay, self.start_delay))
      self.drawing = True

    def stop(self):
      self.codes.append("G1 Z%.2f F%.2f (pen up)" % (self.z_safe, self.z_feedrate))
      # self.codes.append("G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay))
      self.drawing = False

    def go_to_point(self, x, y, stop=False):
      if self.last == (x,y):
        return
      if stop:
        return
      else:
        if self.drawing:
            self.codes.append("G1 Z%.2f F%.2f (pen up)" % (self.z_safe, self.z_feedrate))
            # self.codes.append("G4 P%d (wait %dms)" % (self.stop_delay, self.stop_delay))
            self.drawing = False
        self.codes.append("G1 X%.2f Y%.2f F%.2f" % (x,y, self.xy_feedrate))
      self.last = (x,y)

    def draw_to_point(self, x, y, stop=False):
      if self.last == (x,y):
          return
      if stop:
        return
      else:
        if self.drawing == False:
            self.codes.append("G1 Z%.2f F%.2f (pen down)" % (self.z_active, self.z_feedrate))
            # self.codes.append("G4 P%d (wait %dms)" % (self.start_delay, self.start_delay))
            self.drawing = True
        self.codes.append("G1 X%0.2f Y%0.2f F%0.2f" % (x,y, self.xy_feedrate))
      self.last = (x,y)
