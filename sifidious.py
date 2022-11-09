####################################################################################################
#
# Now available: developmental python x3d.py package on PyPi for import.
#   This approach simplifies Python X3D deployment and use.
#   https://pypi.org/project/x3d
#
# Installation:
#       pip install x3d
# or
#       python -m pip install x3d
#
# Developer options for loading x3d package:
#
#    from x3d import *  # preferred approach, terser source that avoids x3d.* class prefixes
#
# or
#    import x3d         # traditional way to subclass x3d package, all classes require x3d.* prefix,
#                       # but python source is very verbose, for example x3d.Material x3d.Shape etc.
#                       # X3dToPython.xslt stylesheet insertPackagePrefix=true supports this option.
#
####################################################################################################

from x3d import *

newModel=X3D(profile='Immersive',version='3.3',
  head=head(
    children=[
    meta(content='Caffeine.x3d',name='title'),
    meta(content='Autogenerated version of Caffeine.x3d scene produced from Caffeine.xml Chemical Markup Language (CML) version 1.0 source file.',name='description'),
    meta(content='Nicholas F. Polys',name='creator'),
    meta(content='24 November 2005',name='created'),
    meta(content='13 September 2021',name='modified'),
    meta(content='Caffeine.xml',name='reference'),
    meta(content='CML sources http://www.xml-cml.org',name='reference'),
    meta(content='JUMBO Chemical Format Conversion Tool',name='reference'),
    meta(content='http://webbook.nist.gov/chemistry',name='reference'),
    meta(content='Polys.StylesheetTransformationsInteractiveVisualization.Web3d2003Symposium.pdf',name='reference'),
    meta(content='Originally Published in Proceedings of Web3D 2003, ACM Press',name='reference'),
    meta(content='CmlToX3d.xslt',name='generator'),
    meta(content='http://www.web3d.org/x3d/content/examples/Basic/ChemicalMarkupLanguage/Caffeine.x3d',name='identifier'),
    meta(content='../license.html',name='license')]),
  Scene=Scene(
    children=[
    ProtoDeclare(name='Carbon',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoC',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoC_mat',diffuseColor=(0,0,0),shininess=.8,specularColor=(.29,.3,.29),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=.77)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["C"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Hydrogen',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoH',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoH_mat',ambientIntensity=.0933,diffuseColor=(.38,.38,.42),shininess=0.5,specularColor=(.53,.53,.53),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=.32)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["H"],
                fontStyle=FontStyle(size=.4)))])])])),
    ProtoDeclare(name='Nitrogen',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoN',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoN_mat',diffuseColor=(0,0,.72),emissiveColor=(0,0,.13),specularColor=(.5,.5,.5),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=.75)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["N"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Oxygen',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoO',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoO_mat',ambientIntensity=.487,diffuseColor=(.54,.05,.25),shininess=.2,specularColor=(.81,.77,.75),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=.73)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["O"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Fluorine',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoF',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoF_mat',diffuseColor=(1,.48,.79),emissiveColor=(.09,.04,.07),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=.72)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["F"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Silicon',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoSi',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoSi_mat',diffuseColor=(.8,.8,.8),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.18)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["Si"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Phosphorus',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoP',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoP_mat',ambientIntensity=.11,diffuseColor=(.9,.41,0),emissiveColor=(.1,.04,0),shininess=0.8,specularColor=(.1,.1,.1),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.1)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["P"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Sulphur',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoS',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoS_mat',ambientIntensity=.0467,diffuseColor=(.25,.39,.25),emissiveColor=(.05,.08,.05),shininess=0.6,specularColor=(.11,.12,.08),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.3)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["S"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Chlorine',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoCl',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoCl_mat',diffuseColor=(.28,.7,0),emissiveColor=(.06,.15,0),shininess=0.8,specularColor=(.5,.5,.5),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.01)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["Cl"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Bromine',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoBr',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoBr_mat',ambientIntensity=.0833,diffuseColor=(.5,.3,.19),emissiveColor=(.12,.13,.08),shininess=0.17,specularColor=(.08,.08,.05),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.14)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["Br"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='Iodine',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='atoI',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='atoI_mat',diffuseColor=(.56,.37,.74),emissiveColor=(.15,.1,.2),shininess=.09,specularColor=(.12,.12,.12),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.33)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["I"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='unknown',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='position',type='SFVec3f',value=(0,0,0)),
        field(accessType='inputOutput',name='Mat',type='SFFloat',value=.6)]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Transform(DEF='ato_',
            IS=IS(
              connect=[
              connect(nodeField='translation',protoField='position')]),
            children=[
            Shape(
              appearance=Appearance(
                material=Material(DEF='ato__mat',diffuseColor=(1,1,1),emissiveColor=(.15,.1,.2),shininess=.09,specularColor=(.12,.12,.12),
                  IS=IS(
                    connect=[
                    connect(nodeField='transparency',protoField='Mat')]))),
              geometry=Sphere(radius=1.001)),
            Shape(
              appearance=Appearance(
                material=Material(diffuseColor=(0.9,0.9,0.9))),
              geometry=Text(string=["?"],
                fontStyle=FontStyle(size=.8)))])])])),
    ProtoDeclare(name='line',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='bond_set',type='MFVec3f',value=[(-1,0,0),(1,0,0)])]),
      ProtoBody=ProtoBody(
        children=[
        Group(
          children=[
          Shape(
            appearance=Appearance(
              material=Material(diffuseColor=(1,1,1),emissiveColor=(1,1,1))),
            geometry=IndexedLineSet(coordIndex=[0,1,-1],
              coord=Coordinate(DEF='bondo',
                IS=IS(
                  connect=[
                  connect(nodeField='point',protoField='bond_set')]))))])])),
    ProtoDeclare(name='title_text',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='txt',type='MFString')]),
      ProtoBody=ProtoBody(
        children=[
        Transform(
          children=[
          Group(
            children=[
            Transform(
              children=[
              Shape(
                appearance=Appearance(
                  material=Material(diffuseColor=(0.9,0.9,0.9))),
                geometry=Text(DEF='cmpd_name',
                  IS=IS(
                    connect=[
                    connect(nodeField='string',protoField='txt')]),
                  fontStyle=FontStyle(),))])])])])),
    ProtoDeclare(name='ano1_text',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='txt',type='MFString')]),
      ProtoBody=ProtoBody(
        children=[
        Transform(
          children=[
          Group(
            children=[
            Transform(
              children=[
              Shape(
                appearance=Appearance(
                  material=Material(diffuseColor=(0.9,0.9,0.9))),
                geometry=Text(DEF='cmpd_name1',
                  IS=IS(
                    connect=[
                    connect(nodeField='string',protoField='txt')]),
                  fontStyle=FontStyle(size=.8)))])])])])),
    ProtoDeclare(name='ano2_text',
      ProtoInterface=ProtoInterface(
        field=[
        field(accessType='inputOutput',name='txt',type='MFString')]),
      ProtoBody=ProtoBody(
        children=[
        Transform(
          children=[
          Group(
            children=[
            Transform(
              children=[
              Shape(
                appearance=Appearance(
                  material=Material(diffuseColor=(0.9,0.9,0.9))),
                geometry=Text(DEF='cmpd_name2',
                  IS=IS(
                    connect=[
                    connect(nodeField='string',protoField='txt')]),
                  fontStyle=FontStyle(size=.6)))])])])])),
    Background(groundAngle=[1.309,1.570796],groundColor=[(0,0.5,0.7),(0,0.4,0.7),(0.6,0.5,0.7)],skyAngle=[1.309,1.570796],skyColor=[(0,0.5,0.8),(0,0.6,.7),(0.6,0.6,0.7)]),
    PointLight(ambientIntensity=1,location=(0,0,5),radius=30),
    NavigationInfo(type='"EXAMINE" "FLY" "ANY"'),
    Viewpoint(description='Inspect Caffeine',position=(0,2,20)),
    #  Copyright by the U.S. Sec. Commerce on behalf of U.S.A. All rights reserved. 
    #  type="3D" <date day="23" month="11" year="1995"/> 
    Transform(DEF='infogroupa',translation=(-8,2,-4),
      children=[
      Transform(translation=(0,6,0),
        children=[
        Viewpoint(description='title billboard',position=(6,-2,10)),
        ProtoInstance(name='title_text',
          fieldValue=[
          fieldValue(name='txt',value=["Caffeine: C8 H10 N4 O2"])])]),
      Transform(translation=(0,5,0),
        children=[
        ProtoInstance(name='ano1_text',
          fieldValue=[
          fieldValue(name='txt',value=["molecule weight: 194.19"])])]),
      Transform(translation=(0,4,0),
        children=[
        ProtoInstance(name='ano1_text',
          fieldValue=[
          fieldValue(name='txt',value=["melting point: 238"])])]),
      Transform(translation=(0,3,0),
        children=[
        ProtoInstance(name='ano1_text',
          fieldValue=[
          fieldValue(name='txt',value=["specific gravity: 1.23"])])]),
      Transform(
        children=[
        ProtoInstance(name='ano2_text',
          fieldValue=[
          fieldValue(name='txt',value=["water solubility: 1-5"])])])]),
    Group(
      children=[
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_1',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(-2.8709,-1.0499,0.1718))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_2',name='Nitrogen',
          fieldValue=[
          fieldValue(name='position',value=(-2.9099,0.2747,0.1062))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_3',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(-1.8026,0.9662,-0.1184))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_4',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(-0.6411,0.2954,-0.2316))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_5',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(-0.6549,-1.0889,-0.1279))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_6',name='Nitrogen',
          fieldValue=[
          fieldValue(name='position',value=(-1.7352,-1.7187,0.0624))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_7',name='Nitrogen',
          fieldValue=[
          fieldValue(name='position',value=(0.6052,0.7432,-0.4434))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_8',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(1.2863,-0.4175,-0.4514))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_9',name='Nitrogen',
          fieldValue=[
          fieldValue(name='position',value=(0.5994,-1.5633,-0.2698))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_10',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(1.0875,2.0867,-0.6139))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_11',name='Oxygen',
          fieldValue=[
          fieldValue(name='position',value=(-1.8349,2.1699,-0.2205))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_12',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(-4.2178,0.9810,0.2003))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_13',name='Oxygen',
          fieldValue=[
          fieldValue(name='position',value=(-3.8944,-1.6746,0.3323))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_14',name='Carbon',
          fieldValue=[
          fieldValue(name='position',value=(-1.6764,-3.1997,0.1458))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_15',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(2.3776,-0.4481,-0.6036))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_16',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(2.1902,2.0944,-0.7699))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_17',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(0.6074,2.5547,-1.5032))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_18',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(0.8606,2.6915,0.2934))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_19',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(-4.0942,2.0097,0.6091))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_20',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(-4.6699,1.0338,-0.8167))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_21',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(-4.9101,0.4518,0.8943))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_22',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(-2.3049,-3.6334,-0.6659))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_23',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(-0.6444,-3.6030,0.0359))])]),
      Transform(
        children=[
        ProtoInstance(DEF='caffeine_karne_a_24',name='Hydrogen',
          fieldValue=[
          fieldValue(name='position',value=(-2.0682,-3.5218,1.1381))])])]),
    Group(
      children=[
      ProtoInstance(DEF='caffeine_karne_b_1',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-2.8709,-1.0499,0.1718),(-2.9099,0.2747,0.1062)])]),
      ProtoInstance(DEF='caffeine_karne_b_2',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-2.8709,-1.0499,0.1718),(-1.7352,-1.7187,0.0624)])]),
      ProtoInstance(DEF='caffeine_karne_b_3',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-2.8909,-1.0499,0.1718),(-3.9144,-1.6746,0.3323)])]),
      ProtoInstance(DEF='caffeine_karne_b_3_2',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-2.8508999999999998,-1.0499,0.1718),(-3.8744,-1.6746,0.3323)])]),
      ProtoInstance(DEF='caffeine_karne_b_4',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-2.9099,0.2747,0.1062),(-1.8026,0.9662,-0.1184)])]),
      ProtoInstance(DEF='caffeine_karne_b_5',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-2.9099,0.2747,0.1062),(-4.2178,0.9810,0.2003)])]),
      ProtoInstance(DEF='caffeine_karne_b_6',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.8026,0.9662,-0.1184),(-0.6411,0.2954,-0.2316)])]),
      ProtoInstance(DEF='caffeine_karne_b_7',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.8226,0.9662,-0.1184),(-1.8549,2.1699,-0.2205)])]),
      ProtoInstance(DEF='caffeine_karne_b_7_2',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.7826,0.9662,-0.1184),(-1.8149,2.1699,-0.2205)])]),
      ProtoInstance(DEF='caffeine_karne_b_8',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-0.6611,0.2954,-0.2316),(-0.6749,-1.0889,-0.1279)])]),
      ProtoInstance(DEF='caffeine_karne_b_8_2',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-0.6211,0.2954,-0.2316),(-0.6349,-1.0889,-0.1279)])]),
      ProtoInstance(DEF='caffeine_karne_b_9',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-0.6411,0.2954,-0.2316),(0.6052,0.7432,-0.4434)])]),
      ProtoInstance(DEF='caffeine_karne_b_10',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-0.6549,-1.0889,-0.1279),(-1.7352,-1.7187,0.0624)])]),
      ProtoInstance(DEF='caffeine_karne_b_11',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-0.6549,-1.0889,-0.1279),(0.5994,-1.5633,-0.2698)])]),
      ProtoInstance(DEF='caffeine_karne_b_12',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.7352,-1.7187,0.0624),(-1.6764,-3.1997,0.1458)])]),
      ProtoInstance(DEF='caffeine_karne_b_13',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(0.6052,0.7432,-0.4434),(1.2863,-0.4175,-0.4514)])]),
      ProtoInstance(DEF='caffeine_karne_b_14',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(0.6052,0.7432,-0.4434),(1.0875,2.0867,-0.6139)])]),
      ProtoInstance(DEF='caffeine_karne_b_15',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(1.2663,-0.4175,-0.4514),(0.5794,-1.5633,-0.2698)])]),
      ProtoInstance(DEF='caffeine_karne_b_15_2',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(1.3063,-0.4175,-0.4514),(0.6194000000000001,-1.5633,-0.2698)])]),
      ProtoInstance(DEF='caffeine_karne_b_16',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(1.2863,-0.4175,-0.4514),(2.3776,-0.4481,-0.6036)])]),
      ProtoInstance(DEF='caffeine_karne_b_17',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(1.0875,2.0867,-0.6139),(2.1902,2.0944,-0.7699)])]),
      ProtoInstance(DEF='caffeine_karne_b_18',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(1.0875,2.0867,-0.6139),(0.6074,2.5547,-1.5032)])]),
      ProtoInstance(DEF='caffeine_karne_b_19',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(1.0875,2.0867,-0.6139),(0.8606,2.6915,0.2934)])]),
      ProtoInstance(DEF='caffeine_karne_b_20',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-4.2178,0.9810,0.2003),(-4.0942,2.0097,0.6091)])]),
      ProtoInstance(DEF='caffeine_karne_b_21',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-4.2178,0.9810,0.2003),(-4.6699,1.0338,-0.8167)])]),
      ProtoInstance(DEF='caffeine_karne_b_22',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-4.2178,0.9810,0.2003),(-4.9101,0.4518,0.8943)])]),
      ProtoInstance(DEF='caffeine_karne_b_23',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.6764,-3.1997,0.1458),(-2.3049,-3.6334,-0.6659)])]),
      ProtoInstance(DEF='caffeine_karne_b_24',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.6764,-3.1997,0.1458),(-0.6444,-3.6030,0.0359)])]),
      ProtoInstance(DEF='caffeine_karne_b_25',name='line',
        fieldValue=[
        fieldValue(name='bond_set',value=[(-1.6764,-3.1997,0.1458),(-2.0682,-3.5218,1.1381)])])])])
) # X3D model complete

