################################################################################
# Create html files for web site:
# The Developmental Morphology of New Zealand Native Ferns 
# 18.11.22 J. Rugis
#
################################################################################

# user settings
CFNAME = 'contents.txt'
OFNAME = 'index.html'

# global variables

################################################################################
# FUNCTION: 
def write_head(f):
    f.write('<head>\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<style> body {background-color: rgb(50,50,50); color: white; font-size: 2.2vw;} </style>\n')
    f.write('<style> a {text-decoration: none; color: rgb(150,150,150);} </style>\n')
    f.write('<style> object.title {border: 1px solid black; border-radius: 8px; max-width: 80vw;} </style>\n')
    f.write('<style> object.photo {border: 1px solid black; border-radius: 8px; max-width: 60vw;} </style>\n')
    f.write('<style> p.desc {margin-left: 20px; margin-right: 20px;} </style>\n')
    f.write('</head>\n')

################################################################################
# FUNCTION: 
def write_title(f):
    f.write('<p>  </p><br>\n')
    f.write('<big>The Developmental Morphology of<br>\n')
    f.write('New Zealand Native Orchids</big><br>\n')
    f.write('<small>by John Rugis</small>\n')

################################################################################
# FUNCTION: 
def write_foot(f):
    f.write('<p>  </p><br>\n')
    f.write('<small><small>\n')
    f.write('(c)2023 J.Rugis<br>\n')
    f.write('jrugis@gmail.com<br>\n')
    f.write('</small></small>\n')
    f.write('<p>  </p> <img src="images/by-nc-sa.svg">\n')

################################################################################
# FUNCTION: 
def write_photos(f, ifile, css):
    while(True):
        photo = next(ifile, "----").strip()
        if photo[0:4] == "----": break
        caption = next(ifile).strip()
        text = next(ifile).strip()
        f.write('<br><figure><object class="' + css + '" data="images/' + photo + '"></object><figcaption><small><small>' + caption + '</figcaption></figure>\n')
        f.write('<p class="desc">' + text + '</p></small></small><br>\n')
    
################################################################################
# FUNCTION: 
def write_species_page(species, prev, next, ifile):
    gs = species.split('_')               # genus / species
    with open('../' +species + '.html', 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: helvetica">\n')
        write_title(ofile)
        #
        ofile.write('<p>  </p>\n')
        ofile.write('<small>species:</small> <strong><i>' + gs[0] + ' ' + gs[1] + '</i></strong><br>\n')
        ofile.write('&nbsp;&nbsp;&nbsp;<small>\n')
        ofile.write('<a href="' + prev + '.html">prev species /</a>\n')
        ofile.write('<a href="' + next + '.html">next species /</a>\n')
        ofile.write('<a href="index.html">home</a>\n')
        ofile.write('</small><br>\n')
        #
        write_photos(ofile, ifile, 'photo')
        #
        write_foot(ofile)
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def make_species_pages(species, ifile):
    for i in range(0,len(species)):
        iprev = len(species )-1 if (i == 0) else i-1  # previous species index
        inext = 0 if (i >= len(species )-1) else i+1  # next species index
        next(ifile) # skip over the species name
        write_species_page(species[i], species[iprev], species[inext], ifile)

################################################################################
# FUNCTION: 
def make_contents_page(species, ifile):
    with open('../' + OFNAME, 'w') as ofile:
        #
        ofile.write('<!DOCTYPE html>\n')
        ofile.write('<html>\n')
        write_head(ofile)
        ofile.write('<body><span style="font-family: helvetica">\n')
        write_title(ofile)
        ofile.write('<br>\n')
        #
        write_photos(ofile, ifile, 'title')
        #
        ofile.write('<small>Species list:<br>\n')
        ofile.write('<i>\n')
        for s in species:
            gs = (s.split('_')) # genus / species
            ofile.write('&nbsp;&nbsp;&nbsp;<a href="' + s + '.html">' + gs[0] + ' ' + gs[1] + '</a></br>\n')
        ofile.write('</i></small>\n')
        #
        write_foot(ofile)
        ofile.write('</span></body>\n')
        ofile.write('</html>\n')

################################################################################
# FUNCTION: 
def get_species_list():
    slist = []
    with open(CFNAME) as ifile:
        for line in ifile:
            if line[0:4] == "----":
                slist.append(next(ifile).strip())
    return(slist)

################################################################################
#
# MAIN PROGRAM: Create html files
#
################################################################################

species = get_species_list()
with open(CFNAME) as ifile:
    make_contents_page(species, ifile)
    make_species_pages(species, ifile)

################################################################################
################################################################################
