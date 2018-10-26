{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red87\green96\blue106;\red27\green31\blue34;\red255\green255\blue255;
\red109\green109\blue109;\red21\green23\blue26;\red6\green33\blue79;\red203\green35\blue57;\red7\green68\blue184;
\red218\green76\blue12;\red91\green40\blue180;}
{\*\expandedcolortbl;;\cssrgb\c41569\c45098\c49020;\cssrgb\c14118\c16078\c18039;\cssrgb\c100000\c100000\c100000;
\cssrgb\c50196\c50196\c50196;\cssrgb\c10588\c12157\c13725\c29804;\cssrgb\c1176\c18431\c38431;\cssrgb\c84314\c22745\c28627;\cssrgb\c0\c36078\c77255;
\cssrgb\c89020\c38431\c3529;\cssrgb\c43529\c25882\c75686;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clmrg \clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #!/usr/bin/env python\cf3 \strokec3 \cell 
\pard\intbl\itap1\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # -*- coding: utf-8 -*-\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 Module: dspipeline.py\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 Author: zlamberty\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 Created: 2018-10-19\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 Description:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     simple data science pipeline functions and a demo which uses these tools to\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     model a freely available dataset\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 Usage:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     <usage>\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7 """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  argparse\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  logging\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  logging.config\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  os\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  shutil\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  tempfile\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  warnings\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  numpy \cf8 \strokec8 as\cf3 \strokec3  np\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  pandas \cf8 \strokec8 as\cf3 \strokec3  pd\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  plotly.graph_objs \cf8 \strokec8 as\cf3 \strokec3  go\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  plotly.offline\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.datasets\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.ensemble\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.externals.joblib\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.feature_selection\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.linear_model\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.model_selection\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.neural_network\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.pipeline\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 import\cf3 \strokec3  sklearn.preprocessing\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 from\cf3 \strokec3  sklearn.exceptions \cf8 \strokec8 import\cf3 \strokec3  ConvergenceWarning\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # ----------------------------- #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 #   Module Constants            #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # ----------------------------- #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # set up a logger to print out log messages\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf9 \strokec9 LOGGER\cf3 \strokec3  \cf8 \strokec8 =\cf3 \strokec3  logging.getLogger(\cf7 \strokec7 'dspipeline'\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 logging.config.dictConfig(\{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 'version'\cf3 \strokec3 : \cf9 \strokec9 1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 'disable_existing_loggers'\cf3 \strokec3 : \cf9 \strokec9 False\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 'formatters'\cf3 \strokec3 : \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'default'\cf3 \strokec3 : \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'format'\cf3 \strokec3 : \cf7 \strokec7 '\cf9 \strokec9 %(asctime)s\cf7 \strokec7  \cf9 \strokec9 %(levelname)-8s\cf7 \strokec7  [\cf9 \strokec9 %(name)s\cf7 \strokec7 .\cf9 \strokec9 %(funcName)s\cf7 \strokec7 :\cf9 \strokec9 %(lineno)d\cf7 \strokec7 ] \cf9 \strokec9 %(message)s\cf7 \strokec7 '\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'simple'\cf3 \strokec3 : \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'format'\cf3 \strokec3 : \cf7 \strokec7 '\cf9 \strokec9 %(asctime)s\cf7 \strokec7  \cf9 \strokec9 %(levelname)-8s\cf7 \strokec7  [\cf9 \strokec9 %(name)s\cf7 \strokec7 ] \cf9 \strokec9 %(message)s\cf7 \strokec7 '\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'print'\cf3 \strokec3 : \{\cf7 \strokec7 'format'\cf3 \strokec3 : \cf7 \strokec7 '\cf9 \strokec9 %(message)s\cf7 \strokec7 '\cf3 \strokec3 \}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 'root'\cf3 \strokec3 : \{\cf7 \strokec7 'level'\cf3 \strokec3 : \cf7 \strokec7 'DEBUG'\cf3 \strokec3 , \cf7 \strokec7 'handlers'\cf3 \strokec3 : [\cf7 \strokec7 'console'\cf3 \strokec3 ]\},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 'handlers'\cf3 \strokec3 : \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'console'\cf3 \strokec3 : \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'class'\cf3 \strokec3 : \cf7 \strokec7 'logging.StreamHandler'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'formatter'\cf3 \strokec3 : \cf7 \strokec7 'default'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'stream'\cf3 \strokec3 : \cf7 \strokec7 'ext://sys.stdout'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'print'\cf3 \strokec3 : \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'class'\cf3 \strokec3 : \cf7 \strokec7 'logging.StreamHandler'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'formatter'\cf3 \strokec3 : \cf7 \strokec7 'print'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf7 \strokec7 'stream'\cf3 \strokec3 : \cf7 \strokec7 'ext://sys.stdout'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 'loggers'\cf3 \strokec3 : \{\cf7 \strokec7 'print'\cf3 \strokec3 : \{\cf7 \strokec7 'handlers'\cf3 \strokec3 : [\cf7 \strokec7 'print'\cf3 \strokec3 ], \cf7 \strokec7 'propagate'\cf3 \strokec3 : \cf9 \strokec9 False\cf3 \strokec3 \}\}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \})\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # intentionally surpress some annoying sklearn warning messages\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 warnings.filterwarnings(\cf7 \strokec7 'ignore'\cf3 \strokec3 , \cf10 \strokec10 category\cf8 \strokec8 =\cf9 \strokec9 UserWarning\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 warnings.filterwarnings(\cf7 \strokec7 'ignore'\cf3 \strokec3 , \cf10 \strokec10 category\cf8 \strokec8 =\cf3 \strokec3 ConvergenceWarning)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 warnings.filterwarnings(\cf7 \strokec7 'ignore'\cf3 \strokec3 , \cf10 \strokec10 category\cf8 \strokec8 =\cf9 \strokec9 FutureWarning\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # ----------------------------- #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 #   utilities                   #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # ----------------------------- #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 fix_column_names\cf3 \strokec3 (df):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """replace dashes with underscores. eventually should handle punctuation"""\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df.columns \cf8 \strokec8 =\cf3 \strokec3  [col.lower().replace(\cf7 \strokec7 '-'\cf3 \strokec3 , \cf7 \strokec7 '_'\cf3 \strokec3 ) \cf8 \strokec8 for\cf3 \strokec3  col \cf8 \strokec8 in\cf3 \strokec3  df.columns]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 my_cv\cf3 \strokec3 (N\cf8 \strokec8 =\cf9 \strokec9 10\cf3 \strokec3 ):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """factory for creating my prefered cross validation object\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         N (int): the number of folds in our bootstrapping cross validation\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     returns\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         sklearn.model_selection.StratifiedShuffleSplit: the cv object\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  sklearn.model_selection.StratifiedShuffleSplit(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 n_splits\cf8 \strokec8 =\cf3 \strokec3 N,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 test_size\cf8 \strokec8 =\cf9 \strokec9 0.2\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 cross_validate_scores\cf3 \strokec3 (pipelines, X, y, cv\cf8 \strokec8 =\cf9 \strokec9 None\cf3 \strokec3 ):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """given an iterable of pipelines, perform cross-validated scoring\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         pipelines (iterable): a list or iterable of sklearn pipelines\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         X (nd.array): observed predictors\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         y (nd.array): observed targets\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         cv (sklearn.model_selection object): a scikit learn cross validation\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7             object. if `None`, will default to the value defined by `my_cv`\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     returns\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         pd.DataFrame: dataframe of score information\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     raises:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         None\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf9 \strokec9 LOGGER\cf3 \strokec3 .info(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'performing cross validated scoring on \cf9 \strokec9 \{\}\cf7 \strokec7  pipelines'\cf3 \strokec3 .format(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf9 \strokec9 len\cf3 \strokec3 (pipelines)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     cv \cf8 \strokec8 =\cf3 \strokec3  cv \cf8 \strokec8 or\cf3 \strokec3  my_cv()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     dfscores \cf8 \strokec8 =\cf3 \strokec3  pd.DataFrame()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 for\cf3 \strokec3  p \cf8 \strokec8 in\cf3 \strokec3  pipelines:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         fsname \cf8 \strokec8 =\cf3 \strokec3  p.steps[\cf9 \strokec9 0\cf3 \strokec3 ][\cf9 \strokec9 0\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         mname \cf8 \strokec8 =\cf3 \strokec3  p.steps[\cf9 \strokec9 1\cf3 \strokec3 ][\cf9 \strokec9 0\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf9 \strokec9 LOGGER\cf3 \strokec3 .debug(\cf7 \strokec7 'feature selection method: \cf9 \strokec9 \{\}\cf7 \strokec7 '\cf3 \strokec3 .format(fsname))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf9 \strokec9 LOGGER\cf3 \strokec3 .debug(\cf7 \strokec7 'modelling method: \cf9 \strokec9 \{\}\cf7 \strokec7 '\cf3 \strokec3 .format(mname))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         score \cf8 \strokec8 =\cf3 \strokec3  sklearn.model_selection.cross_validate(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 estimator\cf8 \strokec8 =\cf3 \strokec3 p,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 X\cf8 \strokec8 =\cf3 \strokec3 X,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 y\cf8 \strokec8 =\cf3 \strokec3 y,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 return_train_score\cf8 \strokec8 =\cf9 \strokec9 True\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 scoring\cf8 \strokec8 =\cf3 \strokec3 (\cf7 \strokec7 'accuracy'\cf3 \strokec3 , \cf7 \strokec7 'neg_log_loss'\cf3 \strokec3 ),\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 cv\cf8 \strokec8 =\cf3 \strokec3 cv,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 n_jobs\cf8 \strokec8 =-\cf9 \strokec9 1\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         score[\cf7 \strokec7 'fs'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  fsname\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         score[\cf7 \strokec7 'm'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  mname\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         dfscoresnow \cf8 \strokec8 =\cf3 \strokec3  pd.DataFrame(score)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         dfscores \cf8 \strokec8 =\cf3 \strokec3  dfscores.append(dfscoresnow, \cf10 \strokec10 ignore_index\cf8 \strokec8 =\cf9 \strokec9 True\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     agg_results \cf8 \strokec8 =\cf3 \strokec3  dfscores.groupby([\cf7 \strokec7 'fs'\cf3 \strokec3 , \cf7 \strokec7 'm'\cf3 \strokec3 ]).train_neg_log_loss.agg(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         [\cf7 \strokec7 'mean'\cf3 \strokec3 , \cf7 \strokec7 'std'\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf9 \strokec9 LOGGER\cf3 \strokec3 .debug(\cf7 \strokec7 'cross-validation log loss results:\\n\cf9 \strokec9 \{\}\cf7 \strokec7 '\cf3 \strokec3 .format(agg_results))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  dfscores\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 feature_importance_df\cf3 \strokec3 (clf, feature_names):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """create a pandas dataframe of feature importance values\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     the scikit learn estimator object `clf` must have a `get_support` method and\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     an `estimator_` attribute with a `feature_importances_` attribute (i.e. both\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     `clf.get_support()` and `clf.estimator_.feature_importances_` must be\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     defined)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          clf (scikit-learn model object): the scikit learn modelling object\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7               which has estimated feature importance information\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          feature_names (list): a list of feature names for the input columns\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     returns:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          pd.DataFrame: dataframe containing feature importance and support info\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     raises:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          None\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_support \cf8 \strokec8 =\cf3 \strokec3  pd.DataFrame(\{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'feature'\cf3 \strokec3 : feature_names,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'support'\cf3 \strokec3 : clf.get_support()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \})\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # we only have feature importance for records where `support` is true\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_support.loc[\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         df_support.support, \cf7 \strokec7 'importance'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ] \cf8 \strokec8 =\cf3 \strokec3  clf.estimator_.feature_importances_\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_support \cf8 \strokec8 =\cf3 \strokec3  df_support.sort_values(\cf10 \strokec10 by\cf8 \strokec8 =\cf7 \strokec7 'importance'\cf3 \strokec3 , \cf10 \strokec10 ascending\cf8 \strokec8 =\cf9 \strokec9 False\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  df_support\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 feature_importance_plot\cf3 \strokec3 (df_support, height\cf8 \strokec8 =\cf9 \strokec9 1200\cf3 \strokec3 , margin\cf8 \strokec8 =\cf9 \strokec9 250\cf3 \strokec3 ):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """create a plotly barchart showing feature importance values\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          df_support (pd.DataFrame): a dataframe containing support information.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7              must have the columns `feature`, `support`, and `importance`\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          height (int): height of plotly.graph_objs.Layout object (default: 1200)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          margin (int): margin of plotly.graph_objs.Layout object (default: 250)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     returns:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          plotly.Figure: the plotly figure object which was plotted\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     raises:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          None\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # drop the features which weren't chosen, and invert the sort  order (plotly\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # adds bars in this "top to bottom" way for  horizontal bar charts)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     nonzero \cf8 \strokec8 =\cf3 \strokec3  df_support[df_support.support].sort_values(\cf10 \strokec10 by\cf8 \strokec8 =\cf7 \strokec7 'importance'\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     data \cf8 \strokec8 =\cf3 \strokec3  [go.Bar(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 x\cf8 \strokec8 =\cf3 \strokec3 nonzero.importance,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 y\cf8 \strokec8 =\cf3 \strokec3 nonzero.feature,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 orientation\cf8 \strokec8 =\cf7 \strokec7 'h'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # this is\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     layout \cf8 \strokec8 =\cf3 \strokec3  go.Layout(\cf10 \strokec10 height\cf8 \strokec8 =\cf3 \strokec3 height, \cf10 \strokec10 margin\cf8 \strokec8 =\cf3 \strokec3 go.layout.Margin(\cf10 \strokec10 l\cf8 \strokec8 =\cf3 \strokec3 margin))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     fig \cf8 \strokec8 =\cf3 \strokec3  go.Figure(\cf10 \strokec10 data\cf8 \strokec8 =\cf3 \strokec3 data, \cf10 \strokec10 layout\cf8 \strokec8 =\cf3 \strokec3 layout)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     plotly.offline.iplot(fig)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  fig\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 get_ccr_df\cf3 \strokec3 (clf, X, y):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """calculate cumulative capture rate values given a predictor object and\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     observed X and y values\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          clf (scikit-learn model object): the scikit learn modelling object\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7               which has a predict_proba method\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          X (np.array-like): observed predictors\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7          y (np.array-like): observed targets\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     y_pred \cf8 \strokec8 =\cf3 \strokec3  clf.predict_proba(X)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr \cf8 \strokec8 =\cf3 \strokec3  pd.DataFrame(\{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'y_obs'\cf3 \strokec3 : y,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'y_pred'\cf3 \strokec3 : y_pred[:, \cf9 \strokec9 1\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \})\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr \cf8 \strokec8 =\cf3 \strokec3  df_ccr.sort_values(\cf10 \strokec10 by\cf8 \strokec8 =\cf7 \strokec7 'y_pred'\cf3 \strokec3 , \cf10 \strokec10 ascending\cf8 \strokec8 =\cf9 \strokec9 False\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ntargets \cf8 \strokec8 =\cf3 \strokec3  df_ccr.y_obs.sum()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr.loc[:, \cf7 \strokec7 'ccr'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  df_ccr.y_obs.cumsum() \cf8 \strokec8 /\cf3 \strokec3  ntargets\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # we will also define *perfect* capture and *random* capture\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     xarr \cf8 \strokec8 =\cf3 \strokec3  np.array(\cf9 \strokec9 range\cf3 \strokec3 (df_ccr.shape[\cf9 \strokec9 0\cf3 \strokec3 ]))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr.loc[:, \cf7 \strokec7 'x'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  xarr\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     yperf \cf8 \strokec8 =\cf3 \strokec3  np.ones(xarr.shape)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     yperf[:ntargets] \cf8 \strokec8 =\cf3 \strokec3  np.linspace(\cf9 \strokec9 0\cf3 \strokec3 , \cf9 \strokec9 1\cf3 \strokec3 , ntargets)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr.loc[:, \cf7 \strokec7 'perfect'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  yperf\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr.loc[:, \cf7 \strokec7 'random'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  xarr \cf8 \strokec8 /\cf3 \strokec3  xarr.max()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  df_ccr\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 make_ccr_plot\cf3 \strokec3 (df_ccr):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """create a plotly plot of ccr values\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         df_ccr (pd.DataFrame): a pandas data frame containing ccr values.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7             assumes columns named `y_obs`, `y_pred`, `ccr`, `x`, `perfect`, and\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7             `random`\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     returns:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         plotly.graph_objs.Figure: the plotly figure object\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     data \cf8 \strokec8 =\cf3 \strokec3  [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf2 \strokec2 # our capture rate\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         go.Scatter(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 x\cf8 \strokec8 =\cf3 \strokec3 df_ccr.x,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 y\cf8 \strokec8 =\cf3 \strokec3 df_ccr.ccr,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 mode\cf8 \strokec8 =\cf7 \strokec7 'lines'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 line\cf8 \strokec8 =\cf3 \strokec3 \{\cf7 \strokec7 'width'\cf3 \strokec3 : \cf9 \strokec9 2\cf3 \strokec3 \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 name\cf8 \strokec8 =\cf7 \strokec7 'our prediction'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         ),\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf2 \strokec2 # random choice\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         go.Scatter(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 x\cf8 \strokec8 =\cf3 \strokec3 df_ccr.x,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 y\cf8 \strokec8 =\cf3 \strokec3 df_ccr.random,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 mode\cf8 \strokec8 =\cf7 \strokec7 'lines'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 line\cf8 \strokec8 =\cf3 \strokec3 \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 \cf7 \strokec7 'dash'\cf3 \strokec3 : \cf7 \strokec7 'dash'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 \cf7 \strokec7 'color'\cf3 \strokec3 : \cf7 \strokec7 'black'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 \cf7 \strokec7 'width'\cf3 \strokec3 : \cf9 \strokec9 1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 name\cf8 \strokec8 =\cf7 \strokec7 'random'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         ),\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf2 \strokec2 # perfect\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         go.Scatter(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 x\cf8 \strokec8 =\cf3 \strokec3 df_ccr.x,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 y\cf8 \strokec8 =\cf3 \strokec3 df_ccr.perfect,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 mode\cf8 \strokec8 =\cf7 \strokec7 'lines'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 line\cf8 \strokec8 =\cf3 \strokec3 \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 \cf7 \strokec7 'dash'\cf3 \strokec3 : \cf7 \strokec7 'dot'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 \cf7 \strokec7 'color'\cf3 \strokec3 : \cf7 \strokec7 'black'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 \cf7 \strokec7 'width'\cf3 \strokec3 : \cf9 \strokec9 1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 name\cf8 \strokec8 =\cf7 \strokec7 'perfect'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     layout \cf8 \strokec8 =\cf3 \strokec3  go.Layout(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 title\cf8 \strokec8 =\cf7 \strokec7 'cumulative captured response'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 xaxis\cf8 \strokec8 =\cf3 \strokec3 \{\cf7 \strokec7 'title'\cf3 \strokec3 : \cf7 \strokec7 'prediction certainty sort index (most certain to least)'\cf3 \strokec3 \},\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 yaxis\cf8 \strokec8 =\cf3 \strokec3 \{\cf7 \strokec7 'title'\cf3 \strokec3 : \cf7 \strokec7 'fraction of all true cases obtained'\cf3 \strokec3 \}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     fig \cf8 \strokec8 =\cf3 \strokec3  go.Figure(\cf10 \strokec10 data\cf8 \strokec8 =\cf3 \strokec3 data, \cf10 \strokec10 layout\cf8 \strokec8 =\cf3 \strokec3 layout)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     plotly.offline.iplot(fig)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  fig\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # ----------------------------- #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 #   demo using adult dataset    #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # ----------------------------- #\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 load_adult_income_data\cf3 \strokec3 (test_size\cf8 \strokec8 =\cf9 \strokec9 0.2\cf3 \strokec3 , random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 ):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """load a UCI dataset on adult income\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     the adult income dataset is available as part of the [UCI machine learning\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     repository](http://archive.ics.uci.edu/ml/index.php).\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     we *could* use the requests library to download and parse the column names\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     (available [here](http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names)),\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     but instead I've just hard-coded them below.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     also, we *could* use the pre-segregated train and test data sets as our\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     train and test, but that would involve some data munging and cleaning that\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     is a bit of a mess, and also results in enough data points in our final\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     plots that we'd have to change some annoying configuration variables.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     instead, let's pull only the smaller training dataset, and use the\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     `scikit-learn` train / test split function to create a test dataset of our\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     own.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     args:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         test_size (float): passed to the sklearn train_test_split function to\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7             determine the fractional size of the test set (default: 0.20)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         random_state (int): passed to the sklearn train_test_split function to\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7             set the random number generator seed (default: 0.20)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     returns:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         xtrain (np.array): train predictors\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         xtest (np.array): test predictors\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         ytrain (np.array): train target\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7         ytest (np.array): test target\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf7 \strokec7     """\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf9 \strokec9 LOGGER\cf3 \strokec3 .info(\cf7 \strokec7 'downloading adult data set'\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     columns \cf8 \strokec8 =\cf3 \strokec3  [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'age'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'workclass'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'fnlwgt'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'education'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'education-num'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'marital-status'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'occupation'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'relationship'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'race'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'sex'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'capital-gain'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'capital-loss'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'hours-per-week'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'native-country'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'target'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df \cf8 \strokec8 =\cf3 \strokec3  pd.read_csv(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 names\cf8 \strokec8 =\cf3 \strokec3 columns,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 delimiter\cf8 \strokec8 =\cf7 \strokec7 ', '\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 index_col\cf8 \strokec8 =\cf9 \strokec9 False\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 engine\cf8 \strokec8 =\cf7 \strokec7 'python'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  df.shape \cf8 \strokec8 ==\cf3 \strokec3  (\cf9 \strokec9 32561\cf3 \strokec3 , \cf9 \strokec9 15\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # we can use our utility function to fix up some of the column names\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     fix_column_names(df)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # `fnlwgt` and `education_num` should be dropped. Why?\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #     1. `fnlwgt` is a weighting for demographic sampling, and is an\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #        estimate of how many people fall into the given category. we're not\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #        going to use this weighting, so let's get rid of it.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #     2. `education_num` is a numerical representation of the values in the\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #        `education` column. You could argue that you should keep this\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #        numeric column and drop the `education` column, or convert\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #        `education` into a dummy column and drop `education_num`. we'll do\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 #        the latter.\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df \cf8 \strokec8 =\cf3 \strokec3  df.drop([\cf7 \strokec7 'fnlwgt'\cf3 \strokec3 , \cf7 \strokec7 'education_num'\cf3 \strokec3 ], \cf10 \strokec10 axis\cf8 \strokec8 =\cf9 \strokec9 1\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  df.shape[\cf9 \strokec9 1\cf3 \strokec3 ] \cf8 \strokec8 ==\cf3 \strokec3  \cf9 \strokec9 13\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # fixing dummy columns\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     dummycols \cf8 \strokec8 =\cf3 \strokec3  [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'workclass'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'education'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'marital_status'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'occupation'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'relationship'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'race'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'sex'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'native_country'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df \cf8 \strokec8 =\cf3 \strokec3  pd.get_dummies(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 data\cf8 \strokec8 =\cf3 \strokec3 df,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 dummy_na\cf8 \strokec8 =\cf9 \strokec9 False\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 columns\cf8 \strokec8 =\cf3 \strokec3 dummycols\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  df.shape[\cf9 \strokec9 1\cf3 \strokec3 ] \cf8 \strokec8 ==\cf3 \strokec3  \cf9 \strokec9 107\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # fixing column names again, after re-introducing some more noise\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     fix_column_names(df)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         _ \cf8 \strokec8 for\cf3 \strokec3  _ \cf8 \strokec8 in\cf3 \strokec3  df.columns \cf8 \strokec8 if\cf3 \strokec3  _.startswith(\cf7 \strokec7 'sex'\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \} \cf8 \strokec8 ==\cf3 \strokec3  \{\cf7 \strokec7 'sex_female'\cf3 \strokec3 , \cf7 \strokec7 'sex_male'\cf3 \strokec3 \}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # replace our string-valued target column with numerical 0/1 values:\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df.loc[:, \cf7 \strokec7 'target'\cf3 \strokec3 ] \cf8 \strokec8 =\cf3 \strokec3  (df.target \cf8 \strokec8 ==\cf3 \strokec3  \cf7 \strokec7 '>50K'\cf3 \strokec3 ).astype(\cf9 \strokec9 int\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  df.target.unique().tolist() \cf8 \strokec8 ==\cf3 \strokec3  [\cf9 \strokec9 0\cf3 \strokec3 , \cf9 \strokec9 1\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # dropping non-numeric features\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df \cf8 \strokec8 =\cf3 \strokec3  df._get_numeric_data()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  df.shape[\cf9 \strokec9 1\cf3 \strokec3 ] \cf8 \strokec8 ==\cf3 \strokec3  \cf9 \strokec9 107\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # `log`-transform of monetary features\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     moneycols \cf8 \strokec8 =\cf3 \strokec3  [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'capital_gain'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'capital_loss'\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df.loc[:, moneycols] \cf8 \strokec8 =\cf3 \strokec3  np.log1p(df[moneycols])\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  df.capital_gain.max() \cf8 \strokec8 <\cf3 \strokec3  \cf9 \strokec9 20\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # standardize non-target columns\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     nottarget \cf8 \strokec8 =\cf3 \strokec3  [col \cf8 \strokec8 for\cf3 \strokec3  col \cf8 \strokec8 in\cf3 \strokec3  df.columns \cf8 \strokec8 if\cf3 \strokec3  col \cf8 \strokec8 !=\cf3 \strokec3  \cf7 \strokec7 'target'\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df.loc[:, nottarget] \cf8 \strokec8 =\cf3 \strokec3  sklearn.preprocessing.scale(df[nottarget])\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  \cf8 \strokec8 -\cf9 \strokec9 2\cf3 \strokec3  \cf8 \strokec8 <\cf3 \strokec3  df.age.min() \cf8 \strokec8 <\cf3 \strokec3  \cf9 \strokec9 0\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  \cf9 \strokec9 0\cf3 \strokec3  \cf8 \strokec8 <\cf3 \strokec3  df.age.max() \cf8 \strokec8 <\cf3 \strokec3  \cf9 \strokec9 4\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # develop a train-test split\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     dftrain, dftest \cf8 \strokec8 =\cf3 \strokec3  sklearn.model_selection.train_test_split(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         df,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 test_size\cf8 \strokec8 =\cf3 \strokec3 test_size,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 random_state\cf8 \strokec8 =\cf3 \strokec3 random_state,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 stratify\cf8 \strokec8 =\cf3 \strokec3 df.target\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  dftrain.shape[\cf9 \strokec9 0\cf3 \strokec3 ] \cf8 \strokec8 ==\cf3 \strokec3  \cf9 \strokec9 26048\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  \cf9 \strokec9 0.74\cf3 \strokec3  \cf8 \strokec8 <=\cf3 \strokec3  (dftest.target \cf8 \strokec8 ==\cf3 \strokec3  \cf9 \strokec9 0\cf3 \strokec3 ).mean() \cf8 \strokec8 <=\cf3 \strokec3  \cf9 \strokec9 0.76\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     xtrain \cf8 \strokec8 =\cf3 \strokec3  dftrain[nottarget].values\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ytrain \cf8 \strokec8 =\cf3 \strokec3  dftrain[\cf7 \strokec7 'target'\cf3 \strokec3 ].values\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     xtest \cf8 \strokec8 =\cf3 \strokec3  dftest[nottarget].values\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ytest \cf8 \strokec8 =\cf3 \strokec3  dftest[\cf7 \strokec7 'target'\cf3 \strokec3 ].values\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  xtrain.shape \cf8 \strokec8 ==\cf3 \strokec3  (\cf9 \strokec9 26048\cf3 \strokec3 , \cf9 \strokec9 106\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 assert\cf3 \strokec3  ytrain.shape \cf8 \strokec8 ==\cf3 \strokec3  (\cf9 \strokec9 26048\cf3 \strokec3 ,)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  xtrain, ytrain, xtest, ytest\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 adult_data_feature_selectors\cf3 \strokec3 ():\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """create a RFE with random forest estimators and a lasso regression"""\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # RFE with random forests\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf9 \strokec9 LOGGER\cf3 \strokec3 .info(\cf7 \strokec7 'createing feature selection objects'\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     rf \cf8 \strokec8 =\cf3 \strokec3  sklearn.ensemble.RandomForestClassifier(\cf10 \strokec10 n_jobs\cf8 \strokec8 =-\cf9 \strokec9 1\cf3 \strokec3 , \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     rfe \cf8 \strokec8 =\cf3 \strokec3  sklearn.feature_selection.RFE(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 estimator\cf8 \strokec8 =\cf3 \strokec3 rf\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # lasso\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     lr \cf8 \strokec8 =\cf3 \strokec3  sklearn.linear_model.LogisticRegression(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 C\cf8 \strokec8 =\cf9 \strokec9 .1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 penalty\cf8 \strokec8 =\cf7 \strokec7 'l1'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 solver\cf8 \strokec8 =\cf7 \strokec7 'saga'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 n_jobs\cf8 \strokec8 =-\cf9 \strokec9 1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 max_iter\cf8 \strokec8 =\cf9 \strokec9 250\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     lasso \cf8 \strokec8 =\cf3 \strokec3  sklearn.feature_selection.SelectFromModel(\cf10 \strokec10 estimator\cf8 \strokec8 =\cf3 \strokec3 lr)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  \{\cf7 \strokec7 'rfe'\cf3 \strokec3 : rfe, \cf7 \strokec7 'lasso'\cf3 \strokec3 : lasso\}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 adult_data_modellers\cf3 \strokec3 ():\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf7 \strokec7 """a handful of modelers"""\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf9 \strokec9 LOGGER\cf3 \strokec3 .info(\cf7 \strokec7 'createing data modeller objects'\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     cv \cf8 \strokec8 =\cf3 \strokec3  my_cv()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # random forest\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     mrf \cf8 \strokec8 =\cf3 \strokec3  sklearn.ensemble.RandomForestClassifier(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 n_estimators\cf8 \strokec8 =\cf9 \strokec9 100\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 n_jobs\cf8 \strokec8 =-\cf9 \strokec9 1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # logistic regression\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     mLogRegCv \cf8 \strokec8 =\cf3 \strokec3  sklearn.linear_model.LogisticRegressionCV(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 Cs\cf8 \strokec8 =\cf3 \strokec3 np.logspace(\cf8 \strokec8 -\cf9 \strokec9 3\cf3 \strokec3 , \cf9 \strokec9 3\cf3 \strokec3 , \cf9 \strokec9 7\cf3 \strokec3 ),\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 cv\cf8 \strokec8 =\cf3 \strokec3 cv,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 scoring\cf8 \strokec8 =\cf7 \strokec7 'neg_log_loss'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 n_jobs\cf8 \strokec8 =-\cf9 \strokec9 1\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 max_iter\cf8 \strokec8 =\cf9 \strokec9 500\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 verbose\cf8 \strokec8 =\cf9 \strokec9 0\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # neural net\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     mMlp \cf8 \strokec8 =\cf3 \strokec3  sklearn.neural_network.MLPClassifier(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 hidden_layer_sizes\cf8 \strokec8 =\cf3 \strokec3 (\cf9 \strokec9 25\cf3 \strokec3 ,\cf9 \strokec9 10\cf3 \strokec3 ),\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 activation\cf8 \strokec8 =\cf7 \strokec7 'logistic'\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 max_iter\cf8 \strokec8 =\cf9 \strokec9 500\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 ,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  \{\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'random_forest'\cf3 \strokec3 : mrf,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'logistic'\cf3 \strokec3 : mLogRegCv,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf7 \strokec7 'neural_net'\cf3 \strokec3 : mMlp\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \}\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf8 \strokec8 def\cf3 \strokec3  \cf11 \strokec11 adult_data_demo\cf3 \strokec3 ():\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     xtrain, ytrain, xtest, ytest \cf8 \strokec8 =\cf3 \strokec3  load_adult_income_data(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf10 \strokec10 test_size\cf8 \strokec8 =\cf9 \strokec9 0.2\cf3 \strokec3 , \cf10 \strokec10 random_state\cf8 \strokec8 =\cf9 \strokec9 1337\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # feature selection options\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     fs_dict \cf8 \strokec8 =\cf3 \strokec3  adult_data_feature_selectors()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # modelers\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     model_dict \cf8 \strokec8 =\cf3 \strokec3  adult_data_modellers()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # create a pipeline from the above\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     cachedir \cf8 \strokec8 =\cf3 \strokec3  tempfile.mkdtemp()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     memory \cf8 \strokec8 =\cf3 \strokec3  sklearn.externals.joblib.Memory(cachedir, \cf10 \strokec10 verbose\cf8 \strokec8 =\cf9 \strokec9 0\cf3 \strokec3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     pipelines \cf8 \strokec8 =\cf3 \strokec3  [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         sklearn.pipeline.Pipeline(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 steps\cf8 \strokec8 =\cf3 \strokec3 [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 (fsname, fs),\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3                 (modelname, model)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             ],\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3             \cf10 \strokec10 memory\cf8 \strokec8 =\cf3 \strokec3 memory,\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf8 \strokec8 for\cf3 \strokec3  (fsname, fs) \cf8 \strokec8 in\cf3 \strokec3  fs_dict.items()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf8 \strokec8 for\cf3 \strokec3  (modelname, model) \cf8 \strokec8 in\cf3 \strokec3  model_dict.items()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # cross validation\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_scores \cf8 \strokec8 =\cf3 \strokec3  cross_validate_scores(pipelines, xtrain, ytrain)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # select the pair with the best overall negative log loss\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     fs, m \cf8 \strokec8 =\cf3 \strokec3  df_scores.groupby([\cf7 \strokec7 'fs'\cf3 \strokec3 , \cf7 \strokec7 'm'\cf3 \strokec3 ]).mean().test_neg_log_loss.idxmax()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     p_best \cf8 \strokec8 =\cf3 \strokec3  [\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         p \cf8 \strokec8 for\cf3 \strokec3  p \cf8 \strokec8 in\cf3 \strokec3  pipelines\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf8 \strokec8 if\cf3 \strokec3  fs \cf8 \strokec8 in\cf3 \strokec3  p.named_steps\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3         \cf8 \strokec8 and\cf3 \strokec3  m \cf8 \strokec8 in\cf3 \strokec3  p.named_steps\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ][\cf9 \strokec9 0\cf3 \strokec3 ]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # re-fit this model to the *entire* train data (it has only ever been fitted\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # to bootstrapped sub-samples)\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     p_best.fit(xtrain, ytrain)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # get ccr values on test data\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     df_ccr \cf8 \strokec8 =\cf3 \strokec3  get_ccr_df(p_best, xtest, ytest)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     ccr_fig \cf8 \strokec8 =\cf3 \strokec3  make_ccr_plot(df_ccr)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf2 \strokec2 # clean up our pipeline memory\cf3 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     shutil.rmtree(cachedir)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat4 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth3434\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth14705\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf6 \strokec6 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf3 \strokec3     \cf8 \strokec8 return\cf3 \strokec3  p_best, df_scores, df_ccr, ccr_fig\cell \lastrow\row
}