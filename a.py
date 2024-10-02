import os

vals =  ["bedrossian" ,"gubinelli" ,"otto" ,"blondel" ,"kiselev" ,"pehersthofer" ,"cicalese" ,"lubich" ,"rodrigues" ,"gallay" ,"maspero" ,"ryzhik" ,"giuliani" ,"michiels" ,"sasada" ,"gomez_serrano" ,"muratov" ,"xin" ,"graf" ,"nouy"]

names = [ "J. Bedrossian (UCLA)" ,"M. Gubinelli (Oxford)" ,"F. Otto (MIS-MPG Leipzig)" ,"O. Blondel (Lyon)" ,"A. Kiselev (Duke)" ,"B. Pehersthofer (NYU)" ,"M. Cicalese (TUM)" ,"C. Lubich (Tübingen)" ,"M. Rodrigues (Rennes)" ,"T. Gallay (Grenoble)" ,"A. Maspero (SISSA)" ,"L. Ryzhik (Stanford)" ,"A. Giuliani (Rome)" ,"W. Michiels (KULeuven)" ,"M. Sasada (Tokyo)" ,"J. Gomez-Serrano (Brown)" ,"C. Muratov (Pisa)" ,"Z. Xin (CUHK)" ,"G. M. Graf (ETH)" ,"A. Nouy (Nantes)"]



for i, v in enumerate(vals):
    dname = f"content/{v}"
    try:
        os.mkdir(dname)
    except:
        pass
    txt = f"""+++
title = "Course given by Prof. {names[i]}"
draft = false
LinkTitle = "{v}"
tags = 'course'
+++"""
    with open(f"{dname}/_index.md", 'w') as f:
        f.write(txt)





# |             |                                       |
# |-------------|---------------------------------------|
# |**14-18 April**|               [Prof. Gallay (Grenoble)](/gallay)   |
# |**14-18 April** |              [Prof. Rodrigues (Rennes)](/rodrigues)|
# |**14-18 April** |              [Prof. Lenya Ryzhik (Stanford)](/ryzhik)|
# |**21-25 April** |              [Prof Xin (Hong Kong)](/xin)|
# |**21-25 April** |              N - Wim Michiels (Leuven)* |
# |**28-2  April** |              N - Greif*|
# |**28-2  April** |              Prob - Oriane Blondel (Lyon)|
# |**28-2  April** |              Prob - Makiko Sasada (Tokyo)*|
# |**12-16 May** |                N - Matthew Colbroock (Cambridge) |
# |**12-16 May** |                N - Benjamin Peherstorfer (Courant Institute) |
# |**12-16 May** |                Prob - Gubinelli*|
# |**26-30 May** |                PDE - Cyrill Muratov (Pisa)|
# |**26-30 May** |                N - Christian Lubich (Tuebingen) |
# |**26-30 May** |                Prob/N - Gubinelli*/Graf*|
# |**2-6   June** |               N - Wim Michiels (Leuven)|
# |**2-6   June** |               N - Anthony Nouy (Centrale Nantes - Nantes Université)*|
# |**2-6   June** |               Prob/N  Gubinelli*/Graf*|
# |**9-13  June** |               PDE - Javier Gomez-Serrano (Brown)|
# |**9-13  June** |               N - Jean Philippe Lessard (Mc Gill)|
# |**9-13  June** |               PDE - Maspero (SISSA)|
# |**16-20 June** |               PDE - Kiselev|
# |**16-20 June** |               PDE - Bedrossian*|
# |**23-27 June** |               PDE - Felix Otto|
# |**23-27 June** |               PDE - Bedrossian*|
# |**23-27 June** |               PDE - Marco Cicalese|
# |**30-4  July** |               PDE - Bedrossian?|



