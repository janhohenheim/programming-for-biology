import os
from ij import IJ
import ij.measure.ResultsTable as ResTable
from ij.io import DirectoryChooser


def run_analysis(srcDir, outputDir, number):
    # Obtain image with viral signal
    virfile = "061102_MHV_{}vir.png".format(number)
    fullvirfile = os.path.join(srcDir, virfile)
    IJ.open(fullvirfile)

    # Assign a variable to the current image (the one that was opened last,
    # or that was brought to focus by mouse click).
    imp_vir = IJ.getImage()

    # Obtain image with nuclear signal
    nucfile = "061102_MHV_{}nuc.png".format(number)
    fullnucfile = os.path.join(srcDir, nucfile)
    IJ.open(fullnucfile)

    # Smooth image
    IJ.run("Smooth")

    # Assign a variable to the current image (with the nuclear signal in this case)
    imp_nuc = IJ.getImage()

    # Set a threshold for the image
    imp_nuc.getProcessor().threshold(33)

    # Make a binary mask based on the threshold
    IJ.run(imp_nuc, "Convert to Mask", "")

    # Run watershed: maxima are automatically extracted to use as seeds,
    # the mask that was obtained before, is distance-transformed and the
    # watershed algorithm then runs
    IJ.run(imp_nuc, "Watershed", "")

    # Show the watershed image:
    imp_nuc.show()

    # Define which measurements should be performed
    # (here measure the area, the x- and y- coordinates of the nucleus' centroids,
    # and the mean intensity)
    IJ.run(
        imp_nuc,
        "Set Measurements...",
        "area mean centroid redirect=" + imp_vir.getTitle() + " decimal=1",
    )

    # Perform the measurements on the objects that have been identified by the watershed algorithm
    IJ.run("Analyze Particles...", "display exclude clear add")

    # Save the measurements in a csv-file
    results = ResTable.getResultsTable()
    csvfilename = os.path.join(outputDir, "MHV_measurements_{}.csv".format(number))
    results.saveAs(csvfilename)


if __name__ == "__main__":
    # Select the source and output directories:
    # by not hardcoding the whole path, the code is more flexible
    srcDir = DirectoryChooser("Choose directory with Input stack").getDirectory()
    outputDir = DirectoryChooser("Choose directory for Output images").getDirectory()
    for i in range(6):
        run_analysis(srcDir, outputDir, i)