####################################################################################################
# Self-test diagnostics
####################################################################################################

print('Self-test diagnostics for Caffeine.py:')
if        metaDiagnostics(newModel): # built-in utility method in X3D class
    print(metaDiagnostics(newModel)) # display meta info, hint, warning, error, TODO values in this model
# print('check newModel.XML() serialization...')
newModelXML= newModel.XML() # test export method XML() for exceptions during export
newModel.XMLvalidate()
# print(newModelXML) # diagnostic

try:
#   print('check newModel.VRML() serialization...')
    newModelVRML=newModel.VRML() # test export method VRML() for exceptions during export
    # print(prependLineNumbers(newModelVRML)) # debug
    print("Python-to-VRML export of VRML output successful", flush=True)
except Exception as err: # usually BaseException
    # https://stackoverflow.com/questions/18176602/how-to-get-the-name-of-an-exception-that-was-caught-in-python
    print("*** Python-to-VRML export of VRML output failed:", type(err).__name__, err)
    if newModelVRML: # may have failed to generate
        print(prependLineNumbers(newModelVRML, err.lineno))

try:
#   print('check newModel.JSON() serialization...')
    newModelJSON=newModel.JSON() # test export method JSON() for exceptions during export
#   print(prependLineNumbers(newModelJSON)) # debug
    print("Python-to-JSON export of JSON output successful (under development)")
except Exception as err: # usually SyntaxError
    print("*** Python-to-JSON export of JSON output failed:", type(err).__name__, err)
    if newModelJSON: # may have failed to generate
        print(prependLineNumbers(newModelJSON,err.lineno))

print("python Caffeine.py load and self-test diagnostics complete.")
