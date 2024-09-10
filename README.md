# dpnc-langserver
### langchain for dpnc
This repository contains the langserver for the DCPNC service. 
It serves as a project skeleton and is not intended for production use. 
It utilizes an LLM (Large Language Model) to translate bar graph results into natural language, making the data easier for people to understand.


#### Todo
 - You need to create a /.prompt directory and a prompt.txt file inside it if they do not already exist.

#### Run

```shell
cd my-app
poetry run langchain serve --port=8123
```

#### End Point
URL : http://localhost:8123/analyze/stream_log
```json
{"input":{"input_data":"{\"title\":\"'서울' 지역의 평당 가격 정보\",\"x\":[\"2015-10\",\"2015-11\",\"2015-12\",\"2016-01\",\"2016-02\",\"2016-03\",\"2016-04\",\"2016-05\",\"2016-06\",\"2016-07\",\"2016-08\",\"2016-09\",\"2016-10\",\"2016-11\",\"2016-12\",\"2017-01\",\"2017-02\",\"2017-03\",\"2017-04\",\"2017-05\",\"2017-06\",\"2017-07\",\"2017-08\",\"2017-09\",\"2017-10\",\"2017-11\",\"2017-12\",\"2018-01\",\"2018-02\",\"2018-03\",\"2018-04\",\"2018-05\",\"2018-06\",\"2018-07\",\"2018-08\",\"2018-09\",\"2018-10\",\"2018-11\",\"2018-12\",\"2019-01\",\"2019-02\",\"2019-03\",\"2019-04\",\"2019-05\",\"2019-06\",\"2019-07\",\"2019-08\",\"2019-09\",\"2019-10\",\"2019-11\",\"2019-12\",\"2020-01\",\"2020-02\",\"2020-03\",\"2020-04\",\"2020-05\",\"2020-06\",\"2020-07\",\"2020-08\",\"2020-09\",\"2020-10\",\"2020-11\",\"2020-12\",\"2021-01\",\"2021-02\",\"2021-03\",\"2021-04\",\"2021-05\",\"2021-06\",\"2021-07\",\"2021-08\",\"2021-09\",\"2021-10\",\"2021-11\",\"2021-12\",\"2022-01\",\"2022-02\",\"2022-03\",\"2022-04\",\"2022-05\",\"2022-06\",\"2022-07\",\"2022-08\",\"2022-09\",\"2022-10\",\"2022-11\",\"2022-12\",\"2023-01\",\"2023-02\",\"2023-03\",\"2023-04\",\"2023-05\",\"2023-06\",\"2023-07\",\"2023-08\",\"2023-09\",\"2023-10\",\"2023-11\",\"2023-12\",\"2024-01\",\"2024-02\",\"2024-03\",\"2024-04\",\"2024-05\",\"2024-06\"],\"y\":{\"전체\":[19309.090185,19999.999250,19970.247185,20191.734780,20201.652135,20406.610805,20631.404185,20707.437240,20522.313280,20674.379390,20776.858725,20770.247155,21157.024000,21057.850450,21299.172755,21322.313250,21368.594240,21057.850450,21044.627310,21157.024000,22039.668595,21728.924805,20403.305020,21510.742995,21745.453730,22006.610745,22168.594210,21894.214055,21920.660335,22598.346260,22614.875185,22872.726415,22128.924790,22545.453700,22251.238835,23120.660290,24390.081730,24360.329665,24456.197430,25123.966000,25213.222195,25692.561020,25732.230440,25738.842010,26776.858500,26667.767595,26753.718005,26727.271725,26747.106435,26651.238670,26297.519675,26846.279985,26353.718020,26542.147765,26413.222150,27077.684935,27606.610535,26809.916350,26770.246930,26823.139490,26707.437015,27219.833690,28317.354310,28317.354310,28231.403900,28340.494805,28185.122910,28647.932810,29193.387335,30449.585635,31401.651715,31408.263285,31940.494670,32899.172320,33001.651655,31676.031870,32452.891345,31890.907895,32300.825235,28264.461750,28264.461750,28264.461750,27348.759305,28109.089855,28109.089855,29887.602185,29831.403840,30684.296370,30499.172410,30677.684800,30697.519510,31120.659990,31983.469875,31983.469875,31851.238475,32056.197145,32211.569040,34204.957395,35008.263150,37137.188690,37874.378745,38009.915930,38909.089450,38697.519210,41904.130660],\"60㎡이하\":[18684.296820,20892.561200,20895.866985,21246.280195,21282.643830,21652.891750,21877.685130,21943.800830,21692.561170,21854.544635,21791.734720,21702.478525,22019.833885,22132.230575,22191.734705,22023.139670,22042.974380,21719.007450,21719.007450,21791.734720,21355.371100,21520.660350,21061.156235,22370.247095,22528.924775,22912.395835,23157.023925,22803.304930,22833.056995,23778.511505,23788.428860,24191.734630,23907.437120,24330.577600,23527.271845,21920.660335,22499.172710,23196.693345,24456.197430,24462.809000,25302.478390,25619.833750,26095.866790,26790.081640,27375.205585,27209.916335,27183.470055,27123.965925,27206.610550,27094.213860,26826.445275,27537.189050,27084.296505,28208.263405,27818.180775,27874.379120,28337.189020,27352.065090,27299.172530,27408.263435,27262.808895,27887.602260,28730.577435,28730.577435,28618.180745,28687.602230,28608.263390,29011.569160,29586.775750,31342.147585,32145.453340,32145.453340,33656.197085,34885.949105,34885.949105,32935.535955,34122.312770,33242.973960,33943.800380,29424.792285,29424.792285,29424.792285,28614.874960,28614.874960,28614.874960,30436.362495,30360.329440,31282.643455,31157.023625,31375.205435,31391.734360,31735.536000,31586.775675,31586.775675,31365.288080,31659.502945,31894.213680,33933.883025,34399.998710,36902.477955,37626.444870,37795.039905,38657.849790,38591.734090,39160.329110],\"60㎡초과 85㎡이하\":[19444.627370,19715.701740,19722.313310,19953.718260,19963.635615,20254.544695,20482.643860,20512.395925,20555.371130,21153.718215,21236.362840,21196.693420,21609.916545,21514.048780,21461.156220,21487.602500,21560.329770,21223.139700,21203.304990,21358.676885,21272.726475,20965.288470,19662.809180,19629.751330,19616.528190,19500.825715,19398.346380,19361.982745,21067.767805,21662.809105,21685.949600,21917.354550,22277.685115,22842.974350,22499.172710,23745.453655,25219.833765,25190.081700,26082.643650,26793.387425,26912.395685,27077.684935,27345.453520,27557.023760,28390.081580,28119.007210,28304.131170,28337.189020,28343.800590,27438.015500,27011.569235,26892.560975,26909.089900,26975.205600,26780.164285,27490.908060,28350.412160,26608.263465,26591.734540,26561.982475,26489.255205,27047.932870,26089.255220,26089.255220,26013.222165,26009.916380,25514.048630,25583.470115,25963.635390,31467.767415,31467.767415,31464.461630,33890.907820,35342.147435,35523.965610,33917.354100,33775.205345,33775.205345,33775.205345,26261.156040,26261.156040,26261.156040,27140.494850,28393.387365,28393.387365,30409.916215,30409.916215,30740.494715,30128.924490,29695.866655,29788.428635,29788.428635,30826.445125,30826.445125,30700.825295,30776.858350,30839.668265,33609.916095,34238.015245,34238.015245,34895.866460,35927.271380,37355.370500,36485.949045,41401.651340],\"85㎡초과 102㎡이하\":[18912.395985,23444.627220,21530.577705,21530.577705,21530.577705,23732.230515,26763.635360,25537.189125,25560.329620,25560.329620,24033.056950,24512.395775,24462.809000,22310.742965,23239.668550,23239.668550,21999.999175,21345.453745,21345.453745,21183.470280,23557.023910,23557.023910,23361.982595,26072.726295,24046.280090,24168.594135,24720.660230,24720.660230,24776.858575,25861.156055,25861.156055,26770.246930,25094.213935,25094.213935,21990.081820,16730.577885,22618.180970,22618.180970,22618.180970,22618.180970,22618.180970,22618.180970,22618.180970,22618.180970,42076.031480,42076.031480,42076.031480,42076.031480,42076.031480,42076.031480,42076.031480,42076.031480,45735.535475,45735.535475,45735.535475,36423.139130,41609.915795,32852.891330,32852.891330,32852.891330,32852.891330,32852.891330,32294.213665,32294.213665,29560.329470,29560.329470,29560.329470,30171.899695,23206.610700,23057.850375,23057.850375,23285.949540,23285.949540,23285.949540,24046.280090,24046.280090,23897.519765,23897.519765,23897.519765,23897.519765,23897.519765,23897.519765,23897.519765,0.000000,0.000000,28383.470010,28383.470010,28383.470010,28383.470010,28383.470010,28383.470010,28383.470010,33246.279745,33246.279745,33246.279745,33246.279745,34809.916050,41236.362090,41236.362090,41236.362090,41236.362090,41236.362090,41236.362090,41236.362090,39500.824965],\"102㎡초과\":[19434.710015,21656.197535,21656.197535,21656.197535,21348.759530,21061.156235,21001.652105,21001.652105,21041.321525,21067.767805,21828.098355,21722.313235,23937.189185,20991.734750,22383.470235,22383.470235,22786.776005,22178.511565,22188.428920,22066.114875,22971.899965,22261.156190,20674.379390,22112.395865,21682.643815,22743.800800,22862.809060,22862.809060,22839.668565,23940.494970,23940.494970,23973.552820,22826.445425,22856.197490,21411.569445,21613.222330,24373.552805,24300.825535,24942.147825,25742.147795,24224.792480,23821.486710,25398.346155,25887.602335,27867.767550,27867.767550,29309.089810,29659.503020,29431.403855,29593.387320,29715.701365,29021.486515,29880.990615,29867.767475,31047.932720,31094.213710,31097.519495,28776.858425,28776.858425,28770.246855,28684.296445,28684.296445,31342.147585,31342.147585,31342.147585,31342.147585,32175.205405,30135.536060,29963.635240,0.000000,0.000000,0.000000,0.000000,0.000000,29464.461705,29464.461705,29464.461705,29464.461705,29464.461705,29464.461705,29464.461705,29464.461705,29464.461705,29464.461705,32671.073155,32671.073155,35880.990390,35880.990390,35880.990390,35880.990390,35880.990390,39375.205135,39375.205135,39401.651415,39401.651415,39401.651415,41160.329035,49315.700630,49315.700630,45487.601600,45487.601600,45487.601600,45097.518970,54819.832655]}}"},"config":{}}
```
