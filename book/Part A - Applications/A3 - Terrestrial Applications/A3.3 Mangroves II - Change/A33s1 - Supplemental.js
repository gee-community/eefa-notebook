/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var imageCollection = ee.ImageCollection("LANDSAT/MANGROVE_FORESTS"),
    Mangrove = 
    /* color: #01937c */
    /* shown: false */
    ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-13.661310159982044, 9.863979956913798]),
            {
              "landcover": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.662340128243763, 9.860766590107316]),
            {
              "landcover": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666974985421497, 9.860428339147328]),
            {
              "landcover": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.671094858468372, 9.857891445884547]),
            {
              "landcover": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.670579874337513, 9.852310212005683]),
            {
              "landcover": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.671953165353138, 9.847405413374954]),
            {
              "landcover": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66165348273595, 9.847236281087548]),
            {
              "landcover": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661481821358997, 9.851295432063562]),
            {
              "landcover": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658563577950794, 9.848251073512062]),
            {
              "landcover": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659936868966419, 9.84317708019428]),
            {
              "landcover": 1,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.671609842599231, 9.844361018943362]),
            {
              "landcover": 1,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.680021250069935, 9.842500541860387]),
            {
              "landcover": 1,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.681222879708606, 9.84520668687933]),
            {
              "landcover": 1,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.686201059640247, 9.847067148713466]),
            {
              "landcover": 1,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.690149271310169, 9.849096731482412]),
            {
              "landcover": 1,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.690492594064075, 9.851802822424787]),
            {
              "landcover": 1,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.684999430001575, 9.854508891171829]),
            {
              "landcover": 1,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.682767832101185, 9.864318204228617]),
            {
              "landcover": 1,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.68139454108556, 9.870237476020813]),
            {
              "landcover": 1,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.677789652169544, 9.864149080614622]),
            {
              "landcover": 1,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.67864795905431, 9.861950465733774]),
            {
              "landcover": 1,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.651010477364856, 9.872943393406452]),
            {
              "landcover": 1,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655130350411731, 9.876833110681515]),
            {
              "landcover": 1,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.654443704903919, 9.884950633398141]),
            {
              "landcover": 1,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.648950540841419, 9.880553666792991]),
            {
              "landcover": 1,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.646375620187122, 9.87564928855102]),
            {
              "landcover": 1,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.638822519601185, 9.871083077592651]),
            {
              "landcover": 1,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63744922858556, 9.868038901772325]),
            {
              "landcover": 1,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.633157694161731, 9.86753153639998]),
            {
              "landcover": 1,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.633501016915638, 9.864149080614622]),
            {
              "landcover": 1,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63470264655431, 9.860428339147328]),
            {
              "landcover": 1,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.626806223214466, 9.862288715131701]),
            {
              "landcover": 1,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.630239450753528, 9.866685925709453]),
            {
              "landcover": 1,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625261270821888, 9.868038901772325]),
            {
              "landcover": 1,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.621828043282825, 9.867024170246147]),
            {
              "landcover": 1,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.616678201974231, 9.865163820996548]),
            {
              "landcover": 1,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.623029672921497, 9.862457839700498]),
            {
              "landcover": 1,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6204547522672, 9.865163820996548]),
            {
              "landcover": 1,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618394815743763, 9.862119590476139]),
            {
              "landcover": 1,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.627321207345325, 9.861273965896487]),
            {
              "landcover": 1,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.630754434884388, 9.858567952663368]),
            {
              "landcover": 1,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.632814371407825, 9.854508891171829]),
            {
              "landcover": 1,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.630067789376575, 9.865163820996548]),
            {
              "landcover": 1,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.637792551339466, 9.866685925709453]),
            {
              "landcover": 1,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.645002329171497, 9.8715904374934]),
            {
              "landcover": 1,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.649637186349231, 9.872436035590608]),
            {
              "landcover": 1,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.654100382150013, 9.873281631515944]),
            {
              "landcover": 1,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.65289875251134, 9.879200742165947]),
            {
              "landcover": 1,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.653242075265247, 9.882921271500603]),
            {
              "landcover": 1,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.657876932442981, 9.882921271500603]),
            {
              "landcover": 1,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.648778879464466, 9.886134422054315]),
            {
              "landcover": 1,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.642255747140247, 9.880046320709882]),
            {
              "landcover": 1,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6424274085172, 9.877171344793748]),
            {
              "landcover": 1,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.644830667794544, 9.88089189708034]),
            {
              "landcover": 1,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.646032297433216, 9.884443294097883]),
            {
              "landcover": 1,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625261270821888, 9.876325758861322]),
            {
              "landcover": 1,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625261270821888, 9.873281631515944]),
            {
              "landcover": 1,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618738138497669, 9.871928676992896]),
            {
              "landcover": 1,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.616678201974231, 9.873281631515944]),
            {
              "landcover": 1,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.613244974435169, 9.860766590107316]),
            {
              "landcover": 1,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.61822315436681, 9.858906205532225]),
            {
              "landcover": 1,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.621656381905872, 9.854339762525496]),
            {
              "landcover": 1,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.62096973639806, 9.851464562270667]),
            {
              "landcover": 1,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618909799874622, 9.849773256298489]),
            {
              "landcover": 1,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.614618265450794, 9.848420205279472]),
            {
              "landcover": 1,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.609811746896106, 9.848420205279472]),
            {
              "landcover": 1,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.603288614571888, 9.85044977972763]),
            {
              "landcover": 1,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.602945291817981, 9.853155859573075]),
            {
              "landcover": 1,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.609296762765247, 9.855185404889882]),
            {
              "landcover": 1,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.614789926827747, 9.855185404889882]),
            {
              "landcover": 1,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.613073313058216, 9.85501627659046]),
            {
              "landcover": 1,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.605005228341419, 9.859075331836523]),
            {
              "landcover": 1,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6039752600797, 9.8631343371077]),
            {
              "landcover": 1,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.602601969064075, 9.86059746467071]),
            {
              "landcover": 1,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.598310434640247, 9.858398826098787]),
            {
              "landcover": 1,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.594533884347278, 9.856200172865066]),
            {
              "landcover": 1,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.592817270577747, 9.852479341692579]),
            {
              "landcover": 1,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.594190561593372, 9.848589336960218]),
            {
              "landcover": 1,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.597108805001575, 9.84520668687933]),
            {
              "landcover": 1,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.598653757394153, 9.841824002140536]),
            {
              "landcover": 1,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.603288614571888, 9.840809189962322]),
            {
              "landcover": 1,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.605691873849231, 9.84317708019428]),
            {
              "landcover": 1,
              "system:index": "81"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.597108805001575, 9.840978325541894]),
            {
              "landcover": 1,
              "system:index": "82"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.592302286446888, 9.845037553465422]),
            {
              "landcover": 1,
              "system:index": "83"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.590585672677356, 9.851633692391072]),
            {
              "landcover": 1,
              "system:index": "84"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.589899027169544, 9.856707555681723]),
            {
              "landcover": 1,
              "system:index": "85"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.58474918586095, 9.85653842816291]),
            {
              "landcover": 1,
              "system:index": "86"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618394815743763, 9.84351534884146]),
            {
              "landcover": 1,
              "system:index": "87"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618738138497669, 9.841147461034842]),
            {
              "landcover": 1,
              "system:index": "88"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.622343027413685, 9.839117829403516]),
            {
              "landcover": 1,
              "system:index": "89"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.623544657052356, 9.843853617142127]),
            {
              "landcover": 1,
              "system:index": "90"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625776254952747, 9.846559751071275]),
            {
              "landcover": 1,
              "system:index": "91"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.628351175607044, 9.850788040922096]),
            {
              "landcover": 1,
              "system:index": "92"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.629381143868763, 9.853663247072985]),
            {
              "landcover": 1,
              "system:index": "93"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.628007852853138, 9.857722318972954]),
            {
              "landcover": 1,
              "system:index": "94"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.630754434884388, 9.852648471292772]),
            {
              "landcover": 1,
              "system:index": "95"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631784403146106, 9.848251073512062]),
            {
              "landcover": 1,
              "system:index": "96"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.635389292062122, 9.851802822424787]),
            {
              "landcover": 1,
              "system:index": "97"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.621656381905872, 9.862119590476139]),
            {
              "landcover": 1,
              "system:index": "98"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.613244974435169, 9.846390618350565]),
            {
              "landcover": 1,
              "system:index": "99"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.61221500617345, 9.841824002140536]),
            {
              "landcover": 1,
              "system:index": "100"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.612043344796497, 9.838948692871343]),
            {
              "landcover": 1,
              "system:index": "101"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.647062265694935, 9.837933871859953]),
            {
              "landcover": 1,
              "system:index": "102"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.644315683663685, 9.842838811200574]),
            {
              "landcover": 1,
              "system:index": "103"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.642770731271106, 9.839117829403516]),
            {
              "landcover": 1,
              "system:index": "104"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63744922858556, 9.844868419964866]),
            {
              "landcover": 1,
              "system:index": "105"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.657876932442981, 9.858737079141173]),
            {
              "landcover": 1,
              "system:index": "106"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.662511789620716, 9.858567952663368]),
            {
              "landcover": 1,
              "system:index": "107"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.706800424874622, 9.85535453310259]),
            {
              "landcover": 1,
              "system:index": "108"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.70611377936681, 9.852986730233013]),
            {
              "landcover": 1,
              "system:index": "109"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.70559879523595, 9.850618910368206]),
            {
              "landcover": 1,
              "system:index": "110"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.701135599435169, 9.85501627659046]),
            {
              "landcover": 1,
              "system:index": "111"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.70010563117345, 9.864656451196232]),
            {
              "landcover": 1,
              "system:index": "112"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.69787403327306, 9.870913957452]),
            {
              "landcover": 1,
              "system:index": "113"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.51410768826411, 9.628911414362962]),
            {
              "landcover": 1,
              "system:index": "114"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.512734397248485, 9.626711248582774]),
            {
              "landcover": 1,
              "system:index": "115"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.507241233185985, 9.62518804849386]),
            {
              "landcover": 1,
              "system:index": "116"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.506897910432079, 9.623664841537515]),
            {
              "landcover": 1,
              "system:index": "117"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.502263053254344, 9.62620351598291]),
            {
              "landcover": 1,
              "system:index": "118"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.513936026887157, 9.62011066527207]),
            {
              "landcover": 1,
              "system:index": "119"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.516167624787547, 9.618248938979898]),
            {
              "landcover": 1,
              "system:index": "120"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.510331137971141, 9.614356205426008]),
            {
              "landcover": 1,
              "system:index": "121"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.515137656525829, 9.609955670070063]),
            {
              "landcover": 1,
              "system:index": "122"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.509987815217235, 9.605385822784951]),
            {
              "landcover": 1,
              "system:index": "123"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.507756217316844, 9.603354759745566]),
            {
              "landcover": 1,
              "system:index": "124"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.505009635285594, 9.599292597123075]),
            {
              "landcover": 1,
              "system:index": "125"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.50363634426997, 9.59573816487159]),
            {
              "landcover": 1,
              "system:index": "126"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.50363634426997, 9.591675910937065]),
            {
              "landcover": 1,
              "system:index": "127"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.504494651154735, 9.58744434466681]),
            {
              "landcover": 1,
              "system:index": "128"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.507241233185985, 9.584228318994764]),
            {
              "landcover": 1,
              "system:index": "129"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.509644492463329, 9.581858596362853]),
            {
              "landcover": 1,
              "system:index": "130"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.511189444855907, 9.57965812481821]),
            {
              "landcover": 1,
              "system:index": "131"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.510502799348094, 9.574749329210274]),
            {
              "landcover": 1,
              "system:index": "132"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.509987815217235, 9.572040997815119]),
            {
              "landcover": 1,
              "system:index": "133"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.50861452420161, 9.568317006897123]),
            {
              "landcover": 1,
              "system:index": "134"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.509301169709422, 9.56391587411893]),
            {
              "landcover": 1,
              "system:index": "135"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.527497275666454, 9.559514684378756]),
            {
              "landcover": 1,
              "system:index": "136"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.530415519074657, 9.555959835714257]),
            {
              "landcover": 1,
              "system:index": "137"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531960471467235, 9.553082073885204]),
            {
              "landcover": 1,
              "system:index": "138"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538140281037547, 9.554774877907569]),
            {
              "landcover": 1,
              "system:index": "139"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.542603476838329, 9.55511343770186]),
            {
              "landcover": 1,
              "system:index": "140"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.547924979523875, 9.555282717472718]),
            {
              "landcover": 1,
              "system:index": "141"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.550843222932079, 9.558668295208136]),
            {
              "landcover": 1,
              "system:index": "142"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.554276450471141, 9.562053839256034]),
            {
              "landcover": 1,
              "system:index": "143"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.554276450471141, 9.560191794199206]),
            {
              "landcover": 1,
              "system:index": "144"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54157350857661, 9.564085149510012]),
            {
              "landcover": 1,
              "system:index": "145"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.539856894807079, 9.56069962568011]),
            {
              "landcover": 1,
              "system:index": "146"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53934191067622, 9.564931525201379]),
            {
              "landcover": 1,
              "system:index": "147"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.542603476838329, 9.561038179579535]),
            {
              "landcover": 1,
              "system:index": "148"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.548954947785594, 9.566116447629842]),
            {
              "landcover": 1,
              "system:index": "149"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.554104789094188, 9.56899409919021]),
            {
              "landcover": 1,
              "system:index": "150"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.55753801663325, 9.568655553212261]),
            {
              "landcover": 1,
              "system:index": "151"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.560112937287547, 9.57068682402128]),
            {
              "landcover": 1,
              "system:index": "152"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.587150488427461, 9.588802244505368]),
            {
              "landcover": 1,
              "system:index": "153"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.570670996239961, 9.591510442157333]),
            {
              "landcover": 1,
              "system:index": "154"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.575820837548555, 9.59591121720367]),
            {
              "landcover": 1,
              "system:index": "155"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.575820837548555, 9.607082158693155]),
            {
              "landcover": 1,
              "system:index": "156"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.57994071059543, 9.608436187164969]),
            {
              "landcover": 1,
              "system:index": "157"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.566894445946993, 9.610128715137005]),
            {
              "landcover": 1,
              "system:index": "158"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.56071463637668, 9.613513745683104]),
            {
              "landcover": 1,
              "system:index": "159"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.55796805434543, 9.615206248254303]),
            {
              "landcover": 1,
              "system:index": "160"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.562774572900118, 9.610128715137005]),
            {
              "landcover": 1,
              "system:index": "161"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.562087927392305, 9.60437408550142]),
            {
              "landcover": 1,
              "system:index": "162"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.559341345361055, 9.599296389893185]),
            {
              "landcover": 1,
              "system:index": "163"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.558998022607149, 9.594895658802585]),
            {
              "landcover": 1,
              "system:index": "164"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.558654699853243, 9.589817821159402]),
            {
              "landcover": 1,
              "system:index": "165"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.560371313622774, 9.586094025227984]),
            {
              "landcover": 1,
              "system:index": "166"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.564147863915743, 9.59320305470555]),
            {
              "landcover": 1,
              "system:index": "167"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.568611059716524, 9.590494870572455]),
            {
              "landcover": 1,
              "system:index": "168"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.525695715478243, 9.592526010700317]),
            {
              "landcover": 1,
              "system:index": "169"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52775565200168, 9.595234178607734]),
            {
              "landcover": 1,
              "system:index": "170"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52775565200168, 9.588802244505368]),
            {
              "landcover": 1,
              "system:index": "171"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.529815588525118, 9.584739907481588]),
            {
              "landcover": 1,
              "system:index": "172"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.525695715478243, 9.581693122794402]),
            {
              "landcover": 1,
              "system:index": "173"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53324881606418, 9.595234178607734]),
            {
              "landcover": 1,
              "system:index": "174"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.51402274184543, 9.608436187164969]),
            {
              "landcover": 1,
              "system:index": "175"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.498229895165743, 9.649731449891549]),
            {
              "landcover": 1,
              "system:index": "176"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.49754324965793, 9.656839140978562]),
            {
              "landcover": 1,
              "system:index": "177"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.502693090966524, 9.670377185054937]),
            {
              "landcover": 1,
              "system:index": "178"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.43711844497043, 9.683237822077341]),
            {
              "landcover": 1,
              "system:index": "179"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.435745153954805, 9.682560958718609]),
            {
              "landcover": 1,
              "system:index": "180"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.436088476708711, 9.678499749919098]),
            {
              "landcover": 1,
              "system:index": "181"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.43986502700168, 9.672069402255028]),
            {
              "landcover": 1,
              "system:index": "182"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.464240942529024, 9.658869882308721]),
            {
              "landcover": 1,
              "system:index": "183"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.447418127587618, 9.609620957634213]),
            {
              "landcover": 1,
              "system:index": "184"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.457374487450899, 9.61622174573161]),
            {
              "landcover": 1,
              "system:index": "185"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.455314550927461, 9.613682996321328]),
            {
              "landcover": 1,
              "system:index": "186"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.45308295302707, 9.613175244152618]),
            {
              "landcover": 1,
              "system:index": "187"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.45685950332004, 9.607589920004852]),
            {
              "landcover": 1,
              "system:index": "188"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.456687841943086, 9.601835247213083]),
            {
              "landcover": 1,
              "system:index": "189"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.459949408105196, 9.59997342037242]),
            {
              "landcover": 1,
              "system:index": "190"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.46235266738254, 9.601665990650465]),
            {
              "landcover": 1,
              "system:index": "191"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.487586889794649, 9.647362186207621]),
            {
              "landcover": 1,
              "system:index": "192"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.477115545800508, 9.669700295790179]),
            {
              "landcover": 1,
              "system:index": "193"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.500118170312227, 9.668684959338288]),
            {
              "landcover": 1,
              "system:index": "194"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.516597662499727, 9.616390995014688]),
            {
              "landcover": 1,
              "system:index": "195"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.49256506972629, 9.621637680767956]),
            {
              "landcover": 1,
              "system:index": "196"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.495998297265352, 9.622991650968471]),
            {
              "landcover": 1,
              "system:index": "197"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.488616858056368, 9.618083483186357]),
            {
              "landcover": 1,
              "system:index": "198"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.517627630761446, 9.640254295246155]),
            {
              "landcover": 1,
              "system:index": "199"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.521575842431368, 9.643131316780002]),
            {
              "landcover": 1,
              "system:index": "200"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.520202551415743, 9.639577345436397]),
            {
              "landcover": 1,
              "system:index": "201"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52003089003879, 9.638054203397656]),
            {
              "landcover": 1,
              "system:index": "202"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531360540917696, 9.756500193416775]),
            {
              "landcover": 1,
              "system:index": "203"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.529815588525118, 9.752947423648195]),
            {
              "landcover": 1,
              "system:index": "204"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.527583990624727, 9.74939461601333]),
            {
              "landcover": 1,
              "system:index": "205"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52500906997043, 9.752270701303399]),
            {
              "landcover": 1,
              "system:index": "206"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.521232519677461, 9.756161836022985]),
            {
              "landcover": 1,
              "system:index": "207"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.518829260400118, 9.759037862917843]),
            {
              "landcover": 1,
              "system:index": "208"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52449408583957, 9.759037862917843]),
            {
              "landcover": 1,
              "system:index": "209"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.527583990624727, 9.756838550466977]),
            {
              "landcover": 1,
              "system:index": "210"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.528098974755586, 9.760560455339853]),
            {
              "landcover": 1,
              "system:index": "211"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.530158911279024, 9.76495901656875]),
            {
              "landcover": 1,
              "system:index": "212"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.528785620263399, 9.766481581917269]),
            {
              "landcover": 1,
              "system:index": "213"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.525867376855196, 9.769019175354734]),
            {
              "landcover": 1,
              "system:index": "214"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.524150763085665, 9.770710893563262]),
            {
              "landcover": 1,
              "system:index": "215"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52552405410129, 9.767496621613954]),
            {
              "landcover": 1,
              "system:index": "216"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.522434149316133, 9.769188347562617]),
            {
              "landcover": 1,
              "system:index": "217"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.519344244530977, 9.76698910215254]),
            {
              "landcover": 1,
              "system:index": "218"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.519344244530977, 9.765635713138927]),
            {
              "landcover": 1,
              "system:index": "219"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.515567694238008, 9.76326726912586]),
            {
              "landcover": 1,
              "system:index": "220"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.51453772597629, 9.760898808266235]),
            {
              "landcover": 1,
              "system:index": "221"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.511447821191133, 9.76242139218114]),
            {
              "landcover": 1,
              "system:index": "222"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.512134466698946, 9.764789842211282]),
            {
              "landcover": 1,
              "system:index": "223"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.51127615981418, 9.768004140301493]),
            {
              "landcover": 1,
              "system:index": "224"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.514194403222383, 9.77054172212945]),
            {
              "landcover": 1,
              "system:index": "225"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.516940985253633, 9.768680830680962]),
            {
              "landcover": 1,
              "system:index": "226"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.518142614892305, 9.77240260317031]),
            {
              "landcover": 1,
              "system:index": "227"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.521575842431368, 9.774094304174467]),
            {
              "landcover": 1,
              "system:index": "228"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.520202551415743, 9.773925134461207]),
            {
              "landcover": 1,
              "system:index": "229"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526382360986055, 9.766650755415005]),
            {
              "landcover": 1,
              "system:index": "230"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531360540917696, 9.763774794261284]),
            {
              "landcover": 1,
              "system:index": "231"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.525180731347383, 9.75819197523183]),
            {
              "landcover": 1,
              "system:index": "232"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.522434149316133, 9.756161836022985]),
            {
              "landcover": 1,
              "system:index": "233"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.524150763085665, 9.75210152050255]),
            {
              "landcover": 1,
              "system:index": "234"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.536167059472383, 9.74973298027629]),
            {
              "landcover": 1,
              "system:index": "235"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.537025366357149, 9.746010954502083]),
            {
              "landcover": 1,
              "system:index": "236"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538055334618868, 9.74347318584398]),
            {
              "landcover": 1,
              "system:index": "237"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538913641503633, 9.741273770727341]),
            {
              "landcover": 1,
              "system:index": "238"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.536682043603243, 9.740935397884376]),
            {
              "landcover": 1,
              "system:index": "239"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53548041396457, 9.743811556113686]),
            {
              "landcover": 1,
              "system:index": "240"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.534450445702852, 9.747026056559818]),
            {
              "landcover": 1,
              "system:index": "241"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.532562170556368, 9.74550340231482]),
            {
              "landcover": 1,
              "system:index": "242"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52998724990207, 9.744149926040262]),
            {
              "landcover": 1,
              "system:index": "243"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526897345116915, 9.744319110874857]),
            {
              "landcover": 1,
              "system:index": "244"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.524322424462618, 9.74465748028668]),
            {
              "landcover": 1,
              "system:index": "245"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.523807440331758, 9.742458072976037]),
            {
              "landcover": 1,
              "system:index": "246"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.523807440331758, 9.740258651169293]),
            {
              "landcover": 1,
              "system:index": "247"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.528613958886446, 9.735521385749621]),
            {
              "landcover": 1,
              "system:index": "248"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.532562170556368, 9.73670570840598]),
            {
              "landcover": 1,
              "system:index": "249"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.533077154687227, 9.740766211334252]),
            {
              "landcover": 1,
              "system:index": "250"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.532390509179415, 9.742458072976037]),
            {
              "landcover": 1,
              "system:index": "251"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.529472265771211, 9.742119701333845]),
            {
              "landcover": 1,
              "system:index": "252"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.527412329247774, 9.741950515384083]),
            {
              "landcover": 1,
              "system:index": "253"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52998724990207, 9.740597024698355]),
            {
              "landcover": 1,
              "system:index": "254"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526725683739961, 9.740597024698355]),
            {
              "landcover": 1,
              "system:index": "255"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.581828985741915, 9.75430086421618]),
            {
              "landcover": 1,
              "system:index": "256"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.581828985741915, 9.753116604019736]),
            {
              "landcover": 1,
              "system:index": "257"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.585090551904024, 9.753285784305413]),
            {
              "landcover": 1,
              "system:index": "258"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.585262213280977, 9.7510864338945]),
            {
              "landcover": 1,
              "system:index": "259"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.584747229150118, 9.750240526026937]),
            {
              "landcover": 1,
              "system:index": "260"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.55470648818332, 9.730276477790866]),
            {
              "landcover": 1,
              "system:index": "261"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.553333197167696, 9.727400202985306]),
            {
              "landcover": 1,
              "system:index": "262"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.554534826806368, 9.72587745924342]),
            {
              "landcover": 1,
              "system:index": "263"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.541316900780977, 9.72587745924342]),
            {
              "landcover": 1,
              "system:index": "264"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.542861853173555, 9.729430517182633]),
            {
              "landcover": 1,
              "system:index": "265"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.542346869042696, 9.731968392581692]),
            {
              "landcover": 1,
              "system:index": "266"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53874198012668, 9.731968392581692]),
            {
              "landcover": 1,
              "system:index": "267"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.537883673241915, 9.728753747154048]),
            {
              "landcover": 1,
              "system:index": "268"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.535308752587618, 9.727400202985306]),
            {
              "landcover": 1,
              "system:index": "269"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.534450445702852, 9.731460819044104]),
            {
              "landcover": 1,
              "system:index": "270"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.534622107079805, 9.734167868999362]),
            {
              "landcover": 1,
              "system:index": "271"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.540115271142305, 9.737720838768078]),
            {
              "landcover": 1,
              "system:index": "272"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.543205175927461, 9.73941271584591]),
            {
              "landcover": 1,
              "system:index": "273"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.551444922021211, 9.76512819084024]),
            {
              "landcover": 1,
              "system:index": "274"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.556423101952852, 9.762252216534353]),
            {
              "landcover": 1,
              "system:index": "275"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.55195990615207, 9.76326726912586]),
            {
              "landcover": 1,
              "system:index": "276"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.548355017236055, 9.768004140301493]),
            {
              "landcover": 1,
              "system:index": "277"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54749671035129, 9.77240260317031]),
            {
              "landcover": 1,
              "system:index": "278"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.545608435204805, 9.764451493238456]),
            {
              "landcover": 1,
              "system:index": "279"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538398657372774, 9.759037862917843]),
            {
              "landcover": 1,
              "system:index": "280"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.539085302880586, 9.75700772886324]),
            {
              "landcover": 1,
              "system:index": "281"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.544921789696993, 9.74837952116449]),
            {
              "landcover": 1,
              "system:index": "282"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54749671035129, 9.74550340231482]),
            {
              "landcover": 1,
              "system:index": "283"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.552303228905977, 9.74465748028668]),
            {
              "landcover": 1,
              "system:index": "284"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.555908117821993, 9.747026056559818]),
            {
              "landcover": 1,
              "system:index": "285"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.654785070946993, 9.909740584973962]),
            {
              "landcover": 1,
              "system:index": "286"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.650321875146211, 9.90940238439265]),
            {
              "landcover": 1,
              "system:index": "287"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.652381811669649, 9.908049578580023]),
            {
              "landcover": 1,
              "system:index": "288"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.671951208642305, 9.897903357197523]),
            {
              "landcover": 1,
              "system:index": "289"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.674011145165743, 9.893168346572097]),
            {
              "landcover": 1,
              "system:index": "290"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.675727758935274, 9.889786154339548]),
            {
              "landcover": 1,
              "system:index": "291"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.670234594872774, 9.886065702680298]),
            {
              "landcover": 1,
              "system:index": "292"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.67057791762668, 9.88302166546021]),
            {
              "landcover": 1,
              "system:index": "293"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.674011145165743, 9.880315830943365]),
            {
              "landcover": 1,
              "system:index": "294"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.67057791762668, 9.876933506499089]),
            {
              "landcover": 1,
              "system:index": "295"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.672981176904024, 9.873551147289685]),
            {
              "landcover": 1,
              "system:index": "296"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.687400732568086, 9.874904095144537]),
            {
              "landcover": 1,
              "system:index": "297"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.649388511149061, 9.835897848162661]),
            {
              "landcover": 1,
              "system:index": "298"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643637855021131, 9.837504656559055]),
            {
              "landcover": 1,
              "system:index": "299"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.65016098734535, 9.832853347671694]),
            {
              "landcover": 1,
              "system:index": "300"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.651105124918592, 9.82913225343917]),
            {
              "landcover": 1,
              "system:index": "301"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.64767189737953, 9.824988258312377]),
            {
              "landcover": 1,
              "system:index": "302"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.644496161905897, 9.822789382675966]),
            {
              "landcover": 1,
              "system:index": "303"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643981177775037, 9.824988258312377]),
            {
              "landcover": 1,
              "system:index": "304"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.644238669840467, 9.822451092819612]),
            {
              "landcover": 1,
              "system:index": "305"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.645096976725233, 9.826172262217474]),
            {
              "landcover": 1,
              "system:index": "306"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.635655600992811, 9.82676426258091]),
            {
              "landcover": 1,
              "system:index": "307"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.633338172403944, 9.825411117336346]),
            {
              "landcover": 1,
              "system:index": "308"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.630763251749647, 9.82591854745168]),
            {
              "landcover": 1,
              "system:index": "309"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631020743815077, 9.82388882232074]),
            {
              "landcover": 1,
              "system:index": "310"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.629046637980116, 9.82591854745168]),
            {
              "landcover": 1,
              "system:index": "311"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.623725135294569, 9.835982417220407]),
            {
              "landcover": 1,
              "system:index": "312"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.623639304606092, 9.834206462463124]),
            {
              "landcover": 1,
              "system:index": "313"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618746955362928, 9.832937917508435]),
            {
              "landcover": 1,
              "system:index": "314"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.614283759562147, 9.835644140859554]),
            {
              "landcover": 1,
              "system:index": "315"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.610678870646131, 9.837420087890889]),
            {
              "landcover": 1,
              "system:index": "316"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.599435050455702, 9.832599638031681]),
            {
              "landcover": 1,
              "system:index": "317"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.602009971109998, 9.831838507943388]),
            {
              "landcover": 1,
              "system:index": "318"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.605185706583631, 9.831753937825424]),
            {
              "landcover": 1,
              "system:index": "319"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.60844727274574, 9.831500227341687]),
            {
              "landcover": 1,
              "system:index": "320"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.610249717203748, 9.830739094722384]),
            {
              "landcover": 1,
              "system:index": "321"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.611022193400037, 9.82955510716544]),
            {
              "landcover": 1,
              "system:index": "322"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.612052161661756, 9.827948260129261]),
            {
              "landcover": 1,
              "system:index": "323"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.612652976481092, 9.825749404166388]),
            {
              "landcover": 1,
              "system:index": "324"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.611365516153944, 9.822958527474464]),
            {
              "landcover": 1,
              "system:index": "325"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.607159812418592, 9.82092878418678]),
            {
              "landcover": 1,
              "system:index": "326"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.606558997599256, 9.82371967799777]),
            {
              "landcover": 1,
              "system:index": "327"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.608876426188123, 9.826510548269171]),
            {
              "landcover": 1,
              "system:index": "328"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.606558997599256, 9.829470536463448]),
            {
              "landcover": 1,
              "system:index": "329"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.60295410868324, 9.828709399172217]),
            {
              "landcover": 1,
              "system:index": "330"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.60123749491371, 9.830400812995848]),
            {
              "landcover": 1,
              "system:index": "331"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.601838309733045, 9.827863689016356]),
            {
              "landcover": 1,
              "system:index": "332"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.599778373209608, 9.831161946393877]),
            {
              "landcover": 1,
              "system:index": "333"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.601151664225233, 9.827440833127513]),
            {
              "landcover": 1,
              "system:index": "334"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.605099875895155, 9.820167627244706]),
            {
              "landcover": 1,
              "system:index": "335"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.557979365634356, 9.739303420698274]),
            {
              "landcover": 1,
              "system:index": "336"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531028529452716, 9.733720191979573]),
            {
              "landcover": 1,
              "system:index": "337"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.530856868075762, 9.731520712614177]),
            {
              "landcover": 1,
              "system:index": "338"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526050349521075, 9.736596412372151]),
            {
              "landcover": 1,
              "system:index": "339"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.999500577660426, 10.035249558065319]),
            {
              "landcover": 1,
              "system:index": "340"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.995724027367457, 10.039644440416982]),
            {
              "landcover": 1,
              "system:index": "341"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.000530545922144, 10.0437012019244]),
            {
              "landcover": 1,
              "system:index": "342"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.993320768090113, 10.056209229570396]),
            {
              "landcover": 1,
              "system:index": "343"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.990574186058863, 10.06060382706283]),
            {
              "landcover": 1,
              "system:index": "344"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.965854947777613, 10.049448193638165]),
            {
              "landcover": 1,
              "system:index": "345"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.954525296898707, 10.051138465880086]),
            {
              "landcover": 1,
              "system:index": "346"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.946628873558863, 10.066012480342117]),
            {
              "landcover": 1,
              "system:index": "347"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.93598586818777, 10.064998364754487]),
            {
              "landcover": 1,
              "system:index": "348"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.964824979515894, 10.049448193638165]),
            {
              "landcover": 1,
              "system:index": "349"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.96619827053152, 10.045391504205845]),
            {
              "landcover": 1,
              "system:index": "350"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.955898587914332, 10.044039263087305]),
            {
              "landcover": 1,
              "system:index": "351"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.947315519066676, 10.041334763892895]),
            {
              "landcover": 1,
              "system:index": "352"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.947315519066676, 10.036939904492623]),
            {
              "landcover": 1,
              "system:index": "353"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.9431956460198, 10.028488084121358]),
            {
              "landcover": 1,
              "system:index": "354"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.938045804711207, 10.021050299807792]),
            {
              "landcover": 1,
              "system:index": "355"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.935642545433863, 10.027135772396795]),
            {
              "landcover": 1,
              "system:index": "356"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.932552640648707, 10.033221130703813]),
            {
              "landcover": 1,
              "system:index": "357"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.0200999428948, 10.093730404886111]),
            {
              "landcover": 1,
              "system:index": "358"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.020786588402613, 10.084604034450745]),
            {
              "landcover": 1,
              "system:index": "359"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.021473233910426, 10.077505567574326]),
            {
              "landcover": 1,
              "system:index": "360"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.024906461449488, 10.067364629502437]),
            {
              "landcover": 1,
              "system:index": "361"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.026279752465113, 10.055871181133208]),
            {
              "landcover": 1,
              "system:index": "362"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.030056302758082, 10.051814572302199]),
            {
              "landcover": 1,
              "system:index": "363"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.0255931069573, 10.043025078538774]),
            {
              "landcover": 1,
              "system:index": "364"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.030399625511988, 10.042687016316068]),
            {
              "landcover": 1,
              "system:index": "365"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.023533170433863, 10.03896830855453]),
            {
              "landcover": 1,
              "system:index": "366"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.022503202172144, 10.054518983847622]),
            {
              "landcover": 1,
              "system:index": "367"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.027309720726832, 10.053842883082915]),
            {
              "landcover": 1,
              "system:index": "368"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.034519498558863, 10.05722337275972]),
            {
              "landcover": 1,
              "system:index": "369"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.040699308129176, 10.06060382706283]),
            {
              "landcover": 1,
              "system:index": "370"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.042759244652613, 10.051814572302199]),
            {
              "landcover": 1,
              "system:index": "371"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.042415921898707, 10.07277316948383]),
            {
              "landcover": 1,
              "system:index": "372"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.039669339867457, 10.079533716921128]),
            {
              "landcover": 1,
              "system:index": "373"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.036922757836207, 10.081899875029649]),
            {
              "landcover": 1,
              "system:index": "374"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.03383285305105, 10.075477405468384]),
            {
              "landcover": 1,
              "system:index": "375"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.035206144066676, 10.072435138391462]),
            {
              "landcover": 1,
              "system:index": "376"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.032802884789332, 10.070068910826576]),
            {
              "landcover": 1,
              "system:index": "377"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.029026334496363, 10.068378737654886]),
            {
              "landcover": 1,
              "system:index": "378"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.0255931069573, 10.091026322094907]),
            {
              "landcover": 1,
              "system:index": "379"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.042415921898707, 10.10927843988686]),
            {
              "landcover": 1,
              "system:index": "380"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.046879117699488, 10.108264460521394]),
            {
              "landcover": 1,
              "system:index": "381"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.051685636254176, 10.106574487803298]),
            {
              "landcover": 1,
              "system:index": "382"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.057865445824488, 10.10454650881349]),
            {
              "landcover": 1,
              "system:index": "383"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.059925382347926, 10.123473814924237]),
            {
              "landcover": 1,
              "system:index": "384"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.06232864162527, 10.117728143481251]),
            {
              "landcover": 1,
              "system:index": "385"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.064731900902613, 10.114348288716734]),
            {
              "landcover": 1,
              "system:index": "386"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.06507522365652, 10.110968398385992]),
            {
              "landcover": 1,
              "system:index": "387"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.060268705101832, 10.115362248881063]),
            {
              "landcover": 1,
              "system:index": "388"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.054432218285426, 10.115700234891127]),
            {
              "landcover": 1,
              "system:index": "389"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.052028959008082, 10.117052175374186]),
            {
              "landcover": 1,
              "system:index": "390"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.0365794350823, 10.126853573603118]),
            {
              "landcover": 1,
              "system:index": "391"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.035892789574488, 10.122797858916474]),
            {
              "landcover": 1,
              "system:index": "392"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.030742948265894, 10.12752952106626]),
            {
              "landcover": 1,
              "system:index": "393"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.023189847679957, 10.12482572266808]),
            {
              "landcover": 1,
              "system:index": "394"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.0200999428948, 10.125501674403939]),
            {
              "landcover": 1,
              "system:index": "395"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.040012662621363, 10.12482572266808]),
            {
              "landcover": 1,
              "system:index": "396"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.041729276390894, 10.130233296673653]),
            {
              "landcover": 1,
              "system:index": "397"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.025249784203394, 10.117052175374186]),
            {
              "landcover": 1,
              "system:index": "398"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.020786588402613, 10.120094020648413]),
            {
              "landcover": 1,
              "system:index": "399"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.017696683617457, 10.11265834799643]),
            {
              "landcover": 1,
              "system:index": "400"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.005337064476832, 10.108264460521394]),
            {
              "landcover": 1,
              "system:index": "401"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.003277127953394, 10.108602453998687]),
            {
              "landcover": 1,
              "system:index": "402"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.005337064476832, 10.094068413637778]),
            {
              "landcover": 1,
              "system:index": "403"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.003277127953394, 10.092040355803496]),
            {
              "landcover": 1,
              "system:index": "404"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.001217191429957, 10.088322216591616]),
            {
              "landcover": 1,
              "system:index": "405"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.958988492699488, 10.07277316948383]),
            {
              "landcover": 1,
              "system:index": "406"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.95521194240652, 10.067364629502437]),
            {
              "landcover": 1,
              "system:index": "407"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.958645169945582, 10.064660325517268]),
            {
              "landcover": 1,
              "system:index": "408"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.94697219631277, 10.082913937472131]),
            {
              "landcover": 1,
              "system:index": "409"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.121380155297144, 10.071421042988929]),
            {
              "landcover": 1,
              "system:index": "410"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.132366483422144, 10.071759075144007]),
            {
              "landcover": 1,
              "system:index": "411"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.139919584008082, 10.097110476427376]),
            {
              "landcover": 1,
              "system:index": "412"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.132023160668238, 10.101842516928926]),
            {
              "landcover": 1,
              "system:index": "413"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.130649869652613, 10.108264460521394]),
            {
              "landcover": 1,
              "system:index": "414"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.123096769066676, 10.12752952106626]),
            {
              "landcover": 1,
              "system:index": "415"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.108333890648707, 10.125501674403939]),
            {
              "landcover": 1,
              "system:index": "416"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.092197721215113, 10.125839649737824]),
            {
              "landcover": 1,
              "system:index": "417"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.088421170922144, 10.114686275793847]),
            {
              "landcover": 1,
              "system:index": "418"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.099064176293238, 10.114010301283944]),
            {
              "landcover": 1,
              "system:index": "419"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.093914334984644, 10.102180517157963]),
            {
              "landcover": 1,
              "system:index": "420"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.093914334984644, 10.095082437762859]),
            {
              "landcover": 1,
              "system:index": "421"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.104900663109644, 10.086632139121175]),
            {
              "landcover": 1,
              "system:index": "422"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.09528762600027, 10.150172937371915]),
            {
              "landcover": 1,
              "system:index": "423"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.091167752953394, 10.155580083537874]),
            {
              "landcover": 1,
              "system:index": "424"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.097690885277613, 10.160311261454012]),
            {
              "landcover": 1,
              "system:index": "425"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.104214017601832, 10.159635383180365]),
            {
              "landcover": 1,
              "system:index": "426"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.11073714992605, 10.154566250592843]),
            {
              "landcover": 1,
              "system:index": "427"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.116916959496363, 10.175180221816479]),
            {
              "landcover": 1,
              "system:index": "428"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.126186673851832, 10.185655664472218]),
            {
              "landcover": 1,
              "system:index": "429"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.132023160668238, 10.186331487669804]),
            {
              "landcover": 1,
              "system:index": "430"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.130649869652613, 10.181262778780816]),
            {
              "landcover": 1,
              "system:index": "431"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.145756070824488, 10.186669398731471]),
            {
              "landcover": 1,
              "system:index": "432"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.14369613430105, 10.17653191116013]),
            {
              "landcover": 1,
              "system:index": "433"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.138546292992457, 10.166394101608132]),
            {
              "landcover": 1,
              "system:index": "434"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.142666166039332, 10.162338887701564]),
            {
              "landcover": 1,
              "system:index": "435"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.145412748070582, 10.160311261454012]),
            {
              "landcover": 1,
              "system:index": "436"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.135799710961207, 10.159973322495789]),
            {
              "landcover": 1,
              "system:index": "437"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.172878568383082, 10.151524732480077]),
            {
              "landcover": 1,
              "system:index": "438"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.17768508693777, 10.151524732480077]),
            {
              "landcover": 1,
              "system:index": "439"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.181804959984644, 10.14848318545724]),
            {
              "landcover": 1,
              "system:index": "440"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.182834928246363, 10.141048171078742]),
            {
              "landcover": 1,
              "system:index": "441"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.182491605492457, 10.137330599166003]),
            {
              "landcover": 1,
              "system:index": "442"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.180774991722926, 10.199847650708099]),
            {
              "landcover": 1,
              "system:index": "443"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.182491605492457, 10.204578172280252]),
            {
              "landcover": 1,
              "system:index": "444"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.184551542015894, 10.200185547437004]),
            {
              "landcover": 1,
              "system:index": "445"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.187298124047144, 10.204240280213417]),
            {
              "landcover": 1,
              "system:index": "446"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.18764144680105, 10.200861339819124]),
            {
              "landcover": 1,
              "system:index": "447"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.189701383324488, 10.204916063988373]),
            {
              "landcover": 1,
              "system:index": "448"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.1903880288323, 10.202888708359332]),
            {
              "landcover": 1,
              "system:index": "449"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.192791288109644, 10.205591846328486]),
            {
              "landcover": 1,
              "system:index": "450"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.195537870140894, 10.204240280213417]),
            {
              "landcover": 1,
              "system:index": "451"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.172535245629176, 10.204240280213417]),
            {
              "landcover": 1,
              "system:index": "452"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.172535245629176, 10.199847650708099]),
            {
              "landcover": 1,
              "system:index": "453"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.175625150414332, 10.19646866370126]),
            {
              "landcover": 1,
              "system:index": "454"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.17493850490652, 10.193427544749241]),
            {
              "landcover": 1,
              "system:index": "455"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.170131986351832, 10.197820262805768]),
            {
              "landcover": 1,
              "system:index": "456"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.162235563011988, 10.185317752336328]),
            {
              "landcover": 1,
              "system:index": "457"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.152279203148707, 10.195454960609357]),
            {
              "landcover": 1,
              "system:index": "458"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.149532621117457, 10.199509753620669]),
            {
              "landcover": 1,
              "system:index": "459"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.150905912133082, 10.190724303536632]),
            {
              "landcover": 1,
              "system:index": "460"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.137173001976832, 10.202212920280374]),
            {
              "landcover": 1,
              "system:index": "461"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.140262906761988, 10.204578172280252]),
            {
              "landcover": 1,
              "system:index": "462"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.135113065453394, 10.200861339819124]),
            {
              "landcover": 1,
              "system:index": "463"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.134083097191676, 10.205591846328486]),
            {
              "landcover": 1,
              "system:index": "464"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.127903287621363, 10.20322660186085]),
            {
              "landcover": 1,
              "system:index": "465"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.126186673851832, 10.201537130766951]),
            {
              "landcover": 1,
              "system:index": "466"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.122410123558863, 10.197820262805768]),
            {
              "landcover": 1,
              "system:index": "467"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.117603605004176, 10.194779156756098]),
            {
              "landcover": 1,
              "system:index": "468"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.114170377465113, 10.192075927009176]),
            {
              "landcover": 1,
              "system:index": "469"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.10902053615652, 10.195792861998385]),
            {
              "landcover": 1,
              "system:index": "470"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.110050504418238, 10.191400115989413]),
            {
              "landcover": 1,
              "system:index": "471"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.106960599633082, 10.187345219780514]),
            {
              "landcover": 1,
              "system:index": "472"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.09528762600027, 10.194441254291904]),
            {
              "landcover": 1,
              "system:index": "473"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.096317594261988, 10.190048489650911]),
            {
              "landcover": 1,
              "system:index": "474"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.091854398461207, 10.187345219780514]),
            {
              "landcover": 1,
              "system:index": "475"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.09803420803152, 10.185993576250045]),
            {
              "landcover": 1,
              "system:index": "476"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.094600980492457, 10.184979839842379]),
            {
              "landcover": 1,
              "system:index": "477"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.091167752953394, 10.181938611286409]),
            {
              "landcover": 1,
              "system:index": "478"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.08430129787527, 10.184304013780388]),
            {
              "landcover": 1,
              "system:index": "479"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.085674588890894, 10.180586944843554]),
            {
              "landcover": 1,
              "system:index": "480"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.089107816429957, 10.176869832601675]),
            {
              "landcover": 1,
              "system:index": "481"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.214420621605738, 10.1403722521214]),
            {
              "landcover": 1,
              "system:index": "482"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.218540494652613, 10.13597874414021]),
            {
              "landcover": 1,
              "system:index": "483"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.220943753929957, 10.139020409928333]),
            {
              "landcover": 1,
              "system:index": "484"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.214763944359644, 10.137668562031386]),
            {
              "landcover": 1,
              "system:index": "485"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.224720304222926, 10.137668562031386]),
            {
              "landcover": 1,
              "system:index": "486"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.227466886254176, 10.143413876197156]),
            {
              "landcover": 1,
              "system:index": "487"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.234676664086207, 10.212349590792996]),
            {
              "landcover": 1,
              "system:index": "488"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.234676664086207, 10.207619184738817]),
            {
              "landcover": 1,
              "system:index": "489"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.236393277855738, 10.204240280213417]),
            {
              "landcover": 1,
              "system:index": "490"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.239483182640894, 10.21099805338396]),
            {
              "landcover": 1,
              "system:index": "491"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.241543119164332, 10.219107191672828]),
            {
              "landcover": 1,
              "system:index": "492"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.285488431664332, 10.228567591509108]),
            {
              "landcover": 1,
              "system:index": "493"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.28651839992605, 10.2278918580079]),
            {
              "landcover": 1,
              "system:index": "494"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.288921659203394, 10.2278918580079]),
            {
              "landcover": 1,
              "system:index": "495"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.195194547386988, 10.222148065200006]),
            {
              "landcover": 1,
              "system:index": "496"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.19313461086355, 10.220120819414998]),
            {
              "landcover": 1,
              "system:index": "497"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.1958811928948, 10.217755682988003]),
            {
              "landcover": 1,
              "system:index": "498"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.198971097679957, 10.216404168556885]),
            {
              "landcover": 1,
              "system:index": "499"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.52315168974187, 9.621012255759489],
                  [-13.524095827315112, 9.618727414519354],
                  [-13.521950060103197, 9.618727414519354]]]),
            {
              "landcover": 1,
              "system:index": "500"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.486244493696947, 9.617542675945005],
                  [-13.487016969893237, 9.615596310704088],
                  [-13.484098726485033, 9.615511685874274]]]),
            {
              "landcover": 1,
              "system:index": "501"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.52801132696572, 9.618896665130736],
                  [-13.528526311096579, 9.61568093809527],
                  [-13.525779729065329, 9.616188686502388]]]),
            {
              "landcover": 1,
              "system:index": "502"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.463294987854391, 9.581660060195713],
                  [-13.460205083069235, 9.579628855011359],
                  [-13.457630162414938, 9.582337125889376]]]),
            {
              "landcover": 1,
              "system:index": "503"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.480976109680563, 9.657990686442465],
                  [-13.482006077942282, 9.654775331951527],
                  [-13.479431157287985, 9.65528302154379]]]),
            {
              "landcover": 1,
              "system:index": "504"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.50775528448525, 9.663405950907341],
                  [-13.506896977600485, 9.659175282988585],
                  [-13.504493718323141, 9.660359875366272]]]),
            {
              "landcover": 1,
              "system:index": "505"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.446472172912985, 9.663405950907341],
                  [-13.449905400452048, 9.661882916583096],
                  [-13.44733047979775, 9.659344510726331]]]),
            {
              "landcover": 1,
              "system:index": "506"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.60766220587197, 9.722291314738907],
                  [-13.605430607971579, 9.71958416859477],
                  [-13.603199010071188, 9.723137293414952]]]),
            {
              "landcover": 1,
              "system:index": "507"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.60714722174111, 9.785902927708433],
                  [-13.60714722174111, 9.78133547748043],
                  [-13.604057316955954, 9.783534628020057]]]),
            {
              "landcover": 1,
              "system:index": "508"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.578308110412985, 9.78065881284821],
                  [-13.578308110412985, 9.777275469025232],
                  [-13.575389867004782, 9.779474646427087]]]),
            {
              "landcover": 1,
              "system:index": "509"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.701560979065329, 9.777275469025232],
                  [-13.699672703918845, 9.773722920958017],
                  [-13.6972694446415, 9.776937132749193]]]),
            {
              "landcover": 1,
              "system:index": "510"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.959463327400387, 10.056802999864853]),
            {
              "landcover": 1,
              "system:index": "511"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.981779306404293, 10.019108491959036]),
            {
              "landcover": 1,
              "system:index": "512"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.009416788093747, 10.03787177777399]),
            {
              "landcover": 1,
              "system:index": "513"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.006670206062497, 10.038209845027112]),
            {
              "landcover": 1,
              "system:index": "514"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.006155221931637, 10.036857573896196]),
            {
              "landcover": 1,
              "system:index": "515"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.016969888679684, 10.018601361050132]),
            {
              "landcover": 1,
              "system:index": "516"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.008730142585934, 10.053422505790016]),
            {
              "landcover": 1,
              "system:index": "517"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.02005979346484, 10.052746402731378]),
            {
              "landcover": 1,
              "system:index": "518"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.020918100349606, 10.04699946963806]),
            {
              "landcover": 1,
              "system:index": "519"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.996713846199215, 10.049534893889792]),
            {
              "landcover": 1,
              "system:index": "520"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.433250165943592, 9.515253067891168]),
            {
              "landcover": 1,
              "system:index": "521"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.441661573414295, 9.523548647400151]),
            {
              "landcover": 1,
              "system:index": "522"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.440116621021717, 9.50661867948395]),
            {
              "landcover": 1,
              "system:index": "523"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.443721509937733, 9.516776760858239]),
            {
              "landcover": 1,
              "system:index": "524"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.447154737476795, 9.522532872976543]),
            {
              "landcover": 1,
              "system:index": "525"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.445953107838124, 9.529473937981358]),
            {
              "landcover": 1,
              "system:index": "526"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.452647901539295, 9.52913535271861]),
            {
              "landcover": 1,
              "system:index": "527"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.442004896168202, 9.53793846035774]),
            {
              "landcover": 1,
              "system:index": "528"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.439944959644764, 9.543524930040505]),
            {
              "landcover": 1,
              "system:index": "529"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.449729658131092, 9.53759988349555]),
            {
              "landcover": 1,
              "system:index": "530"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.450072980884999, 9.544202071659186]),
            {
              "landcover": 1,
              "system:index": "531"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.452819562916249, 9.50407911200358]),
            {
              "landcover": 1,
              "system:index": "532"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.458484388355702, 9.50255536246944]),
            {
              "landcover": 1,
              "system:index": "533"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.454192853931874, 9.4998464576609]),
            {
              "landcover": 1,
              "system:index": "534"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.454364515308827, 9.491719614665294]),
            {
              "landcover": 1,
              "system:index": "535"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.394283033375233, 9.52913535271861]),
            {
              "landcover": 1,
              "system:index": "536"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.389991498951405, 9.545048496790354]),
            {
              "landcover": 1,
              "system:index": "537"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.431361890797108, 9.493582033213793]),
            {
              "landcover": 1,
              "system:index": "538"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.42758534050414, 9.49307410188631]),
            {
              "landcover": 1,
              "system:index": "539"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.439944959644764, 9.491719614665294]),
            {
              "landcover": 1,
              "system:index": "540"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.446639753345936, 9.480883524227751]),
            {
              "landcover": 1,
              "system:index": "541"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.432906843189686, 9.488671998844872]),
            {
              "landcover": 1,
              "system:index": "542"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.50946781731078, 9.52168639198262]),
            {
              "landcover": 1,
              "system:index": "543"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.530582166676014, 9.523379351872673]),
            {
              "landcover": 1,
              "system:index": "544"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54568836784789, 9.526765246475557]),
            {
              "landcover": 1,
              "system:index": "545"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.552726484302967, 9.527442421367]),
            {
              "landcover": 1,
              "system:index": "546"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.555816389088124, 9.53946205207731]),
            {
              "landcover": 1,
              "system:index": "547"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538821912769764, 9.540816350112253]),
            {
              "landcover": 1,
              "system:index": "548"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.444579816822499, 9.462935496757591]),
            {
              "landcover": 1,
              "system:index": "549"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.38037846184203, 9.45480777971921]),
            {
              "landcover": 1,
              "system:index": "550"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.35239765739867, 9.47174030668765]),
            {
              "landcover": 1,
              "system:index": "551"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.359264112476795, 9.486132298297015]),
            {
              "landcover": 1,
              "system:index": "552"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.359607435230702, 9.484100524314757]),
            {
              "landcover": 1,
              "system:index": "553"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.337463117603749, 9.47123234301792]),
            {
              "landcover": 1,
              "system:index": "554"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.34141132927367, 9.49425927381244]),
            {
              "landcover": 1,
              "system:index": "555"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.341582990650624, 9.498153381271607]),
            {
              "landcover": 1,
              "system:index": "556"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.337978101734608, 9.505772159084684]),
            {
              "landcover": 1,
              "system:index": "557"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.348621107105702, 9.512036360435498]),
            {
              "landcover": 1,
              "system:index": "558"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.352740980152577, 9.512713564520134]),
            {
              "landcover": 1,
              "system:index": "559"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.329910017017811, 9.432624908679694]),
            {
              "landcover": 1,
              "system:index": "560"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.33420155144164, 9.433810289049077]),
            {
              "landcover": 1,
              "system:index": "561"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.332828260426014, 9.429915452536795]),
            {
              "landcover": 1,
              "system:index": "562"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.345874525074452, 9.413658269000564]),
            {
              "landcover": 1,
              "system:index": "563"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.289397932056874, 9.419754802521876]),
            {
              "landcover": 1,
              "system:index": "564"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.282874799732655, 9.414674365391507]),
            {
              "landcover": 1,
              "system:index": "565"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.25901386833617, 9.407900333029371]),
            {
              "landcover": 1,
              "system:index": "566"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.244250989918202, 9.402481011589613]),
            {
              "landcover": 1,
              "system:index": "567"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.280128217701405, 9.39350507376156]),
            {
              "landcover": 1,
              "system:index": "568"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.28150150871703, 9.34235473089528]),
            {
              "landcover": 1,
              "system:index": "569"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.297122694019764, 9.35065447039907]),
            {
              "landcover": 1,
              "system:index": "570"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.288539625172108, 9.360647771582952]),
            {
              "landcover": 1,
              "system:index": "571"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.307422376636952, 9.358784635516088]),
            {
              "landcover": 1,
              "system:index": "572"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.331969953541249, 9.35963151678442]),
            {
              "landcover": 1,
              "system:index": "573"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.334029890064686, 9.35438081966868]),
            {
              "landcover": 1,
              "system:index": "574"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.341068006519764, 9.351840131314342]),
            {
              "landcover": 1,
              "system:index": "575"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.34467289543578, 9.336764998940213]),
            {
              "landcover": 1,
              "system:index": "576"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.291286207203358, 9.319317683374159]),
            {
              "landcover": 1,
              "system:index": "577"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.285106397633045, 9.305426964030449]),
            {
              "landcover": 1,
              "system:index": "578"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.273433424000233, 9.314405175017802]),
            {
              "landcover": 1,
              "system:index": "579"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.282703138355702, 9.318978891913023]),
            {
              "landcover": 1,
              "system:index": "580"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.249572492603749, 9.311864195309921]),
            {
              "landcover": 1,
              "system:index": "581"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.258842206959217, 9.304071742342185]),
            {
              "landcover": 1,
              "system:index": "582"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.252662397388905, 9.30034485562317]),
            {
              "landcover": 1,
              "system:index": "583"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.26004383659789, 9.293738004335609]),
            {
              "landcover": 1,
              "system:index": "584"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.263477064136952, 9.289502777673848]),
            {
              "landcover": 1,
              "system:index": "585"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.27377674675414, 9.29627911574363]),
            {
              "landcover": 1,
              "system:index": "586"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.279784894947499, 9.270528333966]),
            {
              "landcover": 1,
              "system:index": "587"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.25455067253539, 9.256466254018491]),
            {
              "landcover": 1,
              "system:index": "588"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.21009037590453, 9.264937453931857]),
            {
              "landcover": 1,
              "system:index": "589"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.205283857349842, 9.260532455463142]),
            {
              "landcover": 1,
              "system:index": "590"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.24030277824828, 9.232915246293794]),
            {
              "landcover": 1,
              "system:index": "591"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.259185529713124, 9.244097935622158]),
            {
              "landcover": 1,
              "system:index": "592"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.262103773121327, 9.239692676146335]),
            {
              "landcover": 1,
              "system:index": "593"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.27600834465453, 9.234101305928146]),
            {
              "landcover": 1,
              "system:index": "594"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.29025623894164, 9.216648883114125]),
            {
              "landcover": 1,
              "system:index": "595"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.29025623894164, 9.206820925471753]),
            {
              "landcover": 1,
              "system:index": "596"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.294891096119374, 9.20224574851503]),
            {
              "landcover": 1,
              "system:index": "597"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.305877424244374, 9.201398487027035]),
            {
              "landcover": 1,
              "system:index": "598"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.22382328606078, 9.209871010547175]),
            {
              "landcover": 1,
              "system:index": "599"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.192065931324452, 9.215632210520651]),
            {
              "landcover": 1,
              "system:index": "600"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.190177656177967, 9.218851663690847]),
            {
              "landcover": 1,
              "system:index": "601"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.187774396900624, 9.212751622278716]),
            {
              "landcover": 1,
              "system:index": "602"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.206313825611561, 9.193095217068748]),
            {
              "landcover": 1,
              "system:index": "603"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.19034931755492, 9.189536613174072]),
            {
              "landcover": 1,
              "system:index": "604"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.19086430168578, 9.184622291871827]),
            {
              "landcover": 1,
              "system:index": "605"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.18588612175414, 9.18394444910143]),
            {
              "landcover": 1,
              "system:index": "606"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.22056171989867, 9.209701562066911]),
            {
              "landcover": 1,
              "system:index": "607"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.237384534840077, 9.212921069296193]),
            {
              "landcover": 1,
              "system:index": "608"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.248199201588124, 9.214276642509766]),
            {
              "landcover": 1,
              "system:index": "609"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.283218122486561, 9.196484330379587]),
            {
              "landcover": 1,
              "system:index": "610"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.279956556324452, 9.192925760551425]),
            {
              "landcover": 1,
              "system:index": "611"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.289912916187733, 9.193264673504942]),
            {
              "landcover": 1,
              "system:index": "612"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.295062757496327, 9.194620322074341]),
            {
              "landcover": 1,
              "system:index": "613"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.281844831470936, 9.176149164076689]),
            {
              "landcover": 1,
              "system:index": "614"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.282703138355702, 9.17309878850916]),
            {
              "landcover": 1,
              "system:index": "615"
            })]),
    NonMangrove = 
    /* color: #b6c867 */
    /* shown: false */
    ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-13.640199652454818, 9.89526389438857]),
            {
              "landcover": 2,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.64088629796263, 9.8937419219008]),
            {
              "landcover": 2,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.637453070423568, 9.89526389438857]),
            {
              "landcover": 2,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6336765201306, 9.895940324341653]),
            {
              "landcover": 2,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631273260853256, 9.896109431612254]),
            {
              "landcover": 2,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.629556647083724, 9.894080138618607]),
            {
              "landcover": 2,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.628011694691146, 9.892558160646315]),
            {
              "landcover": 2,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.628011694691146, 9.890528845715746]),
            {
              "landcover": 2,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6281833560681, 9.888161295791257]),
            {
              "landcover": 2,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63539313390013, 9.882918803133371]),
            {
              "landcover": 2,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6336765201306, 9.879198273770779]),
            {
              "landcover": 2,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63264655186888, 9.877337993310382]),
            {
              "landcover": 2,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.629041662952865, 9.880043852321075]),
            {
              "landcover": 2,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.62543677403685, 9.883426144785675]),
            {
              "landcover": 2,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631273260853256, 9.88934507288544]),
            {
              "landcover": 2,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.638483038685287, 9.887653961445755]),
            {
              "landcover": 2,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.638483038685287, 9.886301066029677]),
            {
              "landcover": 2,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.620458594105209, 9.883933485655257]),
            {
              "landcover": 2,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.620458594105209, 9.88122765863999]),
            {
              "landcover": 2,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.620286932728256, 9.878352693047196]),
            {
              "landcover": 2,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618226996204818, 9.884779052031762]),
            {
              "landcover": 2,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.612390509388412, 9.881058543712408]),
            {
              "landcover": 2,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.609815588734115, 9.879198273770779]),
            {
              "landcover": 2,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.609472265980209, 9.882580574930365]),
            {
              "landcover": 2,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.614107123157943, 9.8912052854185]),
            {
              "landcover": 2,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.594366064808334, 9.865499598598175]),
            {
              "landcover": 2,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.596254339954818, 9.863639240739971]),
            {
              "landcover": 2,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.593851080677474, 9.863300992728192]),
            {
              "landcover": 2,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.592306128284896, 9.867359945951616]),
            {
              "landcover": 2,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.595567694447006, 9.870742368765931]),
            {
              "landcover": 2,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.59745596959349, 9.872433567144729]),
            {
              "landcover": 2,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.59694098546263, 9.870911488994695]),
            {
              "landcover": 2,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.487671836213329, 9.603185503942363]),
            {
              "landcover": 2,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.488873465852, 9.602508479883612]),
            {
              "landcover": 2,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.489045127228954, 9.599969627609893]),
            {
              "landcover": 2,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.488701804475047, 9.597769273580928]),
            {
              "landcover": 2,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.490075095490672, 9.591506649300088]),
            {
              "landcover": 2,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.48389528592036, 9.598107790515527]),
            {
              "landcover": 2,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.442353232697704, 9.603016248054569]),
            {
              "landcover": 2,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.440808280305125, 9.604708803125543]),
            {
              "landcover": 2,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.438233359650829, 9.60572433210698]),
            {
              "landcover": 2,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.43445680935786, 9.602339223657433]),
            {
              "landcover": 2,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.43720339138911, 9.600985170803016]),
            {
              "landcover": 2,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.43668840725825, 9.59472260595197]),
            {
              "landcover": 2,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.438405021027782, 9.592860740029861]),
            {
              "landcover": 2,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.438748343781688, 9.590491077703861]),
            {
              "landcover": 2,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.439606650666454, 9.589644765716853]),
            {
              "landcover": 2,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.444069846467235, 9.581689329827402]),
            {
              "landcover": 2,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.446301444367625, 9.58050446171579]),
            {
              "landcover": 2,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.459862693146922, 9.594384085635884]),
            {
              "landcover": 2,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.46243761380122, 9.59472260595197]),
            {
              "landcover": 2,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.469132407502391, 9.611817442013729]),
            {
              "landcover": 2,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.469475730256297, 9.615033205784563]),
            {
              "landcover": 2,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.471364005402782, 9.61621795315115]),
            {
              "landcover": 2,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.474282248810985, 9.61621795315115]),
            {
              "landcover": 2,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.472222312287547, 9.611817442013729]),
            {
              "landcover": 2,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.469304068879344, 9.609447912307623]),
            {
              "landcover": 2,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.47016237576411, 9.620787654108952]),
            {
              "landcover": 2,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.46964739163325, 9.624511068472138]),
            {
              "landcover": 2,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.46964739163325, 9.626372760267671]),
            {
              "landcover": 2,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.48938844998286, 9.624341823254763]),
            {
              "landcover": 2,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.492478354768016, 9.624341823254763]),
            {
              "landcover": 2,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.495568259553172, 9.62620351598291]),
            {
              "landcover": 2,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.496083243684032, 9.630434597660521]),
            {
              "landcover": 2,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.423127158478954, 9.615371705455658]),
            {
              "landcover": 2,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.411797507600047, 9.610801931314386]),
            {
              "landcover": 2,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.41248415310786, 9.606570603931203]),
            {
              "landcover": 2,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.408879264191844, 9.615202455662457]),
            {
              "landcover": 2,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.409050925568797, 9.621972381310744]),
            {
              "landcover": 2,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.414887412385204, 9.625865027159046]),
            {
              "landcover": 2,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.419693930939891, 9.63331170291934]),
            {
              "landcover": 2,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.413685782746532, 9.634665626321135]),
            {
              "landcover": 2,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.403557761506297, 9.632296256804214]),
            {
              "landcover": 2,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.405446036652782, 9.63128080763471]),
            {
              "landcover": 2,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.40750597317622, 9.634665626321135]),
            {
              "landcover": 2,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.409565909699657, 9.636527262130242]),
            {
              "landcover": 2,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.431023581818797, 9.63331170291934]),
            {
              "landcover": 2,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.532562170556368, 9.62265315892689]),
            {
              "landcover": 2,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.534278784325899, 9.62400712505879]),
            {
              "landcover": 2,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531875525048555, 9.626376552734179]),
            {
              "landcover": 2,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53050223403293, 9.628407477514115]),
            {
              "landcover": 2,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.551101599267305, 9.632130807889933]),
            {
              "landcover": 2,
              "system:index": "81"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.553504858544649, 9.628407477514115]),
            {
              "landcover": 2,
              "system:index": "82"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.561057959130586, 9.635854097202463]),
            {
              "landcover": 2,
              "system:index": "83"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.566894445946993, 9.630099905501739]),
            {
              "landcover": 2,
              "system:index": "84"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.569641027978243, 9.627053529017628]),
            {
              "landcover": 2,
              "system:index": "85"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.572387610009493, 9.624345615744067]),
            {
              "landcover": 2,
              "system:index": "86"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.576164160302461, 9.6209606936336]),
            {
              "landcover": 2,
              "system:index": "87"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.579597387841524, 9.617914234750414]),
            {
              "landcover": 2,
              "system:index": "88"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.581314001611055, 9.614190747727863]),
            {
              "landcover": 2,
              "system:index": "89"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.586463842919649, 9.611144227856878]),
            {
              "landcover": 2,
              "system:index": "90"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.590583715966524, 9.608436187164969]),
            {
              "landcover": 2,
              "system:index": "91"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.592643652489961, 9.60437408550142]),
            {
              "landcover": 2,
              "system:index": "92"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.597793493798555, 9.600650449498545]),
            {
              "landcover": 2,
              "system:index": "93"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.601570044091524, 9.595234178607734]),
            {
              "landcover": 2,
              "system:index": "94"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.599510107568086, 9.587786664810263]),
            {
              "landcover": 2,
              "system:index": "95"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.347854528954805, 9.631453841784552]),
            {
              "landcover": 2,
              "system:index": "96"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.353347693017305, 9.629084449726962]),
            {
              "landcover": 2,
              "system:index": "97"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.345451269677461, 9.657177598717503]),
            {
              "landcover": 2,
              "system:index": "98"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.348541174462618, 9.663608231103328]),
            {
              "landcover": 2,
              "system:index": "99"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.350257788232149, 9.672069402255028]),
            {
              "landcover": 2,
              "system:index": "100"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.346137915185274, 9.67477693205716]),
            {
              "landcover": 2,
              "system:index": "101"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.369140539696993, 9.638561918174645]),
            {
              "landcover": 2,
              "system:index": "102"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.418922339013399, 9.682899390568524]),
            {
              "landcover": 2,
              "system:index": "103"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.454284582665743, 9.670715629176321]),
            {
              "landcover": 2,
              "system:index": "104"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.451538000634493, 9.678499749919098]),
            {
              "landcover": 2,
              "system:index": "105"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.451538000634493, 9.682899390568524]),
            {
              "landcover": 2,
              "system:index": "106"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.454284582665743, 9.683237822077341]),
            {
              "landcover": 2,
              "system:index": "107"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.447418127587618, 9.679515056722407]),
            {
              "landcover": 2,
              "system:index": "108"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.44535819106418, 9.672069402255028]),
            {
              "landcover": 2,
              "system:index": "109"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.439178381493868, 9.643639023914613]),
            {
              "landcover": 2,
              "system:index": "110"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.441924963525118, 9.641946663826616]),
            {
              "landcover": 2,
              "system:index": "111"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.446388159325899, 9.643639023914613]),
            {
              "landcover": 2,
              "system:index": "112"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.452224646142305, 9.637884964968881]),
            {
              "landcover": 2,
              "system:index": "113"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.45909110122043, 9.642285136523668]),
            {
              "landcover": 2,
              "system:index": "114"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.458747778466524, 9.634161698060968]),
            {
              "landcover": 2,
              "system:index": "115"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.45909110122043, 9.626376552734179]),
            {
              "landcover": 2,
              "system:index": "116"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.44535819106418, 9.628745963790163]),
            {
              "landcover": 2,
              "system:index": "117"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.430938635400118, 9.610128715137005]),
            {
              "landcover": 2,
              "system:index": "118"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.417549047997774, 9.599634905301931]),
            {
              "landcover": 2,
              "system:index": "119"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.415489111474336, 9.591510442157333]),
            {
              "landcover": 2,
              "system:index": "120"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.417549047997774, 9.59117191863368]),
            {
              "landcover": 2,
              "system:index": "121"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.413429174950899, 9.583047252699105]),
            {
              "landcover": 2,
              "system:index": "122"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.413085852196993, 9.580000452816348]),
            {
              "landcover": 2,
              "system:index": "123"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.404502783349336, 9.582370188422113]),
            {
              "landcover": 2,
              "system:index": "124"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.411025915673555, 9.604712595834995]),
            {
              "landcover": 2,
              "system:index": "125"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.407249365380586, 9.601327477271484]),
            {
              "landcover": 2,
              "system:index": "126"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.47831717543918, 9.686622118403308]),
            {
              "landcover": 2,
              "system:index": "127"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.484153662255586, 9.683237822077341]),
            {
              "landcover": 2,
              "system:index": "128"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.477630529931368, 9.681545661122474]),
            {
              "landcover": 2,
              "system:index": "129"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.480033789208711, 9.676130688779114]),
            {
              "landcover": 2,
              "system:index": "130"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.398322973779024, 9.663946682035794]),
            {
              "landcover": 2,
              "system:index": "131"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.392829809716524, 9.664285132627802]),
            {
              "landcover": 2,
              "system:index": "132"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.381843481591524, 9.664962032790449]),
            {
              "landcover": 2,
              "system:index": "133"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.384246740868868, 9.663269779830442]),
            {
              "landcover": 2,
              "system:index": "134"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.427333746484102, 9.621129940544316]),
            {
              "landcover": 2,
              "system:index": "135"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.441581640771211, 9.628407477514115]),
            {
              "landcover": 2,
              "system:index": "136"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.450679693749727, 9.623837879588994]),
            {
              "landcover": 2,
              "system:index": "137"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.463382635644258, 9.619606715297124]),
            {
              "landcover": 2,
              "system:index": "138"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.430423651269258, 9.625361085765237]),
            {
              "landcover": 2,
              "system:index": "139"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.429908667138399, 9.631284600046119]),
            {
              "landcover": 2,
              "system:index": "140"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.434028540185274, 9.634669418694504]),
            {
              "landcover": 2,
              "system:index": "141"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.439006720116915, 9.629761420582756]),
            {
              "landcover": 2,
              "system:index": "142"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.424587164452852, 9.626376552734179]),
            {
              "landcover": 2,
              "system:index": "143"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.43437186293918, 9.622822404990066]),
            {
              "landcover": 2,
              "system:index": "144"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54200354628879, 9.771725920359758]),
            {
              "landcover": 2,
              "system:index": "145"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.540115271142305, 9.772233432596723]),
            {
              "landcover": 2,
              "system:index": "146"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.540801916650118, 9.770710893563262]),
            {
              "landcover": 2,
              "system:index": "147"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538055334618868, 9.772571773657894]),
            {
              "landcover": 2,
              "system:index": "148"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538055334618868, 9.77054172212945]),
            {
              "landcover": 2,
              "system:index": "149"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53822699599582, 9.768511658215099]),
            {
              "landcover": 2,
              "system:index": "150"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538570318749727, 9.76698910215254]),
            {
              "landcover": 2,
              "system:index": "151"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.539600287011446, 9.765974060908194]),
            {
              "landcover": 2,
              "system:index": "152"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53822699599582, 9.765297365025766]),
            {
              "landcover": 2,
              "system:index": "153"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.535308752587618, 9.770034207311948]),
            {
              "landcover": 2,
              "system:index": "154"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53376380019504, 9.772064261937096]),
            {
              "landcover": 2,
              "system:index": "155"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531703863671602, 9.77240260317031]),
            {
              "landcover": 2,
              "system:index": "156"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.533420477441133, 9.771049236172841]),
            {
              "landcover": 2,
              "system:index": "157"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.533420477441133, 9.769865035534101]),
            {
              "landcover": 2,
              "system:index": "158"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53548041396457, 9.768680830680962]),
            {
              "landcover": 2,
              "system:index": "159"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.536167059472383, 9.76698910215254]),
            {
              "landcover": 2,
              "system:index": "160"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.536853704980196, 9.765297365025766]),
            {
              "landcover": 2,
              "system:index": "161"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.536853704980196, 9.763943969134523]),
            {
              "landcover": 2,
              "system:index": "162"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.497199926904024, 9.76326726912586]),
            {
              "landcover": 2,
              "system:index": "163"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.495654974511446, 9.764451493238456]),
            {
              "landcover": 2,
              "system:index": "164"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.49702826552707, 9.763098093908816]),
            {
              "landcover": 2,
              "system:index": "165"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.49754324965793, 9.76242139218114]),
            {
              "landcover": 2,
              "system:index": "166"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.496341620019258, 9.76242139218114]),
            {
              "landcover": 2,
              "system:index": "167"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.55745307021457, 9.72384712346435]),
            {
              "landcover": 2,
              "system:index": "168"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.558139715722383, 9.722324363538974]),
            {
              "landcover": 2,
              "system:index": "169"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.560542974999727, 9.721139989914178]),
            {
              "landcover": 2,
              "system:index": "170"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.559856329491915, 9.718432834451587]),
            {
              "landcover": 2,
              "system:index": "171"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.560886297753633, 9.717079248504964]),
            {
              "landcover": 2,
              "system:index": "172"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.562087927392305, 9.719786414921563]),
            {
              "landcover": 2,
              "system:index": "173"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.564319525292696, 9.720632399933873]),
            {
              "landcover": 2,
              "system:index": "174"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.56346121840793, 9.71826363650775]),
            {
              "landcover": 2,
              "system:index": "175"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.566379461816133, 9.72080159667957]),
            {
              "landcover": 2,
              "system:index": "176"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.566036139062227, 9.717756042162808]),
            {
              "landcover": 2,
              "system:index": "177"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.567237768700899, 9.718771230082542]),
            {
              "landcover": 2,
              "system:index": "178"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.569641027978243, 9.722324363538974]),
            {
              "landcover": 2,
              "system:index": "179"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.573245916894258, 9.724693098204092]),
            {
              "landcover": 2,
              "system:index": "180"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.57170096450168, 9.72012480918325]),
            {
              "landcover": 2,
              "system:index": "181"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.570156012109102, 9.717756042162808]),
            {
              "landcover": 2,
              "system:index": "182"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.571357641747774, 9.716402453478146]),
            {
              "landcover": 2,
              "system:index": "183"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.575134192040743, 9.719109625371203]),
            {
              "landcover": 2,
              "system:index": "184"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.575305853417696, 9.72080159667957]),
            {
              "landcover": 2,
              "system:index": "185"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.576507483056368, 9.717586843876692]),
            {
              "landcover": 2,
              "system:index": "186"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.574619207909883, 9.71741764550502]),
            {
              "landcover": 2,
              "system:index": "187"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.573245916894258, 9.71741764550502]),
            {
              "landcover": 2,
              "system:index": "188"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54372016005832, 9.70574275130077]),
            {
              "landcover": 2,
              "system:index": "189"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.548183355859102, 9.703712293368184]),
            {
              "landcover": 2,
              "system:index": "190"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.547840033105196, 9.70692717941152]),
            {
              "landcover": 2,
              "system:index": "191"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.545780096581758, 9.708280806409537]),
            {
              "landcover": 2,
              "system:index": "192"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.546295080712618, 9.703881498665897]),
            {
              "landcover": 2,
              "system:index": "193"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54200354628879, 9.70692717941152]),
            {
              "landcover": 2,
              "system:index": "194"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54200354628879, 9.710311236647977]),
            {
              "landcover": 2,
              "system:index": "195"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.54200354628879, 9.712172453550373]),
            {
              "landcover": 2,
              "system:index": "196"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.540801916650118, 9.715048859317944]),
            {
              "landcover": 2,
              "system:index": "197"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53822699599582, 9.715218058887388]),
            {
              "landcover": 2,
              "system:index": "198"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.537197027734102, 9.717586843876692]),
            {
              "landcover": 2,
              "system:index": "199"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.535308752587618, 9.715048859317944]),
            {
              "landcover": 2,
              "system:index": "200"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.535823736718477, 9.711834051246822]),
            {
              "landcover": 2,
              "system:index": "201"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.538570318749727, 9.713864459936698]),
            {
              "landcover": 2,
              "system:index": "202"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.53651038222629, 9.710142034598336]),
            {
              "landcover": 2,
              "system:index": "203"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.540630255273165, 9.707434790176865]),
            {
              "landcover": 2,
              "system:index": "204"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.531188879540743, 9.717586843876692]),
            {
              "landcover": 2,
              "system:index": "205"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.530330572655977, 9.72130918640309]),
            {
              "landcover": 2,
              "system:index": "206"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.529815588525118, 9.723001146584146]),
            {
              "landcover": 2,
              "system:index": "207"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.527583990624727, 9.724693098204092]),
            {
              "landcover": 2,
              "system:index": "208"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526725683739961, 9.725200682020445]),
            {
              "landcover": 2,
              "system:index": "209"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526554022363008, 9.722324363538974]),
            {
              "landcover": 2,
              "system:index": "210"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.528098974755586, 9.721647579124117]),
            {
              "landcover": 2,
              "system:index": "211"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.526897345116915, 9.720970793339673]),
            {
              "landcover": 2,
              "system:index": "212"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52174750380832, 9.726046653335084]),
            {
              "landcover": 2,
              "system:index": "213"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52277747207004, 9.727738589541413]),
            {
              "landcover": 2,
              "system:index": "214"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.52277747207004, 9.730276477790866]),
            {
              "landcover": 2,
              "system:index": "215"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.521404181054415, 9.732137583589529]),
            {
              "landcover": 2,
              "system:index": "216"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.517970953515352, 9.733321918244974]),
            {
              "landcover": 2,
              "system:index": "217"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.517970953515352, 9.731799201488183]),
            {
              "landcover": 2,
              "system:index": "218"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.519859228661836, 9.732137583589529]),
            {
              "landcover": 2,
              "system:index": "219"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.50852957778293, 9.740766211334252]),
            {
              "landcover": 2,
              "system:index": "220"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.509731207421602, 9.737213273972818]),
            {
              "landcover": 2,
              "system:index": "221"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.510246191552461, 9.736198142067588]),
            {
              "landcover": 2,
              "system:index": "222"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.511447821191133, 9.737720838768078]),
            {
              "landcover": 2,
              "system:index": "223"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.51453772597629, 9.737720838768078]),
            {
              "landcover": 2,
              "system:index": "224"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.51076117568332, 9.741950515384083]),
            {
              "landcover": 2,
              "system:index": "225"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.50028983168918, 9.754808403012264]),
            {
              "landcover": 2,
              "system:index": "226"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.497714911034883, 9.756500193416775]),
            {
              "landcover": 2,
              "system:index": "227"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.495483313134493, 9.758530330563973]),
            {
              "landcover": 2,
              "system:index": "228"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.501148138573946, 9.752947423648195]),
            {
              "landcover": 2,
              "system:index": "229"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.501834784081758, 9.749563798187735]),
            {
              "landcover": 2,
              "system:index": "230"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.507842932275118, 9.74770278954872]),
            {
              "landcover": 2,
              "system:index": "231"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.509216223290743, 9.749056251407033]),
            {
              "landcover": 2,
              "system:index": "232"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.510417852929415, 9.747533606430212]),
            {
              "landcover": 2,
              "system:index": "233"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.508872900536836, 9.747364423225903]),
            {
              "landcover": 2,
              "system:index": "234"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661651526025118, 10.022341913400517]),
            {
              "landcover": 2,
              "system:index": "235"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.660964880517305, 10.028765438852059]),
            {
              "landcover": 2,
              "system:index": "236"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661308203271211, 10.020989576032427]),
            {
              "landcover": 2,
              "system:index": "237"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658561621239961, 10.020989576032427]),
            {
              "landcover": 2,
              "system:index": "238"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655471716454805, 10.024370408875624]),
            {
              "landcover": 2,
              "system:index": "239"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.652038488915743, 10.024370408875624]),
            {
              "landcover": 2,
              "system:index": "240"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655471716454805, 10.020989576032427]),
            {
              "landcover": 2,
              "system:index": "241"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.652725134423555, 10.018284884376252]),
            {
              "landcover": 2,
              "system:index": "242"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658904943993868, 10.012537339724123]),
            {
              "landcover": 2,
              "system:index": "243"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655471716454805, 10.009156383550605]),
            {
              "landcover": 2,
              "system:index": "244"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658218298486055, 10.00780399122132]),
            {
              "landcover": 2,
              "system:index": "245"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.654441748193086, 10.005775392165521]),
            {
              "landcover": 2,
              "system:index": "246"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.656501684716524, 10.003408677251185]),
            {
              "landcover": 2,
              "system:index": "247"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.65409842543918, 10.00239436558026]),
            {
              "landcover": 2,
              "system:index": "248"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.657874975732149, 10.000365732737786]),
            {
              "landcover": 2,
              "system:index": "249"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655471716454805, 9.999689518975616]),
            {
              "landcover": 2,
              "system:index": "250"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.645515356591524, 10.003070573712783]),
            {
              "landcover": 2,
              "system:index": "251"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.645172033837618, 10.000703839091145]),
            {
              "landcover": 2,
              "system:index": "252"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643798742821993, 9.999689518975616]),
            {
              "landcover": 2,
              "system:index": "253"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.668517981103243, 9.988193669793844]),
            {
              "landcover": 2,
              "system:index": "254"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.669204626611055, 9.984136214247286]),
            {
              "landcover": 2,
              "system:index": "255"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.669204626611055, 9.981093089391116]),
            {
              "landcover": 2,
              "system:index": "256"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.669204626611055, 9.976697414383944]),
            {
              "landcover": 2,
              "system:index": "257"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666458044579805, 9.974330487883972]),
            {
              "landcover": 2,
              "system:index": "258"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66508475356418, 9.973316085548204]),
            {
              "landcover": 2,
              "system:index": "259"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666458044579805, 9.969596583299666]),
            {
              "landcover": 2,
              "system:index": "260"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.669204626611055, 9.966553322616255]),
            {
              "landcover": 2,
              "system:index": "261"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.671951208642305, 9.962833743207232]),
            {
              "landcover": 2,
              "system:index": "262"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.676757727196993, 9.961143011271028]),
            {
              "landcover": 2,
              "system:index": "263"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.681907568505586, 9.960128567903281]),
            {
              "landcover": 2,
              "system:index": "264"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.68431082778293, 9.956408915238322]),
            {
              "landcover": 2,
              "system:index": "265"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.683624182275118, 9.952689220182753]),
            {
              "landcover": 2,
              "system:index": "266"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.682937536767305, 9.949307642450698]),
            {
              "landcover": 2,
              "system:index": "267"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.676414404443086, 9.958099671705611]),
            {
              "landcover": 2,
              "system:index": "268"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.671951208642305, 9.960128567903281]),
            {
              "landcover": 2,
              "system:index": "269"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.668174658349336, 9.96046671604301]),
            {
              "landcover": 2,
              "system:index": "270"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.667584617106092, 9.953089708729708]),
            {
              "landcover": 2,
              "system:index": "271"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.667241294352186, 9.951145308196883]),
            {
              "landcover": 2,
              "system:index": "272"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.667241294352186, 9.950215373414666]),
            {
              "landcover": 2,
              "system:index": "273"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666468818155897, 9.945734741445749]),
            {
              "landcover": 2,
              "system:index": "274"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666726310221327, 9.944551168024388]),
            {
              "landcover": 2,
              "system:index": "275"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666726310221327, 9.942691258273008]),
            {
              "landcover": 2,
              "system:index": "276"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.665696341959608, 9.940746795853128]),
            {
              "landcover": 2,
              "system:index": "277"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.664580543009412, 9.938633236626876]),
            {
              "landcover": 2,
              "system:index": "278"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.662434775797498, 9.938633236626876]),
            {
              "landcover": 2,
              "system:index": "279"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661748130289686, 9.93990137380219]),
            {
              "landcover": 2,
              "system:index": "280"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.662692267862928, 9.942860341415056]),
            {
              "landcover": 2,
              "system:index": "281"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66440888163246, 9.944466626901695]),
            {
              "landcover": 2,
              "system:index": "282"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.664494712320936, 9.946326526548747]),
            {
              "landcover": 2,
              "system:index": "283"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6638938975016, 9.947848254748799]),
            {
              "landcover": 2,
              "system:index": "284"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.662434775797498, 9.947763714479182]),
            {
              "landcover": 2,
              "system:index": "285"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661919791666639, 9.946411067190247]),
            {
              "landcover": 2,
              "system:index": "286"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66088982340492, 9.944889332296516]),
            {
              "landcover": 2,
              "system:index": "287"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66088982340492, 9.942860341415056]),
            {
              "landcover": 2,
              "system:index": "288"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659945685831678, 9.947256472402119]),
            {
              "landcover": 2,
              "system:index": "289"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659173209635389, 9.94962359535643]),
            {
              "landcover": 2,
              "system:index": "290"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6584007334391, 9.95199070115553]),
            {
              "landcover": 2,
              "system:index": "291"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.657542426554334, 9.950722610896857]),
            {
              "landcover": 2,
              "system:index": "292"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.653680045572889, 9.949454515714292]),
            {
              "landcover": 2,
              "system:index": "293"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.653250892130506, 9.950553531823656]),
            {
              "landcover": 2,
              "system:index": "294"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.657027442423475, 9.95833107856939]),
            {
              "landcover": 2,
              "system:index": "295"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658057410685194, 9.960867195046598]),
            {
              "landcover": 2,
              "system:index": "296"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658572394816053, 9.96272700126694]),
            {
              "landcover": 2,
              "system:index": "297"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659001548258436, 9.965263083568694]),
            {
              "landcover": 2,
              "system:index": "298"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659173209635389, 9.966953794146162]),
            {
              "landcover": 2,
              "system:index": "299"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.660117347208631, 9.96500947622598]),
            {
              "landcover": 2,
              "system:index": "300"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.660203177897108, 9.963403291808957]),
            {
              "landcover": 2,
              "system:index": "301"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661061484781873, 9.961036268777496]),
            {
              "landcover": 2,
              "system:index": "302"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661061484781873, 9.959937287960484]),
            {
              "landcover": 2,
              "system:index": "303"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.661748130289686, 9.958246541014008]),
            {
              "landcover": 2,
              "system:index": "304"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.660289008585584, 9.959260990233174]),
            {
              "landcover": 2,
              "system:index": "305"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659602363077772, 9.96230431896613]),
            {
              "landcover": 2,
              "system:index": "306"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.663293082682264, 9.966192975471168]),
            {
              "landcover": 2,
              "system:index": "307"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.663550574747694, 9.964755868686034]),
            {
              "landcover": 2,
              "system:index": "308"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66440888163246, 9.963656900400698]),
            {
              "landcover": 2,
              "system:index": "309"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.665181357828748, 9.962135245892433]),
            {
              "landcover": 2,
              "system:index": "310"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.666039664713514, 9.960613584285971]),
            {
              "landcover": 2,
              "system:index": "311"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.660718162027967, 9.973970149337196]),
            {
              "landcover": 2,
              "system:index": "312"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.660289008585584, 9.972110407252433]),
            {
              "landcover": 2,
              "system:index": "313"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659516532389295, 9.970842395200114]),
            {
              "landcover": 2,
              "system:index": "314"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.658057410685194, 9.969658912833557]),
            {
              "landcover": 2,
              "system:index": "315"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655825812784803, 9.968475426169892]),
            {
              "landcover": 2,
              "system:index": "316"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.655482490030897, 9.96982798200615]),
            {
              "landcover": 2,
              "system:index": "317"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.653851706949842, 9.972448542966447]),
            {
              "landcover": 2,
              "system:index": "318"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.653079230753553, 9.973801082313564]),
            {
              "landcover": 2,
              "system:index": "319"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.649560172526014, 9.973209347040036]),
            {
              "landcover": 2,
              "system:index": "320"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.649731833902967, 9.971434134771844]),
            {
              "landcover": 2,
              "system:index": "321"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.649216849772108, 9.970081585600642]),
            {
              "landcover": 2,
              "system:index": "322"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.647843558756483, 9.968559961074066]),
            {
              "landcover": 2,
              "system:index": "323"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.645783622233045, 9.967122864721723]),
            {
              "landcover": 2,
              "system:index": "324"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643466193644178, 9.965516690714173]),
            {
              "landcover": 2,
              "system:index": "325"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.638058860270155, 9.969320774225237]),
            {
              "landcover": 2,
              "system:index": "326"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.635226447550428, 9.969405308910208]),
            {
              "landcover": 2,
              "system:index": "327"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.634110648600233, 9.970673326553726]),
            {
              "landcover": 2,
              "system:index": "328"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631106574503553, 9.969912516559571]),
            {
              "landcover": 2,
              "system:index": "329"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.629990775553358, 9.967122864721723]),
            {
              "landcover": 2,
              "system:index": "330"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63891716715492, 9.973547481613643]),
            {
              "landcover": 2,
              "system:index": "331"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.642522056070936, 9.972617610691863]),
            {
              "landcover": 2,
              "system:index": "332"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.645783622233045, 9.97498454963648]),
            {
              "landcover": 2,
              "system:index": "333"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643981177775037, 9.977351471383914]),
            {
              "landcover": 2,
              "system:index": "334"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643981177775037, 9.979380247762634]),
            {
              "landcover": 2,
              "system:index": "335"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.644753653971327, 9.980310099378729]),
            {
              "landcover": 2,
              "system:index": "336"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.648272712198866, 9.979887439882406]),
            {
              "landcover": 2,
              "system:index": "337"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.650075156656873, 9.982000731877168]),
            {
              "landcover": 2,
              "system:index": "338"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.65067597147621, 9.979549311890345]),
            {
              "landcover": 2,
              "system:index": "339"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.649302680460584, 9.977266938760529]),
            {
              "landcover": 2,
              "system:index": "340"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.641062934366834, 9.979887439882406]),
            {
              "landcover": 2,
              "system:index": "341"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.640462119547498, 9.982761513637067]),
            {
              "landcover": 2,
              "system:index": "342"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.638144690958631, 9.979718375930274]),
            {
              "landcover": 2,
              "system:index": "343"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.634797294108045, 9.975829880806362]),
            {
              "landcover": 2,
              "system:index": "344"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.646212775675428, 9.98783334659046]),
            {
              "landcover": 2,
              "system:index": "345"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.646212775675428, 9.99020017491354]),
            {
              "landcover": 2,
              "system:index": "346"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.648530204264295, 9.991045466569636]),
            {
              "landcover": 2,
              "system:index": "347"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.651105124918592, 9.992482457343009]),
            {
              "landcover": 2,
              "system:index": "348"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.64715691324867, 9.994173026593714]),
            {
              "landcover": 2,
              "system:index": "349"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643466193644178, 9.99518736392491]),
            {
              "landcover": 2,
              "system:index": "350"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.642607886759412, 9.98741069686363]),
            {
              "landcover": 2,
              "system:index": "351"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.646727759806287, 9.986480865532018]),
            {
              "landcover": 2,
              "system:index": "352"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.64964600321449, 9.99036923342051]),
            {
              "landcover": 2,
              "system:index": "353"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.657370765177381, 9.981916200460754]),
            {
              "landcover": 2,
              "system:index": "354"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.654624183146131, 9.980732758326381]),
            {
              "landcover": 2,
              "system:index": "355"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.652821738688123, 9.979295715665872]),
            {
              "landcover": 2,
              "system:index": "356"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.653250892130506, 9.984283071822539]),
            {
              "landcover": 2,
              "system:index": "357"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.648186881510389, 9.975153616045933]),
            {
              "landcover": 2,
              "system:index": "358"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.646384437052381, 9.973124813341814]),
            {
              "landcover": 2,
              "system:index": "359"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.643380362955702, 9.97278667832957]),
            {
              "landcover": 2,
              "system:index": "360"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.641320426432264, 9.970081585600642]),
            {
              "landcover": 2,
              "system:index": "361"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.639775474039686, 9.973040279621646]),
            {
              "landcover": 2,
              "system:index": "362"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.640290458170545, 9.976421611320037]),
            {
              "landcover": 2,
              "system:index": "363"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.640118796793592, 9.977943199133255]),
            {
              "landcover": 2,
              "system:index": "364"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.637114722696912, 9.976337078455325]),
            {
              "landcover": 2,
              "system:index": "365"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.636256415812147, 9.974477349881646]),
            {
              "landcover": 2,
              "system:index": "366"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63617058512367, 9.973378414370707]),
            {
              "landcover": 2,
              "system:index": "367"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6364280771891, 9.971856805236678]),
            {
              "landcover": 2,
              "system:index": "368"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.636256415812147, 9.969658912833557]),
            {
              "landcover": 2,
              "system:index": "369"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.636256415812147, 9.9673764704207]),
            {
              "landcover": 2,
              "system:index": "370"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.634453971354139, 9.968306356295757]),
            {
              "landcover": 2,
              "system:index": "371"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631879050699842, 9.968052751320142]),
            {
              "landcover": 2,
              "system:index": "372"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631020743815077, 9.966784723482908]),
            {
              "landcover": 2,
              "system:index": "373"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.629132468668592, 9.96500947622598]),
            {
              "landcover": 2,
              "system:index": "374"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.627244193522108, 9.962642464850603]),
            {
              "landcover": 2,
              "system:index": "375"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.626385886637342, 9.960698121228079]),
            {
              "landcover": 2,
              "system:index": "376"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.624411780802381, 9.958415616102878]),
            {
              "landcover": 2,
              "system:index": "377"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.624240119425428, 9.961036268777496]),
            {
              "landcover": 2,
              "system:index": "378"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625270087687147, 9.962811537661368]),
            {
              "landcover": 2,
              "system:index": "379"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.627587516276014, 9.966869258825502]),
            {
              "landcover": 2,
              "system:index": "380"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.626643378702772, 9.966108439953251]),
            {
              "landcover": 2,
              "system:index": "381"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.624583442179334, 9.965770297662408]),
            {
              "landcover": 2,
              "system:index": "382"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.62321015116371, 9.964671332795572]),
            {
              "landcover": 2,
              "system:index": "383"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.621751029459608, 9.9651785478097]),
            {
              "landcover": 2,
              "system:index": "384"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.618575293985975, 9.965770297662408]),
            {
              "landcover": 2,
              "system:index": "385"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.619776923624647, 9.9650940120288]),
            {
              "landcover": 2,
              "system:index": "386"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.62818833109535, 9.97134960061309]),
            {
              "landcover": 2,
              "system:index": "387"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.628359992472303, 9.96957437821436]),
            {
              "landcover": 2,
              "system:index": "388"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.633252341715467, 9.975407215495617]),
            {
              "landcover": 2,
              "system:index": "389"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.63316651102699, 9.973378414370707]),
            {
              "landcover": 2,
              "system:index": "390"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631621558634412, 9.976844275314518]),
            {
              "landcover": 2,
              "system:index": "391"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.637887198893202, 9.984283071822539]),
            {
              "landcover": 2,
              "system:index": "392"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.6364280771891, 9.986058214048352]),
            {
              "landcover": 2,
              "system:index": "393"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.637715537516248, 9.98369135559561]),
            {
              "landcover": 2,
              "system:index": "394"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.640719611612928, 9.98250791991466]),
            {
              "landcover": 2,
              "system:index": "395"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.642007071940077, 9.982846044833973]),
            {
              "landcover": 2,
              "system:index": "396"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.642779548136366, 9.98090182175181]),
            {
              "landcover": 2,
              "system:index": "397"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.659945685831678, 9.970250654554006]),
            {
              "landcover": 2,
              "system:index": "398"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66415138956703, 9.970504257819616]),
            {
              "landcover": 2,
              "system:index": "399"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.665782172648084, 9.967630075922393]),
            {
              "landcover": 2,
              "system:index": "400"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.667756278483045, 9.96923623951836]),
            {
              "landcover": 2,
              "system:index": "401"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.66887207743324, 9.97253307684012]),
            {
              "landcover": 2,
              "system:index": "402"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.679171760050428, 9.97718240611521]),
            {
              "landcover": 2,
              "system:index": "403"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.683978278605116, 9.976506144162817]),
            {
              "landcover": 2,
              "system:index": "404"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.685179908243787, 9.973970149337196]),
            {
              "landcover": 2,
              "system:index": "405"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.688527305094373, 9.97523814921776]),
            {
              "landcover": 2,
              "system:index": "406"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.692303855387342, 9.97413921627307]),
            {
              "landcover": 2,
              "system:index": "407"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.691531379191053, 9.971603203023564]),
            {
              "landcover": 2,
              "system:index": "408"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.689385611979139, 9.970250654554006]),
            {
              "landcover": 2,
              "system:index": "409"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.686209876505506, 9.970081585600642]),
            {
              "landcover": 2,
              "system:index": "410"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.687668998209608, 9.969151704789562]),
            {
              "landcover": 2,
              "system:index": "411"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.688441474405897, 9.96813728633393]),
            {
              "landcover": 2,
              "system:index": "412"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.691016395060194, 9.96881356565509]),
            {
              "landcover": 2,
              "system:index": "413"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.608361442057264, 9.874374531391176]),
            {
              "landcover": 2,
              "system:index": "414"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.607245643107069, 9.871584065858906]),
            {
              "landcover": 2,
              "system:index": "415"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.607331473795545, 9.869892863116872]),
            {
              "landcover": 2,
              "system:index": "416"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.605014045206678, 9.869723742364956]),
            {
              "landcover": 2,
              "system:index": "417"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.60321160074867, 9.87090758580443]),
            {
              "landcover": 2,
              "system:index": "418"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.60398407694496, 9.869554621526174]),
            {
              "landcover": 2,
              "system:index": "419"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.598147590128553, 9.86811709089016]),
            {
              "landcover": 2,
              "system:index": "420"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.596259314982069, 9.86777884747573]),
            {
              "landcover": 2,
              "system:index": "421"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.576775748697889, 9.853826004088361]),
            {
              "landcover": 2,
              "system:index": "422"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.576861579386366, 9.851627320370765]),
            {
              "landcover": 2,
              "system:index": "423"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.578578193155897, 9.84883666224464]),
            {
              "landcover": 2,
              "system:index": "424"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.576432425943983, 9.849259490750422]),
            {
              "landcover": 2,
              "system:index": "425"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.575659949747694, 9.849174925092612]),
            {
              "landcover": 2,
              "system:index": "426"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.585530478922498, 9.841225656527765]),
            {
              "landcover": 2,
              "system:index": "427"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.586302955118787, 9.839872570479478]),
            {
              "landcover": 2,
              "system:index": "428"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.584157187906873, 9.83995713851988]),
            {
              "landcover": 2,
              "system:index": "429"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.630505759684217, 9.831669367685807]),
            {
              "landcover": 2,
              "system:index": "430"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.631879050699842, 9.833699045065439]),
            {
              "landcover": 2,
              "system:index": "431"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.574458857821856, 9.69531181961584]),
            {
              "landcover": 2,
              "system:index": "432"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.57737710123006, 9.69565023860672]),
            {
              "landcover": 2,
              "system:index": "433"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.578578730868731, 9.697849953722374]),
            {
              "landcover": 2,
              "system:index": "434"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.581325312899981, 9.701403309189935]),
            {
              "landcover": 2,
              "system:index": "435"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.58287026529256, 9.704449012462995]),
            {
              "landcover": 2,
              "system:index": "436"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.58458687906209, 9.704956626983607]),
            {
              "landcover": 2,
              "system:index": "437"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.584758540439044, 9.702756958506706]),
            {
              "landcover": 2,
              "system:index": "438"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.58458687906209, 9.701234102640901]),
            {
              "landcover": 2,
              "system:index": "439"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.582698603915606, 9.701234102640901]),
            {
              "landcover": 2,
              "system:index": "440"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.579437037753497, 9.698188370151598]),
            {
              "landcover": 2,
              "system:index": "441"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.578750392245684, 9.695988657256075]),
            {
              "landcover": 2,
              "system:index": "442"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.578063746737872, 9.694634980609585]),
            {
              "landcover": 2,
              "system:index": "443"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.575660487460528, 9.694634980609585]),
            {
              "landcover": 2,
              "system:index": "444"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.573085566806231, 9.694973400283457]),
            {
              "landcover": 2,
              "system:index": "445"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.56810738687459, 9.692604455395546]),
            {
              "landcover": 2,
              "system:index": "446"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.56639077310506, 9.693112087851434]),
            {
              "landcover": 2,
              "system:index": "447"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.56639077310506, 9.692096822171477]),
            {
              "landcover": 2,
              "system:index": "448"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.579780360507403, 9.686005163578422]),
            {
              "landcover": 2,
              "system:index": "449"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.582526942538653, 9.69192761092609]),
            {
              "landcover": 2,
              "system:index": "450"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.583556910800372, 9.693619719539091]),
            {
              "landcover": 2,
              "system:index": "451"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.59282662515584, 9.676529030508604]),
            {
              "landcover": 2,
              "system:index": "452"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.597461482333575, 9.67686746843577]),
            {
              "landcover": 2,
              "system:index": "453"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.5988347733492, 9.68075948009447]),
            {
              "landcover": 2,
              "system:index": "454"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.601409694003497, 9.680251828957084]),
            {
              "landcover": 2,
              "system:index": "455"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.603126307773028, 9.67483683575991]),
            {
              "landcover": 2,
              "system:index": "456"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.601924678134356, 9.671452420702959]),
            {
              "landcover": 2,
              "system:index": "457"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.602439662265216, 9.669083309890828]),
            {
              "landcover": 2,
              "system:index": "458"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.605529567050372, 9.668237194841453]),
            {
              "landcover": 2,
              "system:index": "459"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.606731196689044, 9.665868061379152]),
            {
              "landcover": 2,
              "system:index": "460"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.60209633951131, 9.664683488390903]),
            {
              "landcover": 2,
              "system:index": "461"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.592483302401934, 9.665021938241727]),
            {
              "landcover": 2,
              "system:index": "462"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.583385249423419, 9.667391077663392]),
            {
              "landcover": 2,
              "system:index": "463"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.582183619784747, 9.672467748797905]),
            {
              "landcover": 2,
              "system:index": "464"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.576690455722247, 9.673990735190353]),
            {
              "landcover": 2,
              "system:index": "465"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.571025630282794, 9.68363615537873]),
            {
              "landcover": 2,
              "system:index": "466"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.570682307528887, 9.687528088592995]),
            {
              "landcover": 2,
              "system:index": "467"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.570338984774981, 9.69192761092609]),
            {
              "landcover": 2,
              "system:index": "468"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.566905757235919, 9.691081553418952]),
            {
              "landcover": 2,
              "system:index": "469"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.56261422281209, 9.691081553418952]),
            {
              "landcover": 2,
              "system:index": "470"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.560554286288653, 9.69565023860672]),
            {
              "landcover": 2,
              "system:index": "471"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.9981272866448, 10.157269797971763]),
            {
              "landcover": 2,
              "system:index": "472"
            }),
        ee.Feature(
            ee.Geometry.Point([-14.0475657632073, 10.1680837588802]),
            {
              "landcover": 2,
              "system:index": "473"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.86903793117605, 10.008879012049832]),
            {
              "landcover": 2,
              "system:index": "474"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.863888089867457, 10.008879012049832]),
            {
              "landcover": 2,
              "system:index": "475"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.865261380883082, 10.010231399900807]),
            {
              "landcover": 2,
              "system:index": "476"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.868351285668238, 10.008879012049832]),
            {
              "landcover": 2,
              "system:index": "477"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.877621000023707, 10.01225997111249]),
            {
              "landcover": 2,
              "system:index": "478"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.873157804222926, 10.0048218146976]),
            {
              "landcover": 2,
              "system:index": "479"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.874874417992457, 9.997721597385633]),
            {
              "landcover": 2,
              "system:index": "480"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.876591031761988, 9.994002374025342]),
            {
              "landcover": 2,
              "system:index": "481"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.8662913491448, 9.992988032997298]),
            {
              "landcover": 2,
              "system:index": "482"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.862858121605738, 9.998059706490045]),
            {
              "landcover": 2,
              "system:index": "483"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.86457473537527, 9.984873190890044]),
            {
              "landcover": 2,
              "system:index": "484"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.869724576683863, 9.975743751659701]),
            {
              "landcover": 2,
              "system:index": "485"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.877621000023707, 9.97540561936557]),
            {
              "landcover": 2,
              "system:index": "486"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.875904386254176, 9.982168198547233]),
            {
              "landcover": 2,
              "system:index": "487"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.88105422756277, 9.982844448740403]),
            {
              "landcover": 2,
              "system:index": "488"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.886204068871363, 9.981830072923847]),
            {
              "landcover": 2,
              "system:index": "489"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.890667264672144, 9.988592518649739]),
            {
              "landcover": 2,
              "system:index": "490"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.89478713771902, 9.987578160749882]),
            {
              "landcover": 2,
              "system:index": "491"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.893413846703394, 9.994340486998162]),
            {
              "landcover": 2,
              "system:index": "492"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.893413846703394, 10.0011026726001]),
            {
              "landcover": 2,
              "system:index": "493"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.897877042504176, 9.998059706490045]),
            {
              "landcover": 2,
              "system:index": "494"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.90028030178152, 9.995354823806883]),
            {
              "landcover": 2,
              "system:index": "495"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.8992503335198, 10.005498017776539]),
            {
              "landcover": 2,
              "system:index": "496"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.878994291039332, 9.992988032997298]),
            {
              "landcover": 2,
              "system:index": "497"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.896160428734644, 10.014964713003298]),
            {
              "landcover": 2,
              "system:index": "498"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.90199691555105, 10.01834560865809]),
            {
              "landcover": 2,
              "system:index": "499"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.5434608508915, 9.634974841301608],
                  [-13.545349126037985, 9.632266991548065],
                  [-13.54174423712197, 9.632436232794046]]]),
            {
              "landcover": 2,
              "system:index": "500"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.483379368957907, 9.632436232794046],
                  [-13.484924321350485, 9.629897605196554],
                  [-13.48131943243447, 9.629389877386695]]]),
            {
              "landcover": 2,
              "system:index": "501"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.435829167541891, 9.591646642167026],
                  [-13.433940892395407, 9.586568755869056],
                  [-13.431537633118063, 9.589446234106036]]]),
            {
              "landcover": 2,
              "system:index": "502"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.438919072327048, 9.66560587720521],
                  [-13.439777379211813, 9.662559821578215],
                  [-13.435657506164938, 9.664590528393632]]]),
            {
              "landcover": 2,
              "system:index": "503"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.52801132696572, 9.802649707720889],
                  [-13.531272893127829, 9.798420802628165],
                  [-13.525608067688376, 9.799266587959883]]]),
            {
              "landcover": 2,
              "system:index": "504"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.700941293708981, 9.913100953593409]),
            {
              "landcover": 2,
              "system:index": "505"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.703344552986325, 9.910057166995815]),
            {
              "landcover": 2,
              "system:index": "506"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.707636087410153, 9.905660536482868]),
            {
              "landcover": 2,
              "system:index": "507"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.709009378425778, 9.902109368825391]),
            {
              "landcover": 2,
              "system:index": "508"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.710725992195309, 9.897543525381757]),
            {
              "landcover": 2,
              "system:index": "509"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.712099283210934, 9.892977618451745]),
            {
              "landcover": 2,
              "system:index": "510"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.713300912849606, 9.889426313632375]),
            {
              "landcover": 2,
              "system:index": "511"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.715532510749997, 9.885198519765332]),
            {
              "landcover": 2,
              "system:index": "512"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.717420785896481, 9.88249270315871]),
            {
              "landcover": 2,
              "system:index": "513"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.720854013435543, 9.877926587157914]),
            {
              "landcover": 2,
              "system:index": "514"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.724802225105465, 9.873360407791562]),
            {
              "landcover": 2,
              "system:index": "515"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.678281991951168, 9.891962963848515]),
            {
              "landcover": 2,
              "system:index": "516"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.626096933357418, 9.910902666107052]),
            {
              "landcover": 2,
              "system:index": "517"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625581949226559, 9.908873464578067]),
            {
              "landcover": 2,
              "system:index": "518"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625581949226559, 9.906167843010932]),
            {
              "landcover": 2,
              "system:index": "519"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.625581949226559, 9.903462199130923]),
            {
              "landcover": 2,
              "system:index": "520"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.626611917488278, 9.90177116037774]),
            {
              "landcover": 2,
              "system:index": "521"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.621633737556637, 9.913946444855837]),
            {
              "landcover": 2,
              "system:index": "522"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.621633737556637, 9.91242455901354]),
            {
              "landcover": 2,
              "system:index": "523"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.747289865486325, 9.918850251170033]),
            {
              "landcover": 2,
              "system:index": "524"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.748319833748043, 9.916821098835793]),
            {
              "landcover": 2,
              "system:index": "525"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.749349802009762, 9.91360824861252]),
            {
              "landcover": 2,
              "system:index": "526"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.751581399910153, 9.911071765667707]),
            {
              "landcover": 2,
              "system:index": "527"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.752611368171872, 9.909888066911998]),
            {
              "landcover": 2,
              "system:index": "528"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.759992807380856, 9.912086361200327]),
            {
              "landcover": 2,
              "system:index": "529"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.736818521492184, 9.893146727247624]),
            {
              "landcover": 2,
              "system:index": "530"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.731497018806637, 9.890948306111866]),
            {
              "landcover": 2,
              "system:index": "531"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.72669050025195, 9.889595424255967]),
            {
              "landcover": 2,
              "system:index": "532"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.719137399666012, 9.90109474243695]),
            {
              "landcover": 2,
              "system:index": "533"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.719824045173825, 9.906675148754557]),
            {
              "landcover": 2,
              "system:index": "534"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.723600595466793, 9.91360824861252]),
            {
              "landcover": 2,
              "system:index": "535"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.7294370822832, 9.920033917561932]),
            {
              "landcover": 2,
              "system:index": "536"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.730982034675778, 9.924599447866193]),
            {
              "landcover": 2,
              "system:index": "537"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.738878458015622, 9.914453738566584]),
            {
              "landcover": 2,
              "system:index": "538"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.744714944832028, 9.910902666107052]),
            {
              "landcover": 2,
              "system:index": "539"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.746774881355465, 9.905660536482868]),
            {
              "landcover": 2,
              "system:index": "540"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.747976510994137, 9.89889637450345]),
            {
              "landcover": 2,
              "system:index": "541"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.74265500830859, 9.895006918256664]),
            {
              "landcover": 2,
              "system:index": "542"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.741110055916012, 9.88722786760753]),
            {
              "landcover": 2,
              "system:index": "543"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.744543283455075, 9.889595424255967]),
            {
              "landcover": 2,
              "system:index": "544"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.774927347175778, 9.920710296437226]),
            {
              "landcover": 2,
              "system:index": "545"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.774927347175778, 9.914115542846634]),
            {
              "landcover": 2,
              "system:index": "546"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.775957315437497, 9.91191726216291]),
            {
              "landcover": 2,
              "system:index": "547"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.780420511238278, 9.91293185507927]),
            {
              "landcover": 2,
              "system:index": "548"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.783682077400387, 9.907182453713716]),
            {
              "landcover": 2,
              "system:index": "549"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.780420511238278, 9.906844250494784]),
            {
              "landcover": 2,
              "system:index": "550"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.775442331306637, 9.90971896674098]),
            {
              "landcover": 2,
              "system:index": "551"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.769090860359372, 9.9147919339376]),
            {
              "landcover": 2,
              "system:index": "552"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.764456003181637, 9.920203012411678]),
            {
              "landcover": 2,
              "system:index": "553"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.755014627449215, 9.921555768067503]),
            {
              "landcover": 2,
              "system:index": "554"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.747118204109372, 9.927135826088241]),
            {
              "landcover": 2,
              "system:index": "555"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.760507791511715, 9.930348543625744]),
            {
              "landcover": 2,
              "system:index": "556"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.794668405525387, 9.923415797972327]),
            {
              "landcover": 2,
              "system:index": "557"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.796213357917965, 9.917497484343334]),
            {
              "landcover": 2,
              "system:index": "558"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.794496744148434, 9.913439150360041]),
            {
              "landcover": 2,
              "system:index": "559"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.797071664802731, 9.905998740922067]),
            {
              "landcover": 2,
              "system:index": "560"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.801191537849606, 9.899572796973985]),
            {
              "landcover": 2,
              "system:index": "561"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.808057992927731, 9.910057166995815]),
            {
              "landcover": 2,
              "system:index": "562"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.799474924080075, 9.920033917561932]),
            {
              "landcover": 2,
              "system:index": "563"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.802736490242184, 9.92493763276433]),
            {
              "landcover": 2,
              "system:index": "564"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.804968088142575, 9.941339180848713]),
            {
              "landcover": 2,
              "system:index": "565"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.813551156990231, 9.93846474216451]),
            {
              "landcover": 2,
              "system:index": "566"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.817842691414059, 9.930517633148913]),
            {
              "landcover": 2,
              "system:index": "567"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.827627389900387, 9.920203012411678]),
            {
              "landcover": 2,
              "system:index": "568"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.823679178230465, 9.912762756477909]),
            {
              "landcover": 2,
              "system:index": "569"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.820932596199215, 9.90904256518501]),
            {
              "landcover": 2,
              "system:index": "570"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.822992532722653, 9.904138612192435]),
            {
              "landcover": 2,
              "system:index": "571"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.821619241707028, 9.900249218050838]),
            {
              "landcover": 2,
              "system:index": "572"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.825395791999997, 9.892470291541834]),
            {
              "landcover": 2,
              "system:index": "573"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.828657358162106, 9.887904314104395]),
            {
              "landcover": 2,
              "system:index": "574"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.835867135994137, 9.886213195252276]),
            {
              "landcover": 2,
              "system:index": "575"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.842218606941403, 9.894330486381278]),
            {
              "landcover": 2,
              "system:index": "576"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.846510141365231, 9.901263847052817]),
            {
              "landcover": 2,
              "system:index": "577"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.751238077156247, 9.897205312230422]),
            {
              "landcover": 2,
              "system:index": "578"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.751924722664059, 9.893484944578221]),
            {
              "landcover": 2,
              "system:index": "579"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.751753061287106, 9.890102755604609]),
            {
              "landcover": 2,
              "system:index": "580"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.749864786140622, 9.88773520261068]),
            {
              "landcover": 2,
              "system:index": "581"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.744199960701168, 9.885705857900248]),
            {
              "landcover": 2,
              "system:index": "582"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.743684976570309, 9.88249270315871]),
            {
              "landcover": 2,
              "system:index": "583"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.744886606208981, 9.878264820146166]),
            {
              "landcover": 2,
              "system:index": "584"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.735960214607418, 9.875220710736242]),
            {
              "landcover": 2,
              "system:index": "585"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.732698648445309, 9.874036882806081]),
            {
              "landcover": 2,
              "system:index": "586"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.755529611580075, 9.876742768961105]),
            {
              "landcover": 2,
              "system:index": "587"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.761537759773434, 9.874036882806081]),
            {
              "landcover": 2,
              "system:index": "588"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.765657632820309, 9.870147132490299]),
            {
              "landcover": 2,
              "system:index": "589"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.772352426521481, 9.873191288820733]),
            {
              "landcover": 2,
              "system:index": "590"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.78162214087695, 9.888242536830802]),
            {
              "landcover": 2,
              "system:index": "591"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.783510416023434, 9.892301182397773]),
            {
              "landcover": 2,
              "system:index": "592"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.788316934578122, 9.891793854443343]),
            {
              "landcover": 2,
              "system:index": "593"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.810804574958981, 9.88164713090347]),
            {
              "landcover": 2,
              "system:index": "594"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.826940744392575, 9.862367494036468]),
            {
              "landcover": 2,
              "system:index": "595"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.801019876472653, 9.868625043771626]),
            {
              "landcover": 2,
              "system:index": "596"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.879640787117184, 9.97025124536242]),
            {
              "landcover": 2,
              "system:index": "597"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.870714395515622, 9.973294471519242]),
            {
              "landcover": 2,
              "system:index": "598"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.934229104988278, 10.045140145886094]),
            {
              "landcover": 2,
              "system:index": "599"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.930795877449215, 10.051225165678396]),
            {
              "landcover": 2,
              "system:index": "600"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.933714120857418, 10.054436657725878]),
            {
              "landcover": 2,
              "system:index": "601"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.940065591804684, 10.05494373250028]),
            {
              "landcover": 2,
              "system:index": "602"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.941267221443356, 10.052746402731378]),
            {
              "landcover": 2,
              "system:index": "603"
            }),
        ee.Feature(
            ee.Geometry.Point([-13.940752237312497, 10.051056138897241]),
            {
              "landcover": 2,
              "system:index": "604"
            })]),
    MangroveTraining = 
    /* color: #cf11d6 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      },
      {
        "type": "polygon"
      }
    ] */
    ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.772867907259272, 10.831865509758982],
                  [-14.772867907259272, 10.829800117522154],
                  [-14.769735087129877, 10.829800117522154],
                  [-14.769735087129877, 10.831865509758982]]], null, false),
            {
              "landcover": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.765529383394526, 10.838525248913346],
                  [-14.766130198213862, 10.835743350576333],
                  [-14.763641108248041, 10.837724402042513]]]),
            {
              "landcover": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.913246520634662, 10.88669795665154],
                  [-14.913589843388568, 10.88475937330651],
                  [-14.911658652897845, 10.886192240473294]]]),
            {
              "landcover": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.895136245366107, 10.88551795090026],
                  [-14.89530790674306, 10.884000793781476],
                  [-14.893848785038958, 10.884464370387377]]]),
            {
              "landcover": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.050952041676988, 10.935378624515092],
                  [-15.051295364430894, 10.933018994799562],
                  [-15.048548782399644, 10.934030266976446]]]),
            {
              "landcover": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.056273544362535, 10.927794033632864],
                  [-15.05738934331273, 10.924675867811173],
                  [-15.052840316823472, 10.926361366917918]]]),
            {
              "landcover": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.033013427785386, 10.937738235455122],
                  [-15.033270919850816, 10.934198812004023],
                  [-15.030266845754136, 10.93613707293644]]]),
            {
              "landcover": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.024859512380113, 10.944058529371569],
                  [-15.024516189626206, 10.940940534549906],
                  [-15.022112930348863, 10.943805720202793]]]),
            {
              "landcover": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.033528411916246, 10.968495730093942],
                  [-15.034987533620347, 10.965546519857721],
                  [-15.031554306081285, 10.96563078341557]]]),
            {
              "landcover": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.984546455644416, 10.987837291653708],
                  [-14.98471811702137, 10.985056790571315],
                  [-14.982143196367073, 10.985899369423139]]]),
            {
              "landcover": 1,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.970813545488166, 10.976293827966234],
                  [-14.97124269893055, 10.973007649961247],
                  [-14.968753608964729, 10.974440091021131],
                  [-14.970899376176643, 10.97688365091855]]]),
            {
              "landcover": 1,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.913425310937384, 11.025767991764447],
                  [-14.913854464379767, 11.023156342914417],
                  [-14.911365374413947, 11.023830319031457]]]),
            {
              "landcover": 1,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.906121064559587, 10.955341109815576],
                  [-14.907837678329118, 10.949610933953918],
                  [-14.9013145460049, 10.949610933953918]]]),
            {
              "landcover": 1,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.96670177455577, 10.846156206496804],
                  [-14.967130927998152, 10.844133061873753],
                  [-14.965070991474715, 10.844638849312554]]]),
            {
              "landcover": 1,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.743433698959846, 10.875987708548102],
                  [-14.743691191025276, 10.874723371063938],
                  [-14.74257539207508, 10.875229106700816]]]),
            {
              "landcover": 1,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.758668646164436, 10.881424298639294],
                  [-14.758754476852912, 10.87990712068018],
                  [-14.75755284721424, 10.880497135248563]]]),
            {
              "landcover": 1,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.581574563265484, 10.84536404443417],
                  [-14.581832055330914, 10.841570626993633],
                  [-14.57942879605357, 10.842582209681508]]]),
            {
              "landcover": 1,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.603118066073101, 10.845279746791512],
                  [-14.603976372957867, 10.842160717310577],
                  [-14.600457314730328, 10.842413612804403]]]),
            {
              "landcover": 1,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.544370475152173, 10.714539815401963],
                  [-14.544713797906079, 10.712009776250197],
                  [-14.542653861382641, 10.71335913309481]]]),
            {
              "landcover": 1,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.555700126031079, 10.620070724737218],
                  [-14.557245078423657, 10.617033732301914],
                  [-14.554841819146313, 10.616696286835134]]]),
            {
              "landcover": 1,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.49149877105061, 10.606741478020858],
                  [-14.492700400689282, 10.602860702077397],
                  [-14.489782157281079, 10.60353562316791]]]),
            {
              "landcover": 1,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.525144400933423, 10.557468847876851],
                  [-14.525659385064282, 10.554262478003922],
                  [-14.522397818902173, 10.554768749154126]]]),
            {
              "landcover": 1,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.547632041314282, 10.528104002109169],
                  [-14.549005332329907, 10.525572418817276],
                  [-14.546087088921704, 10.525572418817276],
                  [-14.547460379937329, 10.529285400531567]]]),
            {
              "landcover": 1,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.502835338713801, 10.41292156162942],
                  [-14.503178661467707, 10.408700677058924],
                  [-14.499402111174739, 10.409544858543237]]]),
            {
              "landcover": 1,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.494767253997004, 10.393842709127481],
                  [-14.495968883635676, 10.390128106675817],
                  [-14.492707317473567, 10.390634645974284]]]),
            {
              "landcover": 1,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.47914606869427, 10.369359288904414],
                  [-14.47914606869427, 10.365644395693769],
                  [-14.476227825286067, 10.366319834100443]]]),
            {
              "landcover": 1,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.576993053557551, 10.460191559812422],
                  [-14.577679699065364, 10.457490610691979],
                  [-14.575104778411067, 10.458672278824194]]]),
            {
              "landcover": 1,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.627633159758723, 10.477747155867581],
                  [-14.628663128020442, 10.475552760727757],
                  [-14.625058239104426, 10.476059160985555]]]),
            {
              "landcover": 1,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.458669826688668, 10.353920649385334],
                  [-14.459699794950387, 10.351049912543393],
                  [-14.457296535673043, 10.351387647653238]]]),
            {
              "landcover": 1,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.139551326932809, 10.164877141176504],
                  [-14.14126794070234, 10.16115984608325],
                  [-14.13852135867109, 10.16115984608325]]]),
            {
              "landcover": 1,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.092859432401559, 10.157611478625247],
                  [-14.09457604617109, 10.154907934134476],
                  [-14.092001125516793, 10.154738961845052]]]),
            {
              "landcover": 1,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.0758649560832, 10.146121256763173],
                  [-14.077066585721871, 10.143755571644597],
                  [-14.07483498782148, 10.14392454973268]]]),
            {
              "landcover": 1,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.086507961454293, 10.137841282399306],
                  [-14.086679622831246, 10.135644518587286],
                  [-14.083933040799996, 10.135644518587286]]]),
            {
              "landcover": 1,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.114660427274606, 10.118069866300507],
                  [-14.114660427274606, 10.114183034389438],
                  [-14.11157052248945, 10.115028001850106]]]),
            {
              "landcover": 1,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.108137294950387, 10.096607207508624],
                  [-14.108223125638863, 10.09398765106267],
                  [-14.10607735842695, 10.095339682858716]]]),
            {
              "landcover": 1,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.100927517118356, 10.095170679194851],
                  [-14.101270839872262, 10.09288912104627],
                  [-14.09809510439863, 10.093311633034737]]]),
            {
              "landcover": 1,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.021705791654488, 10.082326141150112],
                  [-14.021877453031442, 10.080636032223616],
                  [-14.020075008573434, 10.081058560286214]]]),
            {
              "landcover": 1,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.9989606592082, 10.0360984726324],
                  [-13.99921815127363, 10.03390101484509],
                  [-13.997158214750192, 10.034915227984722]]]),
            {
              "landcover": 1,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.982309505643746, 10.021899251579727],
                  [-13.982652828397653, 10.019025524007592],
                  [-13.980592891874215, 10.020377869566946]]]),
            {
              "landcover": 1,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.02342240542402, 10.024603913085619],
                  [-14.024624035062692, 10.021392125035309],
                  [-14.021448299589059, 10.021899251579727]]]),
            {
              "landcover": 1,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.835067067440528, 9.863594689892103],
                  [-13.834895406063575, 9.86190344613282],
                  [-13.833951268490333, 9.8628336312745]]]),
            {
              "landcover": 1,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.78159454851963, 9.855138384324128],
                  [-13.78434113055088, 9.852686015145009],
                  [-13.780650410946388, 9.852686015145009],
                  [-13.78210953265049, 9.856068588553256]]]),
            {
              "landcover": 1,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.730782780941505, 9.849895365972753],
                  [-13.732327733334083, 9.84795035410826],
                  [-13.72992447405674, 9.8484577496128]]]),
            {
              "landcover": 1,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.690013203915138, 9.850402758486885],
                  [-13.690528188045997, 9.84795035410826],
                  [-13.68821075945713, 9.848288617864625]]]),
            {
              "landcover": 1,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.681773457821388, 9.867822761312134],
                  [-13.682030949886817, 9.865285924971385],
                  [-13.67971352129795, 9.865708732384784]]]),
            {
              "landcover": 1,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.656796727474708, 9.882536026645745],
                  [-13.65748337298252, 9.879745630321658],
                  [-13.65473679095127, 9.880252976868517]]]),
            {
              "landcover": 1,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.658856663998145, 9.860635007617953],
                  [-13.659371648129005, 9.857844425704632],
                  [-13.656367574032325, 9.858859185497039]]]),
            {
              "landcover": 1,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.65525177508213, 9.812684457771793],
                  [-13.656281743343849, 9.809893470949143],
                  [-13.653449330624122, 9.810400924847407]]]),
            {
              "landcover": 1,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.572682652767677, 9.778006894151861],
                  [-13.57311180621006, 9.77445435389848],
                  [-13.569163594540138, 9.776738134132595]]]),
            {
              "landcover": 1,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.532513890560645, 9.73579688260377],
                  [-13.532599721249122, 9.732413083234764],
                  [-13.529853139217872, 9.73410498720453]]]),
            {
              "landcover": 1,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.543843541439552, 9.590008806122597],
                  [-13.543929372128028, 9.587131332658355],
                  [-13.540324483212013, 9.588908598563034]]]),
            {
              "landcover": 1,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.50891045122959, 9.585861851311003],
                  [-13.508996281918067, 9.583153608560922],
                  [-13.50616386919834, 9.58518479265003]]]),
            {
              "landcover": 1,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.542556081112403, 9.577059983359076],
                  [-13.543242726620216, 9.574605575646206],
                  [-13.540238652523536, 9.574605575646206]]]),
            {
              "landcover": 1,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.530389026199542, 9.527893347398814],
                  [-13.530303195511065, 9.525523232532972],
                  [-13.52867241243001, 9.526792938971614]]]),
            {
              "landcover": 1,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.451424792801104, 9.537796863571655],
                  [-13.452454761062823, 9.535257527857542],
                  [-13.450738147293292, 9.535426817493349]]]),
            {
              "landcover": 1,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.454943851028643, 9.544737618029338],
                  [-13.455630496536456, 9.542282977117766],
                  [-13.453570560013018, 9.542875478266838]]]),
            {
              "landcover": 1,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.404647067581378, 9.536019330556984],
                  [-13.404904559646807, 9.533395336318703],
                  [-13.402758792434893, 9.533733917354596]]]),
            {
              "landcover": 1,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.35263367036458, 9.463471170308926],
                  [-13.352376178299151, 9.46186257739953],
                  [-13.350058749710284, 9.462709206184886]]]),
            {
              "landcover": 1,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.281136706863604, 9.376427045404881],
                  [-13.279935077224932, 9.373293725915216],
                  [-13.277875140701495, 9.37549552094412]]]),
            {
              "landcover": 1,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.258134082351885, 9.403016779052459],
                  [-13.25701828340169, 9.400899836835583],
                  [-13.253499225174151, 9.402339358952185]]]),
            {
              "landcover": 1,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.2767593417513, 9.352206597362429],
                  [-13.2767593417513, 9.348226152497125],
                  [-13.27324028352376, 9.351020937696008]]]),
            {
              "landcover": 1,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.319159701858721, 9.36406297170052],
                  [-13.32345123628255, 9.362962039686883],
                  [-13.31993217805501, 9.359743910725987]]]),
            {
              "landcover": 1,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.276330188308917, 9.28597285948887],
                  [-13.276587680374346, 9.282076366483075],
                  [-13.273411944900714, 9.284109324760125]]]),
            {
              "landcover": 1,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.22035537324127, 9.227099179359078],
                  [-13.221042018749083, 9.223879801424738],
                  [-13.217952113963927, 9.224472846935972]]]),
            {
              "landcover": 1,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.282496791698302, 9.227014459263557],
                  [-13.281981807567442, 9.223795080556025],
                  [-13.279578548290099, 9.225828375789598]]]),
            {
              "landcover": 1,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.201730113841856, 9.201512786400121],
                  [-13.200614314891661, 9.198293175278035],
                  [-13.198554378368224, 9.201343333913732]]]),
            {
              "landcover": 1,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.184306484081114, 9.042107056466508],
                  [-13.184993129588927, 9.039987948233751],
                  [-13.183019023753966, 9.040072712802496]]]),
            {
              "landcover": 1,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.260438304759825, 9.024984305436146],
                  [-13.259408336498106, 9.023458476277755],
                  [-13.257691722728575, 9.024560464650595]]]),
            {
              "landcover": 1,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.642733884742919, 9.878367396851779],
                  [-13.643291784218016, 9.876929904698706],
                  [-13.641231847694579, 9.877352697160317]]]),
            {
              "landcover": 1,
              "system:index": "68"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.637626958778563, 9.870714792841605],
                  [-13.637498212745848, 9.869150426476896],
                  [-13.635996175697509, 9.869869190324037]]]),
            {
              "landcover": 1,
              "system:index": "69"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.71767956322163, 9.790239249343115],
                  [-13.71793705528706, 9.788293886948836],
                  [-13.716048780140575, 9.788801373889488]]]),
            {
              "landcover": 1,
              "system:index": "70"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.722228589710888, 9.789647183733882],
                  [-13.721713605580028, 9.788124724462955],
                  [-13.71991116112202, 9.78905511706901]]]),
            {
              "landcover": 1,
              "system:index": "71"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.718709531483348, 9.787532655083849],
                  [-13.71793705528706, 9.786686839854307],
                  [-13.716735425648388, 9.787194329250488]]]),
            {
              "landcover": 1,
              "system:index": "72"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.72566181724995, 9.785502694914687],
                  [-13.724717679676708, 9.784233963509804],
                  [-13.723258557972606, 9.785248949021314]]]),
            {
              "landcover": 1,
              "system:index": "73"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.702487531361278, 9.789308860054645],
                  [-13.702830854115184, 9.787278910741135],
                  [-13.701028409657177, 9.788463049348552],
                  [-13.70317417686909, 9.789985507068423]]]),
            {
              "landcover": 1,
              "system:index": "74"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.697509351429638, 9.80064251559769],
                  [-13.697337690052684, 9.798866371277441],
                  [-13.695535245594677, 9.799965890311366]]]),
            {
              "landcover": 1,
              "system:index": "75"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.487795754889769, 9.654477745850699],
                  [-13.487967416266722, 9.65312390200053],
                  [-13.485478326300901, 9.65312390200053]]]),
            {
              "landcover": 1,
              "system:index": "76"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.439584340971981, 9.671575492304996],
                  [-13.43936976425079, 9.669967883805594],
                  [-13.43786772720245, 9.670898605452638]]]),
            {
              "landcover": 1,
              "system:index": "77"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.448296155852352, 9.662183565542307],
                  [-13.448553647917782, 9.66057591215856],
                  [-13.446794118804013, 9.661083593004093]]]),
            {
              "landcover": 1,
              "system:index": "78"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.451471891325985, 9.66599113502486],
                  [-13.451471891325985, 9.664425806120096],
                  [-13.45009860031036, 9.66506039979714]]]),
            {
              "landcover": 1,
              "system:index": "79"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.471642103117977, 9.675932918788158],
                  [-13.471599187773739, 9.674494551243551],
                  [-13.470526304167782, 9.67538295545391]]]),
            {
              "landcover": 1,
              "system:index": "80"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.493915166777645, 9.681347894319272],
                  [-13.494430150908505, 9.679951854290938],
                  [-13.492498960417782, 9.679571115094394]]]),
            {
              "landcover": 1,
              "system:index": "81"
            })]),
    NonMangroveTraining = 
    /* color: #0d3bff */
    /* shown: false */
    ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.016362274220933, 10.95631951504912],
                  [-15.01670559697484, 10.954465652887245],
                  [-15.014988983205308, 10.955729651075279]]]),
            {
              "landcover": 2,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.028464401296128, 10.951853372862459],
                  [-15.028893554738511, 10.9499573487322],
                  [-15.026318634084214, 10.950589358124523]]]),
            {
              "landcover": 2,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.030567253163804, 10.957794169840307],
                  [-15.03091057591771, 10.955687517889313],
                  [-15.028464401296128, 10.954760586280573],
                  [-15.028121078542222, 10.956193115725121]]]),
            {
              "landcover": 2,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.064427459767808, 10.939929285941478],
                  [-15.062968338063706, 10.936811247682382],
                  [-15.05962094121312, 10.939339389326674],
                  [-15.061766708425035, 10.942457400993268]]]),
            {
              "landcover": 2,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.01115396907215, 10.978358203146746],
                  [-15.011497291826057, 10.976041046340452],
                  [-15.008707794450569, 10.976672999999328]]]),
            {
              "landcover": 2,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.018235000871467, 10.979242930950159],
                  [-15.01866415431385, 10.976462348929923],
                  [-15.016303810380744, 10.978189683264663]]]),
            {
              "landcover": 2,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-15.023599418901252, 10.982697556991285],
                  [-15.023685249589729, 10.980717471399375],
                  [-15.021453651689338, 10.981812839538087]]]),
            {
              "landcover": 2,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.94775758632801, 11.03259186797311],
                  [-14.947929247704963, 11.029306317720359],
                  [-14.94501100429676, 11.031243954363834]]]),
            {
              "landcover": 2,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.92827402004383, 11.037225273846428],
                  [-14.929046496240119, 11.034866458168958],
                  [-14.926729067651252, 11.035119189326004]]]),
            {
              "landcover": 2,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.931449755517463, 11.018101472815468],
                  [-14.932393893090705, 11.015826752939146],
                  [-14.930076464501838, 11.016163749585782]]]),
            {
              "landcover": 2,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.717083677597541, 10.887661504655835],
                  [-14.717169508286018, 10.88547006877135],
                  [-14.715281233139534, 10.886818646608011]]]),
            {
              "landcover": 2,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.707556471176643, 10.873501173067645],
                  [-14.707985624619026, 10.871309633085449],
                  [-14.705839857407112, 10.872236825042815]]]),
            {
              "landcover": 2,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.564665917635601, 10.855985357241925],
                  [-14.56492340970103, 10.851686299903761],
                  [-14.560889367342632, 10.85396227913996]]]),
            {
              "landcover": 2,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.501528172847433, 10.829671752536575],
                  [-14.50358810937087, 10.826299651525124],
                  [-14.498953252193136, 10.82646825747719]]]),
            {
              "landcover": 2,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.49586334740798, 10.843328373277828],
                  [-14.498438268062277, 10.838439037462708],
                  [-14.492258458491964, 10.839282032096412]]]),
            {
              "landcover": 2,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.456994834283032, 10.749958141773662],
                  [-14.460428061822094, 10.746922447900886],
                  [-14.456136527398266, 10.746585146697118]]]),
            {
              "landcover": 2,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.442231955865063, 10.732418155960152],
                  [-14.442918601372876, 10.728538983147049],
                  [-14.438798728326, 10.729382285818327]]]),
            {
              "landcover": 2,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.604451957085766, 10.529960483311568],
                  [-14.605310263970532, 10.52692259915962],
                  [-14.60136205230061, 10.52894785858715]]]),
            {
              "landcover": 2,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.48600560698811, 10.471222760291694],
                  [-14.486177268365063, 10.466833862095141],
                  [-14.48325902495686, 10.468353103116165]]]),
            {
              "landcover": 2,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.500432079436457, 10.441284422659384],
                  [-14.500432079436457, 10.438245668318906],
                  [-14.496998851897395, 10.439089769725399]]]),
            {
              "landcover": 2,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.549012249114192, 10.45462082650194],
                  [-14.549870555998957, 10.452257454900492],
                  [-14.546952312590754, 10.452257454900492]]]),
            {
              "landcover": 2,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.534936016204036, 10.443647877725367],
                  [-14.534936016204036, 10.439427409646498],
                  [-14.530129497649348, 10.44111560375287]]]),
            {
              "landcover": 2,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.356874630155465, 10.29244737636023],
                  [-14.357389614286324, 10.289069376182145],
                  [-14.354471370878121, 10.2909272807549]]]),
            {
              "landcover": 2,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.315847561063668, 10.324198808708294],
                  [-14.316362545194528, 10.32115891654387],
                  [-14.314130947294137, 10.322003333980634]]]),
            {
              "landcover": 2,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.15851990908613, 10.089339998450072],
                  [-14.159635708036324, 10.087058398980245],
                  [-14.157318279447457, 10.088072445184688]]]),
            {
              "landcover": 2,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.039730236234567, 10.046493936082012],
                  [-14.040245220365426, 10.044550094321767],
                  [-14.038786098661324, 10.045648788926059]]]),
            {
              "landcover": 2,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-14.001278087797067, 10.069734616761512],
                  [-14.00170724123945, 10.06762189672479],
                  [-13.999990627469918, 10.068213459729401]]]),
            {
              "landcover": 2,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.967031643094918, 10.078100852215877],
                  [-13.968061611356637, 10.07590368008197],
                  [-13.9660016748332, 10.076410721134172]]]),
            {
              "landcover": 2,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.96900574892988, 10.101846256417112],
                  [-13.970035717191598, 10.100240750496802],
                  [-13.967804119291207, 10.100494251964397]]]),
            {
              "landcover": 2,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.947118923368356, 10.008291081164497],
                  [-13.947633907499215, 10.005924384584203],
                  [-13.945144817533395, 10.006685110366224]]]),
            {
              "landcover": 2,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.936304256620309, 10.017419606331591],
                  [-13.938364193143746, 10.01454583906799],
                  [-13.935617611112496, 10.015052976317214]]]),
            {
              "landcover": 2,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.865245156545589, 10.011587522650414],
                  [-13.865931802053401, 10.008967277018833],
                  [-13.862241082448909, 10.008967277018833]]]),
            {
              "landcover": 2,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.849194817800472, 10.015222021890791],
                  [-13.849366479177425, 10.012939899216223],
                  [-13.847392373342464, 10.01378513170792]]]),
            {
              "landcover": 2,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.871596627492854, 9.977522681370168],
                  [-13.872884087820003, 9.97473309468144],
                  [-13.868678384084651, 9.975493893420309],
                  [-13.87219744231219, 9.977860811466533]]]),
            {
              "landcover": 2,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.885329537649104, 9.931449178193983],
                  [-13.885844521779964, 9.928067380758433],
                  [-13.882582955617854, 9.92891283339319]]]),
            {
              "landcover": 2,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.719195637997169, 9.885749180963948],
                  [-13.719367299374122, 9.883550710348658],
                  [-13.716792378719825, 9.885072730032563]]]),
            {
              "landcover": 2,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.712758336361427, 9.899785223586706],
                  [-13.71292999773838, 9.897164080446853],
                  [-13.710097585018653, 9.898516931131878]]]),
            {
              "landcover": 2,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.585042271908302, 9.704664636543379],
                  [-13.585643086727638, 9.70153433202078],
                  [-13.582982335384864, 9.70280337791928]]]),
            {
              "landcover": 2,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.603495869930763, 9.704072419011773],
                  [-13.604697499569435, 9.699334641080256],
                  [-13.60032013445713, 9.699673056010699]]]),
            {
              "landcover": 2,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.568047795589942, 9.681736594181228],
                  [-13.568047795589942, 9.678775293678653],
                  [-13.565472874935645, 9.680298251483626]]]),
            {
              "landcover": 2,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.579463277157325, 9.671498844445082],
                  [-13.580149922665138, 9.667945172458403],
                  [-13.577145848568458, 9.66929895669111]]]),
            {
              "landcover": 2,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.550280843075294, 9.648314689092652],
                  [-13.551053319271583, 9.645353094436604],
                  [-13.548306737240333, 9.645860798225591]]]),
            {
              "landcover": 2,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.53637627154209, 9.6554224100717],
                  [-13.537577901180763, 9.65296857096865],
                  [-13.535174641903419, 9.653053186407726]]]),
            {
              "landcover": 2,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.354779437576495, 9.451194876126811],
                  [-13.356066897903643, 9.448231567078778],
                  [-13.35289116243001, 9.448824230929024]]]),
            {
              "landcover": 2,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.30122108796712, 9.458137385977457],
                  [-13.301993564163409, 9.455766788608837],
                  [-13.299161151443682, 9.456698096666363]]]),
            {
              "landcover": 2,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.380013659988604, 9.43282194906301],
                  [-13.379327014480792, 9.430197165246152],
                  [-13.376837924514971, 9.431636565296552]]]),
            {
              "landcover": 2,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.292037204300128, 9.406827242400094],
                  [-13.290663913284503, 9.402508714101591],
                  [-13.2877456698763, 9.405387738957764]]]),
            {
              "landcover": 2,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.245417934276427, 9.18405875410957],
                  [-13.243443828441466, 9.181432101976078],
                  [-13.241383891918028, 9.18388929326906]]]),
            {
              "landcover": 2,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.066632610179747, 9.154740824313496],
                  [-13.06731925568756, 9.152113955250934],
                  [-13.064915996410216, 9.152791858802239]]]),
            {
              "landcover": 2,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.074958186961974, 9.158977668998714],
                  [-13.075129848338927, 9.15618135717263],
                  [-13.073155742503966, 9.157028726715863]]]),
            {
              "landcover": 2,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.729721799006377, 9.85583516805335],
                  [-13.729721799006377, 9.85245259225134],
                  [-13.727490201105987, 9.853974755654882]]]),
            {
              "landcover": 2,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.717018857111846, 9.87917399489423],
                  [-13.717877163996612, 9.877144597357086],
                  [-13.714958920588408, 9.877482831149154]]]),
            {
              "landcover": 2,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.728520169367705, 9.83097242702757],
                  [-13.729206814875518, 9.828266165435217],
                  [-13.726288571467315, 9.828266165435217]]]),
            {
              "landcover": 2,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.514183618018233, 9.825400785383925],
                  [-13.51401195664128, 9.82408992060949],
                  [-13.512552834937178, 9.824935640413306]]]),
            {
              "landcover": 2,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.518603898474776, 9.822229329432322],
                  [-13.518560983130538, 9.82117217069405],
                  [-13.517616845557296, 9.821595034594583]]]),
            {
              "landcover": 2,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.525341607520186, 9.831320755143555],
                  [-13.526028253027999, 9.830009913831383],
                  [-13.524440385291182, 9.830179054937869]]]),
            {
              "landcover": 2,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.543580628821456, 9.823836204246815],
                  [-13.54323730606755, 9.822398474517083],
                  [-13.542035676428878, 9.822652191982112]]]),
            {
              "landcover": 2,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.708849929637964, 9.918043253117057],
                  [-13.708849929637964, 9.916690482958893],
                  [-13.707304977245386, 9.917113224233205]]]),
            {
              "landcover": 2,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.704386733837183, 9.911025697281337],
                  [-13.704644225902612, 9.909588348034493],
                  [-13.703356765575464, 9.910095648488015]]]),
            {
              "landcover": 2,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.640357040233667, 9.89622915380466],
                  [-13.640700362987573, 9.894199861550709],
                  [-13.638983749218042, 9.894622631804186]]]),
            {
              "landcover": 2,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.64160671314408, 9.893653002898159],
                  [-13.641563797799842, 9.893124538436428],
                  [-13.640962982980506, 9.893261939278268]]]),
            {
              "landcover": 2,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.638013196876708, 9.880523623305505],
                  [-13.63797028153247, 9.879339814453012],
                  [-13.636983228614989, 9.87972032490587]]]),
            {
              "landcover": 2,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.61247856705493, 9.877437255587456],
                  [-13.61273605912036, 9.876168876898934],
                  [-13.611620260170165, 9.876507111693881]]]),
            {
              "landcover": 2,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.605569196632567, 9.87041883220746],
                  [-13.605526281288329, 9.86906586592114],
                  [-13.604152990272704, 9.869742349759118]]]),
            {
              "landcover": 2,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.598144842079344, 9.869150426476896],
                  [-13.598316503456298, 9.867628333151876],
                  [-13.597114873817626, 9.867628333151876]]]),
            {
              "landcover": 2,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.705663266834911, 9.8058863147593],
                  [-13.705234113392528, 9.803941044100654],
                  [-13.70420414513081, 9.8052097001726]]]),
            {
              "landcover": 2,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Polygon(
                [[[-13.438532915038143, 9.665229624575522],
                  [-13.438897695464169, 9.664129661994533],
                  [-13.43763169280914, 9.664489265541672]]]),
            {
              "landcover": 2,
              "system:index": "66"
            })]),
    nationalborder = ee.FeatureCollection("projects/gee-book/assets/A3-3/Border5km");
