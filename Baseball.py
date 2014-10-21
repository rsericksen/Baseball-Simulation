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

print "New York Yankees Batting Averages";

for i in range(0,8):
	print nyyPlayerName[i];
	print nyyAvg[i];
	i+=1;

print "\n";
print "Baltimore Orioles Batting Averages";

for i in range(0,8):
        print balPlayerName[i];
        print balAvg[i];
        i+=1;
