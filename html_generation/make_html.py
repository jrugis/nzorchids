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
def write_head(f):
    f.write('<head>\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<style> body {background-color: rgb(50,50,50); color: white;} </style>\n')
    f.write('<style> a {text-decoration: none; color: rgb(150,150,150);} </style>\n')
    f.write('<style> object.title {border: 1px solid black; border-radius: 8px; max-width: 80vw;} </style>\n')
    f.write('<style> object.photo {border: 1px solid black; border-radius: 8px; max-width: 60vw;} </style>\n')
    f.write('<style> p.desc {margin-left: 20px; margin-right: 20px;} </style>\n')
    f.write('</head>\n')

################################################################################
# FUNCTION: 
def write_title(f):
    f.write('<p>  </p><br>\n')
    f.write('<big>The Developmental Morphology of \n')
    f.write('New Zealand Native Orchids</big><br>\n')
    f.write('&nbsp;&nbsp;&nbsp;<small>by John Rugis</small>\n')

################################################################################
# FUNCTION: 
def write_foot(f, dir):
    f.write('<p>  </p><br>\n')
    f.write('<small><small>\n')
    f.write('(c)2022 J.Rugis<br>\n')
    f.write('jrugis@gmail.com<br>\n')
    f.write('</small></small>\n')
    f.write('<p>  </p> <img src="' + dir + '/by-sa.svg">\n')

################################################################################
# FUNCTION: 
def write_photos(f, info, css):
    photos = info.split('$')
    for p in photos:
         details= p.split('%')
         f.write('<br><figure><object class="' + css + '" data="' + details[0][0:5] + '"></object><figcaption><small><small>' + details[0][5:] + '</small></figcaption></figure>\n')
         f.write('<p class="desc">' + details[1] + '</p></small><br>\n')
    

################################################################################
# FUNCTION: 
def write_species_page(species, prev, next, info):
    gs = species.split('_')               # genus / species
    with open('../x' + species + '/' + SFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: helvetica">\n')
        write_title(ofile)
        ofile.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="../index.html"><small>Contents</a></small><br>\n')
        #
        ofile.write('<p>  </p>\n')
        ofile.write('species: <big><i>' + gs[0] + ' ' + gs[1] + '</i></big><br>\n')
        ofile.write('<small>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<a href="../x' + prev + '/species.html">prev /</a>\n')
        ofile.write('<a href="../x' + next + '/species.html">next species</a>\n')
        ofile.write('</small><br>\n')
        #
        write_photos(ofile, info, 'photo')
        #
        write_foot(ofile, '..')
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def make_species_pages(species, ifile):
    i = 0
    for line in ifile:
        iprev = len(species )-1 if (i == 0) else i-1                # previous species index
        inext = 0 if (i >= len(species )-1) else i+1  # next species index
        info = next(ifile).strip()
        write_species_page(species[i], species[iprev], species[inext], info)
        i += 1

################################################################################
# FUNCTION: 
def make_contents_page(species, intro):
    with open('../' + IFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: helvetica">\n')
        write_title(ofile)
        ofile.write('<br>\n')
        #
        write_photos(ofile, intro, 'title')
        #
        ofile.write('<small>species list:<br>\n')
        ofile.write('<i>\n')
        for s in species:
            gs = (s.split('_')) # genus / species
            ofile.write('&nbsp;&nbsp;&nbsp;<a href="./x' + s + '/species.html">' + gs[0] + ' ' + gs[1] + '</a></br>\n')
        ofile.write('</i></small>\n')
        #
        write_foot(ofile, '.')
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def get_species_list():
    slist = []
    with open(CFNAME) as ifile:
        next(ifile) # skip a line
        for line in ifile:
            slist.append(line.strip())
            next(ifile) # skip a line
    return(slist)

################################################################################
#
# MAIN PROGRAM: Create html files
#
################################################################################

species = get_species_list()
with open(CFNAME) as ifile:
    make_contents_page(species, next(ifile))
    make_species_pages(species, ifile)

################################################################################
################################################################################