/***** End of imports. If edited, may not auto-convert in the playground. *****/
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  Chapter:      A3.3 Mangroves
//  Section:      Supplemental (Assignment 1)
//  Author:       Celio de Sousa, David Lagomasino, and Lola Fatoyinbo
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
 //****************************************
//STEP 1 - TEMPORAL AND SPATIAL PARAMETERS
//****************************************

//Temporal
var year = 2020; // Year
var startDay = (year)+'-01-01'; // beginning of date filter | month-day
var endDay = (year)+'-12-30'; // end of date filter | month-day

//Spatial
var aoi = ee.FeatureCollection('projects/gee-book/assets/A3-3/CoastalPrefectures5k');

//****************************
//STEP 2 - AUXILIARY FUNCTIONS
//****************************

var maskL8sr = function (image) {
  var cloudShadowBitMask = 1 << 3;
  var cloudsBitMask = 1 << 5;
  var qa = image.select('pixel_qa');
  var mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0)
      .and(qa.bitwiseAnd(cloudsBitMask).eq(0));
  return image.updateMask(mask).divide(10000)
      .select("B[0-9]*")
      .copyProperties(image, ["system:time_start"]);
};


var addIndicesL8 = function(img) {
  // NDVI (Normalized Difference Vegetation Index)
  var ndvi = img.normalizedDifference(['B5','B4']).rename('NDVI');

  // NDMI (Normalized Difference Mangrove Index - Shi et al 2016 )
  var ndmi = img.normalizedDifference(['B7','B3']).rename('NDMI');

  // MNDWI (Modified Normalized Difference Water Index - Hanqiu Xu, 2006)
  var mndwi = img.normalizedDifference(['B3','B6']).rename('MNDWI');

  // SR (Simple Ratio)
  var sr = img.select('B5').divide(img.select('B4')).rename('SR');

  // Band Ratio 6/5
  var ratio65 = img.select('B6').divide(img.select('B5')).rename('R65');

  // Band Ratio 4/6
  var ratio46 = img.select('B4').divide(img.select('B6')).rename('R46');

  // GCVI (Green Chlorophyll Vegetation Index)
  var gcvi = img.expression('(NIR/GREEN)-1',{
    'NIR':img.select('B5'),
    'GREEN':img.select('B3')
  }).rename('GCVI');

   return img
    .addBands(ndvi) // This will add each spectral index to each Landsat scene
    .addBands(ndmi)
    .addBands(mndwi)
    .addBands(sr)
    .addBands(ratio65)
    .addBands(ratio46)
    .addBands(gcvi);
};


