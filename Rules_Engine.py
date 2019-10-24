import csv
import colorsys
import webcolors
import math

class Color:
	def __init__(self,RGB,HLS,HSV):
		self.RGB = RGB
		self.HLS = HLS
		self.HSV = HSV

def complementaryColor(ColorInput):
	# Convert RGB (base 256) to HLS (between 0 and 1 )
	ColorInput.HLS = list(colorsys.rgb_to_hls(ColorInput.RGB[0] / 255, ColorInput.RGB[1] / 255, ColorInput.RGB[2] / 255))

	# Change the Hue value to the Hue opposite
	HueValue = ColorInput.HLS[0] * 360
	ColorInput.HLS[0] = ((HueValue + 180) % 360)/360

	# Convert HLS (between 0 and 1) to RGB (base 256)
	return list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorInput.HLS[0],ColorInput.HLS[1],ColorInput.HLS[2])))

def splitComplementaryColor(ColorInput):
	# Convert RGB (base 256) to HLS (between 0 and 1 )
	ColorInput.HLS = list(colorsys.rgb_to_hls(ColorInput.RGB[0] / 255, ColorInput.RGB[1] / 255, ColorInput.RGB[2] / 255))

	# Find the first triadic Hue
	FirstSplitComplementaryHue = ((ColorInput.HLS[0] * 360 + 150) % 360) / 360

	# Find the second triadic Hue
	SecondSplitComplementaryHue = ((ColorInput.HLS[0] * 360 + 210) % 360) / 360

	ColorOutput1 = Color("",[FirstSplitComplementaryHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")
	ColorOutput2 = Color("",[SecondSplitComplementaryHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")

	ColorOutput1.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput1.HLS[0],ColorOutput1.HLS[1],ColorOutput1.HLS[2])))
	ColorOutput2.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput2.HLS[0],ColorOutput2.HLS[1],ColorOutput2.HLS[2])))

	return [ColorOutput1.RGB,ColorOutput2.RGB]


class Product:
#Defining  Common Class for article
    def __init__(self, pid, gender, masterCategory, subCategory, articleType, baseColor, season, year, usage, productDisplayName):
        self.baseColor = baseColor
        self.season = season
        self.usage = usage
        self.articleType = articleType
        self.pid = pid
        self.gender = gender
        self.masterCategory = masterCategory
        self.subCategory = subCategory
        self.year = year
        self.productDisplayName= productDisplayName


