//generated for tooltip shader by Godlander
vec2 pad = vec2(5,5);
ivec3 sizes = ivec3(16,16,8);
uint base = 0x50332fffu;
uint[] tl = uint[](0x97a359ffu,0x97a170ffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x96a25cffu,0x7b8245ffu,0x95995affu,0x341e25ffu,0x371b20ffu,0x371e1dffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xa4b361ffu,0x7e8559ffu,0x422425ffu,0x462827ffu,0x482b29ffu,0x351e1fffu,0x281519ffu,0xffffff5eu,0x371b20ffu,0x4b2e2bffu,0x846755ffu,0x50332fffu,0x462829ffu,0x422724ffu,0x6b4e4affu,0xffffff5eu,0x341b1fffu,0x482b29ffu,0x6b5042ffu,0x4b302effu,0x351819ffu,0x2f1517ffu,0x2d171effu,0xffffff5eu,0x331a1effu,0x452a2affu,0x44282bffu,0x2f1819ffu,0x4b302effu,0x44282bffu,0x321e20ffu,0xffffff5eu,0x35191effu,0x48282affu,0x48282affu,0x2d151dffu,0x44282bffu,0x321e20ffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x3c2023ffu,0x654343ffu,0x321a22ffu,0x44282bffu,0x50332fffu,0x50332fffu);
uint[] tr = uint[](0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x96a25cffu,0x97a359ffu,0xffffff5eu,0x35191effu,0x331a1effu,0x341b1fffu,0x371b20ffu,0xa4b361ffu,0x7b8245ffu,0x97a170ffu,0x3c2023ffu,0x48282affu,0x452a2affu,0x482b29ffu,0x4b2e2bffu,0x7e8559ffu,0x95995affu,0xffffff5eu,0x654343ffu,0x48282affu,0x44282bffu,0x6b5042ffu,0x846755ffu,0x422425ffu,0x341e25ffu,0xffffff5eu,0x321a22ffu,0x2d151dffu,0x2f1819ffu,0x4b302effu,0x50332fffu,0x462827ffu,0x371b20ffu,0xffffff5eu,0x44282bffu,0x44282bffu,0x4b302effu,0x351819ffu,0x462829ffu,0x482b29ffu,0x371e1dffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x44282bffu,0x2f1517ffu,0x422724ffu,0x351e1fffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2d171effu,0x6b4e4affu,0x281519ffu,0xffffff5eu,0xffffff5eu);
uint[] bl = uint[](0xffffff43u,0xffffff43u,0x3c2023ffu,0x654343ffu,0x321a22ffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff43u,0x35191effu,0x48282affu,0x48282affu,0x2d151dffu,0x44282bffu,0x50332fffu,0x50332fffu,0xffffff43u,0x331a1effu,0x452a2affu,0x44282bffu,0x2f1819ffu,0x4b302effu,0x44282bffu,0x50332fffu,0xffffff43u,0x341b1fffu,0x482b29ffu,0x6b5042ffu,0x4b302effu,0x351819ffu,0x2f1517ffu,0x2d171effu,0xffffff43u,0x371b20ffu,0x4b2e2bffu,0x846755ffu,0x50332fffu,0x462829ffu,0x422724ffu,0x6b4e4affu,0xffffff43u,0xa4b361ffu,0x7e8559ffu,0x422425ffu,0x462827ffu,0x482b29ffu,0x351e1fffu,0x351e1fffu,0x96a25cffu,0x7b8245ffu,0x95995affu,0x341e25ffu,0x371b20ffu,0x371e1dffu,0xffffff5eu,0xffffff5eu,0x97a359ffu,0x97a170ffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu);
uint[] br = uint[](0x50332fffu,0x50332fffu,0x50332fffu,0x2d171effu,0x6b4e4affu,0x281519ffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x44282bffu,0x2f1517ffu,0x422724ffu,0x351e1fffu,0xffffff5eu,0xffffff5eu,0x44282bffu,0x44282bffu,0x4b302effu,0x351819ffu,0x462829ffu,0x482b29ffu,0x371e1dffu,0xffffff5eu,0x321a22ffu,0x2d151dffu,0x2f1819ffu,0x4b302effu,0x50332fffu,0x462827ffu,0x371b20ffu,0xffffff5eu,0x654343ffu,0x48282affu,0x44282bffu,0x6b5042ffu,0x846755ffu,0x422425ffu,0x341e25ffu,0xffffff5eu,0x3c2023ffu,0x48282affu,0x452a2affu,0x482b29ffu,0x4b2e2bffu,0x7e8559ffu,0x95995affu,0xffffff5eu,0xffffff5eu,0x35191effu,0x331a1effu,0x341b1fffu,0x371b20ffu,0xa4b361ffu,0x7b8245ffu,0x97a170ffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x96a25cffu,0x97a359ffu);
uint[] t = uint[](0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x97a359ffu,0x97a359ffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x97a170ffu,0x7b8245ffu,0xa4b361ffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x29151cffu,0x2a151cffu,0x341b1fffu,0x341b1fffu,0x341b1fffu,0xa4b361ffu,0x291417ffu,0x281316ffu,0x341b1fffu,0x341b1fffu,0x331a1effu,0x32181dffu,0x30161affu,0x3b2226ffu,0x341b1fffu,0x341b1fffu,0x6d4d4affu,0x6d4d4affu,0x6b4c49ffu,0x6d4c47ffu,0x6c4b44ffu,0x6b4d45ffu,0x6b4d45ffu,0x6a4c44ffu,0x694541ffu,0x694541ffu,0x6a4642ffu,0x684440ffu,0x684440ffu,0x6b4743ffu,0x6b4743ffu,0x6a4642ffu,0x2f1921ffu,0x301a22ffu,0x2f181dffu,0x2f181dffu,0x2e171affu,0x2d181affu,0x341f21ffu,0x321e20ffu,0x321a1effu,0x341d20ffu,0x331c1fffu,0x331c1fffu,0x2d151dffu,0x3c242cffu,0x341c24ffu,0x331b23ffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu);
uint[] l = uint[](0xffffff5eu,0xffffff5eu,0x341b1fffu,0x6a4642ffu,0x331b23ffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x341b1fffu,0x6b4743ffu,0x341c24ffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x341b1fffu,0x6b4743ffu,0x3c242cffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x30161affu,0x684440ffu,0x2d151dffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x32181dffu,0x684440ffu,0x331c1fffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x331a1effu,0x6a4642ffu,0x331c1fffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x96a25cffu,0x694541ffu,0x341d20ffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0x96a25cffu,0x7b8245ffu,0x694541ffu,0x321a1effu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0x7e8559ffu,0x3b2226ffu,0x694541ffu,0x321a1effu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x341b1fffu,0x694541ffu,0x341d20ffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x331a1effu,0x6a4642ffu,0x331c1fffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x32181dffu,0x684440ffu,0x331c1fffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x30161affu,0x684440ffu,0x2d151dffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x3b2226ffu,0x6b4743ffu,0x3c242cffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff5eu,0xffffff5eu,0x341b1fffu,0x6b4743ffu,0x341c24ffu,0x50332fffu,0x50332fffu,0x50332fffu,0xffffff43u,0xffffff43u,0x341b1fffu,0x6a4642ffu,0x331b23ffu,0x50332fffu,0x50332fffu,0x50332fffu);
uint[] r = uint[](0x50332fffu,0x50332fffu,0x50332fffu,0x2f1921ffu,0x6d4d4affu,0x29151cffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x301a22ffu,0x6d4d4affu,0x2a151cffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2f181dffu,0x6b4c49ffu,0x291419ffu,0x97a359ffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2f181dffu,0x6d4c47ffu,0x291417ffu,0xa4b361ffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2e171affu,0x6c4b44ffu,0xa4b361ffu,0x7b8245ffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2d181affu,0x6b4d45ffu,0xa4b361ffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x341f21ffu,0x6b4d45ffu,0x392125ffu,0x97a359ffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x321a1effu,0x694541ffu,0x341b1fffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x321a1effu,0x694541ffu,0x341b1fffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x341f21ffu,0x6b4d45ffu,0x392125ffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2d181affu,0x6b4d45ffu,0x2d1619ffu,0x97a359ffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2e171affu,0x6c4b44ffu,0x281316ffu,0x7b8245ffu,0x97a359ffu,0x50332fffu,0x50332fffu,0x50332fffu,0x2f181dffu,0x6d4c47ffu,0x97a170ffu,0x7b8245ffu,0x97a170ffu,0x50332fffu,0x50332fffu,0x50332fffu,0x2f181dffu,0x6b4c49ffu,0x291419ffu,0x97a170ffu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x301a22ffu,0x6d4d4affu,0x2a151cffu,0xffffff5eu,0xffffff5eu,0x50332fffu,0x50332fffu,0x50332fffu,0x2f1921ffu,0x6d4d4affu,0x29151cffu,0xffffff5eu,0xffffff5eu);
uint[] b = uint[](0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x50332fffu,0x2f1921ffu,0x301a22ffu,0x2f181dffu,0x2f181dffu,0x2e171affu,0x2d181affu,0x341f21ffu,0x321e20ffu,0x321a1effu,0x341d20ffu,0x331c1fffu,0x331c1fffu,0x2d151dffu,0x3c242cffu,0x341c24ffu,0x331b23ffu,0x6d4d4affu,0x6d4d4affu,0x6b4c49ffu,0x6d4c47ffu,0x6c4b44ffu,0x6b4d45ffu,0x6b4d45ffu,0x6a4c44ffu,0x694541ffu,0x694541ffu,0x6a4642ffu,0x684440ffu,0x684440ffu,0x6b4743ffu,0x6b4743ffu,0x6a4642ffu,0x351e1fffu,0x341b1fffu,0x291419ffu,0x291417ffu,0x341b1fffu,0x341b1fffu,0x96a25cffu,0x362124ffu,0x341b1fffu,0x341b1fffu,0x331a1effu,0x32181dffu,0x30161affu,0x3b2226ffu,0x341b1fffu,0x341b1fffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0x7e8559ffu,0x7b8245ffu,0x97a170ffu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu,0xffffff5eu);
