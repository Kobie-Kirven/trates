
<!-- ![TRATES logo](https://github.com/Kobie-Kirven/trates/blob/main/docs/_static/trates_logo.png) -->


<img src="https://github.com/Kobie-Kirven/trates/blob/main/docs/_static/trates_logo.png" height="200">
<h1>TRATES</h1>
<h3>TRAnsporter TErmini Simulations</h3>

TRATES is a tool that prepares all of the files that are necessary for 
molecular dynamics simulations of glucose transporter termani. 


<h3>Installing TRATES</h3>
TRATES can be easily installed with:

```bash
pip3 install git+git://github.com/Kobie-Kirven/trates
```

<h3>Using TRATES</h3>

TRATES takes as input 2 fasta files, each containing only one sequence. 


<h3> TRATES Command Line Options</h3>

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
usage: trates-rmsd [-h] [-psf PSF] [-dcd DCD] [-o OUT] [-p IMAGE] [-vmd VMD]
                   [-s SMOOTH]

RMSD calculations

optional arguments:
  -h, --help            show this help message and exit
  -psf PSF, --psf-file PSF
                        PSF file
  -dcd DCD, --dcd-file DCD
                        DCD file
  -o OUT, --out-file OUT
                        Output Data File
  -p IMAGE, --image-file IMAGE
                        Output image
  -vmd VMD, --vmd-path VMD
                        Path to vmd
  -s SMOOTH, --s SMOOTH
                        s
```
```text
usage: trates-native-contacts [-h] [-psf PSF] [-dcd DCD] [-vmd VMD] [-o OUT]
                              [-f FRAME] [-d DISTANCE] [-inter INTER]

Calculate native contacts

optional arguments:
  -h, --help            show this help message and exit
  -psf PSF, --psf-file PSF
                        PSF file
  -dcd DCD, --dcd-file DCD
                        DCD file
  -vmd VMD, --vmd-path VMD
                        Path to vmd
  -o OUT, --out-file OUT
                        Output Data File
  -f FRAME, --frame-span FRAME
                        Start and stop frame
  -d DISTANCE, --contact-distance DISTANCE
                        Cutoff distance for native contacts
  -inter INTER, --intermolecular INTER
                        Intramoleular native contacts
```