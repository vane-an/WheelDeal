#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:41:19 2024

@author: vanessa
"""

import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
import pickle

###################### Overall setup
st.set_page_config(
    page_title="WheelDeal", 
    page_icon="🚘",
    layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write("")
with col2:
    st.image("Logo_WheelDeal.webp", use_column_width=True)
    st.title("WheelDeal")
    st.write("        ")
    st.write("🚘 Die perfekte App für jeden, der sein E-Auto verkaufen möchte 🚘")
with col3:
    st.write("")


###################### Definition Funktionen
@st.cache_data()
def load_data_1():
    data_filter = pd.read_excel('carsales_data_V3.xlsx')
    return data_filter

@st.cache_data()
def load_data_2():
    data_for_prediction = pd.read_excel('data_one_hot_encoded.xlsx')
    return data_for_prediction

@st.cache_data()
def load_data_3():
    data_matches = pd.read_excel('carsales_data_V2_Mai08.xlsx')
    return data_matches

def load_model_gb():
    filename_gb_regressor = "carsale_gb_regressor.sav"
    loaded_gb = pickle.load(open(filename_gb_regressor, "rb"))
    return loaded_gb

data_filter = load_data_1()
data_for_prediction = load_data_2() 
data_matches = load_data_3()
model_gb = load_model_gb()

#####
prediction_data = pd.read_csv("data_one_hot_encoded.csv")
predictions_gb = model_gb.predict(prediction_data)

#Save the predicted value and the value difference to the data
data_filter["predictions_gb"] = np.exp(predictions_gb)
data_filter["value_difference_gb"] = data_filter["predictions_gb"] - data_filter["price"]

########################## die WheelDeal App #######################################

### Section 1 of the App: Suche, Bewertung
tab1, tab2 = st.tabs(["Inserat erstellen", "Inserat bewerten"])

### Suche ########################################################################
with tab1: #Traum E-Auto anhand von Filtern auswählen
    st.header("Finden Sie den perfekten Preis für ihr altes E-Auto")
    st.subheader("Bitte geben Sie folgende Informationen zu ihrem E-Auto an:")
    st.write("   ")
   
    row1_col1, row1_col2, row1_col3, row1_col4, row1_col5 = st.columns(5)
    row2_col1, row2_col2, row2_col3, row2_col4, row2_col5 = st.columns(5)
    row3_col1, row3_col2, row3_col3, row3_col4, row3_col5 = st.columns(5)
    
    # Filter 1 - Wahl der Automarke
    with row1_col1:
        options_marke = data_filter["Marke"].unique()
        selectbox_marke = st.selectbox('Automarke', options_marke)
   
    # Filter 2 - Wahl des Modells (abhängig von der Marke)
    with row1_col2:
        options_modell = []
        if selectbox_marke == 'Audi':
            options_modell = data_filter["Audi"].dropna().unique()
        elif selectbox_marke == 'BMW':
            options_modell = data_filter["BMW"].dropna().unique()
        elif selectbox_marke == 'Citroen':
            options_modell = data_filter["Citroen"].dropna().unique()
        elif selectbox_marke == 'CUPRA':
            options_modell = data_filter["CUPRA"].dropna().unique()
        elif selectbox_marke == 'Dacia':
            options_modell = data_filter["Dacia"].dropna().unique()
        elif selectbox_marke == 'Fiat':
            options_modell = data_filter["Fiat"].dropna().unique()
        elif selectbox_marke == 'Ford':
            options_modell = data_filter["Ford"].dropna().unique()
        elif selectbox_marke == 'Hyundai':
            options_modell = data_filter["Hyundai"].dropna().unique()
        elif selectbox_marke == 'Jaguar':
            options_modell = data_filter["Jaguar"].dropna().unique()
        elif selectbox_marke == 'Jeep':
            options_modell = data_filter["Jeep"].dropna().unique()
        elif selectbox_marke == 'Kia':
            options_modell = data_filter["Kia"].dropna().unique()
        elif selectbox_marke == 'Mazda':
            options_modell = data_filter["Mazda"].dropna().unique()
        elif selectbox_marke == 'Mercedes-Benz':
            options_modell = data_filter["Mercedes-Benz"].dropna().unique()
        elif selectbox_marke == 'MG':
            options_modell = data_filter["MG"].dropna().unique()
        elif selectbox_marke == 'Mini':
            options_modell = data_filter["Mini"].dropna().unique()
        elif selectbox_marke == 'Nissan':
            options_modell = data_filter["Nissan"].dropna().unique()
        elif selectbox_marke == 'Opel':
            options_modell = data_filter["Opel"].dropna().unique()
        elif selectbox_marke == 'Peugeot':
            options_modell = data_filter["Peugeot"].dropna().unique()
        elif selectbox_marke == 'Polestar':
            options_modell = data_filter["Polestar"].dropna().unique()
        elif selectbox_marke == 'Porsche':
            options_modell = data_filter["Porsche"].dropna().unique()
        elif selectbox_marke == 'Renault':
            options_modell = data_filter["Renault"].dropna().unique()
        elif selectbox_marke == 'SEAT':
            options_modell = data_filter["SEAT"].dropna().unique()
        elif selectbox_marke == 'Skoda':
            options_modell = data_filter["Skoda"].dropna().unique()
        elif selectbox_marke == 'smart':
            options_modell = data_filter["smart"].dropna().unique()
        elif selectbox_marke == 'SsangYong':
            options_modell = data_filter["SsangYong"].dropna().unique()
        elif selectbox_marke == 'Tesla':
            options_modell = data_filter["Tesla"].dropna().unique()
        elif selectbox_marke == 'Toyota':
            options_modell = data_filter["Toyota"].dropna().unique()
        elif selectbox_marke == 'Volkswagen':
            options_modell = data_filter["Volkswagen"].dropna().unique()
        elif selectbox_marke == 'Volvo':
            options_modell = data_filter["Volvo"].dropna().unique()
    
        selectbox_modell = st.selectbox('Modell', options_modell)
    
    #### Filter 3 - Aussenfarbe des Autos
    with row1_col3:
        options_color = data_filter["color"].unique()
        selectbox_color = st.selectbox('Aussenfarbe', options_color)
    
    #### Filter 4 - Innenfarbe des Autos
    with row1_col4:
        options_interior_color = data_filter["interior_color"].unique()
        selectbox_interior_color = st.selectbox('Farbe innen', options_interior_color)
   
    
    #### Filter 5 - Innenaustattung des Autos
    with row1_col5:
        options_interior = data_filter["interior"].unique()
        selectbox_interior = st.selectbox('Innenausstattung', options_interior)
        
    
    #### Filter 6 - Garantie in Monaten
    with row2_col1:
        warranty_input = st.text_input("Garantie in Monaten:")
        warranty_input = float(warranty_input) if warranty_input else 0.0

    
    #### Filter 7 - Kilometerstand
    with row2_col2:
        mileage_input = st.text_input("Kilometerstand in km:")
        mileage_input = float(mileage_input) if mileage_input else 0.0

    
    #### Filter 8 - Alter Auto
    with row2_col3:
        age_input = st.text_input("Alter in Monaten:")
        age_input = float(age_input) if age_input else 0.0
    
    #### Filter 9 - Number of Owners
    with row2_col4:
        owner_input = st.text_input("Anzahl bisheriger Besitzer:")
        owner_input = float(owner_input) if owner_input else 0.0
 
    
    #### Filter 10 - PS
    with row3_col1:
        ps_input = st.text_input("Leistung in PS:")
        ps_input = float(ps_input) if ps_input else 0.0

            
    #### Filter 11 - Elektrische Reichweite
    with row3_col2:
        reach_input = st.text_input("Reichweite in km:")
        reach_input = float(reach_input) if reach_input else 0.0

    
    #### Filter 12 - Consumption
    with row3_col3:
        consumption_input = st.text_input("Stromverbrauch in kWh/100km:")
        consumption_input = float(consumption_input) if consumption_input else 0.0
        


    ###  Prediction                                         

    # Updating the selected options directly in the data_one_hot_encoded DataFrame
    # Update feature values based on selected options
    for feature_name, feature_options in data_for_prediction.items():
        selected_option = None
        if feature_name == 'Marke':
            selected_option = selectbox_marke
        elif feature_name == 'Modell':
            selected_option = selectbox_modell
        elif feature_name == 'color':
            selected_option = selectbox_color
        elif feature_name == 'interior_color':
            selected_option = selectbox_interior_color
        elif feature_name == 'interior':
            selected_option = selectbox_interior

        if selected_option is not None:
            data_for_prediction[feature_name] = data_for_prediction[feature_name].apply(lambda x: 1 if x == selected_option else 0)
    
    
    data_for_prediction["warranty"] = warranty_input
    data_for_prediction["mileage"] = mileage_input
    data_for_prediction["age"] = age_input
    data_for_prediction["number_owner"] = owner_input
    data_for_prediction["ps"] = ps_input
    data_for_prediction["reach"] = reach_input
    data_for_prediction["consumption"] = consumption_input

    # If no matching data, display an error message
    if data_for_prediction.empty:
        st.subheader('🚨**Ihr Preis konnte nicht berechnet werden.** Bitte tragen Sie mehr Informationen zu ihrem E-Auto ein🚨')
    
    ## Otherwise start with the prediction
    else:
        predictions = model_gb.predict(data_for_prediction)
        predictions = np.exp(predictions)
        best_price = predictions
        min_price = best_price * 0.95
        max_price = best_price * 1.05
        
        st.subheader('🔮 **Vorhergesagter Preis:**')
        col1, col2, col3 = st.columns(3)
        with col1:
            ui.metric_card(
                title = "Mindest Preis",
                content = f"{min_price[0]:,.2f} €",
                key = "card1")
        with col2:
            ui.metric_card(
                title = "Bester Preis",
                content = f"{best_price[0]:,.2f} €",
                key = "card2")
        with col3:
            ui.metric_card(
                title = "Höchster Preis",
                content = f"{max_price[0]:,.2f}€",
                key = "card3")
    
    
    ## Matches / Alternative listings
    data_matches = data_matches.loc[(data_matches["Marke"] == selectbox_marke) &
                            (data_matches["Modell"] == selectbox_modell)&
                            (data_matches["reach"] >= reach_input - reach_input * 0.1) & 
                            (data_matches["reach"] <= reach_input + reach_input * 0.1) &
                            (data_matches["age"] >= age_input - age_input * 0.5) &
                            (data_matches["age"] <= age_input + age_input * 0.5) &
                            (data_matches["ps"] >= ps_input - ps_input * 0.1) &
                            (data_matches["ps"] <= ps_input + ps_input * 0.1)]
    
    if not data_matches.empty:
        if st.checkbox("Zeige ähnliche bereits inserierte Angebote", False):
            st.subheader("Ähnliche Angebote bei AutoScout")
            col1, col2 = st.columns(2)
            with col1:
                ui.metric_card(
                    title="Anzahl ähnlicher Angebote",
                    content=f"{data_matches.shape[0]}",
                    key="card4"
                )
            with col2:
                ui.metric_card(
                    title="Durchschnittspreis der ähnlichen Angebote",
                    content=f"{data_matches['price'].mean():,.2f} €",
                    key="card5"
                )

            st.write(data_matches)
    else:
        st.subheader('🚨**Keine ähnlichen Angebote gefunden.** 🚨')
            
    
with tab2:
    st.header("Bewertung ihres bereits inserierten Angebots")
    
    # URL input box
    url = st.text_input("Bitte geben Sie den URL ihres Fahrzeugangebots ein:")
    
    if url:
        # Check if URL is in the database
        if url in data_filter['Link'].values:
            car_info = data_filter[data_filter['Link'] == url].iloc[0]
            st.subheader("Informationen zum ausgewählten Auto")
            row1_col1, row1_col2, row1_col3, row1_col4, row1_col5 = st.columns(5)
            row2_col1, row2_col2, row2_col3, row2_col4, row2_col5 =st.columns(5)
            row3_col1, row3_col2, row3_col3, row3_col4, row3_col5 =st.columns(5)
            with row1_col1:
                ui.metric_card(
                    title="Marke",
                    content="{}".format(car_info["Marke"]),
                    key="card6"
                )
            with row1_col2:
                ui.metric_card(
                    title="Modell",
                    content="{}".format(car_info["Modell"]),
                    key="card7"
                )
            with row1_col3:
                ui.metric_card(
                    title="Aussenfarbe",
                    content="{}".format(car_info["color"]),
                    key="card8"
                )
            with row1_col4:
                ui.metric_card(
                    title="Innenfarbe",
                    content="{}".format(car_info["interior_color"]),
                    key="card9"
                )
            with row1_col5:
                ui.metric_card(
                    title="Innenausstattung",
                    content="{}".format(car_info["interior"]),
                    key="card10"
                )
            with row2_col1:
                ui.metric_card(
                    title="Alter",
                    content="{} Monat(e)".format(car_info["age"]),
                    key="card11"
                )
            with row2_col2:        
                 ui.metric_card(
                    title="Garantie",
                    content="{} Monat(e)".format(car_info["warranty"]),
                    key="card12"
                 )
            with row2_col3:
                ui.metric_card(
                    title="Kilometerstand",
                    content="{} km".format(car_info["mileage"]),
                    key="card13"
                )
            with row3_col1:
                ui.metric_card(
                    title="Leistung",
                    content="{} PS".format(car_info["ps"]),
                    key="card14"
                )
            with row3_col2:
                ui.metric_card(
                    title="Reichweite",
                    content="{} km".format(car_info["reach"]),
                    key="card15"
                )
            with row3_col3:
                ui.metric_card(
                    title="Stromverbrauch",
                    content="{} kWh/100km".format(car_info["consumption"]),
                    key="card16"
                 )
            
            
            st.write("   ")
            
            st.subheader("Bewertung")
            row4_col1, row4_col2, row4_col3 = st.columns(3)
            with row4_col1:
                ui.metric_card(
                    title="Aktueller Preis",
                    content="{:.2f} €".format(car_info["price"]),
                    key="card17"
                )
            with row4_col2:
                ui.metric_card(
                    title="Zu erwartender Preis",
                    content="{:.2f} €".format(car_info["predictions_gb"]),
                    key="card18"
                )
            with row4_col3:
                ui.metric_card(
                    title="Differenz",
                    content="{:.2f} €".format(car_info["value_difference_gb"]),
                    key="card19"
                )
                
            
            st.write("   ")
            
            st.subheader("Empfehlung")
            if car_info["value_difference_gb"] > 0:
                st.write("Ihr derzeitiger Preis für Ihr E-Auto liegt {:.2f} € zu tief.".format(car_info["value_difference_gb"]))
                st.write("Sie können den **Preis** Ihres E-Autos noch **erhöhen**.")
            else:
                st.write("Ihr derzeitiger Preis für Ihr E-Auto liegt {:.2f} € zu hoch.".format(abs(car_info["value_difference_gb"])))
                st.write("Sie sollten den **Preis** Ihres E-Autos **senken**.")
            
           
            data_matches2 = data_filter.loc[
               (data_filter["Marke"] == car_info["Marke"]) &
               (data_filter["Modell"] == car_info["Modell"]) &
               (data_filter["reach"] >= car_info["reach"] * 0.9) & 
               (data_filter["reach"] <= car_info["reach"] * 1.1) &
               (data_filter["age"] >= car_info["age"] * 0.5) &
               (data_filter["age"] <= car_info["age"] * 1.5) &
               (data_filter["ps"] >= car_info["ps"] * 0.9) &
               (data_filter["ps"] <= car_info["ps"] * 1.1)
               ]
            
            if not data_matches2.empty:
                if st.checkbox("Zeige ähnliche bereits inserierte Angebote", False):
                    st.subheader("Ähnliche Angebote bei AutoScout")
                    col1, col2 = st.columns(2)
                    with col1:
                        ui.metric_card(
                            title="Anzahl ähnlicher Angebote",
                            content=f"{data_matches2.shape[0]}",
                            key="card4"
                    )
                    with col2:
                        ui.metric_card(
                            title="Durchschnittspreis der ähnlichen Angebote",
                            content=f"{data_matches2['price'].mean():,.2f} €",
                            key="card5"
                    )
        
            else:
                st.error("🚨URL nicht in der Datenbank gefunden.🚨")
            
            
            
            
            
            