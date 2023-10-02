import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io
import webbrowser
import streamlit_menu as menu
#import streamlit_authenticator as stauth
import streamlit.components.v1 as components
#from print_print import*
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import extra_streamlit_components as stx
# Create a connection to the database





#st.markdown('<style>' + open('./style/style.css').read() + '</style>', unsafe_allow_html=True)
with st.sidebar:
    st.image("https://www.campus-teranga.com/site/images/actualite/20210804-610aa19bbdf57.jpg")
    choose = option_menu("Application de detection Paludisme", ["About", "Prediction Paludisme","Enregistrer Patient","Contact"],
                    icons=['house',
                    'bi bi-graph-down-arrow', 
                    'bi bi-droplet-fill',
                    'bi bi-file-person-fill',
                    'bi bi-file-person-fill'],
                    menu_icon="app-indicator", default_index=0,
                    styles={
    "container": {"padding": "5!important", "background-color": "#FF9333"},
    "icon": {"color": "black", "font-size": "25px"},
    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#33B8FF"},
    "nav-link-selected": {"background-color": "#02ab21"},
}
)
st.image("https://www.campus-teranga.com/site/images/actualite/20210804-610aa19bbdf57.jpg")
if (choose == "About"):
    col1, col2 = st.columns( [0.9, 0.4])

    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
    </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">A propos du createur</p>',
                    unsafe_allow_html=True)
    with col2:               # To display brand log
        st.image("https://www.campus-teranga.com/site/images/actualite/20210804-610aa19bbdf57.jpg",width=150)
    st.write("Abdoulaye BA etudiant en Master 2 Big Data Analytics Universite Numerique Cheikh Hamidou KANE Ex(UVS), Aussi ingenieur des traveaux informatiques à l'hopaital aristide le dantec et Administrateur Reseaux et sytemes d'information et gestionnaire de parc informatique le lien du repos sur github est disponibles sur ce lien:https://github.dev/lbfacto/deploiement-palu-layeba ")
    st.write("Ce projet est realiser avec Dr Oumy Niass de l'universite virtuelle du senegal")
    st.write("Dans le module de cas industrielle sur des données reels de patient dans une base de données avec les ")
    st.write("prelevements de differenetes sujet et diverses criteres sont eablies selon des cas de prevelemenet differentes sur des barometre divers")
    st.write("En outre il a ete fait et concue une application pour faire des prediction selon le type de donnes a notre disposition qui va afficher les resultat de la personne selon son antigene")
#st.image(profile, width=700 )rue
#analyse des donnes

elif (choose =="Prediction Paludisme"):
    st.title("Predictioon Paludisme sur des sujets au senegal") #titre de l
    palu_pedict = pickle.load(open('trained_model.pkl','rb'))
# change the input_data to a numpy array
#Les colones
    col1,col2, col3,col4=st.columns(4)

    Age = st.text_input('Age')

    ratio =st.text_input('ratio')

    G6PD = st.text_input('G6PD')

    EP_6M_AVT = st.text_input('EP_6M_AVT')

    AcPf_6M_AVT = st.text_input('AcPf_6M_AVT')

    EP_1AN_AVT = st.text_input('EP_1AN_AVT')

    AcPf_1AN_AVT =st.text_input('AcPf_1AN_AVT')

    EP_6M_APR = st.text_input('EP_6M_APR')

    AcPf_6M_APR = st.text_input('AcPf_6M_APR')

    EP_1AN_APR = st.text_input('EP_1AN_APR')

    AcPf_1AN_APR = st.text_input('AcPf_1AN_APR')
    palu_diagnosis =''
    if st.button('Resultat Paludisme'):
        palu_pediction = palu_pedict.predict([[Age,ratio,G6PD,EP_6M_AVT,AcPf_6M_AVT,EP_1AN_AVT,AcPf_1AN_AVT,EP_6M_APR	,AcPf_6M_APR,EP_1AN_APR	,AcPf_1AN_APR]])
        if(palu_pediction[0]==1):
            palu_diagnosis = 'Antigene positif Personne atteint du paludisme'
        else:
            palu_diagnosis= 'Antigene negatif personne n_est pas atteint du paludisme'
        st.success(palu_diagnosis)
