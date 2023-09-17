import numpy as np


def make_stats():
    # 4-view
    # NoComm
    stats_list = [
        [11, 17] + [19, 18] + [19, 18, 18,19,19,17],
        [760.84, 746.16] + [755.96, 759.91] + [759.65, 745.68, 743.65, 739.54, 729.54, 745.68],
        [503, 495] + [510, 512] + [515, 511, 509, 506, 514, 509],
        [255.79, 256.03] + [265.12, 261.69] + [257.95, 269.51, 260.58, 259.65, 261.82, 254.74],
        [67, 64] + [69, 72] + [63, 69, 70,68,71,72],
    ]
    # # Monolith
    # stats_list = [
    #     [16,] + [15, 15, 14, 15] + [17, 16, 15, 14, 15, 15, 14, 16],
    #     #[745.46,] + [732.15, 736.15, 741.52, 740.31] + [724.98, 722.54, 720.85, 732.05, 730.59, 733.85, 731.25, 729.54],
    #     [495,] + [481, 480, 483, 479] + [491,482,471,489,488,480,495,480],
    #     [254.35,] + [239.54, 238.48, 237.69, 240.12]+[240.69,242.54,245.53,245.58,254.76,249.68,251.85,250.68],
    #     [66,] + [66, 68, 70, 65] + [67,66,68,65,66,67,66,68],
    # ]
    # AllComm
    stats_list = [
        [8, 30, 15] + [17, 16, 17] + [17, 16, 17, 18, 17, 16],
        # [760.33, 721.39, 747.27] + [751.21, 748.96, 746.85] + [741.56, 749.58, 751.58, 751.19, 758.35, 748.51],
        [501, 488, 500] + [489, 500, 492] + [510, 495, 492, 502, 490, 487],
        [254.04, 240.69, 254.22] + [250.96, 249.85, 251.69] + [256.62, 250.61, 256.58, 252.51, 250.25, 249.58],
        [68, 72, 70] + [69, 70, 70] + [69, 69, 68, 71, 71, 68],
    ]
    # AllComm, 30 (60, 30, 20, 10, 2)
    stats_list = [
        [14, 16, 16] + [],
        [498, 510, 513] + [],
        [248.03, 253.23, 256.73] + [],
        [69, 75, 68] + [],
    ]
    # AllComm, 10 (60, 30, 20, 10, 2)
    stats_list = [
        [17, 16, 16, 16] + [],
        [495, 501, 505, 510] + [],
        [253.11, 255.98, 256.38, 252.38] + [],
        [66, 70, 72, 70] + [],
    ]
    # 2-view
    # Monolith
    stats_list = [
        [2,5,7,6,6,7,4,6,7,5,6,5,5,5,4] + [],
        [200,201,199,198,199,200,201,220,199,199,200,201,200,199,199] + [],
        [143.56,140.87,135.52,136.05,132.84,130.99,135.97,136.89,137.41,132.68,132.06,131.86,134.85,135.61,131.06] + [],
        [23,30,24,25,23,24,25,25,24,23,25,24,25,26,27] + [],
    ]
    # AllComm
    stats_list = [
        [5,6,8,5,7,6,6,6,5,6,6,8,7,8,7,6] + [],
        [201,201,199,210,198,198,199,203,202,199,201,202,203,204,201,199] + [],
        [138.95,140.36,141.65,139.87,139.85,138.66,137.88,140.76,138.47,140.08,141.78,138.4,137.85,139.64,138.99] + [],
        [24,32,25,27,26,27,28,26,28,29,27,26,26,26,27] + [],
    ]
    # NoComm
    stats_list = [
        [3,5,9,8,9,8,5,8,9,5,6,6] + [],
        [201,201,202,198,199,201,199,201,203,204,203,202,203,203] + [],
        [145.68,146.85,136.85,139.56,138.52,141.52,139.85,138.68,137.58,140.52,138.58,140.25,139.54,135.68] + [],
        [29,29,25,25,28,27,26,27,28,25,27,28,28,29] + [],
    ]
    # AllComm, raw img
    stats_list = [
        [9,21,20,18,18,31,17,18,18,19,18] + [],
        [506,487,506,509,510,511,509,510,505,501,515,] + [],
        [256.58,257.58,251.41,257.68,257.53,250.25,250.69,250.63,251.63,252.69,253.68,] + [],
        [69,69,71,69,74,69,66,72,74,74,71,] + [],
    ]
    for each_stats in stats_list:
        print('each_stats: {}, np.mean(each_stats): {}, np.std(each_stats): {}'.format(each_stats, np.mean(each_stats),
                                                                                       np.std(each_stats)))