//**************************************************************
//STEP 3 - CREATE AUXILIARY MASKS AND BANDS FOR MANGROVE MAPPING
//**************************************************************

// WATER MASK
// The objective of this mask is to remove water pixels from the Landsat composite as we are only focusing on Mangroves

// We will create a Water Mask using the Global Surface Water dataset

var globalwater = ee.Image('JRC/GSW1_0/GlobalSurfaceWater'); // Load the dataset

// The Global Water Dataset has different bands. One of them is the the frequency with which water was present (occurrence).
// Esentially, this band shows how many times a given pixel was classified as water relative to the total time span of the dataset

var occurrence = globalwater.select('occurrence'); // Select the occurrence band.

// Masks are composed by zeros and non-zero values. When you set or apply a mask to an image, the output image will keep it's original values where the mask
// has non zero values whereas the it will be masked where the mask has zero values.
// For this example, we want to create a watermask. Thus Watermask has to have zero where there is water and non zero values 
// For our mask, we want to make sure we are selecting permanent water. We want to filter the dataset for water pixels that occurred more than 50% of the time over the 35 years time spam.

var waterMask = occurrence.lt(50) // Selects lower than 50%. Automatically, values above 90% are set to 0
                          .unmask(1); // Since the water dataset only includes water, set other areas to 1 

