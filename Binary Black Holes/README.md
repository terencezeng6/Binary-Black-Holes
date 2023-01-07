This project is tracing the path of two black holes that form and inspiral and eventually merge into a singular black hole, using parameters from LIGO.
LIGO, or the Laser Interferometer Gravitational-Wave Observatory, detects and observes cosmic gravitational waves with laser interferometry. 
Its data is publically available, and was utilized in this project.

LIGO first detected the merger of a binary black hole on September 14, 2015. These black holes had estimated masses of 29 and 36 solar masses, respectively.
The other important parameters obtained from LIGO were their starting velocities. All other parameters, such as the accelerations of the systems, can be
calculated manually.

These calculations involve fairly rudimentary principles such as Kepler's Third Law and the conservation of momentum. For instance, the black holes (treated
as point masses) must move around a common center of mass, with a common angular frequency such that they remain opposite of each other. The path was iterated
using Euler's method, shown below.

![inspiral path](https://github.com/terencezeng6/personal-projects/blob/main/Binary%20Black%20Holes/inspiral%20path.JPG)

Besides the path, additional graphs were constructed depicting orbital energy of the system over time, and the system's radius (i.e. half the distance
between the two black holes).

![total energy](https://github.com/terencezeng6/personal-projects/blob/main/Binary%20Black%20Holes/total%20energy%20over%20time.JPG)

![radius](https://github.com/terencezeng6/personal-projects/blob/main/Binary%20Black%20Holes/radius%20over%20time.JPG)
