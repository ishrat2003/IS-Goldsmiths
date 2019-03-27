var normalizedValue = 1000;
var xCat = "x";
var yCat = "y";
var rCat = "number_of_blocks";
var colorCat = "topic";
var labelCat = "label";
var givenWidth = 600;
var givenHeight = 400;

var excludedLabels = [];

var rawData = 
[{'number_of_blocks': 160, 'total_count': 1632, 'label': 'Brexit', 'stemmed_word': 'brexit', 'score': 258021, 'appeared': 1548806400, 'index': 3, 'topic': 9, 'x': 622.5113, 'y': 158.1027}, {'number_of_blocks': 150, 'total_count': 935, 'label': 'EU', 'stemmed_word': 'eu', 'score': 106971, 'appeared': 1548806400, 'index': 21, 'topic': 9, 'x': 538.317, 'y': 228.11934}, {'number_of_blocks': 148, 'total_count': 982, 'label': 'UK', 'stemmed_word': 'uk', 'score': 84157, 'appeared': 1548806400, 'index': 19, 'topic': 9, 'x': 518.9062, 'y': -106.433}, {'number_of_blocks': 135, 'total_count': 957, 'label': 'deal', 'stemmed_word': 'deal', 'score': 142767, 'appeared': 1546560000, 'index': 79, 'topic': 9, 'x': 538.9048, 'y': -144.35278}, {'number_of_blocks': 107, 'total_count': 388, 'label': 'government', 'stemmed_word': 'govern', 'score': 16278, 'appeared': 1548806400, 'index': 38, 'topic': 9, 'x': 219.53929, 'y': -4.9700737}, {'number_of_blocks': 72, 'total_count': 234, 'label': 'company', 'stemmed_word': 'compani', 'score': 13330, 'appeared': 1546560000, 'index': 144, 'topic': 8, 'x': 76.06316, 'y': 28.048107}, {'number_of_blocks': 55, 'total_count': 94, 'label': 'delays', 'stemmed_word': 'delay', 'score': 0, 'appeared': 1546560000, 'index': 134, 'topic': 8, 'x': 26.775593, 'y': -0.14624384}, {'number_of_blocks': 52, 'total_count': 91, 'label': 'Commons', 'stemmed_word': 'common', 'score': 0, 'appeared': 1546560000, 'index': 148, 'topic': 8, 'x': 62.297565, 'y': -27.236322}, {'number_of_blocks': 50, 'total_count': 137, 'label': 'firm', 'stemmed_word': 'firm', 'score': 0, 'appeared': 1548979200, 'index': 303, 'topic': 8, 'x': 54.78024, 'y': 2.0392933}, {'number_of_blocks': 44, 'total_count': 107, 'label': 'food', 'stemmed_word': 'food', 'score': 1170, 'appeared': 1548806400, 'index': 11, 'topic': 8, 'x': 19.802418, 'y': 7.4193907}, {'number_of_blocks': 70, 'total_count': 105, 'label': 'impact', 'stemmed_word': 'impact', 'score': 0, 'appeared': 1548806400, 'index': 75, 'topic': 7, 'x': 27.96674, 'y': -5.116446}, {'number_of_blocks': 53, 'total_count': 81, 'label': 'services', 'stemmed_word': 'servic', 'score': 0, 'appeared': 1548979200, 'index': 329, 'topic': 7, 'x': 31.259478, 'y': 9.386785}, {'number_of_blocks': 50, 'total_count': 104, 'label': 'event', 'stemmed_word': 'event', 'score': 0, 'appeared': 1546560000, 'index': 89, 'topic': 7, 'x': 63.364353, 'y': -6.0283833}, {'number_of_blocks': 50, 'total_count': 78, 'label': 'end', 'stemmed_word': 'end', 'score': 0, 'appeared': 1546560000, 'index': 221, 'topic': 7, 'x': 30.976446, 'y': -6.397584}, {'number_of_blocks': 44, 'total_count': 69, 'label': 'department', 'stemmed_word': 'depart', 'score': 0, 'appeared': 1546560000, 'index': 295, 'topic': 7, 'x': 11.146773, 'y': 2.3355412}, {'number_of_blocks': 91, 'total_count': 181, 'label': 'March', 'stemmed_word': 'march', 'score': 0, 'appeared': 1546560000, 'index': 222, 'topic': 6, 'x': 115.09977, 'y': 7.0442934}, {'number_of_blocks': 45, 'total_count': 107, 'label': 'jobs', 'stemmed_word': 'job', 'score': 10065, 'appeared': 1548892800, 'index': 373, 'topic': 6, 'x': 32.017075, 'y': -5.486749}, {'number_of_blocks': 43, 'total_count': 89, 'label': 'uncertainty', 'stemmed_word': 'uncertainti', 'score': 2154, 'appeared': 1548892800, 'index': 368, 'topic': 6, 'x': 36.883724, 'y': -7.3524404}, {'number_of_blocks': 39, 'total_count': 75, 'label': 'tariffs', 'stemmed_word': 'tariff', 'score': 0, 'appeared': 1546560000, 'index': 224, 'topic': 6, 'x': 21.64054, 'y': 5.8658757}, {'number_of_blocks': 35, 'total_count': 40, 'label': 'prospects', 'stemmed_word': 'prospect', 'score': 0, 'appeared': 1548979200, 'index': 512, 'topic': 6, 'x': 14.042708, 'y': 1.6896331}, {'number_of_blocks': 48, 'total_count': 73, 'label': 'Tuesday', 'stemmed_word': 'tuesday', 'score': 0, 'appeared': 1548892800, 'index': 386, 'topic': 5, 'x': 54.85675, 'y': -17.921812}, {'number_of_blocks': 44, 'total_count': 148, 'label': 'referendum', 'stemmed_word': 'referendum', 'score': 807, 'appeared': 1548806400, 'index': 15, 'topic': 5, 'x': 70.70791, 'y': -27.534681}, {'number_of_blocks': 43, 'total_count': 57, 'label': 'member', 'stemmed_word': 'member', 'score': 0, 'appeared': 1548806400, 'index': 20, 'topic': 5, 'x': 19.547132, 'y': 5.9845014}, {'number_of_blocks': 43, 'total_count': 61, 'label': 'Brussels', 'stemmed_word': 'brussel', 'score': 0, 'appeared': 1548806400, 'index': 590, 'topic': 5, 'x': 27.948957, 'y': -9.904829}, {'number_of_blocks': 36, 'total_count': 39, 'label': 'result', 'stemmed_word': 'result', 'score': 0, 'appeared': 1546560000, 'index': 209, 'topic': 5, 'x': 6.4999933, 'y': -5.4231625}, {'number_of_blocks': 28, 'total_count': 28, 'label': 'lot', 'stemmed_word': 'lot', 'score': 0, 'appeared': 1548547200, 'index': 1075, 'topic': 4, 'x': 3.7881305, 'y': -8.992727}, {'number_of_blocks': 24, 'total_count': 36, 'label': 'Cabinet', 'stemmed_word': 'cabinet', 'score': 0, 'appeared': 1546560000, 'index': 96, 'topic': 4, 'x': 8.68329, 'y': -3.359828}, {'number_of_blocks': 21, 'total_count': 70, 'label': 'prices', 'stemmed_word': 'price', 'score': 3213, 'appeared': 1548806400, 'index': 71, 'topic': 4, 'x': 16.087626, 'y': 15.958055}, {'number_of_blocks': 21, 'total_count': 46, 'label': 'Dr', 'stemmed_word': 'dr', 'score': 0, 'appeared': 1546560000, 'index': 287, 'topic': 4, 'x': 5.134421, 'y': 8.173101}, {'number_of_blocks': 19, 'total_count': 19, 'label': 'home', 'stemmed_word': 'home', 'score': 0, 'appeared': 1546560000, 'index': 109, 'topic': 4, 'x': -9.613866, 'y': -3.119786}, {'number_of_blocks': 31, 'total_count': 69, 'label': 'extension', 'stemmed_word': 'extens', 'score': 1260, 'appeared': 1548806400, 'index': 54, 'topic': 3, 'x': 29.629461, 'y': -6.7740016}, {'number_of_blocks': 25, 'total_count': 37, 'label': 'Wednesday', 'stemmed_word': 'wednesday', 'score': 0, 'appeared': 1548892800, 'index': 382, 'topic': 3, 'x': 11.633179, 'y': -7.941662}, {'number_of_blocks': 25, 'total_count': 33, 'label': 'Bill', 'stemmed_word': 'bill', 'score': 0, 'appeared': 1547510400, 'index': 868, 'topic': 3, 'x': 24.86006, 'y': -4.7250338}, {'number_of_blocks': 21, 'total_count': 44, 'label': 'meeting', 'stemmed_word': 'meet', 'score': 0, 'appeared': 1547078400, 'index': 934, 'topic': 3, 'x': 14.232071, 'y': -17.550953}, {'number_of_blocks': 18, 'total_count': 23, 'label': 'effect', 'stemmed_word': 'effect', 'score': 0, 'appeared': 1548979200, 'index': 542, 'topic': 3, 'x': -0.79512733, 'y': 0.81750524}, {'number_of_blocks': 23, 'total_count': 29, 'label': 'bid', 'stemmed_word': 'bid', 'score': 0, 'appeared': 1547078400, 'index': 895, 'topic': 2, 'x': 28.166088, 'y': -14.85258}, {'number_of_blocks': 22, 'total_count': 22, 'label': 'Nick', 'stemmed_word': 'nick', 'score': 0, 'appeared': 1547510400, 'index': 862, 'topic': 2, 'x': -0.7557282, 'y': -6.2451673}, {'number_of_blocks': 17, 'total_count': 17, 'label': 'correspondent', 'stemmed_word': 'correspond', 'score': 0, 'appeared': 1547510400, 'index': 830, 'topic': 2, 'x': 0.047701254, 'y': -2.5518198}, {'number_of_blocks': 15, 'total_count': 30, 'label': 'care', 'stemmed_word': 'care', 'score': 0, 'appeared': 1548892800, 'index': 1366, 'topic': 2, 'x': 20.117401, 'y': -10.487552}, {'number_of_blocks': 15, 'total_count': 19, 'label': 'board', 'stemmed_word': 'board', 'score': 0, 'appeared': 1548892800, 'index': 1448, 'topic': 2, 'x': -0.68010974, 'y': 1.9392748}, {'number_of_blocks': 28, 'total_count': 33, 'label': 'How', 'stemmed_word': 'how', 'score': 0, 'appeared': 1548979200, 'index': 521, 'topic': 1, 'x': 12.558273, 'y': -11.087481}, {'number_of_blocks': 21, 'total_count': 24, 'label': 'editor', 'stemmed_word': 'editor', 'score': 0, 'appeared': 1548892800, 'index': 412, 'topic': 1, 'x': 2.9318633, 'y': 1.593473}, {'number_of_blocks': 19, 'total_count': 27, 'label': 'Laura', 'stemmed_word': 'laura', 'score': 0, 'appeared': 1547510400, 'index': 878, 'topic': 1, 'x': 8.839909, 'y': -0.6617545}, {'number_of_blocks': 17, 'total_count': 20, 'label': 'JeanClaude', 'stemmed_word': 'jeanclaud', 'score': 0, 'appeared': 1548979200, 'index': 458, 'topic': 1, 'x': 4.882944, 'y': 4.234272}, {'number_of_blocks': 17, 'total_count': 20, 'label': 'Juncker', 'stemmed_word': 'juncker', 'score': 0, 'appeared': 1548979200, 'index': 459, 'topic': 1, 'x': 4.882944, 'y': 4.234272}]
;