def planning_time():
    metrics = {}
    metrics['PlanningTime'] = [5.817413330078125e-05, 7.486343383789062e-05, 0.00019288063049316406,
                               6.961822509765625e-05, 5.2928924560546875e-05, 6.842613220214844e-05,
                               6.580352783203125e-05, 5.435943603515625e-05, 0.0018458366394042969,
                               5.316734313964844e-05, 7.05718994140625e-05, 6.747245788574219e-05,
                               0.0001881122589111328, 6.67572021484375e-05, 6.532669067382812e-05,
                               0.00018453598022460938, 0.00018978118896484375, 0.00047588348388671875,
                               5.221366882324219e-05, 0.00014090538024902344, 7.081031799316406e-05,
                               5.53131103515625e-05, 0.00019097328186035156, 7.390975952148438e-05,
                               0.0001862049102783203, 6.699562072753906e-05, 0.00018715858459472656,
                               6.818771362304688e-05, 8.296966552734375e-05, 6.914138793945312e-05,
                               0.0002269744873046875, 5.5789947509765625e-05, 0.00019216537475585938,
                               0.0008282661437988281, 7.224082946777344e-05, 6.771087646484375e-05,
                               0.0001952648162841797, 0.00018525123596191406, 8.225440979003906e-05,
                               6.890296936035156e-05, 5.5789947509765625e-05, 5.555152893066406e-05,
                               6.914138793945312e-05, 0.00023412704467773438, 7.963180541992188e-05,
                               6.794929504394531e-05, 7.271766662597656e-05, 0.0002353191375732422,
                               6.747245788574219e-05, 6.771087646484375e-05, 8.678436279296875e-05,
                               7.104873657226562e-05, 5.4836273193359375e-05, 0.0009074211120605469,
                               0.00018644332885742188, 5.555152893066406e-05, 6.890296936035156e-05,
                               0.0001442432403564453, 6.961822509765625e-05, 0.00018930435180664062,
                               6.67572021484375e-05, 6.937980651855469e-05, 5.2928924560546875e-05,
                               0.0001881122589111328, 7.43865966796875e-05, 0.00018930435180664062,
                               5.3882598876953125e-05, 6.985664367675781e-05, 0.0009090900421142578,
                               6.0558319091796875e-05, 0.0001862049102783203, 6.723403930664062e-05,
                               6.747245788574219e-05, 7.581710815429688e-05, 0.0009768009185791016,
                               3.910064697265625e-05, 6.532669067382812e-05, 0.00018835067749023438,
                               0.00026726722717285156, 5.340576171875e-05, 0.0001862049102783203, 6.961822509765625e-05,
                               6.866455078125e-05, 0.00018334388732910156, 5.173683166503906e-05, 7.891654968261719e-05,
                               6.818771362304688e-05, 6.723403930664062e-05, 6.818771362304688e-05,
                               0.00013375282287597656, 6.413459777832031e-05, 6.699562072753906e-05,
                               7.033348083496094e-05, 6.747245788574219e-05, 0.00018715858459472656,
                               7.271766662597656e-05, 6.723403930664062e-05, 0.0001857280731201172,
                               5.14984130859375e-05, 5.459785461425781e-05, 5.936622619628906e-05,
                               7.009506225585938e-05, 6.914138793945312e-05, 5.841255187988281e-05,
                               6.771087646484375e-05, 7.62939453125e-05, 7.653236389160156e-05, 6.937980651855469e-05,
                               0.00015211105346679688, 6.723403930664062e-05, 0.00018024444580078125,
                               5.269050598144531e-05, 0.0001862049102783203, 5.245208740234375e-05,
                               5.650520324707031e-05, 0.0009133815765380859, 5.340576171875e-05, 0.00018715858459472656,
                               6.771087646484375e-05, 4.601478576660156e-05, 5.9604644775390625e-05,
                               6.771087646484375e-05, 0.0001857280731201172, 7.462501525878906e-05,
                               3.886222839355469e-05, 5.269050598144531e-05, 0.0009539127349853516,
                               0.0001804828643798828, 6.580352783203125e-05, 0.00018286705017089844,
                               5.030632019042969e-05, 0.0002510547637939453, 7.343292236328125e-05,
                               5.173683166503906e-05, 7.62939453125e-05, 7.557868957519531e-05, 7.796287536621094e-05,
                               9.369850158691406e-05, 9.393692016601562e-05, 9.298324584960938e-05,
                               0.00011134147644042969, 0.0002503395080566406, 0.0003020763397216797,
                               0.0002663135528564453, 7.62939453125e-05, 9.34600830078125e-05, 8.96453857421875e-05,
                               9.1552734375e-05, 9.179115295410156e-05, 0.00035381317138671875, 0.00026988983154296875,
                               6.961822509765625e-05, 7.104873657226562e-05, 9.393692016601562e-05,
                               9.703636169433594e-05, 8.940696716308594e-05, 7.009506225585938e-05,
                               7.581710815429688e-05, 0.00027489662170410156, 0.00025343894958496094,
                               9.322166442871094e-05, 9.202957153320312e-05, 9.1552734375e-05, 9.202957153320312e-05,
                               7.295608520507812e-05, 9.322166442871094e-05, 0.0002446174621582031,
                               7.343292236328125e-05, 0.00010991096496582031, 0.007874250411987305, 0.00794076919555664,
                               0.009355545043945312, 0.014231681823730469, 0.011466264724731445, 0.009512662887573242,
                               0.008643865585327148, 0.009533405303955078, 0.009033679962158203, 0.01722860336303711,
                               0.009536504745483398, 0.011623144149780273, 0.007956743240356445, 0.007865428924560547,
                               0.009318351745605469, 0.008563041687011719, 0.008877277374267578, 0.009014368057250977,
                               0.008631229400634766, 0.009353876113891602, 0.007678508758544922, 0.008416414260864258,
                               0.009291410446166992, 0.008208036422729492, 0.008527994155883789, 0.008353233337402344,
                               0.007869720458984375, 0.00805211067199707, 0.009834766387939453, 0.009228944778442383,
                               0.008044719696044922, 0.01615428924560547, 0.007983922958374023, 0.011294126510620117,
                               0.00852060317993164, 0.009723901748657227, 0.010741949081420898, 0.00835561752319336,
                               0.008091211318969727, 0.007743358612060547, 0.013791322708129883, 0.008067131042480469,
                               0.009019136428833008, 0.00807809829711914, 0.007982254028320312, 0.007871150970458984,
                               0.007973670959472656, 0.009005308151245117, 0.008260965347290039, 0.0088348388671875,
                               0.007888317108154297, 0.005331277847290039, 0.009972810745239258, 0.009324312210083008,
                               0.011428356170654297, 0.00818490982055664, 0.008410930633544922, 0.008838653564453125,
                               0.009438753128051758, 0.01636981964111328, 0.011066913604736328, 0.010065317153930664,
                               0.021750688552856445, 0.007842302322387695, 0.0075702667236328125, 0.007570981979370117,
                               0.00829768180847168, 0.007503509521484375, 0.008715152740478516, 0.007501840591430664,
                               0.0074808597564697266, 0.00818943977355957, 0.007561683654785156, 0.008098840713500977,
                               0.007397174835205078, 0.008248567581176758, 0.0076236724853515625, 0.008294820785522461,
                               0.009073734283447266, 0.007883787155151367, 0.010242223739624023, 0.004423379898071289,
                               0.004573345184326172, 0.007837772369384766, 0.007615566253662109, 0.012128114700317383,
                               0.009384870529174805, 0.00794839859008789, 0.011260032653808594, 0.0077702999114990234,
                               0.007781267166137695, 0.008869409561157227, 0.008307456970214844, 0.004360198974609375,
                               0.009734392166137695, 0.007569074630737305, 0.007425546646118164, 0.00847482681274414,
                               0.008821487426757812, 0.007608175277709961, 0.007622957229614258, 0.009355783462524414,
                               0.00809168815612793, 0.007333278656005859, 0.009044647216796875, 0.007718324661254883,
                               0.004456520080566406, 0.009055137634277344, 0.007898807525634766, 0.009630203247070312,
                               0.00829768180847168, 0.00789332389831543, 0.015038013458251953, 0.01365804672241211,
                               0.013722896575927734, 0.013617515563964844, 0.015871286392211914, 0.013604879379272461,
                               7.499598741531372, 5.755696535110474, 7.536776542663574, 4.682226896286011,
                               3.052199602127075, 3.242751359939575, 4.692947626113892, 0.12761449813842773,
                               4.127173185348511, 3.7717785835266113, 3.921107530593872, 3.9644935131073,
                               3.029561996459961, 5.822118520736694, 3.154383659362793, 2.2414164543151855,
                               2.4868922233581543, 2.6131625175476074, 5.699693441390991, 4.069500684738159,
                               7.56031060218811, 5.985118627548218, 0.013634204864501953, 0.016283512115478516,
                               0.013153076171875, 0.014518976211547852, 0.013168573379516602, 2.4858648777008057,
                               3.6822333335876465, 3.693086624145508, 3.6969614028930664, 3.58176589012146,
                               3.619811773300171, 3.7360446453094482, 3.6860709190368652, 3.420961618423462,
                               2.7156834602355957, 3.693511486053467, 3.697280168533325, 3.5476670265197754,
                               2.2122442722320557, 2.252680778503418, 2.8677823543548584, 3.5962798595428467,
                               3.7118492126464844, 3.7123141288757324, 2.138967752456665, 2.678821325302124,
                               3.714607000350952, 3.7127277851104736, 2.119828701019287, 2.2972230911254883,
                               2.9288296699523926, 2.77374005317688, 3.70550799369812, 3.066953659057617,
                               2.279974937438965, 3.7186574935913086, 3.7157089710235596, 1.9430961608886719,
                               2.6852798461914062, 1.9910197257995605, 3.713870048522949, 2.0083913803100586,
                               2.0783724784851074, 3.6958324909210205, 2.3771164417266846, 2.184307336807251,
                               2.191166639328003, 3.5753333568573, 3.187373638153076, 2.276695728302002,
                               3.5417838096618652, 3.6833412647247314, 2.2186338901519775, 2.611459493637085,
                               3.8948636054992676, 2.2828328609466553, 4.265320062637329, 2.7085471153259277,
                               3.067235231399536, 3.2117245197296143, 5.928914785385132, 5.043061256408691,
                               2.410297393798828, 3.8360557556152344, 3.309924364089966, 1.8580849170684814,
                               4.405233144760132, 2.897118091583252, 4.6665074825286865, 2.742281913757324,
                               2.5760300159454346, 4.099278450012207, 4.897963523864746, 3.04131817817688,
                               5.342176914215088, 4.552327394485474, 2.890531301498413, 2.7982819080352783,
                               4.761734962463379, 2.5855724811553955][:-190]
    # [2.0899415016174316, 1.9481520652770996, 2.0635533332824707, 1.9854512214660645,
    #                        1.9890663623809814, 1.9726593494415283, 1.9552099704742432, 1.9283440113067627,
    #                        1.9644277095794678, 1.9249725341796875, 1.9100127220153809, 1.880878210067749,
    #                        1.9524052143096924, 1.9429223537445068, 1.976003646850586, 1.917266845703125,
    #                        1.8531415462493896, 1.9075992107391357, 1.8947222232818604, 1.8332102298736572,
    #                        1.9265806674957275, 1.9546229839324951, 1.9279696941375732, 0.18220090866088867,
    #                        0.13639044761657715, 1.9246249198913574, 0.13857007026672363, 1.9309794902801514,
    #                        0.1948409080505371, 1.9358775615692139, 0.14339137077331543, 0.18849730491638184,
    #                        0.18418431282043457, 0.1433124542236328, 1.885392665863037, 0.14048409461975098,
    #                        1.8718485832214355, 0.1831350326538086, 0.13856792449951172, 1.912877082824707,
    #                        0.1853466033935547, 1.9416227340698242, 0.19012928009033203, 0.18152999877929688,
    #                        1.9857594966888428, 0.14798903465270996, 0.13489866256713867, 0.13645219802856445,
    #                        1.908506155014038, 0.13243651390075684, 0.13802075386047363, 0.18282270431518555,
    #                        1.996342420578003, 1.929062843322754, 0.14138484001159668, 0.1823575496673584,
    #                        0.18410730361938477, 0.18024945259094238, 0.13158559799194336, 0.1330552101135254,
    #                        0.17952919006347656, 0.1820666790008545, 0.183335542678833, 0.1344928741455078,
    #                        0.17949867248535156, 0.17824602127075195, 0.15659737586975098, 0.1363530158996582,
    #                        0.17469263076782227, 0.1806640625, 0.13637065887451172, 0.14136958122253418,
    #                        0.17870688438415527, 0.18143534660339355, 0.17638111114501953, 0.13369989395141602,
    #                        0.13543701171875, 0.17477059364318848, 0.18032431602478027, 0.13541078567504883,
    #                        0.1293179988861084, 0.13511157035827637, 0.13471674919128418, 0.181318998336792,
    #                        0.13585114479064941, 0.13837337493896484, 0.13326334953308105, 0.14281296730041504,
    #                        0.1327042579650879, 1.900996446609497, 0.1827092170715332, 0.1344013214111328,
    #                        1.898449182510376, 0.13869500160217285, 0.13488435745239258, 1.9350426197052002,
    #                        1.8749146461486816, 0.13671398162841797, 0.1843714714050293, 0.1843256950378418,
    #                        1.7971398830413818, 0.1383664608001709, 0.13883280754089355, 0.18279027938842773,
    #                        1.9116499423980713, 1.7838904857635498, 0.17784976959228516, 0.18095707893371582,
    #                        0.13462424278259277, 0.17545199394226074, 1.5443994998931885, 1.627058506011963,
    #                        0.15279316902160645, 0.17930316925048828, 0.13327646255493164, 1.5828967094421387,
    #                        0.17885589599609375, 1.9256985187530518, 0.17540454864501953, 0.14010977745056152,
    #                        0.14063000679016113, 0.14890170097351074, 0.13227152824401855, 0.17856502532958984,
    #                        0.12825751304626465, 0.13522768020629883, 0.14582443237304688, 0.14419269561767578,
    #                        0.18805503845214844, 0.13720130920410156, 0.19164037704467773, 0.19107866287231445,
    #                        0.19653654098510742, 0.15197372436523438, 0.1898033618927002, 0.14378952980041504,
    #                        0.1971418857574463, 0.19989538192749023, 0.15041828155517578, 0.14021682739257812,
    #                        0.14110541343688965, 0.16092157363891602, 0.17641901969909668, 0.2015852928161621,
    #                        0.2720367908477783, 0.3017239570617676, 0.40248942375183105, 0.6494541168212891,
    #                        0.19150781631469727, 0.13645696640014648, 0.1833961009979248, 0.9799294471740723,
    #                        0.8977904319763184, 1.5727806091308594, 0.8985598087310791, 0.8490586280822754,
    #                        0.5863685607910156, 0.14837908744812012, 0.13172531127929688, 0.13320040702819824,
    #                        0.1322469711303711, 0.1793837547302246, 0.13040471076965332, 0.13317418098449707,
    #                        0.1858363151550293, 0.13356852531433105, 0.1898815631866455, 0.1422746181488037,
    #                        0.17887258529663086, 0.15400314331054688, 0.19040751457214355, 0.16976094245910645,
    #                        0.18663573265075684, 0.14086294174194336, 0.1396334171295166, 0.1374068260192871,
    #                        0.14040541648864746, 0.16029119491577148, 0.1904430389404297, 0.18929314613342285,
    #                        0.18166184425354004, 0.13814544677734375, 0.18800830841064453, 0.17899799346923828,
    #                        0.13881325721740723, 0.13993620872497559, 0.18423676490783691, 0.13447356224060059,
    #                        0.13722777366638184, 0.13821768760681152, 0.13669466972351074, 0.13651299476623535,
    #                        0.14383220672607422, 0.13749313354492188, 0.14120221138000488, 0.13626885414123535,
    #                        0.14040613174438477, 0.1905066967010498, 0.13666892051696777, 0.14426493644714355,
    #                        0.1416492462158203, 0.18694090843200684, 0.13961386680603027, 0.13804149627685547,
    #                        0.14017796516418457, 0.19278907775878906, 0.14914989471435547, 0.14054131507873535,
    #                        0.1368272304534912, 0.13895583152770996, 0.19282007217407227, 0.14670276641845703,
    #                        0.1373884677886963, 0.14041519165039062, 0.14125394821166992, 0.18436670303344727,
    #                        0.13827252388000488, 0.14373350143432617, 0.14065003395080566, 0.1369638442993164,
    #                        0.1780719757080078, 0.14277362823486328, 0.13875246047973633, 0.14286160469055176,
    #                        0.1402580738067627, 0.1355428695678711, 0.16600728034973145, 0.18761754035949707,
    #                        0.1767423152923584, 0.1408839225769043, 0.1850569248199463, 0.14107489585876465,
    #                        0.13930487632751465, 0.1929950714111328, 0.14534592628479004, 0.1881566047668457,
    #                        0.19304728507995605, 0.13978052139282227, 0.14168453216552734, 0.14673590660095215,
    #                        0.19281697273254395, 0.15119552612304688, 0.14300894737243652, 0.1987321376800537,
    #                        0.14425230026245117, 0.1874830722808838, 0.14675116539001465, 0.14085698127746582,
    #                        0.14069819450378418, 0.1398630142211914, 0.14015579223632812, 0.13841032981872559,
    #                        0.1866295337677002, 0.1920163631439209, 0.1450817584991455, 0.14296555519104004,
    #                        0.13873863220214844, 0.19809436798095703, 0.14020848274230957, 0.17517614364624023,
    #                        0.18284082412719727, 0.14314699172973633, 0.13785457611083984, 0.17856717109680176,
    #                        0.1324305534362793, 0.13793516159057617, 0.14583230018615723, 0.18175840377807617,
    #                        0.14725661277770996, 0.1399824619293213, 0.13937616348266602, 0.18878865242004395,
    #                        0.13414263725280762, 0.13918614387512207, 0.14259696006774902, 0.14711356163024902,
    #                        0.13857769966125488, 0.13910293579101562, 0.13837933540344238, 0.18657279014587402,
    #                        0.18808245658874512, 0.14203405380249023, 0.18123769760131836, 0.1352531909942627,
    #                        0.1843724250793457, 0.138106107711792, 0.1889796257019043, 0.18258237838745117,
    #                        0.17720866203308105, 0.1345047950744629, 0.13624072074890137, 0.13225293159484863,
    #                        0.1340036392211914, 0.13741183280944824, 0.1724386215209961, 0.137070894241333,
    #                        0.13718080520629883, 0.1362318992614746, 0.18565797805786133, 0.13721323013305664,
    #                        0.1398000717163086, 0.18397760391235352, 0.186079740524292, 0.18229079246520996,
    #                        0.13672924041748047, 0.18126368522644043, 0.13833022117614746, 0.1355123519897461,
    #                        0.20057463645935059, 0.18245148658752441, 0.1694471836090088, 0.13942432403564453,
    #                        0.14168763160705566, 0.1935124397277832, 0.13910770416259766, 0.13668537139892578,
    #                        0.13972878456115723, 0.1354212760925293, 0.13978052139282227, 0.18776273727416992,
    #                        0.14648938179016113, 0.18855977058410645, 0.18983125686645508, 0.14367246627807617,
    #                        0.13918495178222656, 0.18778467178344727, 0.18772506713867188, 0.1384890079498291,
    #                        0.13608741760253906, 0.13457155227661133, 0.139190673828125, 0.13862276077270508,
    #                        0.1374375820159912, 0.14807415008544922, 0.18715953826904297, 0.1456289291381836,
    #                        0.13421392440795898, 0.18921470642089844, 0.13587689399719238, 0.1357259750366211,
    #                        0.1818392276763916, 0.13681268692016602, 0.17869257926940918, 0.13619160652160645,
    #                        0.1771378517150879, 0.13648462295532227, 0.13670659065246582, 0.1382596492767334,
    #                        0.13528990745544434, 0.18203520774841309, 0.17205810546875, 0.13996481895446777,
    #                        0.18109560012817383, 0.1815938949584961, 0.13326215744018555, 0.14542269706726074,
    #                        0.13565945625305176, 0.13456058502197266, 0.1820669174194336, 0.13489747047424316,
    #                        0.13607454299926758, 0.13382220268249512, 0.13799667358398438, 0.18422436714172363,
    #                        0.16581392288208008, 0.17887306213378906, 0.13372087478637695, 0.13495755195617676,
    #                        0.17854952812194824, 0.1342618465423584, 0.13312602043151855, 0.14637112617492676,
    #                        0.13691115379333496, 0.18212032318115234, 0.13800978660583496, 0.17969059944152832,
    #                        0.17785334587097168, 0.17821598052978516, 0.17783331871032715, 0.13455748558044434,
    #                        0.13764739036560059, 0.17998671531677246, 0.17588496208190918, 0.13244938850402832,
    #                        0.1349468231201172, 0.17764830589294434, 0.1325547695159912, 0.13408374786376953,
    #                        0.13602590560913086, 0.18024897575378418, 0.1357896327972412, 0.13639593124389648,
    #                        0.13236331939697266, 0.13394927978515625, 0.1748645305633545, 0.179351806640625,
    #                        0.13346290588378906, 0.14574074745178223, 0.13270187377929688, 0.1780853271484375,
    #                        0.18058133125305176, 0.13628649711608887, 0.16420888900756836, 0.13055753707885742,
    #                        0.17968535423278809, 0.13129138946533203, 0.13397932052612305, 0.13336968421936035,
    #                        0.1547091007232666, 0.13155388832092285, 0.1787254810333252, 0.13222956657409668,
    #                        0.16377925872802734, 0.13120079040527344, 0.13297057151794434, 0.18447661399841309,
    #                        0.1298964023590088, 0.17886114120483398, 0.1826784610748291, 0.14319300651550293,
    #                        0.18152260780334473, 0.12902283668518066, 0.13308143615722656, 0.13858675956726074,
    #                        0.16967272758483887, 0.13574576377868652, 0.17733407020568848, 0.13606619834899902,
    #                        0.13644075393676758, 0.13476872444152832, 0.13556194305419922, 0.16692042350769043,
    #                        0.1338798999786377, 0.1331019401550293, 0.13940644264221191, 0.1640481948852539,
    #                        0.13582396507263184, 0.13113665580749512, 0.18105506896972656, 0.13709759712219238,
    #                        0.17987370491027832, 0.13630437850952148, 0.13364171981811523, 0.18042826652526855,
    #                        0.18468832969665527, 0.1701514720916748, 0.13996410369873047, 0.1753983497619629,
    #                        0.13837289810180664, 0.16013407707214355, 0.15308594703674316, 0.13281512260437012,
    #                        0.1392984390258789, 0.13501739501953125, 0.17896437644958496, 0.13342690467834473,
    #                        0.13928604125976562, 0.14179515838623047, 0.14284920692443848, 0.14723467826843262,
    #                        0.13759946823120117, 0.19759678840637207, 0.1840193271636963, 0.1358659267425537,
    #                        0.14275431632995605, 0.13786911964416504, 0.18804597854614258, 0.1373734474182129,
    #                        0.16260218620300293, 0.18715929985046387, 0.13591599464416504, 0.1408219337463379,
    #                        0.13968658447265625, 0.1411299705505371, 0.13553643226623535, 0.14165329933166504,
    #                        0.1433413028717041, 0.1421515941619873, 0.1467738151550293, 0.14394497871398926,
    #                        0.1822972297668457, 0.16957569122314453, 0.14470362663269043, 0.1874685287475586,
    #                        0.18462347984313965, 0.13640260696411133, 0.13571548461914062, 0.19452452659606934,
    #                        0.1684119701385498, 0.19490790367126465, 0.1454756259918213, 0.13710284233093262,
    #                        0.14456510543823242, 0.13690662384033203, 0.19501876831054688, 0.15164542198181152,
    #                        0.1895143985748291, 0.1825392246246338, 0.13875508308410645, 0.14455151557922363,
    #                        0.19043636322021484, 0.13772034645080566, 0.18621087074279785, 0.18001198768615723,
    #                        0.131072998046875, 0.1358017921447754, 0.1336805820465088, 0.18712186813354492,
    #                        0.1616055965423584, 0.1930983066558838, 0.18110132217407227, 0.19252729415893555,
    #                        0.13570809364318848, 0.17856907844543457]
    len_planning_time = len(metrics['PlanningTime'])
    mean_planning_time = np.mean(metrics['PlanningTime'])
    std_planning_time = np.std(metrics['PlanningTime'])
    sum_planning_time = np.sum(metrics['PlanningTime'])
    print('length of planning : {}, mean planning time: {}, std planning time: {}, sum of the planning time: {}'.format(
        len_planning_time,
        mean_planning_time,
        std_planning_time,
        sum_planning_time))


if __name__ == "__main__":
    make_stats()
    # planning_time()