def importCSV(inputcode,CSVfile):
#importing rows from CSV file to create ITEM input object and LIST of possible match objects
    my_list = []
    with open(CSVfile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            P = Product(row[0],row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            if(P.pid!=inputcode):
                my_list.append(P)
            elif(P.pid==inputcode):
                inputProduct = P
    infoblock=[inputProduct,my_list]
    return infoblock

def UsageandSeasonRule(P1,S):
#Applying Usage and Season rule
    input1 = []
    for sample in S:
        if (sample.usage == P1.usage):
            if (sample.season == P1.season):
                input1.append(sample)
    return input1


def ArticleRule(P1,input1):
#Applying article Rule
    input2 = []
    for sample in input1:
        if(P1.usage == "Formal"):
            if(P1.articleType == "Shirts"):
                if(sample.articleType == "Blazer" or sample.articleType == "Trousers"):
                    input2.append(sample)
            elif(P1.articleType == "Blazer"):
                if(sample.articleType == "Shirts" or sample.articleType == "Trousers"):
                    input2.append(sample)
            elif(P1.articleType == "Trousers"):
                if(sample.articleType == "Blazers" or sample.articleType == "Shirts"):
                    input2.append(sample)
        elif(P1.usage == "Casual"):
            if(P1.articleType == "Jackets"):
                if(sample.articleType == "Jeans" or sample.articleType == "Shirts" or sample.articleType == "Shorts" or sample.articleType == "Track Pants" or sample.articleType == "Trousers" or sample.articleType == "Tshirts"):
                    input2.append(sample)
            elif(P1.articleType == "Jeans"):
                if(sample.articleType == "Jackets" or sample.articleType == "Shirts" or sample.articleType == "Shorts" or sample.articleType == "Sweaters" or sample.articleType == "Sweatshirts" or sample.articleType == "Tshirts"):
                    input2.append(sample)
            elif(P1.articleType == "Shirts"):
                if(sample.articleType == "Jackets" or sample.articleType == "Sweaters" or sample.articleType == "Jeans" or sample.articleType == "Track Pants" or sample.articleType == "Trousers" or sample.articleType == "Tshirts"):
                    input2.append(sample)
            elif(P1.articleType == "Shorts"):
                if(sample.articleType == "Jackets" or sample.articleType == "Shirts"):
                    input2.append(sample)
            elif(P1.articleType == "Sweaters"):
                if(sample.articleType == "Jeans" or sample.articleType == "Shirts" or sample.articleType == "Trousers"):
                    input2.append(sample)
            elif(P1.articleType == "Sweatshirts"):
                if(sample.articleType == "Jeans" or sample.articleType == "Track Pants" or sample.articleType == "Trousers"):
                    input2.append(sample)
            elif(P1.articleType == "Track Pants"):
                if(sample.articleType == "Jackets" or sample.articleType == "Sweatshirts" or sample.articleType == "Tshirts"):
                    input2.append(sample)
            elif(P1.articleType == "Trousers"):
                if(sample.articleType == "Jackets" or sample.articleType == "Shirts" or sample.articleType == "Sweaters" or sample.articleType == "Sweatshirts"):
                    input2.append(sample)
            elif(P1.articleType == "Tshirts"):
                if(sample.articleType == "Jackets" or sample.articleType == "Jeans" or sample.articleType == "Shirts" or sample.articleType == "Shorts" or sample.articleType == "Track Pants" or sample.articleType == "Trousers"):
                    input2.append(sample)
        elif(P1.usage == "Party"):
            if(P1.articleType == "Shirts"):
                if(sample.articleType == "Jackets" or sample.articleType == "Sweaters" or sample.articleType == "Jeans" or sample.articleType == "Blazers" or sample.articleType == "Trousers" or sample.articleType == "Tshirts"):
                    input2.append(sample)
    return input2


def compNsplit(Item):
    #Finding Complimentory and Split Complimentory values of input object color
	Article_RGB1 = ArticleRGB(Item.baseColor)
	Color_obj=Color_object(Article_RGB1)
	Split= splitComplementaryColor(Color_obj)
	Comp= complementaryColor(Color_obj)
	Split.append(Comp)
	return Split


def ArticleRGB(baseColor):
    #Obtaining Color RGB values from Color Name
	Article_hex=webcolors.name_to_hex(baseColor)
	basecolorRGB=webcolors.hex_to_rgb(Article_hex)
	return basecolorRGB

def Color_object(basecolorRGB):
    # Converting RGB values to color object
	Colorobj = Color([basecolorRGB.red, basecolorRGB.green, basecolorRGB.blue],"","")
	return Colorobj

def PercDiff(complRGB, Article):
    #Finding Percentage difference between expected and actual values
	r1= complRGB[0]
	g1= complRGB[1]
	b1= complRGB[2]

	r2 = Article.red
	g2 = Article.green
	b2 = Article.blue

	d=math.sqrt((r2-r1)**2+(g2-g1)**2+(b2-b1)**2)

	p=(d/math.sqrt((255)**2+(255)**2+(255)**2))*100
	return p

def PercThresCheck(pd):
    #Checking if percentage difference is under defined threshold.
	if (pd<35):
		r = 1
	else:
		r = 0
	return r

def ArticleMatching(ITEMcompValue,ListItem):
    #Matching the color RGB of the LIST with Split/Complementary values of input Item
	Article_RGB = ArticleRGB(ListItem.baseColor)
	pd = PercDiff(ITEMcompValue,Article_RGB)
	result = PercThresCheck(pd)
	return result


def Colormatch(Item,List2):
    #Finding the matching objects from LIST and forming final Array
    ITEMcompValues = compNsplit(Item)  #Array of Complimentary and splitcomplimentary colour values of Input Item
    List=[]
    for b1 in List2:
	    for x1 in ITEMcompValues:
		    r =ArticleMatching(x1,b1)
		    if ((r==1) and (b1 not in List)):
			    List.append(b1)
    return List




inputcode= input("Please Enter Product ID: ") #Giving input item ProductID

CSVfile='Data1.csv' #CSV file path

infoblock=importCSV(inputcode,CSVfile)
Item = infoblock[0] #Object of input Item
print("\n"+Item.pid + ": "+ Item.productDisplayName)
List0 = infoblock[1] #List of objects possible Matches

List1 = UsageandSeasonRule(Item,List0) #Output list after first filter based on Usage and Season
List2 = ArticleRule(Item,List1) #Output list after second filter based on Article rule
List3 = Colormatch(Item,List2) #Final Ouput after applying Color Rule


#Displaying final list details
print("\n \nPossible Matches: ")
for A in List3:
	print(A.pid + ": "+ A.productDisplayName)