Map.addLayer(waterMask, {}, 'Water Mask');



// ELEVATION/SLOPE MASK

// The objective of this mask is to remove pixels that are unlikely to be mangrove based on the slope. Generally, it will occur near shore where
// elevation and slope is very low.

// We will create a mask using the SRTM Elevation Data
var srtm = ee.Image('USGS/SRTMGL1_003');

var elevation = srtm.select('elevation');

// In this case, we want to create a mask where pixels that have higher altitude values are removed 
// Hence, we select everything that is UNDER 25 meters; everything else will be set to 0 automatically.
var elevMask = elevation.lte(25);
Map.addLayer(elevMask, {}, 'Elevation Mask');
Map.addLayer(ee.Image().paint(aoi, 0, 2), {palette:['red']}, 'StudyArea');

//*********************************************************
//STEP 4 - LANDSAT 8 IMAGE COLLECTION AND CLOUD-FREE MOSAIC
//*********************************************************

// Map the function over one year of data.
var collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
    .filterDate(startDay, endDay)
    .map(maskL8sr)
    .map(addIndicesL8);

    
var composite = collection
                .median()
                .mask(waterMask)
                .updateMask(elevMask)
                .clip(aoi);

// Display the results.
//Map.centerObject(Mangroves2016,9);
Map.addLayer(composite, {bands: ['B5', 'B6', 'B4'], min: 0, max: 0.3}, 'Composite');