if choose == "Enregistrer Patient":

    conn = sqlite3.connect('dbuvs.db')
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Enregister Resultat</p>', unsafe_allow_html=True)

    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Medecin
    ( Fonction text, service text,Nom text, Prenom text,Email text, Telephone numeric, date numeric)''')
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
    #st.write('Please help us improve!')
        st.title('Partie Medecin')
        Fonction = st.text_input(label='Fonction Docteur')
        service = st.text_input(label='Enter service')
        Nom=st.text_input(label='Entrer Name') #Collect user feedback
        Prenom=st.text_input(label=' Prenom') #Collect user feedback
        Email=st.text_input(label='Entrer Email') #Collect user feedback
        Telephone=st.text_input(label='Entrer Telephone') #Collect user feedback
        date=st.date_input("Entrer la date")
        submitted = st.form_submit_button('Submit')

        if submitted:
            c.execute("INSERT INTO Medecin VALUES(?,?,?,?,?,?,?)", (Fonction, service, Nom,Prenom, Email, Telephone, date))
            conn.commit()
            st.write('Donnees Medecins enregistrer')
    # Connect to SQLite3 database
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS malades
    (Nom text, Age integer,Prenom text, Email text, Telephone numeric,Adresse text, Resultat text, NomMedcin text,Avis text,date numeric)''')
    with st.form(key='columns_in_form3',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
    #st.write('Please help us improve!')
        st.title('Partie patient')

        Nom=st.text_input(label='Nom') #Collect user feedback
        Prenom=st.text_input(label=' Prenom') #Collect user feedback
        Age=st.text_input(label='Entrer Age') #Collect user feedback
        Email=st.text_input(label='Entrer Email') #Collect user feedback
        Telephone=st.text_input(label='Entrer Telephone') #Collect user feedback
        Adresse=st.text_input(label='Entrer Adresse') #Collect user feedback
        Resultat=st.text_input(label='Entrer Resultat') #Collect user feedback
        NomMedcin = st.text_input(label='Docteur Traitant')
        Avis=st.text_input(label='Recommandation Medcin') #Collect user feedback
        date=st.date_input("Entrer la date")
        submitted = st.form_submit_button('Submit')

        if submitted:
            c.execute("INSERT INTO malades VALUES(?,?,?,?,?,?,?,?,?,?)", (Nom, Prenom,Age, Email, Telephone,Adresse, Resultat, NomMedcin,Avis,date))
            conn.commit()
            st.success('Donner Patient enregistrer')
    conn.close()



elif choose == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
    </style> """, unsafe_allow_html=True,)

    st.markdown('<p class="font">Votre Avis</p>', unsafe_allow_html=True,)
    st.write("Nous aimerions entendre vos commentaires et vos suggestions.")
    st.write("Veuillez nous contacter en utilisant les informations ci-dessous.")
    with st.form(key='columns_in_form3',clear_on_submit=True):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button('envoyer')

        if submitted:
            if name and email and message:
                st.success("Merci pour votre message! Nous vous répondrons dès que possible.")
            else:
                st.error("Veuillez remplir tous les champs.")





from operator import index
import streamlit as st
import plotly.express as px
#from pycaret.regression import setup, compare_models, pull, save_model, load_model
from pandas_profiling import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
from memory_profiler import profile
import os
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score,precision_score, recall_score, roc_curve, auc
# Data Viz Pkg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import seaborn as sns
# ML Packages
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import io
from  PIL import Image
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt


st.set_page_config(layout="wide", page_title=" 💻📊 Analyse de Données UVS ")
st.markdown('<style>' + open('./style/style.css').read() + '</style>', unsafe_allow_html=True)
# git, linkedin = st.columns(2)
# git.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/lbfacto/A_BA_UVS_ProjetPaludisme)")
# git.info(" 👆 Récupérez l'intégralité du code ici")


st.title(" 💻 Analyse automatisée Des Données de sur le paludisme 📊 ")



    # Then, drop the column as usual.
@profile
def main():

    with st.sidebar:
        st.image("https://www.campus-teranga.com/site/images/actualite/20210804-610aa19bbdf57.jpg")
        st.title("UVS Senegal")
        st.image("./style/data.PNG")
        choice = option_menu("Application AUTOML UVS SENEGAL", ["Upload","Profiling AutoML","Plots","Model Building", "Analyser AutoML","metriques","Exporter"],
                    icons =['upload file',
                    "bi bi-binoculars",
                    "bi bi-kanban-fill",
                    "bi bi-lightbulb-fill",
                    "bi bi-graph-up-arrow",
                    "bi bi-hourglass-split",
                    'download'],
                    menu_icon="app-indicator", default_index=0,
                    styles={
        "container": {"padding": "5!important", "background-color": "#26c0f7 ", "font-size": "20px"},
        "icon": {"color": "black", "font-size": "13px"},
        "nav-link": {"font-size": "13px", "text-align": "left", "margin":"0px", "--hover-color": "#f0a80d"},
        "nav-link-selected": {"background-color": "#2ad509"},

    }

)
    df = pd.read_csv('Data.SoucheO7O3_final.csv', index_col=0)
    if choice == "Upload":

        data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xls"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())


    elif choice == "Profiling AutoML":

        st.title("Analyse Exploratoire des Données 💻📊")
        profile_df = df.profile_report() # faire un profiling sur le dataset
        st_profile_report(profile_df)


    elif choice == 'Model Building':
        st.subheader("Building ML Models")
        data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xls"])

        if data is not None:

#pretraitement es données et entrainementdes donnees pour tous ces models
                df = pd.read_csv(data)
                st.dataframe(df.head())
                df=df.drop(['ID','Type_Hb', 'Gpe_ABO', 'Rhesus','Sexe', 'TEST'], axis=1)
                conditionlist=[(df['ratio']>2),# ratio > 2 antigenepositif au palu
                            (df['ratio']<=2)] # ratio<=2 antigene nagtif au palu
                diagnostic = ['0', '1']
                df['Resultat'] = np.select(conditionlist, diagnostic)

                features = ['Age',	'ratio',	'G6PD',	'EP_6M_AVT',	'AcPf_6M_AVT',	'EP_1AN_AVT','AcPf_1AN_AVT',	'EP_6M_APR'	,'AcPf_6M_APR',	'EP_1AN_APR',	'AcPf_1AN_APR']
                target = ['Resultat']

                for attr in ['mean', 'ste', 'largest']:
                    for feature in features:
                        target.append(feature + "_" + attr)

                df['Resultat'] = df['Resultat'].astype(str).astype(int)
                X = df.drop(columns='Resultat', axis=1)
                Y = df['Resultat']
                seed =None
        # prepare models
                models = []
                models.append(('LR', LogisticRegression()))
                models.append(('LDA', LinearDiscriminantAnalysis()))
                models.append(('KNN', KNeighborsClassifier()))
                models.append(('CART', DecisionTreeClassifier()))
                models.append(('NB', GaussianNB()))
                models.append(('SVM', SVC(kernel='linear', C=1, probability=True)))
        # evaluation des models

                model_names = []
                model_mean = []
                model_std = []
                all_models = []
                scoring = 'accuracy'
                for name, model in models:

                    kfold = model_selection.KFold(n_splits=10, random_state=seed)
                    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
                    model_names.append(name)
                    model_mean.append(cv_results.mean())
                    model_std.append(cv_results.std())

                    accuracy_results = {"model name":name,"model_accuracy":cv_results.mean(),"standard deviation":cv_results.std()}
                    all_models.append(accuracy_results)


                if st.checkbox("Metrics As Table"):
                    st.dataframe(pd.DataFrame(zip(model_names,model_mean,model_std),columns=["Algo","Mean of Accuracy","Std"]))
                if st.checkbox("Metrics As JSON"):
                    st.json(all_models)

    elif choice == "metriques":
        st.subheader(" Affichage des metriques d'evaluastion")
        df = pd.read_csv('Data.SoucheO7O3_final.csv', index_col=0)
        st.dataframe(df.head())
        df=df.drop(['ID','Type_Hb', 'Gpe_ABO', 'Rhesus','Sexe', 'TEST'], axis=1)
        conditionlist=[(df['ratio']>2),# ratio > 2 antigenepositif au palu
                    (df['ratio']<=2)] # ratio<=2 antigene nagtif au palu
        diagnostic = ['0', '1']
        df['Resultat'] = np.select(conditionlist, diagnostic)

        features = ['Age',	'ratio',	'G6PD',	'EP_6M_AVT',	'AcPf_6M_AVT',	'EP_1AN_AVT','AcPf_1AN_AVT',	'EP_6M_APR'	,'AcPf_6M_APR',	'EP_1AN_APR',	'AcPf_1AN_APR']
        target = ['Resultat']

        for attr in ['mean', 'ste', 'largest']:
            for feature in features:
                target.append(feature + "_" + attr)

        df['Resultat'] = df['Resultat'].astype(str).astype(int)
        X = df.drop(columns='Resultat', axis=1)
        Y = df['Resultat']
        # Prédire les résultats sur l'ensemble de test
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
        classifier = svm.SVC(kernel='linear', C=1, probability=True)

        classifier.fit(X_train, Y_train)
        y_pred = classifier.predict(X_test)

        # Calculer les métriques de précision, rappel et courbe ROC
        precision = precision_score(Y_test, y_pred)
        recall = recall_score(Y_test, y_pred)
        roc_auc = roc_auc_score(Y_test, y_pred)
        fpr, tpr, thresholds = roc_curve(Y_test, y_pred)
        clf = svm.SVC(kernel='linear', C=1, probability=True)
        clf.fit(X, Y)

        # Prédire les classes pour les données d'entraînement
        y_pred = clf.predict(X)

        # Calculer les métriques de performance
        acc = accuracy_score(Y, y_pred)
        prec = precision_score(Y, y_pred, average='macro')
        rec = recall_score(Y, y_pred, average='macro')

        # Calculer les points de la courbe ROC
        fpr, tpr, thresholds = roc_curve(Y, clf.predict_proba(X)[:,1], pos_label=1)
        roc_auc = auc(fpr, tpr)

        # Afficher les métriques de performance dans Streamlit
        st.write("Accuracy:", acc)
        st.write("Precision:", prec)
        st.write("Recall:", rec)

        # Afficher la courbe ROC dans Streamlit
        st.write("AUC:", roc_auc)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        # Afficher les résultats dans Streamlit
        st.title("Rapport de Machine Learning - SVM")
        st.write("Precision: ", precision)
        st.write("Recall: ", recall)
        st.write("AUC-ROC: ", roc_auc)

        # Afficher la courbe ROC
        plt.figure()
        plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic example')
        plt.legend(loc="lower right")
        st.pyplot()




    elif choice == 'Plots':
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.subheader("Vizualisation des Données")

        data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xls"])
        if data is not None:
            df1 = pd.read_csv(data)
            st.dataframe(df1.head())


            if st.checkbox("Show Value Counts"):
                st.write(df1.iloc[:,-1].value_counts().plot(kind='bar'))
                st.pyplot()

            # visualisation

            all_columns_names = df1.columns.tolist()
            type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
            selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

            

            if st.button("Generate Plot"):
                st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

                # Plot By Streamlit
            if type_of_plot == 'area':
                    cust_data = df1[selected_columns_names]
                    st.area_chart(cust_data)

            if type_of_plot == 'bar':
                    cust_data = df1[selected_columns_names]
                    st.bar_chart(cust_data)

            if type_of_plot == 'line':
                    cust_data = df1[selected_columns_names]
                    st.line_chart(cust_data)


                #nos plots
            if type_of_plot:
                    cust_plot= df1[selected_columns_names].plot(kind=kind)
                    st.write(cust_plot)
                    st.pyplot()

    elif choice == 'Analyser AutoML':
        st.header("Analyse de la qualité et exploration les données")
        profile_df = df.profile_report()

#aut ml pour profiler les donnees
        st_profile_report(profile_df)
        profile_df.to_file("A_BA_UVS.html")

        st.success("Rapport genéré correctement, rendez-vous dans l'onglet 'EXPORTER' pour télécharger votre rapport 💾 ")
    elif choice == 'Exporter':
        with open("A_BA_UVS.html", 'rb') as f:
            dw = st.download_button("Télécharger le rapport 💾 ", f, "rapport_analyse_donneesUVS.html")
            if dw :
                st.balloons()

                st.success("Rapport correctement téléchargé.")
    #else:
    # comment
        #add_page_visited_detail('A Propos', datetime.now())
        #st.subheader("A Propos")

if __name__ == '__main__':
    main()








