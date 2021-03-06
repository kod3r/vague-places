import datetime

class cReport():
    """
        \brief Report printing class
        \details Class to record information about the execution and finally print it.
    """
    #__NPOINTS = 0;
    __alpha = 1;
    __optalpha = 1;
    __date = str(datetime.datetime.now());
    __countries = [];
    __country_val = [];
    __live = False;
    __WKTashape = "";
    __WKTchull = "";
    __query = "";
    __ofilename = "";

    def set_country_count(self,places):
        """
            \brief For a set of places, counts the places in each country.
        """
        self.__NPOINTS = len(places);
        for p in places:
            try:
                index = self.__countries.index(p.country)
                self.__country_val[index] += 1
            except:
                self.__countries.append(p.country)
                self.__country_val.append(1)

    def print_report(self):
        """
            \brief Prints the report to the standart output
        """
        self.__print_title();
        
        self.__print_banner("DATASET")
        if(self.__live):
            print "DBpedia Live "+str(self.__date)
        else:
            print "DBpedia Last release version"

        print "QUERY: "+str(self.__query).ljust(20);
        print "Retrieved Points:\t",str(self.__NPOINTS).ljust(20);
        print "Skipped Points:\t",str(self.__NPOINTS - sum(self.__country_val)).ljust(20);
        print "FILE:\t",str(self.__ofilename).ljust(20);
        print;
        print "country".rjust(30),"|".rjust(5),"total_points".rjust(5)
        
        for i,c in enumerate(self.__countries):
            print str(c).rjust(30),"|".rjust(5),str(self.__country_val[i]).rjust(5)

      
        self.__print_banner("GEOMETRIES")
        print "---- Alpha Shape WKT ---";
        print self.__WKTashape;
        print "Alpha:"+str(self.__alpha).ljust(20)
        print "Optimal Alpha: "+str(self.__optalpha).ljust(20);
        print
        print "---- Convex Hull Shape WKT ---";
        print self.__WKTchull;

    def __print_title(self):
        print;
        print "###########################################"
        print "# REPORT GENERATED BY vagueplaces.py"
        print "#  "+str(self.__date).center(40)
        print "#"
        print "###########################################"
        print;

    def __print_banner(self,text):
        print;
        print "###########################################"
        print "#"
        print "#"+str(text).center(40)
        print "#"
        print "###########################################"
        print;

    def write_report(self,fileh):
        """
            \todo Implement write_report to file
        """
        pass;

    def set_alphas(self,alpha,optalpha):
        """
            \brief Sets the report alpha values
            \param alpha used alpha
            \param optalpha Optimal alpha
        """
        self.__alpha = alpha;
        self.__optalpha = optalpha;

    def set_wkt_ashape(self,wkt):
        """
            \brief sets the WKT for the alpha shape
        """
        self.__WKTashape = wkt;

    def set_wkt_chull(self,wkt):
        """
            \brief sets the WKT for the convex hull
        """
        self.__WKTchull = wkt;

    def set_query(self,query):
        self.__query = query;
    
    def set_points_filename(self,ofile):
        """
            \brief Sets the path to the points file
            \param ofile String path
        """
        self.__ofilename = ofile;
    
    def set_live(self,live):
        """
            \brief sets if DBpedia live is the used DBpedia version
            \param live Boolean
        """
        self.__live = live;
