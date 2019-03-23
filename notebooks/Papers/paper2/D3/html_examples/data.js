var normalizedValue = 1000;
var xCat = "x";
var yCat = "y";
var rCat = "number_of_blocks";
var colorCat = "topic";
var labelCat = "label";
var givenWidth = 500;
var givenHeight = 300;

var excludedLabels = ['company', 'people'];

var rawData = [
    {'number_of_blocks': 6, 'total_count': 6, 'label': 'lot', 'stemmed_word': 'lot', 'score': 0, 'appeared': 1548547200, 'index': 1075, 'topic': 1, 'x': -0.006640327, 'y': -0.0011349397}, 
    {'number_of_blocks': 5, 'total_count': 7, 'label': 'congestion', 'stemmed_word': 'congest', 'score': 0, 'appeared': 1548806400, 'index': 47, 'topic': 1, 'x': -0.0062636416, 'y': 1.3320649e-05}, 
    {'number_of_blocks': 5, 'total_count': 5, 'label': 'anything', 'stemmed_word': 'anyth', 'score': 0, 'appeared': 1546560000, 'index': 136, 'topic': 1, 'x': -0.006554896, 'y': 0.0007550996}, 
    {'number_of_blocks': 4, 'total_count': 25, 'label': 'traffic', 'stemmed_word': 'traffic', 'score': 568, 'appeared': 1546560000, 'index': 190, 'topic': 1, 'x': -0.00621887, 'y': -0.00065661815}, 
    {'number_of_blocks': 4, 'total_count': 5, 'label': 'beginning', 'stemmed_word': 'begin', 'score': 0, 'appeared': 1546560000, 'index': 273, 'topic': 1, 'x': -0.006429816, 'y': 0.0019743848},
    {'number_of_blocks': 9, 'total_count': 13, 'label': 'Westminster', 'stemmed_word': 'westminst', 'score': 0, 'appeared': 1547510400, 'index': 820, 'topic': 2, 'x': -0.0063148914, 'y': -0.0005034851}, 
    {'number_of_blocks': 5, 'total_count': 5, 'label': 'correspondent', 'stemmed_word': 'correspond', 'score': 0, 'appeared': 1547510400, 'index': 830, 'topic': 2, 'x': -0.006493056, 'y': 0.013479831}, 
    {'number_of_blocks': 4, 'total_count': 17, 'label': 'medicines', 'stemmed_word': 'medicin', 'score': 1099, 'appeared': 1548806400, 'index': 69, 'topic': 2, 'x': -0.0064118854, 'y': -0.0011161555}, 
    {'number_of_blocks': 3, 'total_count': 3, 'label': 'Six', 'stemmed_word': 'six', 'score': 0, 'appeared': 1546560000, 'index': 162, 'topic': 2, 'x': -0.0067194044, 'y': -0.0014735431}, 
    {'number_of_blocks': 3, 'total_count': 3, 'label': 'potential', 'stemmed_word': 'potenti', 'score': 0, 'appeared': 1546560000, 'index': 248, 'topic': 2, 'x': -0.0064815464, 'y': 0.0071121734},
    {'number_of_blocks': 10, 'total_count': 16, 'label': 'supply', 'stemmed_word': 'suppli', 'score': 0, 'appeared': 1548806400, 'index': 51, 'topic': 3, 'x': -0.0060816095, 'y': -0.00046289279}, 
    {'number_of_blocks': 6, 'total_count': 7, 'label': 'Singapore', 'stemmed_word': 'singapor', 'score': 0, 'appeared': 1548979200, 'index': 499, 'topic': 3, 'x': -0.006197974, 'y': 0.0014584741}, 
    {'number_of_blocks': 5, 'total_count': 7, 'label': 'Dyson', 'stemmed_word': 'dyson', 'score': 0, 'appeared': 1548115200, 'index': 1185, 'topic': 3, 'x': -0.0066187694, 'y': 4.541478e-05}, 
    {'number_of_blocks': 4, 'total_count': 4, 'label': 'Folkestone', 'stemmed_word': 'folkeston', 'score': 0, 'appeared': 1546560000, 'index': 108, 'topic': 3, 'x': -0.006561169, 'y': 0.001359288}, 
    {'number_of_blocks': 4, 'total_count': 6, 'label': 'output', 'stemmed_word': 'output', 'score': 0, 'appeared': 1548892800, 'index': 360, 'topic': 3, 'x': -0.0064010373, 'y': -0.0018643462},
    {'number_of_blocks': 8, 'total_count': 21, 'label': 'system', 'stemmed_word': 'system', 'score': 0, 'appeared': 1546560000, 'index': 115, 'topic': 4, 'x': -0.009115067, 'y': -0.0020998046}, 
    {'number_of_blocks': 8, 'total_count': 9, 'label': 'chain', 'stemmed_word': 'chain', 'score': 0, 'appeared': 1546560000, 'index': 266, 'topic': 4, 'x': -0.006379469, 'y': -0.00012958026}, 
    {'number_of_blocks': 7, 'total_count': 12, 'label': 'staff', 'stemmed_word': 'staff', 'score': 0, 'appeared': 1548979200, 'index': 335, 'topic': 4, 'x': -0.0063235257, 'y': -0.0012433582}, 
    {'number_of_blocks': 6, 'total_count': 18, 'label': 'hour', 'stemmed_word': 'hour', 'score': 0, 'appeared': 1546560000, 'index': 138, 'topic': 4, 'x': -0.0063859457, 'y': -0.00020138663}, 
    {'number_of_blocks': 5, 'total_count': 17, 'label': 'lorries', 'stemmed_word': 'lorri', 'score': 0, 'appeared': 1546560000, 'index': 126, 'topic': 4, 'x': -0.0060817357, 'y': -0.0028742733},
    {'number_of_blocks': 16, 'total_count': 36, 'label': 'leaders', 'stemmed_word': 'leader', 'score': 0, 'appeared': 1546560000, 'index': 275, 'topic': 5, 'x': -0.006486021, 'y': 0.0024823442}, 
    {'number_of_blocks': 14, 'total_count': 21, 'label': 'Tuesday', 'stemmed_word': 'tuesday', 'score': 0, 'appeared': 1548892800, 'index': 386, 'topic': 5, 'x': -0.006279667, 'y': 0.001235261}, 
    {'number_of_blocks': 10, 'total_count': 50, 'label': 'Labour', 'stemmed_word': 'labour', 'score': 475, 'appeared': 1547510400, 'index': 754, 'topic': 5, 'x': -0.006665205, 'y': -0.0006407688}, 
    {'number_of_blocks': 9, 'total_count': 18, 'label': 'Conservative', 'stemmed_word': 'conserv', 'score': 0, 'appeared': 1548806400, 'index': 562, 'topic': 5, 'x': -0.0061991042, 'y': -0.002522709}, 
    {'number_of_blocks': 8, 'total_count': 9, 'label': 'cooperation', 'stemmed_word': 'cooper', 'score': 0, 'appeared': 1548806400, 'index': 32, 'topic': 5, 'x': -0.005977442, 'y': 0.00079200725},
    {'number_of_blocks': 14, 'total_count': 33, 'label': 'Supporters', 'stemmed_word': 'support', 'score': 0, 'appeared': 1546560000, 'index': 163, 'topic': 6, 'x': -0.006409639, 'y': -0.00017577806}, 
    {'number_of_blocks': 10, 'total_count': 12, 'label': 'one', 'stemmed_word': 'one', 'score': 0, 'appeared': 1546560000, 'index': 194, 'topic': 6, 'x': -0.0062366165, 'y': -0.0002663266}, 
    {'number_of_blocks': 9, 'total_count': 19, 'label': 'point', 'stemmed_word': 'point', 'score': 0, 'appeared': 1548806400, 'index': 2, 'topic': 6, 'x': -0.006195297, 'y': -0.01469486}, 
    {'number_of_blocks': 9, 'total_count': 12, 'label': 'director', 'stemmed_word': 'director', 'score': 0, 'appeared': 1546560000, 'index': 142, 'topic': 6, 'x': -0.0064773858, 'y': 0.0001551492}, 
    {'number_of_blocks': 8, 'total_count': 9, 'label': 'National', 'stemmed_word': 'nation', 'score': 0, 'appeared': 1546560000, 'index': 204, 'topic': 6, 'x': -0.006229415, 'y': -0.0007090289},
    {'number_of_blocks': 16, 'total_count': 25, 'label': 'impact', 'stemmed_word': 'impact', 'score': 0, 'appeared': 1548806400, 'index': 75, 'topic': 7, 'x': -0.006248543, 'y': 0.004889142}, 
    {'number_of_blocks': 12, 'total_count': 42, 'label': 'referendum', 'stemmed_word': 'referendum', 'score': 269, 'appeared': 1548806400, 'index': 15, 'topic': 7, 'x': -0.0064780167, 'y': -0.0083273705}, 
    {'number_of_blocks': 12, 'total_count': 21, 'label': 'Europe', 'stemmed_word': 'europ', 'score': 0, 'appeared': 1546560000, 'index': 233, 'topic': 7, 'x': -0.0055369125, 'y': -0.034189463}, 
    {'number_of_blocks': 10, 'total_count': 16, 'label': 'problems', 'stemmed_word': 'problem', 'score': 0, 'appeared': 1548806400, 'index': 50, 'topic': 7, 'x': -0.0063740495, 'y': -0.00036136026}, 
    {'number_of_blocks': 10, 'total_count': 13, 'label': 'France', 'stemmed_word': 'franc', 'score': 0, 'appeared': 1546560000, 'index': 257, 'topic': 7, 'x': -0.0063578635, 'y': -0.0004441744},
    {'number_of_blocks': 25, 'total_count': 92, 'label': 'government', 'stemmed_word': 'govern', 'score': 3464, 'appeared': 1548806400, 'index': 38, 'topic': 8, 'x': -0.00985474, 'y': 0.001619976}, 
    {'number_of_blocks': 23, 'total_count': 43, 'label': 'March', 'stemmed_word': 'march', 'score': 0, 'appeared': 1546560000, 'index': 222, 'topic': 8, 'x': -0.0066930978, 'y': 0.00019632699}, 
    {'number_of_blocks': 21, 'total_count': 57, 'label': 'business', 'stemmed_word': 'busi', 'score': 2332, 'appeared': 1546560000, 'index': 252, 'topic': 8, 'x': -0.0070714336, 'y': 0.0002495665}, 
    {'number_of_blocks': 19, 'total_count': 45, 'label': 'year', 'stemmed_word': 'year', 'score': 713, 'appeared': 1546560000, 'index': 125, 'topic': 8, 'x': -0.0063267453, 'y': 0.00032176403}, 
    {'number_of_blocks': 18, 'total_count': 58, 'label': 'company', 'stemmed_word': 'compani', 'score': 2666, 'appeared': 1546560000, 'index': 144, 'topic': 8, 'x': 36.789196, 'y': -17.899542},
    {'number_of_blocks': 38, 'total_count': 412, 'label': 'Brexit', 'stemmed_word': 'brexit', 'score': 68149, 'appeared': 1548806400, 'index': 3, 'topic': 9, 'x': -0.008204111, 'y': -0.00033251054}, 
    {'number_of_blocks': 36, 'total_count': 244, 'label': 'UK', 'stemmed_word': 'uk', 'score': 22039, 'appeared': 1548806400, 'index': 19, 'topic': 9, 'x': -0.0062510213, 'y': -0.0019864764}, 
    {'number_of_blocks': 36, 'total_count': 233, 'label': 'EU', 'stemmed_word': 'eu', 'score': 27899, 'appeared': 1548806400, 'index': 21, 'topic': 9, 'x': -0.0063492088, 'y': -0.00039245043}, 
    {'number_of_blocks': 33, 'total_count': 249, 'label': 'deal', 'stemmed_word': 'deal', 'score': 39845, 'appeared': 1546560000, 'index': 79, 'topic': 9, 'x': -0.008216094, 'y': -0.0007724921}, 
    {'number_of_blocks': 26, 'total_count': 65, 'label': 'people', 'stemmed_word': 'peopl', 'score': 0, 'appeared': 1548806400, 'index': 36, 'topic': 9, 'x': 19.32575, 'y': -20.543592}
    ];