|**14-18 April**|               [Prof. Gallay (Grenoble)](/gallay)   |
|**14-18 April** |              [Prof. Rodrigues (Rennes)](/rodrigues)|
|**14-18 April** |              [Prof. Lenya Ryzhik (Stanford)](/ryzhik)|
|**21-25 April** |              [Prof Xin (Hong Kong)](/xin)|
|**21-25 April** | [N - Wim Michiels (Leuven)*](/michiels)|
|**28-2  April** | [N - Greif*](/greif)|
|**28-2  April** | [Prob - Oriane Blondel (Lyon)](/blondel)|
|**28-2  April** | [Prob - Makiko Sasada (Tokyo)*](/sasada)|
|**12-16 May**   | [N - Matthew Colbroock (Cambridge)](/colbroock)|
|**12-16 May**   | [N - Benjamin Peherstorfer (Courant Institute)](/peherstorfer)|
|**12-16 May**   | [Prob - Gubinelli*](/gubinelli)|
|**26-30 May**   | [PDE - Cyrill Muratov (Pisa)](/muratov)|
|**26-30 May**   | [N - Christian Lubich (Tuebingen)](/lubich)|
|**26-30 May**   | [Prob/N - Gubinelli*/Graf*](/graf)|
|**2-6   June**  | [N - Wim Michiels (Leuven)](michiels)|
|**2-6   June**  | [N - Anthony Nouy (Centrale Nantes - Nantes Université)*](/nouy)|
|**2-6   June**  | [Prob/N  Gubinelli*/Graf*]()|
|**9-13  June**  | [PDE - Javier Gomez-Serrano (Brown)]()|
|**9-13  June**  | [N - Jean Philippe Lessard (Mc Gill)]()|
|**9-13  June**  | [PDE - Maspero (SISSA)]()|
|**16-20 June**  | [PDE - Kiselev]()|
|**16-20 June**  | [PDE - Bedrossian*]()|
|**23-27 June**  | [PDE - Felix Otto]()|
|**23-27 June**  | [PDE - Bedrossian*]()|
|**23-27 June**  | [PDE - Marco Cicalese]()|
|**30-4  July**  | [PDE - Bedrossian?]()|





vals = [
       ["**21-25 April** "      ,       "N - Wim Michiels (Leuven)*                    "  ],
       [ "**28-2  April** "      ,       "N - Greif*                                    " ],
       [ "**28-2  April** "      ,       "Prob - Oriane Blondel (Lyon)                  " ],
       [ "**28-2  April** "      ,       "Prob - Makiko Sasada (Tokyo)*                 " ],
       [ "**12-16 May**   "      ,       "N - Matthew Colbroock (Cambridge)             " ],
       [ "**12-16 May**   "      ,       "N - Benjamin Peherstorfer (Courant Institute) " ],
       [ "**12-16 May**   "      ,       "Prob - Gubinelli*                             " ],
       [ "**26-30 May**   "      ,       "PDE - Cyrill Muratov (Pisa)                   " ],
       [ "**26-30 May**   "      ,       "N - Christian Lubich (Tuebingen)              " ],
       [ "**26-30 May**   "      ,       "Prob/N - Gubinelli*/Graf*                     " ],
       [ "**2-6   June**  "      ,       "N - Wim Michiels (Leuven)                     " ],
       [ "**2-6   June**  "      ,       "N - Anthony Nouy (Centrale Nantes - Nantes Université)*"],
       [ "**2-6   June**  "      ,       "Prob/N  Gubinelli*/Graf*                      " ],
       [ "**9-13  June**  "      ,       "PDE - Javier Gomez-Serrano (Brown)            " ],
       [ "**9-13  June**  "      ,       "N - Jean Philippe Lessard (Mc Gill)           " ],
       [ "**9-13  June**  "      ,       "PDE - Maspero (SISSA)                         " ],
       [ "**16-20 June**  "      ,       "PDE - Kiselev                                 " ],
       [ "**16-20 June**  "      ,       "PDE - Bedrossian*                             " ],
       [ "**23-27 June**  "      ,       "PDE - Felix Otto                              " ],
       [ "**23-27 June**  "      ,       "PDE - Bedrossian*                             " ],
       [ "**23-27 June**  "      ,       "PDE - Marco Cicalese                          " ],
       [ "**30-4  July**  "      ,       "PDE - Bedrossian?                             "]
        ]

for v in vals:
    print(f"|{v[0]}| [{v[1].strip()}]()|")
