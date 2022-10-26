# from lib2to3.pgen2.pgen import DFAState
# from socketserver import DatagramRequestHandler
# from turtle import color
# from xml.sax.handler import all_features
# from matplotlib import legend
import streamlit as st 
from PIL import Image 
# from streamlit.components.v1 import html
# import math

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import pandas as pd 
import base64 #for gif

# import numpy as np
# from scipy import stats

# DIABETES DATA
# DIABETES_DATA_URL = ("D:/diabetes-prediction/dashboard/latest_dataset.csv") 
# DIABETES_PARAMS_URL = ("D:/diabetes-prediction/dashboard/latest_params.csv")
# DIABETIC RETINOPATHY DATA
# RETINOPATHY_DATA_URL = ("D:/diabetes-prediction/dashboard/retinopathy_dataset.csv") 
# RETINOPATHY_PARAMS_URL = ("D:/diabetes-prediction/dashboard/retinopathy_params.csv")

# LINKS FOR DEPLOYMENT
DIABETES_DATA_URL = ("latest_dataset.csv")
DIABETES_PARAMS_URL = ("latest_params.csv")
RETINOPATHY_DATA_URL = ("retinopathy_dataset.csv") 
RETINOPATHY_PARAMS_URL = ("retinopathy_params.csv")

## Set the Page Config
st.set_page_config(page_title="Retimark - Exploratory Visualization Dashboard", page_icon=':kr:',layout='wide')

#st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

