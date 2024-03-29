import os

arquivo1 = open('manager.json','w')
arquivo2 = open('watchers.json','w')
b = [
    {
        "name": "[CV] [Qt] OpenCV GUI",
        "managers": [
            "csaftoiu",
            "merlin"
        ],
        "watchers": [
            "merlin",
            "morris"
        ],
        "priority": 850
    },
    {
        "name": "[Web] pm-site",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 260
    },
    {
        "name": "Annotations",
        "managers": [
            "luanda"
        ],
        "watchers": [
            "csaftoiu",
            "merlin",
            "victor"
        ],
        "priority": 10
    },
    {
        "name": "[OCR] tesseract MRZ reading ",
        "managers": [
            "csaftoiu"
        ],
        "watchers": [
            "arturc",
            "merlin"
        ],
        "priority": 560
    },
    {
        "name": "Deepgammon",
        "managers": [
            "morris"
        ],
        "watchers": [
            "merlin",
            "victor"
        ],
        "priority": 150
    },
    {
        "name": "python training lucas",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "morris"
        ],
        "priority": 2160
    },
    {
        "name": "python training alysson",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "morris"
        ],
        "priority": 2180
    },
    {
        "name": "unity render different passport text",
        "managers": [
            "csaftoiu"
        ],
        "watchers": [
            "merlin",
            "morris"
        ],
        "priority": 2230
    },
    {
        "name": "[template] unity render passport text",
        "managers": [
            "csaftoiu"
        ],
        "watchers": [
            "merlin",
            "morris"
        ],
        "priority": 2235
    },
    {
        "name": "unity render diff passport text artur",
        "managers": [
            "arturc",
            "csaftoiu"
        ],
        "watchers": [
            "merlin",
            "morris"
        ],
        "priority": 815
    },
    {
        "name": "unity render diff passport text - kennedy",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "merlin",
            "morris"
        ],
        "priority": 2260
    },
    {
        "name": "Unity Render Passport Text [Template]",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "merlin",
            "morris"
        ],
        "priority": 2265
    },
    {
        "name": "mateus silva bg deep checkers",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2295
    },
    {
        "name": "Android Camera App rrocha",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2300
    },
    {
        "name": "bg deep learning aporto",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2305
    },
    {
        "name": "bg deep checkers rvalentim",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2310
    },
    {
        "name": "tourney site famador",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2320
    },
    {
        "name": "chess board finder eliaquim",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "victor-mgr"
        ],
        "priority": 2330
    },
    {
        "name": "tourney site ariel",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2340
    },
    {
        "name": "tourney site tbarbalho",
        "managers": [
            "victor-mgr"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 2345
    },
    {
        "name": "[CHESS] Live Demo Executive",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "morris"
        ],
        "priority": 750
    },
    {
        "name": "[EXECUTIVE] Merlin",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "merlin",
            "morris"
        ],
        "priority": 20
    },
    {
        "name": "[INHOUSE-TOOLS] NN-Webapp",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "merlin",
            "morris"
        ],
        "priority": 755
    },
    {
        "name": "[INHOUSE-TOOLS] Annotators app",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 760
    },
    {
        "name": "[IOS-APPS] IOS streaming app",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2375
    },
    {
        "name": "[IOS-APPS] IOS PI app",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2380
    },
    {
        "name": "[HR] Candidate tests",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2385
    },
    {
        "name": "[CHATBOT] merlin",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2390
    },
    {
        "name": "[ID-VERIFY-PIPELINE] finger detector",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 735
    },
    {
        "name": "[ID-VERIFY-PIPELINE] Background evaluator",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2395
    },
    {
        "name": "[ID-VERIFY-PIPELINE] Passport finder",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2400
    },
    {
        "name": "[CHATBOT] rodrigo",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2405
    },
    {
        "name": "[BG-CLUB-SITE] frontend",
        "managers": [
            "ariel",
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "morris"
        ],
        "priority": 2435
    },
    {
        "name": "morris bg data gathering",
        "managers": [
            "victor"
        ],
        "watchers": [
            "csaftoiu",
            "morris"
        ],
        "priority": 130
    },
    {
        "name": "sportsparsers - pinnacle API",
        "managers": [
            "csaftoiu"
        ],
        "watchers": [
            "Alex",
            "csaftoiu",
            "morris"
        ],
        "priority": 340
    },
    {
        "name": "[INHOUSE-TOOLS] NN-Webapp 2",
        "managers": [
            "merlin"
        ],
        "watchers": [
            "csaftoiu",
            "jpfarias",
            "merlin",
            "morris"
        ],
        "priority": 2520
    },
    {
        "name": "sportsparsers - tipster.de",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 295
    },
    {
        "name": "sportsparsers - matchbook",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 395
    },
    {
        "name": "matchbook parser - mfilho",
        "managers": [
            "csaftoiu",
            "morris"
        ],
        "watchers": [
            "jpfarias",
            "merlin"
        ],
        "priority": 2575
    },
    {
        "name": "sportsparsers - gg.bet",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 310
    },
    {
        "name": "sportsparsers - betway",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 300
    },
    {
        "name": "Runningball Parser",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 155
    },
    {
        "name": "sportsparsers - unikrn",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 145
    },
    {
        "name": "sportsparsers - unibet",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 250
    },
    {
        "name": "sportsparsers - esportscalendar",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 55
    },
    {
        "name": "sportsparsers - 22bet",
        "managers": [
            "morris"
        ],
        "watchers": [
            "csaftoiu",
            "merlin"
        ],
        "priority": 45
    }
]

w = []
m = ''
p = -1
a = sorted(b, key=lambda k: k['priority'],reverse = True)
for i in a:
    for s in i['managers']:

        m = m + '"%s":['%(s)
        for x in a:
            if i['managers'] == x['managers']:
                m = m + '"%s",'%(x['name'])
        m = m[:-1] + '],'
arquivo1.write('{'+ m[:-1]+'}')
arquivo1.close()
print(' watchers ___________________________________________________')
m = ''
for i in a:
    for s in i['watchers']:
        m = m + '"%s":['%(s)
        for x in a:
            if i['watchers'] == x['watchers']:
                m = m + '"%s",'%(x['name'])
        m = m[:-1] + '],'
arquivo2.write('{'+ m[:-1]+'}')
arquivo2.close()