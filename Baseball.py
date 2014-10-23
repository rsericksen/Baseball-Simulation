from random import randrange

def getDouble(single,double,batter):
	return (single[batter]+double[batter])*100;

def getTriple(single,double,triple,batter):
	return (single[batter]+double[batter]+triple[batter])*100;

nyyPlayerName = ["Ellsbury","Jeter","Beltran","Teixeira","McCann","Gardner","Johnson","Suzuki"]
balPlayerName = ["Markakis","Flaherty","Davis","Jones","Cruz","Hardy","Lough","Weeks"];
nyyAvg = [0.271,0.256,0.233,0.216,0.232,0.256,0.219,0.284];
balAvg = [0.276,0.221,0.196,0.281,0.271,0.268,0.247,0.273];
nyySingle = [0.692,0.839,0.596,0.621,0.661,0.648,0.614,0.843];
balSingle = [0.763,0.629,0.523,0.663,0.554,0.739,0.698,0.667];
nyyDouble = [0.173,0.128,0.245,0.147,0.130,0.176,0.205,0.127];
balDouble = [0.153,0.242,0.182,0.166,0.193,0.198,0.140,0.000];
nyyTriple = [0.032,0.007,0.000,0.000,0.009,0.056,0.045,0.019];
balTriple = [0.005,0.017,0.000,0.011,0.013,0.000,0.069,0.333];
nyyHomeRun = [0.103,0.027,0.160,0.232,0.200,0.120,0.136,0.010];
balHomeRun = [0.079,0.112,0.295,0.160,0.240,0.063,0.093,0.000];

inning = 1;
outs = 0;
nyyScore = 0;
balScore = 0;
batter = 0;
onBase = 0;
x = 0;

firstBase = False;
secondBase = False;
thirdBase = False;

while (inning<=9 or nyyScore==balScore):
	print "-------------------------------------------";
	print "Top of Inning "+str(inning);
	print "-------------------------------------------";
	while (outs<3):
		print nyyPlayerName[batter]+" is up at bat.";
		x = randrange(0,100);
		if(x<=nyyAvg[batter]*100):
			x = randrange(0,100)

			if (x<nyySingle[batter]*100):
				print nyyPlayerName[batter]+" hit a single.";
                                print "\n";
				if thirdBase:
					nyyScore += 1;
					onBase -= 1;
					thirdBase = False;
					print "Yankees Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

				if secondBase:
					thirdBase = True;
					secondBase = False;

				if firstBase:
					secondBase = True;
					firstBase = False;

				onBase += 1;
				firstBase = True;

			elif ((x>=nyySingle[batter]*100) and (x<getDouble(nyySingle,nyyDouble,batter))):
				print nyyPlayerName[batter]+" hit a double.";
                                print "\n";
				if thirdBase:
                                        nyyScore += 1;
                                        onBase -= 1;
                                        thirdBase = False;
					print "Yankees Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if secondBase:
                                        nyyScore +=1;
					onBase -= 1;
                                        secondBase = False;
					print "Yankees Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if firstBase:
                                        thirdBase = True;
                                        firstBase = False;

				onBase += 1;
				secondBase = True;

			elif ((x>=getDouble(nyySingle,nyyDouble,batter)) and (x<getTriple(nyySingle,nyyDouble,nyyTriple,batter))):
				print nyyPlayerName[batter]+" hit a triple.";
                                print "\n";

				if thirdBase:
                                        nyyScore += 1;
                                        onBase -= 1;
                                        thirdBase = False;
					print "Yankees Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if secondBase:
                                        nyyScore += 1;
                                        onBase -= 1;
					secondBase = False;
					print "Yankees Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if firstBase:
                                        nyyScore += 1;
					onBase -= 1;
                                        firstBase = False;
					print "Yankees Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

				onBase += 1;
				thirdBase = True;

			elif ((x>=getTriple(nyySingle,nyyDouble,nyyTriple,batter))):
				print nyyPlayerName[batter]+" hit a home run.";
                                print "\n";
				nyyScore += (onBase+1);
				firstBase = False;
				secondBase = False;
				thirdBase = False;
				onBase = 0;
				print "Yankees Score!";
				print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
				print "\n";

		else:
			outs += 1;
			print nyyPlayerName[batter]+" is out.";
			print str(outs)+" outs.";
			print "\n";

		batter += 1;
		if (batter == 8):
			batter = 0;
	
	firstBase = False;
        secondBase = False;
        thirdBase = False;
        onBase = 0;
	batter = 0;
	outs = 0;	

	print "\n";
	print "-------------------------------------------";
	print "Bottom of Inning "+str(inning);
	print "-------------------------------------------";	

	while (outs<3):
		print balPlayerName[batter]+" is up at bat.";
		x = randrange(0,100);
                if(x<=balAvg[batter]*100):
                        x = randrange(0,100)

                        if (x<balSingle[batter]*100):
                                print balPlayerName[batter]+" hit a single.";
                                print "\n";
				if thirdBase:
                                        balScore += 1;
                                        onBase -= 1;
                                        thirdBase = False;
					print "Orioles Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if secondBase:
                                        thirdBase = True;
                                        secondBase = False;

                                if firstBase:
                                        secondBase = True;
                                        firstBase = False;

                                onBase += 1;
                                firstBase = True;

		elif ((x>=balSingle[batter]*100) and (x<getDouble(balSingle,balDouble,batter))):
                                print balPlayerName[batter]+" hit a double.";
                                print "\n";
				if thirdBase:
                                        balScore += 1;
                                        onBase -= 1;
                                        thirdBase = False;
					print "Orioles Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if secondBase:
                                        balScore +=1;
                                        onBase -= 1;
                                        secondBase = False;
					print "Orioles Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if firstBase:
                                        thirdBase = True;
                                        firstBase = False;

                                onBase += 1;
                                secondBase = True;

		elif ((x>=getDouble(balSingle,balDouble,batter)) and (x<getTriple(balSingle,balDouble,balTriple,batter))):
                                print balPlayerName[batter]+" hit a triple.";
                                print "\n";
				if thirdBase:
                                        balScore += 1;
                                        onBase -= 1;
                                        thirdBase = False;
					print "Orioles Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if secondBase:
                                        balScore += 1;
                                        onBase -= 1;
                                        secondBase = False;
					print "Orioles Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                if firstBase:
                                        balScore += 1;
                                        onBase -= 1;
                                        firstBase = False;
					print "Orioles Score!";
					print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
					print "\n";

                                onBase += 1;
                                thirdBase = True;

		elif ((x>=getTriple(balSingle,balDouble,balTriple,batter))):
                                print balPlayerName[batter]+" hit a home run.";
                                print "\n";
				balScore += (onBase+1);
                                firstBase = False;
                                secondBase = False;
                                thirdBase = False;
                                onBase = 0;
				print "Orioles Score!";
				print "Yankees: "+str(nyyScore)+"     "+"Orioles: "+str(balScore);
				print "\n";

                else:
                        outs += 1;
			print balPlayerName[batter]+" is out.";
			print str(outs)+" outs.";
			print "\n";

		batter += 1;
                if (batter == 8):
                        batter = 0;
	
	inning += 1;
	firstBase = False;
        secondBase = False;
        thirdBase = False;
        onBase = 0;
	batter = 0;
	outs = 0;

	print "\n";
print "-------------------------------------------";
print "After "+str(inning-1)+" Innings";
print "Yankees: "+str(nyyScore)+"     "+ "Orioles: "+str(balScore);
print "-------------------------------------------";