//************************************************************
//STEP 5 - CREATE STRATIFICATION MAP BASED ON MANGROVE DATASET
//************************************************************

//Mangrove Strata

//First, let's load the global mangrove dataset for the year 2000
var dataset = ee.FeatureCollection('projects/gee-book/assets/A3-3/Mangroves2000');
var mangrove = ee.Image(1).clip(dataset);

//All other classes Strata

// First we create an image of zeros where values 1 will be added where there is a pixel from the composite, including the mangrove areas
var nonmangrove = ee.Image(0).where(composite.select('B1'),2).selfMask()
// Now we have an image of values of 1 where there is composite. Now we set this image to zero where there is pixel of mangrove
var strata = nonmangrove.where(mangrove,1).rename('landcover');

Map.addLayer (strata, {palette:['#B3E283','#E8E46E'], min:1, max:2}, 'Strata')

// Selecting samples based on the strata created above

var stratified = strata.addBands(ee.Image.pixelLonLat()).stratifiedSample({
      numPoints: 1,
      classBand: 'landcover',
      scale: 30,
      region: aoi,
      classValues:[1,2],     // 
      classPoints:[1000,1000]  // Insert the number of points per class. 
    }).map(function(f) { // set these points to geometry and get their coordinates
       return f.setGeometry(ee.Geometry.Point([f.get('longitude'), f.get('latitude')]))
    });

