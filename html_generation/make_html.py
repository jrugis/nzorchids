################################################################################
# Create html files for web site:
# The Developmental Morphology of New Zealand Native Ferns 
# 18.11.22 J. Rugis
#
################################################################################

# user settings
CFNAME = 'contents.txt'
IFNAME = 'index.html'
SFNAME = 'species.html'

# global variables

################################################################################
# FUNCTION: 
def get_species_list():
    slist = []
    with open(CFNAME) as ifile:
        for line in ifile:
            slist.append(line.strip())
            next(ifile) # skip a line
    return(slist)

################################################################################
# FUNCTION: 
def write_head(f):
    f.write('<head>\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<style> body {background-color: rgb(50,50,50); color: white;} </style>\n')
    f.write('<style> a {text-decoration: none; color: rgb(150,150,150);} </style>\n')
    f.write('<style> img {border: 1px solid black; border-radius: 8px;} </style>\n')
    f.write('</head>\n')

################################################################################
# FUNCTION: 
def write_foot(f):
    f.write('<p>  </p><br>\n')
    f.write('<font face="helvetica"> <small><small>\n')
    f.write('(c)2022 J.Rugis<br>\n')
    f.write('jrugis@gmail.com<br>\n')
    f.write('</small></small></font>\n')

################################################################################
# FUNCTION: 
def make_contents_page(species):
    with open('../' + IFNAME, 'w') as ofile:
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body>\n')
        ofile.write('<font face="helvetica">\n')
        ofile.write('<big>The Developmental Morphology of \n')
        ofile.write('New Zealand Native Orchids</big><br>\n')
        ofile.write('<small>by John Rugis</small><br>\n')
        ofile.write('<p>  </p><figure><img src="cover.jpg" width="100%"><figcaption><small><small>Coastal cliff habitat: Muriwai, New Zealand</small></small></figcaption></figure><br>\n')
        ofile.write('</font>\n')
        ofile.write('<font face="helvetica"> Introduction<br>\n')
        ofile.write('<small>&nbsp;&nbsp;&nbsp;An introduction goes here.</small><br>\n')
        ofile.write('<p>  </p><small>species list:<br>\n')
        ofile.write('<i>\n')
        for s in species:
            gs = (s.split('_')) # genus / species
            ofile.write('&nbsp;&nbsp;&nbsp;<a href="./x' + s + '/species.html">' + gs[0] + ' ' + gs[1] + '</a></br>\n')
        ofile.write('</i></small> </font>\n')
        write_foot(ofile)
        ofile.write('<p>  </p> <img src="by-nc-sa.svg" width="100">\n')
        ofile.write('</body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def write_species_page(species, prev, next, info):
    gs = species.split('_')               # genus / species
    with open('../x' + species + '/' + SFNAME, 'w') as ofile:
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body>\n')
        ofile.write('<font face="helvetica">\n')
        ofile.write('<big>The Developmental Morphology of \n')
        ofile.write('New Zealand Native Orchids</big><br>\n')
        ofile.write('<small>by John Rugis &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="../index.html">Contents</a></small><br>\n')
        ofile.write('<p>  </p> </font>\n')
        ofile.write('<font face="helvetica">\n')
        ofile.write('species: <big><i>' + gs[0] + ' ' + gs[1] + '</i></big><br>\n')
        ofile.write('<small>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<a href="../x' + prev + '/species.html">prev</a>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<a href="../x' + next + '/species.html">next</a>\n')
        ofile.write('</small><br> <p>  </p>\n')
        txt = info[1:].split('#')
        ofile.write('<figure><img src="' + info[0] + '.jpg" width="75%"><figcaption><small><small>' + txt[0] + '</small></small></figcaption></figure></font> \n')
        ofile.write('<font face="helvetica"><small>\n')
        ofile.write(txt[1])
        ofile.write('</small> </font>\n')
        write_foot(ofile)
        ofile.write('<p>  </p> <img src="../by-nc-sa.svg" width="100">\n')
        ofile.write('</body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def make_species_pages(species):
    with open(CFNAME) as ifile:
        i = 0
        for line in ifile:
            iprev = 0 if (i == 0) else i-1                # previous species index
            inext = i if (i >= len(species )-1) else i+1  # next species index
            info = next(ifile).strip()
            write_species_page(species[i], species[iprev], species[inext], info)
            i += 1

################################################################################
#
# MAIN PROGRAM: Create html files
#
################################################################################

species = get_species_list()
make_contents_page(species)
make_species_pages(species)

################################################################################
################################################################################
