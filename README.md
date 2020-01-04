# simple-link-colorgen
A simple tool to generate WCAG 2-acceptable link colours, given a body and background colour in hex format.
Requires Python3

## Background
This is a simple script. No guarantees included. It will write to a local file called BODY_BACKGROUND.txt

## Usage
1) Make the script executable
```bash
$ chmod +x cr.py
```

2) Execute the script with body and background colour inputs
```bash
$ ./cr.py --body 2B2D32 --background FFFFFF
```

Profit!

## TODO
- Add a UI to preview colours
- Parallelise operations for speed (it's so damn slow!)
- Add more permutations (e.g. derive body colours given background and link, etc)

