MinusOne: Use your 3D printer as a 2D plotter or drag knife!
===========================================

Summary
=======

This is an Inkscape extension that allows you to save your Inkscape drawings as
G-Code files suitable for plotting with any 3D printer that has a pen or knife strapped to the hot end.

**Work in progress.  Use at your own risk.**

Original Author: [Marty McGuire](http://github.com/martymcguire)
Website: [http://github.com/martymcguire/inkscape-unicorn](http://github.com/martymcguire/inkscape-unicorn)

Modifications: Greg Zapf

Credits
=======

* Marty McGuire pulled this all together into an Inkscape extension.
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.
* Greg Zapf altered the code to optimize for generic 3D printer use, moving the Z axis to perform cuts instead of servo commands.

Install
=======

Copy the contents of `src/` to your Inkscape `extensions/` folder.

Typical locations include:

* OS X - `/Applications/Inkscape.app/Contents/Resources/extensions`
* Linux - `/usr/share/inkscape/extensions`
* Windows - `C:\Program Files\Inkscape\share\extensions`

Usage
=====

* Size and locate your image appropriately:
	* The CupCake CNC build platform size is 100mm x 100mm.
	* Setting units to **mm** in Inkscape makes it easy to size your drawing.
	* The extension will automatically attempt to center everything.
* Convert all text to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* Save as G-Code:
	* **File | Save a Copy**.
	* Select **MinusOne Plotter or Knife G-Code (\*.gcode)**.
	* Save your file.
* Preview
	* For OS X, [Pleasant3D](http://www.pleasantsoftware.com/developer/pleasant3d/index.shtml) is great for this.
	* [NC Viewer](https://ncviewer.com/) is a web based viewer that previews these non-extrusion g-code files nicely.
* Print!
	* Send your `.gcode` file to your printer (copy to SD Card, upload to Octoprint, etc)
	* Set up your knife or pen, and affix an appropriate medium on the bed.
	* Print!

TODOs
=====

* Provide clean way to update header and footer.
* Provide clean way to enter offset for cutter from printer's usual hot end.
* Tutorials?
