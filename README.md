# phaser

The phaser module provides an implementation of the phase estimation
algorithm of "Estimating the phase of synchronized oscillators";
S. Revzen & J. M. Guckenheimer; Phys. Rev. E; 2008, v. 78, pp. 051907
doi://10.1103/PhysRevE.78.051907

Phaser takes in multidimensional data from multiple experiments and
fits the parameters of the phase estimator, which may then be used on
new data or the training data. The output of Phaser is a phase
estimate for each time sample in the data. This phase estimate has
several desirable properties, such as:

  1. Time derivative of phase is approximately constant.
  1. Phase estimates are robust to measurement errors in any one
     variable.
  1. Phase estimates are robust to systematic changes in the
     measurement error.

This fork is a code cleanup plus translation to modern numpy and
scipy. I'm using Python 3.6, numpy 1.19, and scipy 1.5.
