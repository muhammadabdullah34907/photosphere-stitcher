# photosphere-stitcher
photosphere stitcher

Code organization
-----------------

The application entry point is `stitcher.py`, which implements the projection
and blending stages of panorama generation.

`features.py` contains the SIFT feature extraction, FLANN matching and
homography computation with RANSAC. We also include an implementation of
*[Multi-Scale Oriented Patches (MSOP)](http://matthewalunbrown.com/mops/mops.html#)*
that we didn't use because of the superior performance of SIFT.

`bundle_adj.py` includes the panorama discovery, focal and rotation estimation,
and the bundle adjustment stages of panorama generation.

The remaining modules are experiments or accessory functions.
`pano_tests.py` are the unit tests for different critical functions; run them
to ensure that the functionality is correct if you plan to modify the code.
`profiler.py` is a small self-contained Python profiler to guide the
optimization of the slow sections of the code.
`blend.py` is a set of experiments on Laplacian blending, Poisson blending and
and seam detection with graph cuts; the blending code actually used in panorama
generation has been moved to `stitcher`.

Usage
-----

Run the application by passing the image path and options, e.g.:

```bash
    python stitcher.py data/CMU2 -s 2
```

The path is the only mandatory argument. The following optional arguments are
available:

*  `-s`, `--shrink SHRINK`: downsample the images by a factor of *SHRINK* to
   speed up generation; stitching may fail for large factors because there
   aren't enough features to match.
*  `--ba {none,incr,last}`: how to apply bundle adjustment; skip it (*none*),
   apply it incrementally after adding an image (*incr*, default) or only after
   adding all the images (*last*)
*  `--equalize`, `-e`: compensate the exposure differences between images;
   disabled by default because it may lead to chromatic aberration.
*  `--crop`, `-c`: crops the largest rectangle from the panorama; disabled by
   default
*  `-b`, `--blend {none,linear,multiband}`: how to blend the images, either by
   simply pasting them on the mosaic (*none*), using linear blending (*linear*)
   or multi-band blending (*multiband*, default)
*  `-o OUT`, `--out OUT`: saves the mosaic to the *OUT* file, with the format
   determined by the extension (JPG, PNG supported).

The application stores the features and matches in a Numpy NPZ file and the
result of bundle adjustment (intrinsic and extrinsic camera parameters) in a
PKL file, tagged by the dataset name and shrink factor; the application checks
if the files exist and loads them instead of re-running the pipeline.
Delete the files if you want to re-generate the panorama for scratch.
