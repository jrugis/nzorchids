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
    f.write('<style> body {background-color: black; color: white;} </style>\n')
    f.write('<style> a {text-decoration: none; color: gray;} </style>\n')
    f.write('</head>\n')

################################################################################
# FUNCTION: 
def write_foot(f):
    f.write('<p>  </p><br>\n')
    f.write('<font face="helvetica"> <small>\n')
    f.write('(c)2022 J.Rugis<br>\n')
    f.write('jrugis@gmail.com<br>\n')
    f.write('</small></font>\n')

################################################################################
# FUNCTION: 
def make_contents_page(species):
    with open('../' + IFNAME, 'w') as ofile:
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body>\n')
        ofile.write('<font face="helvetica">\n')
        ofile.write('The Developmental Morphology of<br>\n')
        ofile.write('New Zealand Native Orchids<br>\n')
        ofile.write('<small>by John Rugis</small><br>\n')
        ofile.write('<p>  </p> <img src="cover.jpg" width="70%"><br>\n')
        ofile.write('<small>Coastal Orchid Habitat: Muriwai, New Zealand</small><br>\n')
        ofile.write('</font> <p>  </p>\n')
        ofile.write('<font face="helvetica"> Species:<br>\n')
        ofile.write('<small><i>\n')
        for s in species:
            gs = (s.split('_')) # genus / species
            ofile.write('&nbsp;&nbsp;&nbsp;<a href="./x' + s + '/species.html">' + gs[0] + ' ' + gs[1] + '</a></br>\n')
        ofile.write('</i></small> </font>\n')
        write_foot(ofile)
        ofile.write('<p>  </p> <img src="by-sa.svg" width="100">\n')
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
        ofile.write('The Developmental Morphology of<br>\n')
        ofile.write('New Zealand Native Orchids<br>\n')
        ofile.write('<small>by John Rugis &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="../index.html">Contents</a></small><br>\n')
        ofile.write('<p>  </p> </font>\n')
        ofile.write('<font face="helvetica">\n')
        ofile.write('Species: <i>' + gs[0] + ' ' + gs[1] + '</i><br>\n')
        ofile.write('<small>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<a href="../x' + prev + '/species.html">prev</a>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<a href="../x' + next + '/species.html">next</a>\n')
        ofile.write('</small><br> </font> <p>  </p>\n')
        ofile.write('<img src="' + info[0] + '.jpg" width="50%"><br>\n')
        ofile.write('<font face="helvetica"><small>\n')
        ofile.write(info[1:])
        ofile.write('</small> </font>\n')
        write_foot(ofile)
        ofile.write('<p>  </p> <img src="../by-sa.svg" width="100">\n')
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