var paletteSamples = ee.List([
  'FFFFFF',  //NULL
  '01937C', // Mangrove
  'B6C867', // Non-Mangrove
 ]);

// We use this function to colorize the samples based on the palette
var features = stratified.map(function(f) {
  var landcover = f.get('landcover');
  return ee.Feature(ee.Geometry.Point([f.get('longitude'), f.get('latitude')]), f.toDictionary())
      .set({style: {color: paletteSamples.get(landcover) }}); 
});

// Add the features / sample location into the map with the style set above
Map.addLayer(features.style({styleProperty: "style"}),{}, 'Samples/Location')

//************************************************************
//STEP 6 - CLASSIFICATION
//************************************************************

// First, we will select the predictors to assign to each sample point in the sample sets
var bands = ['B5','B6','B7','NDVI','MNDWI','SR'];

// Create the sample sets
// Automatic
var samplesAutomatic = composite.select(bands).sampleRegions({
  collection: stratified,
  properties: ['landcover'],
  scale: 30,
  geometries: true,
});

// Create the sample set with the samples you selected manually via geometry
var manualpoints = MangroveTraining.merge(NonMangroveTraining);
var samplesManual = composite.select(bands).sampleRegions({
  collection: manualpoints,       
  properties: ['landcover'], 
  scale: 30,
  geometries: true,
});

