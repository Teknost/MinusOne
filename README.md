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

History and Credits
=======

* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* Marty McGuire pulled this all together into the great [Inkscape-Unicorn](http://github.com/martymcguire/inkscape-unicorn) extension.
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
	* Set your Document Properties to your *available* bed size, in mm, with no multipliers. (subtract from full bed size appropriately to deal with offsets from where you attach the cutter)
	* Setting units to **mm** in Inkscape makes it easy to size your drawing.
	* The extension will automatically zero at the bottom left of your document, so place your objects accordingly.
* Convert all text to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* Save as G-Code:
	* **File | Save a Copy**.
	* Select **MinusOne Plotter or Knife G-Code (\*.gcode)**.
	* Save your file.  The next dialogue will offer options including a homing offset, where you can specify where cutting zero is in relation to your machine's zero.
* Preview
	* For OS X, [Pleasant3D](http://www.pleasantsoftware.com/developer/pleasant3d/index.shtml) is great for this.
	* [NC Viewer](https://ncviewer.com/) is a web-based viewer that previews these non-extruding g-code files nicely.
* Print!
	* Send your `.gcode` file to your printer (copy to SD Card, upload to Octoprint, etc)
	* Set up your knife or pen, and affix an appropriate medium on the bed.
	* Auto-level and save a mesh, if your printer can do that.
	* Print!

TODOs
=====
* All original goals and todos complete!
* Provide clean way to customize header and footer... use however templates are loaded?
* Mimic pen registration option and behavior for a similar pause to attach pen or blade?
* Add back centered zero code as an option for delta printers?
* Math tricks to compensate for knife and finishing cuts?
* Try with Inkscape 1.x and adjust for compatibility if needed?
* Tutorials?

If you want any of these potential features, let me know in the [Discussions](/Teknost/MinusOne/discussions) section!
