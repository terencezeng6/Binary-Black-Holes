This project is about tracing the path of two black holes that form and inspiral and eventually merge into a singular black hole, using parameters from LIGO.
LIGO, or the Laser Interferometer Gravitational-Wave Observatory, detects and observes cosmic gravitational waves with laser interferometry. 
Its data is publically available, and was utilized in this project.

LIGO first detected the merger of a binary black hole on September 14, 2015. These black holes had estimated masses of 29 and 36 solar masses, respectively.
The other important parameters obtained from LIGO were their starting velocities. All other parameters, such as the accelerations of the systems, can be
calculated manually.

These calculations involve fairly rudimentary principles such as Kepler's Third Law and the conservation of momentum. For instance, the black holes (treated
as point masses) must move around a common center of mass, with a common angular frequency such that they remain opposite of each other. The path was iterated
using Euler's method, shown below.

<img src="inspiral path.JPG" alt="inspiral path" width="600"/>

We can notice that the two black holes, whose paths depicted by the green and red curves, start at roughly the same distance opposite of their center of mass (depicted by the blue dot). Their paths are also opposing, in vertical directions, resulting in spiraling paths due to their acceleration towards each other.

Besides the path, additional graphs were constructed depicting orbital energy of the system over time, and the system's radius (i.e. half the distance
between the two black holes).

<img src="total energy over time.JPG" alt="total energy" width="600"/>

<img src="radius over time.JPG" alt="radius" width="600"/>

The graph ends when the two black holes have merged into a single one. The radius at which this event occurs is called the Schwarzschild radius, shown by the dotted red line.