## hide the menu bar at top right and message from Streamlit
st.markdown("""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)

##Set the Title of Dashboard
st.markdown("# Exploratory Visualization Dashboard of Diabetes Dataset")

##Description of data 
placeholder1 = st.empty()

def show_placeholder1(show_desc):
    if show_desc:
        with placeholder1.container():
            st.subheader("**Clinical Data**")
            st.markdown("📋 Korea National Health & Nutrition Survey Data")
            col1_1, col1_2, col1_3, col1_4 = st.columns(4)   
            with col1_1:
                st.markdown("📅 3 Files")
            with col1_2:
                st.markdown("🧑 8637 Participants")
            with col1_3:
                st.markdown("🩸 42 Clinical Features")
            with col1_4:
                st.markdown("💊 Diabetes")
            st.write("")
            st.markdown("📋 Clinical Trial Data from RetiMark")
            col2_1, col2_2, col2_3, col2_4 = st.columns(4)
            with col2_1:
                st.markdown("📅 3 Files")
            with col2_2:
                st.markdown("🧑 650 Participants")
            with col2_3:
                st.markdown("🩸 5 Clinical Features")
            with col2_4:
                st.markdown("💊 Diabetic Retinopathy")
            st.write("")
            st.markdown("📋 Clinical Trial Data from RetiMark")
            col3_1, col3_2, col3_3, col3_4 = st.columns(4)
            with col3_1:
                st.markdown("📅 3 Files")
            with col3_2:
                st.markdown("🧑 650 Participants")
            with col3_3:
                st.markdown("🩸 5 Clinical Features")
            with col3_4:
                st.markdown("💊 Age-related Macular Degeneration")
                
            st.subheader("**Biomarker Data**")
            st.markdown("📋 Clinical Trial Data from RetiMark")
            col1_1, col1_2, col1_3, col1_4 = st.columns(4)
            with col1_1:
                st.markdown("📅 3 Files")
            with col1_2:
                st.markdown("🧑 650 Participants")
            with col1_3:
                st.markdown("🥦 5 Proteins")
            with col1_4:
                st.markdown("💊 Diabetic Retinopathy")
            st.write("")
            st.markdown("📋 Clinical Trial Data from RetiMark")
            col2_1, col2_2, col2_3, col2_4 = st.columns(4)
            with col2_1:
                st.markdown("📅 3 Files")
            with col2_2:
                st.markdown("🧑 650 Participants")
            with col2_3:
                st.markdown("🥦 5 Proteins")
            with col2_4:
                st.markdown("💊 Age-related Macular Degeneration")
    else:
        placeholder1.empty()

show_placeholder1(True)

##Mascot gif for homepage
# mascot = open("D:/diabetes-prediction/dashboard/mascot.gif", "rb")
## Mascot link for deployment
mascot = open("mascot.gif", "rb")
contents = mascot.read()
mascot_url = base64.b64encode(contents).decode("utf-8")
mascot.close()
col1, col2, col3 = st.columns((1,3,1))
with col2:
    placeholder = st.markdown(f'<img src="data:image/gif;base64,{mascot_url}" width="500" height="500" alt="gif">',unsafe_allow_html=True)

# st.sidebar.markdown("[![Foo](http://retimark.com/layout/images/common/logo_on.png)](http://retimark.com/layout/eng/home.php?go=main)")
# logo = Image.open('D:/diabetes-prediction/dashboard/logo.png')
# company logo link for deployment
logo = Image.open('logo.png')
col1, col2, col3 = st.sidebar.columns(3)
with col2:
    st.image(logo)
st.sidebar.markdown("## Side Panel")
st.sidebar.markdown("Use this panel to explore the dataset.")

##reading and loading df

@st.cache(persist=True, show_spinner=True)
# Load  the Data 
def load_data(data):
	#Parse date and Time 
    df = pd.read_csv(data)
    return df

#st.markdown("-----")

#image = Image.open('C:/Users/yeoyu/Downloads/diabetes-prediction/dashboard/blooddrop.png')
#image = Image.open('C:/diabetes-prediction/dashboard/mascot.png')

#displaying the image on streamlit app

#placeholder = st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

# st.markdown("## Now, Explore about the dataset")
# # Create a text element and let the reader know the data is loading.
# # data_load_state = st.text('Loading dataset...')
# # Load 8037 rows of data into the dataframe.
disease_set = ['Diabetes', 'Diabetic Retinopathy']
st.sidebar.subheader('Disease Set')
disease = st.sidebar.selectbox("Choose dataset.", disease_set, key="disease")
if disease == 'Diabetes':
    df = load_data(DIABETES_DATA_URL)
elif disease == 'Diabetic Retinopathy':
    df = load_data(RETINOPATHY_DATA_URL)
# # Notify the reader that the data was successfully loaded.
# # data_load_state.text('Loading dataset...Completed!')

##checkbox

## VARIABLES
## demographic - age 
age_num = ['age']
age_cat = ['age_grp']
age_all = age_num + age_cat
## demographic - gender
sex_num = []
sex_cat = ['sex']
sex_all = sex_num + sex_cat
## body measurement - currently not used
body_num = ['he_ht','he_wt','he_wc','he_bmi']
body_cat = []
body_bmi = ['he_bmi']
body_all = body_num + body_cat
## diagnosis
diagnosis_num = []
diagnosis_cat = ['he_dmfh']
diagnosis_all = diagnosis_num + diagnosis_cat
## treatment
treatment_num = ['de1_dur','he_glu','he_hba1c','he_bun','he_crea']
treatment_cat = ['de1_3','de1_31','de1_32','he_dm']
treatment_all = treatment_num + treatment_cat
## drinking and smoking
alcohol_smoking_num = []
alcohol_smoking_cat = ['dr_month','dr_high','sm_presnt']
alcohol_smoking_all = alcohol_smoking_num + alcohol_smoking_cat
## comorbidities
# comorbidities_num = ['he_sbp','he_dbp','he_chol','he_hdl_st2','he_tg']
# comorbidities_cat = ['he_obe','he_hp','he_hchol','di3_dg','di4_dg']
# comorbidities_all = comorbidities_num + comorbidities_cat
##### obesity
obesity_num = []
obesity_cat = ['he_obe']
obesity_all = obesity_num + obesity_cat
##### hyperlipidemia
hyperlipidemia_num = ['he_chol','he_hdl_st2','he_tg']
hyperlipidemia_cat = ['he_hchol']
hyperlipidemia_all = hyperlipidemia_num + hyperlipidemia_cat
##### hypertension
hypertension_num = ['he_sbp','he_dbp']
hypertension_cat = ['he_hp']
hypertension_all = hypertension_num + hypertension_cat
##### cardiovascular disease
cardiovascular_num = []
cardiovascular_cat = ['di4_dg']
cardiovascular_all = cardiovascular_num + cardiovascular_cat
##### stroke
stroke_num = []
stroke_cat = ['di3_dg']
stroke_all = stroke_num + stroke_cat
# nutrition
nutrition_num = ['n_en','n_prot','n_fat','n_cho','n_en_prot','n_en_fat','n_en_cho','n_en_tot']
nutrition_cat = []
nutrition_all = nutrition_num + nutrition_cat
## physcal activities
physical_activity_num = ['pa_vigmet','pa_modmet','pa_walkmet','pa_totmet','pa_vig_tm','pa_mod_tm','pa_walk_tm']
physical_activity_cat = ['pa_aerobic','pa_walk']
physical_activity_all = physical_activity_num + physical_activity_cat
## all variables
numerical_variables = ['age','he_ht','he_wt','he_wc','he_bmi',
                       'de1_dur','he_glu','he_hba1c','he_bun','he_crea','he_sbp','he_dbp','he_chol','he_tg','he_hdl_st2',
                       'n_en','n_prot','n_fat','n_cho','n_en_prot','n_en_fat','n_en_cho','n_en_tot',
                       'pa_vigmet','pa_modmet','pa_walkmet','pa_totmet','pa_vig_tm','pa_mod_tm','pa_walk_tm']
categorical_variables = ['age_grp','sex','he_dmfh','de1_3','de1_31','de1_32','he_dm',
                         'dr_month','dr_high','sm_presnt','he_obe','he_hp','he_hchol','di3_dg','di4_dg',
                         'pa_aerobic','pa_walk']
all_variables = numerical_variables + categorical_variables

## functions 

def findOutliers():
    Q1 = df[numerical_variables].quantile(0.25)
    Q3 = df[numerical_variables].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[numerical_variables] < (Q1 - 1.5 * IQR)) | (df[numerical_variables] > (Q3 + 1.5 * IQR))).sum()
    return outliers.values
    #outliers_df = pd.DataFrame({'Variable':outliers.index, 'Number of Outliers':outliers.values})
    #return outliers_df

##Function to set title - if false, print title; if true, do not print title
def set_title(placeholder, title, headername):
    show_placeholder1(False)
    placeholder.empty() 
    if (title == False):
        st.title(headername)
        return True, False
    else:
        return title, False

##QUICK EXPLORE
titleShown = False

st.sidebar.subheader('Quick Explore')
if st.sidebar.checkbox('Dataset Quick Look'):
    titleShown = set_title(placeholder, titleShown, 'Quick Explore')
    st.subheader('Dataset Quick Look')
    st.write(df.head())

##LIST OF VARIABLES
if st.sidebar.checkbox("Show Columns"):
    titleShown = set_title(placeholder, titleShown, 'Quick Explore')
    st.subheader('List of Variables')
    def load_data(nrows):
        if disease == 'Diabetes':
            df = pd.read_csv(DIABETES_PARAMS_URL, nrows = nrows)
        elif disease == 'Diabetic Retinopathy':
            df = pd.read_csv(RETINOPATHY_PARAMS_URL, nrows = nrows)
        return df
    params_df = load_data(42)     
    def color_type(type): #colour code the cell according to the variable type 
        if type == 'Basic Info':
            color = '#f94144' 
        elif type == 'Demographic':
            color = '#f3722c' 
        elif type == 'Treatment':
            color = '#f9c74f'
        elif type == 'Alcohol and Smoking':
            color = '#90be6d' 
        elif type == 'Comorbidities':
            color = '#43aa8b' 
        elif type == 'Nutrition':
            color = '#4d908e'
        elif type == 'Physical Activity':
            color = '#577590'
        else:
            color = '#f8961e' 
        return f'background-color: {color}' 
    st.write(params_df.style.applymap(color_type, subset=['Type'])) 

if st.sidebar.checkbox('Statistical Description'):
    titleShown = set_title(placeholder, titleShown, 'Quick Explore')
    st.subheader('Statistical Data Description')
    description = df[numerical_variables].describe().transpose()
    description['outliers'] = findOutliers()
    st.write(description)

##DIVIDING INTO CATEGORIES
# st.title('View Variables Across Categories')
st.sidebar.subheader('Clinical Categories')
# st.markdown("Tick the box on the side panel to explore the dataset.")

years = ['All','2012','2017','2018']
cat_plots = ['piechart','barplot']
num_plots = ['histogram','boxplot','violin plot']
cat_x_plots = ['boxplot', 'violin plot']
sns.set_theme(style="whitegrid") #to have grids in every plot

##FUNCTIONS 
def set_data(diabetes_option,df): #returns the df according to the year selected
    if diabetes_option == 'All':
        return df
    else:
        return df[df['he_dm']==diabetes_option]

def create_hue_cols(): #returns list of hue options
    hue_cols = ['he_dm','age_grp','sex','year']
    hue_cols.append(None)
    return hue_cols

def get_legend_order(hue_var):
    if hue_var == 'age_grp':
        legend_order = ['40-49','50-59','60-69','70-79']
    elif hue_var == 'sex':
        legend_order = ['male', 'female']
    elif hue_var == 'he_dm':
        legend_order = ['yes','no']
    elif hue_var == 'he_hp':
        legend_order = ['normal','prehypertension','hypertension']
    elif hue_var == 'he_hchol':
        legend_order = ['yes','no']
    elif hue_var == 'he_htg':
        legend_order = ['yes','no']
    elif hue_var == 'di4_dg':
        legend_order = ['yes','no']
    elif hue_var == 'he_dmfh':
        legend_order = ['yes','no']
    elif hue_var == 'he_obe':
        legend_order = ['underweight','normal','obesity']
    else:
        legend_order = []
    return legend_order

def create_histogram(data, variable, title):
    #sns.set(rc = {'figure.figsize':(15,6)}) ##resize plot
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax = sns.histplot(x=variable,kde=True,data=data,color="coral")
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black', which='both')
    ax.set_title(title, color="black")
    ax.grid(False)
    fig.set_figheight(5)
    fig.set_figwidth(5)
    return fig

def create_count_plot(x_var, hue, title, data):
    #sns.set(rc = {'figure.figsize':(15,10)}) ##resize plot
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax = sns.countplot(x=x_var,hue=hue,data=data,palette="pastel")
    # legend_order = get_legend_order(hue)
    # if hue!=None:
    #     ax.legend(labels=legend_order)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black', which='both')
    ax.set_title(title, color="black")
    ax.grid(False)
    fig.set_figheight(5)
    fig.set_figwidth(5)
    return fig

def create_pie_chart(variable, title, data):
    counts = data[variable].value_counts(dropna=True).tolist()
    labels = data[variable].dropna().unique()
    total_count = data.shape[0]
    palette_color = sns.color_palette('Set2')
    percentages = []
    for i in range(len(labels)):
        percentages.append(counts[i]/total_count)
    fig, ax = plt.subplots(figsize=(15, 10))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    patches, texts, pcts = ax.pie(percentages, labels=None, autopct='%1.0f%%', 
        colors=palette_color,
        shadow=False, startangle=0,   
        pctdistance=0.5,labeldistance=1.2) 
    for i, patch in enumerate(patches):
        texts[i].set_color(patch.get_facecolor())
        pcts[i].set_color(patch.get_facecolor())
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.setp(pcts, color='black')
    #plt.setp(texts,color='black')
    fig.set_figheight(6)
    fig.set_figwidth(6)
    #ax.legend(frameon=False, bbox_to_anchor=(1.5,0.8))
    return fig
    #return fig
    #st.pyplot(fig)
    
def create_bar_plot(x, y, hue, title, data):
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax = sns.barplot(x=x,y=y,hue=hue,data=data,palette="pastel")
    # legend_order = get_legend_order(hue)
    # if hue!=None:
    #     ax.legend(labels=legend_order)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black', which='both')
    ax.set_title(title, color="black")
    ax.grid(False)
    fig.set_figheight(5)
    fig.set_figwidth(5)
    return fig      

def create_scatter_plot(x, y, hue, title, data):
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax = sns.scatterplot(x=x, y=y,data=data,palette="pastel",hue=hue)
    # legend_order = get_legend_order(hue)
    # if hue!=None:
    #     ax.legend(labels=legend_order)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black', which='both')
    ax.set_title(title, color="black")
    ax.grid(False)
    fig.set_figheight(5)
    fig.set_figwidth(5)
    return fig    

def create_box_plot(x, y, hue, title, data):
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    if y==None:
        ax = sns.boxplot(x=x, hue=hue, data=data, palette="pastel")
    else:
        ax = sns.boxplot(x=x, y=y, hue=hue, data=data, palette="pastel")
    # legend_order = get_legend_order(hue)
    # if hue!=None:
    #     ax.legend(labels=legend_order)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black', which='both')
    ax.set_title(title, color="black")
    ax.grid(False)
    fig.set_figheight(5)
    fig.set_figwidth(5)
    return fig

def create_violin_plot(x, y, hue, title, data):
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    if y==None:
        ax = sns.violinplot(x=x, data=data, palette="pastel", hue=hue, split=True)
    else:
        ax = sns.violinplot(x=x, y=y, data=data, palette="pastel", hue=hue, split=True)
    # legend_order = get_legend_order(hue)
    # if hue!=None:
    #     ax.legend(labels=legend_order)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.grid(False)
    ax.tick_params(colors='black', which='both')
    ax.set_title(title, color="black")
    ax.grid(False)
    fig.set_figheight(5)
    fig.set_figwidth(5)
    return fig

##Function to create legend
def write_legend(category):
    if "Demographic" in category:
        st.write("1. age: Age ranging from 40-79 years old")
        st.write("2. sex: Male / Female")
        st.write("3. age_grp: Age groups (40-49, 50-59, 60-69, 70-79)")
        #st.write("3. he_ht: Height (cm)")
        #st.write("4. he_wt: Weight (kg)")
        #st.write("5. he_wc: Waist circumference (cm)")
        st.write("4. he_bmi: Body mass index (kg/m2)")
    elif "Diagnosis" in category:
        st.write("1. he_dmfh: Diabetes family history (No/Yes)")
    elif "Treatment" in category:
        st.write("1. de1_dur: Duration of diabetes")
        st.write("2. de1_3: Diabetes treatment (No/Yes)")
        st.write("3. de1_31: Diabetes treatment with insulin injection (No/Yes)")
        st.write("4. de1_32: Diabetes treatment with oral medication (No/Yes)")
        st.write("5. he_glu: Fasting blood sugar (mg/dL)")
        st.write("6. he_hba1c: hemoglobin_A1c (%)")
        st.write("7. he_bun: blood urea nitrogen (mg/dL)")
        st.write("8. he_crea:blood serum creatinine (mg/dL)")
        st.write("9. he_dm: Diabetes status (No/Yes)")
    elif "Alcohol Drinking 🍺 and Smoking 🚬" in category:
        st.write("1. dr_month: Drinking more than once a month (No/Yes)")
        st.write("""
                2. dr_high: High risk drinking (No/Yes)
                    * Having drinks at least twice a week 
                    * For men, ≥ 7 drinks once a month
                    * For women, ≥ 5 drinks once a month         
                """)
        st.write("""
                3. sm_presnt: Current smoking status (No/Yes)
                    * More than 100 cigarettes in lifetime & currently smoking
                """)
    elif "Obesity" in category:
        st.write("1. he_obe: Obesity status (Underweight/Normal/Obesity)")
    elif "Hyperlipidemia" in category:
        st.write("1. he_chol: Total cholesterol (mg/dL)")
        st.write("2. he_hdl_st2: HDL cholesterol (mg/dL)")
        st.write("3. he_tg: Triglycerides (mg/dL)")
        st.write("""
                4. he_hchol: Hyperlipidemia status (No/Yes)
                    * Total cholesterol ≥ 240 or uses yslipidemia medication 
                """)
    elif "Hypertension" in category:
        st.write("1. he_sbp: Systolic Blood Pressure (mmHg)")
        st.write("2. he_dbp: Diastolic Blood Pressure (mmHg)")
        st.write("""
                3. he_hp: Hypertension Status 
                    * Normal:  Systolic Blood Pressure < 120 and Diastolic Blood Pressure < 180 
                    * Prehypertension: 120 ≤ Systolic Blood Pressure < 140 or 80 ≤ Diastolic Blood Pressure < 90    
                    * Hypertension:  140 ≤ Systolic Blood Pressure or 90 ≤ Diastolic Blood Pressure or uses hypertension medication          
                """)
    elif "Cardiovascular" in category:
        st.write("1. di4_dg: Myocardial infarction or angina diagnosis status (No/Yes)")
    elif "Stroke" in category:
        st.write("1. di3_dg: Stroke Diagnosis (No/Yes)")
    elif "Nutrition" in category:
        st.write("1. n_en: Daily intake of energy (kcal)") 
        st.write("2. n_prot: Daily intake of protein (g)")
        st.write("3. n_fat: Daily intake of fat (g)")
        st.write("4. n_cho: Daily intake of carbohydrate (g)")
        st.write("5. n_en_prot: Energy intake from protein")  
        st.write("6. n_en_fat: Energy intake from fat")  
        st.write("7. n_en_cho: Energy intake from carbohydrate")  
        st.write("8. n_en_tot: Total dietary energy") 
    elif "Physical Activity" in category:
        st.write("1. pa_vigmet: MET score of vigorous activities") 
        st.write("2. pa_modmet: MET score of moderate activities") 
        st.write("3. pa_walkmet: MET score of walking") 
        st.write("4. pa_totmet: MET score of all activities") 
        st.write("5. pa_vig_tm: Total minutes of vigorous activitiesy") 
        st.write("6. pa_mod_tm: Total minutes of moderate activities") 
        st.write("7. pa_walk_tm: Total minutes of walking") 
        st.write("""
                8. pa_walk: Regular walking exercise in a week (No/Yes)
                    * In a week, walking exercise for ≥ 5 days 
                    * Each day, walking exercise for ≥ 30 minutes 
                """)
        st.write("""
                9. pa_aerobic: Aerobic activity status (No/Yes)
                    * In a week, aerobic exercise for ≥ 150 minutes 
                    * In a week, vigorous exercise for ≥ 75 minutes 
                """)


def plot_individual_visualization(category,x_cols,year_key,x_var_key,v_key,h_key):
    st.header(category)

    with st.expander("Legend of Variables"):
        write_legend(category)
    
    st.write("")  #Add extra blank line

    row1_1, row1_spacer1, row1_2  = st.columns((2.3, .4, 5))
    with row1_1:
        st.subheader('Distribution of Single Variable')
        year = st.selectbox("Choose disease group.", ['All','diabetes','non-diabetes'], key=year_key)
        x_var = st.selectbox("Choose a variable.",x_cols,key=x_var_key)
        if (x_var in categorical_variables): #can choose between bar plot and pie chart for now
            visualization = st.selectbox("Choose plot.", cat_plots,key=v_key)
            if visualization!='piechart':
                hue_var_opt = st.selectbox("Filter by (Optional).",create_hue_cols(), key=h_key)  
        else:
            visualization = st.selectbox("Choose plot.",num_plots,key=v_key)
    with row1_2:
        input_data = set_data(year, df)
        if (x_var in categorical_variables):
            if visualization=='barplot':
                fig = create_count_plot(x_var, hue_var_opt, "Bar plot for "+x_var, input_data)
                st.pyplot(fig)
                fig.savefig('chart.png')
            else:
                fig = create_pie_chart(x_var, "Pie chart for "+x_var+" in diabetes", input_data)
                fig.savefig("chart.png")
                pie_image = Image.open('chart.png') 
                st.image(pie_image) ##Print as image because the resizing doesn't reflect when pyplot
        else: 
            if visualization=='histogram':
                fig = create_histogram(input_data, x_var, "Histogram for "+x_var)
                st.pyplot(fig)
                fig.savefig('chart.png')
            elif visualization=='boxplot':
                fig = create_box_plot('age_grp', x_var, None, "Box plot for "+x_var, input_data)
                st.pyplot(fig)
                fig.savefig('chart.png')
            else:
                fig = create_violin_plot('sex', x_var, None, "Violin plot for "+x_var, input_data)
                st.pyplot(fig)
                fig.savefig('chart.png')
    row2_1, row2_spacer1 = st.columns((2.3, .4)) ##Download graph button
    with row2_1:
        with open("chart.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )

##Plot variable across age with he_dm hue
def plot_cross_category_vars(sub_header,x_cols,x_var_key):
    row1_1, row1_spacer1, row1_2  = st.columns((2.3, .4, 5))
    with row1_1:
        st.subheader(sub_header)
        x_var = st.selectbox("Choose a variable.",x_cols,key=x_var_key)
    with row1_2:
        if (x_var in categorical_variables):
            fig = create_violin_plot(x_var, 'age', 'he_dm', x_var +" across age", df)
            st.pyplot(fig)
            fig.savefig('chart.png')
        else:
            fig = create_violin_plot('age_grp', x_var, 'he_dm', x_var +" across age", df)
            st.pyplot(fig)
            fig.savefig('chart.png')
    row2_1, row2_spacer1 = st.columns((2.3, .4)) ##Download graph button
    with row2_1:
        with open("chart.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )
                    
##Plot variable across diabetes duration for those with diabetes
def plot_across_duration(sub_header,x_cols,x_var_key):
    diabetes_df = df[df['he_dm']=="diabetes"]
    row1_1, row1_spacer1, row1_2  = st.columns((2.3, .4, 5))
    with row1_1:
        st.subheader(sub_header)
        x_var = st.selectbox("Choose a variable.",x_cols,key=x_var_key)
    with row1_2:
        if (x_var in categorical_variables):
            fig = create_violin_plot(x_var, 'de1_dur', None, x_var +" vs Diabetes Duration", diabetes_df)
            st.pyplot(fig)
            fig.savefig('chart.png')
        else:
            fig = create_scatter_plot(x_var, 'de1_dur', None, x_var +" vs Diabetes Duration", diabetes_df)
            st.pyplot(fig)
            fig.savefig('chart.png')
    row2_1, row2_spacer1 = st.columns((2.3, .4)) ##Download graph button
    with row2_1:
        with open("chart.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )
                    

## DEMOGRAPHIC - 1
title2Shown = False
if st.sidebar.checkbox('Demographic'):
    title2Shown = set_title(placeholder, title2Shown, "View Variables Across Categories")
    st.header('Demographic 📋')
    with st.expander("Legend of Variables"):
        write_legend('Demographic')
    ## AGE   
    plot_individual_visualization('Age',age_all,'y0','x0','v0','h0')
    ## GENDER 
    plot_individual_visualization('Gender',sex_all,'y1','x1','v1','h1')
    ## BMI
    plot_individual_visualization('BMI',body_bmi,'y1.1','x1.1','v1.1','h1.1')

## DIAGNOSIS - 2
if st.sidebar.checkbox('Diagnosis'):
    title2Shown = set_title(placeholder, title2Shown, "View Variables Across Categories")
    ##Individual variables
    plot_individual_visualization('Diagnosis 👨‍⚕️',diagnosis_all,'y2','x2','v2','h2')

## TREATMENT - 3
if st.sidebar.checkbox('Treatment'): 
    title2Shown = set_title(placeholder, title2Shown, "View Variables Across Categories")
    ##Individual variables
    plot_individual_visualization('Treatment 🩺',treatment_all,'y3','x3','v3','h3')
    ##Multiple variables
    st.write("")
    st.subheader('Type of Diabetes Treatment vs Fasting blood sugar')
    col1, col2 = st.columns(2)
    with col1:
        fig = create_box_plot('de1_31', 'he_glu', None, "Diabetes treatment with insulin injection vs Fasting blood sugar", df)
        st.pyplot(fig)
        fig.savefig('chart1.png')
        with open("chart1.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )
    with col2:
        fig = create_box_plot('de1_32', 'he_glu', None, "Diabetes treatment with oral medication vs Fasting blood sugar", df)
        st.pyplot(fig)
        fig.savefig('chart2.png')
        with open("chart2.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )
    st.write("")
    st.subheader('Type of Diabetes Treatment vs Hemoglobin_A1c')
    col1, col2 = st.columns(2)
    with col1:
        fig = create_box_plot('de1_31', 'he_hba1c', None, "Diabetes treatment with insulin injection vs Hemoglobin_A1c", df)
        st.pyplot(fig)
        fig.savefig('chart1.png')
        with open("chart1.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )
    with col2:
        fig = create_box_plot('de1_32', 'he_hba1c', None, "Diabetes treatment with oral medication vs Hemoglobin_A1c", df)
        st.pyplot(fig)
        fig.savefig('chart2.png')
        with open("chart2.png", "rb") as file: 
                    btn = st.download_button(
                        label="Download Graph 📂",
                        data=file,
                        file_name="chart.png",
                        mime="image/png",
                        )

## CORMOBIDITIES
if st.sidebar.checkbox('Comorbidities'):
    with st.sidebar.expander('Expand To View', expanded=True):
        value1 = st.checkbox('Obesity')
        value2 = st.checkbox('Hyperlipidemia')
        value3 = st.checkbox('Hypertension')
        value4 = st.checkbox('Cardiovascular Disease')
        value5 = st.checkbox('Stroke')
    #OBESITY   
    if value1:
        title2Shown = set_title(placeholder, title2Shown, 'View Variables Across Categories') 
        ## Individual variables
        plot_individual_visualization('Obesity ⚖️',obesity_all,'y8','x8','v8','h8')
        ## Multiple variables
        x_col = ['he_obe']
        plot_cross_category_vars("Obesity Status Across Age", x_col, "multiobe")
        plot_across_duration("Obesity and Diabetes Duration",x_col,"durobe")
    #HYPERLIPIDEMIA
    if value2:
        title2Shown = set_title(placeholder, title2Shown, 'View Variables Across Categories') 
        ## Individual variables
        plot_individual_visualization('Hyperlipidemia 💊',hyperlipidemia_all,'y9','x9','v9','h9')
        ##Multiple variables
        x_col = ['he_obe']
        plot_cross_category_vars("Hyperlipidemia Across Age", hyperlipidemia_all, "multihyperlipidemia")
        plot_across_duration("Hyperlipidemia and Diabetes Duration",hyperlipidemia_all,"durheyperlipidemia")
    #HYPERTENSION
    if value3:
        title2Shown = set_title(placeholder, title2Shown, 'View Variables Across Categories') 
        ## Individual variables
        plot_individual_visualization('Hypertension 😖',hypertension_all,'y10','x10','v10','h10')
        ##Multiple variables
        plot_cross_category_vars("Hypertension Across Age", hypertension_all, "multihypertension")
        plot_across_duration("Hypertension and Diabetes Duration",hypertension_all,"durhypertension")
    #CARDIOVASCULAR DISEASE 
    if value4:
        title2Shown = set_title(placeholder, title2Shown, 'View Variables Across Categories') 
        ## Individual variables
        plot_individual_visualization('Cardiovascular Disease 💓',cardiovascular_all,'y11','x11','v11','h11')
        ##Multiple variables
        plot_cross_category_vars("Cardiovascular Disease Across Age", cardiovascular_all, "multicardi")
        plot_across_duration("Cardiovascular Disease and Diabetes Duration",cardiovascular_all,"durcardi")
    #STROKE
    if value5:
        title2Shown = set_title(placeholder, title2Shown, 'View Variables Across Categories') 
        ## Individual variables
        plot_individual_visualization('Stroke Analysis 😵‍💫',stroke_all,'y12','x12','v12','h12')
        ##Multiple variables
        plot_cross_category_vars("Stroke Across Age", stroke_all, "multistroke")
        plot_across_duration("Stroke and Diabetes Duration",stroke_all,"durstroke")

##Sidebar - prevalence
st.sidebar.subheader('Treatment and Prevalence')
title4Shown = False
age_grp_labels = ['40-49', '50-59', '60-69', '70-79']

##Function to create tabs 
def set_tabs(header, listTabs):
    st.header(header)

    tabs_font_css = """<style> button[data-baseweb="tab"] { font-size: 100%; } </style>""" 
    st.write(tabs_font_css, unsafe_allow_html=True) 

    whitespace = 5
    return st.tabs([s.center(whitespace,"\u2001") for s in listTabs]) 

##Function to create metric container (gender)
def create_metric_gender(total, male, female): #total %, male %, female %
    col1, col2, col3 = st.columns(3)
    col1.metric("Total (%) ", total)
    col2.metric("Men (%) ", male)
    col3.metric("Women (%) ", female)

##Function to create metric container (age grp)
def create_metric_age(prev_age_grp): #[ag1 %, ag2 %, ag3 %, ag4 %]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("P(40-49)(%)", prev_age_grp[0], 0)
    col2.metric("P(50-59)(%)", prev_age_grp[1], round(prev_age_grp[1]-prev_age_grp[0], 2))
    col3.metric("P(60-69)(%)", prev_age_grp[2], round(prev_age_grp[2]-prev_age_grp[1], 2))
    col4.metric("P(70-79)(%)", prev_age_grp[3], round(prev_age_grp[3]-prev_age_grp[2], 2)) 

##Function to create metric container (year)
def create_metric_year(prev_year_grp): #[2012 %, 2017 %, 2018 %]
    col1, col2, col3 = st.columns(3)
    col1.metric("2012 (%) ", prev_year_grp[0], 0)
    col2.metric("2017 (%) ", prev_year_grp[1], round(prev_year_grp[1]-prev_year_grp[0], 2))
    col3.metric("2018 (%) ", prev_year_grp[2], round(prev_year_grp[2]-prev_year_grp[1], 2))

##Design of metric container and text  
st.markdown("""
            <style>
            div[data-testid="metric-container"] {
                background-color: #99D6EA;
                border: 5px solid #99D6EA;
                border-radius: 5px;
                padding: 5% 5% 5% 5%;
                color: black;
            }

            /* breakline for metric text */
            div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
                color: #141311;
                font-size: 20px;
            }
            
            </style>
            """
            , unsafe_allow_html=True)

##Function to create line plot to see trend
def create_prevalence_barplot(x, y, title):
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax = sns.barplot(x=x, y=y)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black', which='both')
    ax.tick_params(labelsize=6)
    #ax.set_title(title, fontweight="bold", color="#fe6e00", fontsize=8)
    ax.set_title(title, fontsize=8)
    ax.grid(False)
    fig.set_figwidth(5)
    fig.set_figheight(2)
    return fig

## DIABETES TREATMENT
if st.sidebar.checkbox('Diabetes Treatment'):
    title4Shown = set_title(placeholder, title4Shown, 'View Treatment and Prevalence')
    st.header("Diabetes Management")
    t_rate = 98.95
    c_rate = 24.06
    col1, col2 = st.columns([1,3])
    with col1:
        st.subheader("The treatment rate of glycemia:")
        st.metric("Treatment rate (%)", t_rate)
        st.subheader("The control rate of glycemia:")
        st.metric("Control rate (%)", c_rate)
    with col2:
        dia_management = {"Treatment group":71.31, "Control group":27.56}
        labels = list(dia_management.keys())
        values = list(dia_management.values())
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#D7E8F3')
        plt.bar(labels, values, width=[0.5,0.5])
        plt.ylabel("Percentage (%)") 
        ax.set_title("Treatment rate and control rate of glycemia")
        ax.grid(False)
        ax.set_facecolor("#D7E8F3")
        fig.set_figwidth(6)
        fig.set_figheight(5)
        st.pyplot(fig)

## DIABETES PREVALENCE
if st.sidebar.checkbox('Diabetes Prevalence'):      
    title4Shown = set_title(placeholder, title4Shown, 'View Treatment and Prevalence')
    tab1, tab2, tab3 = set_tabs("Prevalence of Diabetes",["Gender", "Age Groups", "Years"])
    with tab1:
        st.subheader("Fasting glucose ≥ 126 mg/dL")
        create_metric_gender(6.29,8.35,4.80)
        st.subheader("Addition of HbA1c ≥ 6.5%")
        create_metric_gender(10.31,12.33,8.85)
    with tab2:
        st.subheader("Fasting glucose ≥ 126 mg/dL")
        prev_age_grp = [1.79,5.44,8.74,11.08]
        create_metric_age(prev_age_grp) 
        st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of diabetes prevalence across age groups when fasting glucose ≥ 126 mg/dL (%)"))
        st.subheader("Addition of HbA1c ≥ 6.5%")
        prev_age_grp = [2.84,8.44,14.04,19.49]
        create_metric_age(prev_age_grp) 
        st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of diabetes prevalence across age groups when addition of HbA1c ≥ 6.5% (%)"))
    with tab3:
        st.subheader("Fasting glucose ≥ 126 mg/dL")
        prev_year_grp =[5.14,7.01,6.47]
        create_metric_year(prev_year_grp) 
        st.subheader("Addition of HbA1c ≥ 6.5%")
        prev_year_grp =[5.14,7.01,6.47]
        create_metric_year(prev_year_grp) 

##COMORBIDITIES
title5Shown = False
if st.sidebar.checkbox('Diabetic Comorbidities'):
    title5Shown = set_title(placeholder, title5Shown, 'View Comorbidities') 
    comorbedities_labels = ['Impaired fasting glucose','Obesity','Abdominal obesity','Hypertension','Hypercholesterolemia']
    comorbedities_prev = [13.6, 45.19, 48.56, 2.2, 4.39]
    st.pyplot(create_prevalence_barplot(comorbedities_labels,comorbedities_prev,"Comparison of the prevalence of comorbedities in diabetes (%)"))
    with st.sidebar.expander('Expand To View',expanded=True):
        value1 = st.checkbox('Impaired Fasting Glucose')
        value2 = st.checkbox('Obesity',key='o2')
        value3 = st.checkbox('Abdominal Obesity')
        value4 = st.checkbox('Hypertension',key='h2')
        value5 = st.checkbox('Hypercholesterolemia')
    #PREVALENCE OF IMPAIRED FASTING GLUCOSE
    if value1:
        title5Shown = set_title(placeholder, title5Shown, 'View Comorbidities') 
        tab1, tab2, tab3 = set_tabs("Impaired Fasting Glucose",["Gender", "Age Groups","Years"])
        with tab1:
            create_metric_gender(13.6, 12.7, 14.6)
        with tab2:
            prev_age_grp = [5.08, 12.81, 13.27, 15.77]
            create_metric_age(prev_age_grp)     
            st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of impaired fasting glucose across age groups (%)"))
        with tab3:
            prev_year_grp = [9.66,16.89,12.75]
            create_metric_year(prev_year_grp)     
        st.write("")
    #OBESITY IN DIABETES
    if value2:
        title5Shown = set_title(placeholder, title5Shown, 'View Comorbidities') 
        tab1, tab2 = set_tabs("Obesity in Diabetes",["Gender","Age Groups"])
        with tab1:
            st.subheader("Underweight")
            create_metric_gender(0.84,0.6,1.11) 
            st.subheader("Normal")
            create_metric_gender(53.97,57.34,50.22) 
            st.subheader("Overweight")
            create_metric_gender(45.19,42.06,48.67) 
        with tab2:
            prev_age_grp = [59.32,47.78,46.90,39.72] 
            create_metric_age(prev_age_grp)     
            st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of obesity in diabetes across age groups (%)"))
        st.write("")
    #ABDOMINAL OBESITY IN DIABETES
    if value3:
        title5Shown = set_title(placeholder, title5Shown, 'View Comorbidities') 
        tab1, tab2 = set_tabs("Abdominal Obesity in Diabetes",["Gender", "Age Groups"])
        with tab1:
            create_metric_gender(48.56,43.93,53.88)
        with tab2:
            prev_age_grp = [50.75,43.42,50.41,49.73]
            create_metric_age(prev_age_grp)
            st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of abdominal obesity in diabetes across age groups (%)"))
        st.write("")
    #HYPERTENSION IN DIABETES
    if value4:
        title5Shown = set_title(placeholder, title5Shown, 'View Comorbidities') 
        tab1, tab2 = set_tabs("Hypertension in Diabetes",["Gender", "Age Groups"])
        with tab1:
            create_metric_gender(2.2, 1.59, 2.88)
        with tab2:
            prev_age_grp = [0,3.45,3.54,0.56]
            create_metric_age(prev_age_grp)
            st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of hypertension in diabetes across age groups (%)"))
        st.write("")
    #HYPERCHOLESTEROLEMIA IN DIABETES
    if value5:
        title5Shown = set_title(placeholder, title5Shown, 'View Comorbidities') 
        tab1, tab2 = set_tabs("Hypercholesterolemia in Diabetes",["Gender", "Age Groups"])
        with tab1:
            create_metric_gender(4.39,3.57,5.31)
        with tab2:
            prev_age_grp = [10.17,3.45,5.01,3.38]
            create_metric_age(prev_age_grp)
            st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Trend of hypercholesterolemia in diabetes across age groups (%)"))

##Sidebar - lifestyle
st.sidebar.subheader('Lifestyle')
title6Shown = False

##Function to create metric container (gender)
def create_metric_gender_value(total, male, female): #total %, male %, female %
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", total)
    col2.metric("Men", male)
    col3.metric("Women", female)

##Function to create metric container (age grp)
def create_metric_age_value(prev_age_grp): #[ag1 %, ag2 %, ag3 %, ag4 %]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("P(40-49)", prev_age_grp[0], 0)
    col2.metric("P(50-59)", prev_age_grp[1], round(prev_age_grp[1]-prev_age_grp[0], 2))
    col3.metric("P(60-69)", prev_age_grp[2], round(prev_age_grp[2]-prev_age_grp[1], 2))
    col4.metric("P(70-79)", prev_age_grp[3], round(prev_age_grp[3]-prev_age_grp[2], 2)) 
    

## SMOKING AND DRINKING IN DIABETES
if st.sidebar.checkbox('Smoking and Drinking'): 
    with st.sidebar.expander('Expand To View', expanded=True):
        value1 = st.checkbox('Smoking/Drinking Visualisation')
        value2 = st.checkbox('Health Behaviours')
    if value1:
        title6Shown = set_title(placeholder, title6Shown, 'Lifestyle')
        ##Individual variables
        plot_individual_visualization('Alcohol Drinking 🍺 and Smoking 🚬',alcohol_smoking_all,'y4','x4','v4','h4')
        ##Multiple variables
        x_cols = ['dr_month','sm_presnt']
        plot_cross_category_vars('Drinking and Smoking Across Age',x_cols,'multialc')
    if value2:
        title6Shown = set_title(placeholder, title6Shown, 'Lifestyle')
        tab1, tab2 = set_tabs("Health Behaviours 🚬🍺",["Smoking 🚬", "Drinking 🍺"])
        with tab1:
            create_metric_gender(16.95, 29.96, 2.43)
        with tab2:
            create_metric_gender(9.1, 16.67, 0.66)

## PHYSICAL ACTIVITIES
if st.sidebar.checkbox('Physical Activities'):
    with st.sidebar.expander('Expand To View', expanded=True):
        value1 = st.checkbox('Physical Activity Visualisation')
        value2 = st.checkbox('Physical Activity Level')
        value3 = st.checkbox('MET Score')
    #PHYSICAL ACTIVITY VISUALISATION     
    if value1:
        title6Shown = set_title(placeholder, title6Shown, 'View Lifestyle') 
        ##Individual variables
        plot_individual_visualization('Physical Activity 🏃‍♂️',physical_activity_all,'y6','x6','v6','h6')
        ##Multiple variables
        x_cols = ['pa_aerobic', 'pa_walk', 'pa_vigmet', 'pa_modmet','pa_walkmet']
        plot_cross_category_vars('Physical Activity Across Age',x_cols,'multipa')
    #PHYSICAL ACTIVITY LEVEL
    if value2:
        title6Shown = set_title(placeholder, title6Shown, 'View Lifestyle') 
        st.header('Physical Activity Level 🏋️‍♂️')
        #0–600 MET-mins/week
        st.subheader("0–600 MET-mins/week")
        col1, col2 = st.columns(2)
        col1.metric("Diabetes (%)", 40.27)
        col2.metric("Non-Diabetes (%)", 36.32)
        #600-1200 MET-mins/week
        st.subheader("600-1200 MET-mins/week")
        col1, col2 = st.columns(2)
        col1.metric("Diabetes (%)", 19.77)
        col2.metric("Non-Diabetes (%)", 19.06)
        #≥1200 MET-mins/week
        st.subheader("≥1200 MET-mins/week")
        col1, col2 = st.columns(2)
        col1.metric("Diabetes (%)", 39.96)
        col2.metric("Non-Diabetes (%)", 44.62)
    #MET SCORE (min/week)
    if value3: 
        title6Shown = set_title(placeholder, title6Shown, 'View Lifestyle')     
        st.header('MET Score 🚶‍♂️')
        #Vigorous
        st.subheader("Vigorous Physical Activity (min/week)")
        col1, col2 = st.columns(2)
        col1.metric("Diabetes", 174)
        col2.metric("Non-Diabetes", 309)
        #Moderate
        st.subheader("Moderate Physical Activity (min/week)")
        col1, col2 = st.columns(2)
        col1.metric("Diabetes", 497)
        col2.metric("Non-Diabetes", 593)
        #Walking
        st.subheader("Vigorous Physical Activity (min/week)")
        col1, col2 = st.columns(2)
        col1.metric("Diabetes", 792)
        col2.metric("Non-Diabetes", 823)
        

##NUTRITION 
if st.sidebar.checkbox('Nutrition'):
    with st.sidebar.expander('Expand To View', expanded=True):
        value1 = st.checkbox('Nutrition Visualisation')
        value2 = st.checkbox('Daily Intake of Energy')
        value3 = st.checkbox('Energy Intake Percentage')
    ##Nutrition visualisation    
    if value1:
        title6Shown = set_title(placeholder, title6Shown, 'View Nutrition')
        ##Individual variables
        plot_individual_visualization('Nutrition Visualisation 🥦',nutrition_all,'y7','x7','v7','h7')
        ##Multiple variables
        x_cols = ['n_fat','n_cho', 'n_prot']
        plot_cross_category_vars('Nutrition Across Age Groups',x_cols,'multinut')
    #Daily intake of energy
    if value2:
        title6Shown = set_title(placeholder, title6Shown, 'View Nutrition')
        tab1, tab2 = set_tabs("Daily Intake of Energy 🍚",["Gender", "Age Groups"])
        with tab1:
            st.subheader("Diabetes (kcal):")
            create_metric_gender_value(1828, 2082, 1545)
            st.subheader("Non-diabetes (kcal):")
            create_metric_gender_value(1828, 2303, 1665)
        with tab2:
            st.subheader("Across Age Groups (kcal):")
            prev_age_grp = [2154,1986,1881,1633]
            create_metric_age_value(prev_age_grp)
            st.pyplot(create_prevalence_barplot(age_grp_labels, prev_age_grp, "Daily intake of energy in diabetes across age groups"))
    #Energy intake percentage
    if value3:
        title6Shown = set_title(placeholder, title6Shown, 'View Nutrition')
        tab1, tab2 = set_tabs("Energy Intake Percentage 🥓🥐🍔 ",["Diabetes", "Non-Diabetes"])
        with tab1:
            # protein
            st.subheader("Protein for Diabetic (%) 🥓")
            col1, col2, col3 = st.columns(3)
            create_metric_gender(14.00,14.57,13.36)
            # carbohydrate
            st.subheader("Carbohydrate for Diabetic (%) 🥐")
            col1, col2, col3 = st.columns(3)
            create_metric_gender(70.63,69.51,71.87)
            # fat
            st.subheader("Fat for Diabetic (%) 🍔")
            col1, col2, col3 = st.columns(3)
            create_metric_gender(15.37,15.91,14.76)
        with tab2:
            # protein
            st.subheader("Protein for Non-Diabetic (%) 🥓")
            col1, col2, col3 = st.columns(3)
            create_metric_gender(14.67,15.16,14.34)
            # carbohydrate
            st.subheader("Carbohydrate for Non-Diabetic (%) 🥐")
            col1, col2, col3 = st.columns(3)
            create_metric_gender(67.33,66.64,67.80)
            # fat
            st.subheader("Fat for Non-Diabetic (%) 🍔")
            col1, col2, col3 = st.columns(3)
            create_metric_gender(18.00,18.21,17.85)


