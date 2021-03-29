
<!-- ![TRATES logo](https://github.com/Kobie-Kirven/trates/blob/main/docs/_static/trates_logo.png) -->


<img src="https://github.com/Kobie-Kirven/trates/blob/main/docs/_static/trates_logo.png" height="200">
<h1>TRATES</h1>
<h3>TRAnsporter TErmini Simulations</h3>

TRATES is a tool that prepares all of the files that are necessary for 
molecular dynamics simulations and provides analysis of simulation data 
for glucose transporter termini.  


<h3>Installing TRATES</h3>
TRATES can be easily installed with:

```bash
pip3 install git+git://github.com/Kobie-Kirven/trates
```

<h3>Using TRATES</h3>

TRATES is made up of several subpackages including
* trates-prepare
* trates-rmsd
* trates-contacts
* trates-plot 


<h3> TRATES Command Line Options</h3>

Trates Prepare:

```text
usage: trates-prepare [-h] -1 IN1 -s1 S1 -2 IN2 -s2 S2 -o OUT_PATH -nc NC -vmd
                      VMD -n OUT_NAME -a ANCHOR -d DISTANCE [-t TIME]

TRAnsporter TErmani Simulations

optional arguments:
  -h, --help            show this help message and exit
  -1 IN1, --input-1 IN1
                        First FASTA input file
  -s1 S1, --slice-1 S1  The positons of the start and stop residue (inclusive)
                        for the first terminus seperated by a dash (start-
                        stop)
  -2 IN2, --input-2 IN2
                        Second FASTA input file
  -s2 S2, --slice-2 S2  The positons of the start and stop residue (inclusive)
                        for the second terminus seperated by a dash (start-
                        stop)
  -o OUT_PATH, --output-path OUT_PATH
                        Path and name of output folder (Ex. ~/Desktop/output
  -nc NC, --n-and-c NC  Boolean (T/F) if the simulation is for a combination
                        of the N-terminus and C-terminus
  -vmd VMD, --vmd-path VMD
                        Path to VMD
  -n OUT_NAME, --out-name OUT_NAME
                        Name of output files
  -a ANCHOR, --anchoring-residues ANCHOR
                        Anchoring residue for each terminus in comma-seperated
                        format
  -d DISTANCE, --distance-apart DISTANCE
                        Distance between alpha carbons of anchoring residues
                        in angstroms
  -t TIME, --simulation-time TIME
                        How long to run the simulation in nanoseconds

```
```text
usage: trates-rmsd [-h] [-psf PSF] [-dcd DCD] [-o OUT] [-vmd VMD]

RMSD calculations

optional arguments:
  -h, --help            show this help message and exit
  -psf PSF, --psf-file PSF
                        PSF file
  -dcd DCD, --dcd-file DCD
                        DCD file
  -o OUT, --out-file OUT
                        Output Data File
  -vmd VMD, --vmd-path VMD
                        Path to vmd
```
```text
usage: trates-native-contacts [-h] [-psf PSF] [-dcd DCD] [-vmd VMD] [-o OUT]
                              [-f FRAME] [-d DISTANCE] [-t TYPE] [-r CUTOFF]
                              [-c CHAIN]

Calculate native contacts

optional arguments:
  -h, --help            show this help message and exit
  -psf PSF, --psf-file PSF
                        Protein structure (PSF) file
  -dcd DCD, --dcd-file DCD
                        Trajectory (DCD) file
  -vmd VMD, --vmd-path VMD
                        Path to vmd
  -o OUT, --out-file OUT
                        Name of output file (.txt)
  -f FRAME, --frame-span FRAME
                        Begining and ending frame of simulation
  -d DISTANCE, --contact-distance DISTANCE
                        Cutoff distance in angstroms for native contacts
  -t TYPE, --contact-type TYPE
                        Type of native coontact (options: inter, intra, all)
  -r CUTOFF, --residue-cut-off CUTOFF
                        Intramolecular: Cutoff for native contacts (only
                        interactions more than a specified distance apart
  -c CHAIN, --chain-number CHAIN
                        Intramolecular: Chain number (1 or 2)
```
```text
usage: trates-plot [-h] [-i INPUT] [-o IMAGE] [-s SMOOTH] [-d TYPE]

Plot the output data

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input-file INPUT
                        Input data file
  -o IMAGE, --image-file IMAGE
                        Output image
  -s SMOOTH, --sliding-widow SMOOTH
                        Sliding window length for smoothing
  -d TYPE, --data-type TYPE
                        Data type (rmsd, conacts)
```