// Create the Ground Truth sample set that will be used to validate the land cover classification maps
var groundtruth = ee.FeatureCollection('users/celiohelder/TutorialAssets/GroundTruth');
Map.addLayer(groundtruth)

var samplesgroundtruth = composite.select(bands).sampleRegions({
  collection: groundtruth,       // Set of geometries selected in 4.1
  properties: ['landcover'], // Label from each geometry
  scale: 30,
  geometries: true,
});


// Train two classifiers: one with the samples collected automatically via stratification and one with the samples you selected manually
var RandomForest1 = ee.Classifier.smileRandomForest(200,5).train({
  features: samplesAutomatic, 
  classProperty: 'landcover', 
  inputProperties: bands
});

var RandomForest2 = ee.Classifier.smileRandomForest(200,5).train({
  features: samplesManual, 
  classProperty: 'landcover', 
  inputProperties: bands
});


// Classify the Landsat 8 Composite using the two classifiers to produce 2 land cover maps

var classifiedrf1 = composite.select(bands)           // select the predictors
                            .classify(RandomForest1); // apply the Random Forest trained with the automatically selected samples

var classifiedrf2 = composite.select(bands)           // select the predictors
                            .classify(RandomForest2); // apply the Random Forest classifier trained with mannually selected samples

// Color palette for the classification outputs
var paletteMAP = [
  '01937C', // Mangrove
  'B6C867', // Non-Mangrove
];

// Add the classifications to the map editor
Map.addLayer (classifiedrf1, {min: 1, max: 2, palette:paletteMAP}, 'Classification Automatic Samples');
Map.addLayer (classifiedrf2, {min: 1, max: 2, palette:paletteMAP}, 'Classification Manual Samples');


var validation1 = samplesgroundtruth.classify(RandomForest1);
var validation2 = samplesgroundtruth.classify(RandomForest2);
var testAccuracy1 = validation1.errorMatrix('landcover', 'classification');
var testAccuracy2 = validation2.errorMatrix('landcover', 'classification');
var kappa1 = testAccuracy1.kappa();
var kappa2 = testAccuracy2.kappa();

print('Overall Accuracy Map 1: ', testAccuracy1.accuracy());
print('Overall Accuracy Map 2: ', testAccuracy2.accuracy());
print('Kappa: ', kappa1);
print('Kappa: ', kappa2);

print('Validation error matrix Map1: ', testAccuracy1);
print('Validation error matrix Map2: ', testAccuracy2);

var legend = ui.Panel({
  style: {
    position: 'bottom-left', // Position in the map
    padding: '8px 15px'      // Padding (border) size
  }
});
var makeRow = function(color, name) {
  // Create the label that is actually the colored boxes that represent each class
  var colorBox = ui.Label({
    style: {
      backgroundColor: '#' + color,
      // Use padding to give the label color box height and width.
      padding: '8px', 
      margin: '0 0 4px 0'
    }
  });
  // Create the label filled with the description text.
  var description = ui.Label({
    value: name,
    style: {margin: '0 0 4px 6px'}
  });
  return ui.Panel({
    widgets: [colorBox, description],
    layout: ui.Panel.Layout.Flow('horizontal')
  });
};
legend.add(makeRow('01937C', 'Mangrove'));
legend.add(makeRow('B6C867', 'Non-mangrove'));

//Map.add (legend);



