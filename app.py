from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import warnings
import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
warnings.filterwarnings("ignore")


st.set_page_config(layout="wide")
st.title("Airbnb Data Analysis")


def data():
    df = pd.read_csv(
        "C:/Users/rdine/Data_Science/data_science_practise/DataScience_projects/airnb_analyst/imp_df.csv")
    return df


df = data()


def Data_Analysis():
    tab1, tab2, tab3 = st.tabs(
        ["Price Analysis", "Avalibility Analysis", "Location Based"])

    with tab1:
        st.title("Price Analysis")
        col1, col2 = st.columns(2)

        with col1:

            country = st.selectbox("Select the country",
                                   df["country"].unique())

            df1 = df[df["country"] == country]
            df1.reset_index(drop=True, inplace=True)

            room_type = st.selectbox(
                "Select the Room Type ", df1["room_type"].unique())

            df2 = df1[df1["room_type"] == room_type]
            df2.reset_index(drop=True, inplace=True)

            df_bar = pd.DataFrame(df2.groupby("property_type")[
                                  ["price", "review_scores", "number_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)

            fig_bar = px.bar(df_bar, x='property_type', y="price", title="PRICE FOR PROPERTY_TYPES", hover_data=[
                             "number_of_reviews", "review_scores"], color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            property_type = st.selectbox(
                "Select the property type", df2["property_type"]. unique())

            df3 = df2[df2["property_type"] == property_type]
            df3.reset_index(drop=True, inplace=True)

            df_pie = pd.DataFrame(df3.groupby("host_response_time")[
                                  ["price", "bedrooms"]].sum())

            df_pie.reset_index(inplace=True)

            fig_pie = px.pie(df_pie, values="price", names="host_response_time",
                             hover_data=["bedrooms"],
                             color_discrete_sequence=px.colors.sequential.BuPu_r,
                             title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                             width=500, height=500)
            st.plotly_chart(fig_pie)

        col1, col2 = st.columns(2)

        with col1:

            host_response_time_1 = st.selectbox(
                "Select the host response time", df3["host_response_time"].unique())

            df4 = df3[df3["host_response_time"] == host_response_time_1]

            df_bed_bar = pd.DataFrame(df4.groupby("bed_type")[
                                      ["minimum_nights", "maximum_nights", "price"]].sum())

            df_bed_bar.reset_index(inplace=True)

            fig_bed_bar = px.bar(df_bed_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'],
                                 title='MINIMUM NIGHTS AND MAXIMUM NIGHTS', hover_data="price",
                                 barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow, width=500, height=500)

            st.plotly_chart(fig_bed_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_bed_bar = pd.DataFrame(df4.groupby("bed_type")[
                                      ["bedrooms", "beds", "accommodates", "price"]].sum())

            df_bed_bar.reset_index(inplace=True)

            fig_bed_bar_2 = px.bar(df_bed_bar, x='bed_type', y=['bedrooms', 'beds', 'accommodates'],
                                   title='BEDROOMS AND BEDS ACCOMMODATES', hover_data="price",
                                   barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=500, height=500)

            st.plotly_chart(fig_bed_bar_2)

    with tab2:
        df_ava = data()

        st.title("Avalibility Analysis")

        col1, col2 = st.columns(2)

        with col1:

            country_availability = st.selectbox(
                "Select the country availability", df_ava["country"].unique())

            df1_ava = df[df["country"] == country_availability]
            df1_ava.reset_index(drop=True, inplace=True)

            property_availability = st.selectbox(
                "Select the Property Type", df1_ava["property_type"].unique())

            df2_ava = df1_ava[df1_ava["property_type"]
                              == property_availability]
            df2_ava.reset_index(drop=True, inplace=True)

            df_ava_sun_30 = px.sunburst(df2_ava, path=["room_type", "bed_type", "is_location_exact"], values="availability_30",
                                        width=500, height=500, title="Availability_30", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_ava_sun_30)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_ava_sun_60 = px.sunburst(df2_ava, path=["room_type", "bed_type", "is_location_exact"], values="availability_60",
                                        width=500, height=500, title="Availability_60", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_ava_sun_60)

        col3, col4 = st.columns(2)

        with col3:
            df_ava_sun_90 = px.sunburst(df2_ava, path=["room_type", "bed_type", "is_location_exact"], values="availability_90",
                                        width=500, height=500, title="Availability_90", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_ava_sun_90)

        with col4:

            df_ava_sun_365 = px.sunburst(df2_ava, path=["room_type", "bed_type", "is_location_exact"], values="availability_365",
                                         width=500, height=500, title="availability_365", color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_ava_sun_365)

        room_type_ava = st.selectbox(
            "Select the room type availability", df2_ava["room_type"].unique())

        df3_ava = df2_ava[df2_ava["room_type"] == room_type_ava]

        df_bar_ava = pd.DataFrame(df3_ava.groupby("host_response_time")[
                                  ["availability_30", "availability_60", "availability_90", "availability_365", "price"]].sum())
        df_bar_ava.reset_index(inplace=True)

        fig_df_bar_a_ava = px.bar(df_bar_ava, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"],
                                  title='AVAILABILITY BASED ON HOST RESPONSE TIME', hover_data="price",
                                  barmode='group', color_discrete_sequence=px.colors.sequential.Plotly3, width=800)

        st.plotly_chart(fig_df_bar_a_ava)

    with tab3:

        st.title("Location Based Analysis")
        st.write("")

        df_loc = data()

        country_loc = st.selectbox(
            "Select the country location", df_loc["country"].unique())

        df1_loc = df_loc[df_loc["country"] == country_loc]
        df1_loc.reset_index(drop=True, inplace=True)

        property_type_loc = st.selectbox(
            " Select the property type", df1_loc["property_type"].unique())

        df2_loc = df1_loc[df1_loc["property_type"] == property_type_loc]
        df2_loc.reset_index(drop=True, inplace=True)

        def select_the_df(sel_val):
            if sel_val == str(df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str("(30% of the Value)"):

                df_val_30 = df2_loc[df2_loc["price"] <=
                                    differ_max_min*0.30 + df2_loc['price'].min()]
                df_val_30.reset_index(drop=True, inplace=True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str("(30% to 60% of the Value)"):

                df_val_60 = df2_loc[df2_loc["price"] >=
                                    differ_max_min*0.30 + df2_loc['price'].min()]
                df_val_60_1 = df_val_60[df_val_60["price"] <=
                                        differ_max_min*0.60 + df2_loc['price'].min()]
                df_val_60_1.reset_index(drop=True, inplace=True)
                return df_val_60_1

            elif sel_val == str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str('to')+' '+str(df2_loc['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100 = df2_loc[df2_loc["price"] >=
                                     differ_max_min*0.60 + df2_loc['price'].min()]
                df_val_100.reset_index(drop=True, inplace=True)
                return df_val_100

        differ_max_min = df2_loc["price"].max() - df2_loc["price"].min()

        val_sel = st.radio("Select the price range", [str(df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str("(30% of the Value)"),

                                                      str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str('to')+' '+str(
                                                          differ_max_min*0.60 + df2_loc['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                      str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str('to')+' '+str(df2_loc['price'].max())+' '+str("(60% to 100% of the Value)")])

        df_vel_sel = select_the_df(val_sel)

        st.dataframe(df_vel_sel)

        df_vel_sel_corr = df_vel_sel.drop(columns=["listing_url", "name", "property_type",
                                                   "room_type", "bed_type", "cancellation_policy",
                                                   "images", "host_url", "host_name", "host_location",
                                                   "host_response_time", "host_thumbnail_url",
                                                   "host_response_rate", "host_is_superhost", "host_has_profile_pic",
                                                   "host_picture_url", "host_neighbourhood",
                                                   "host_identity_verified", "host_verifications",
                                                   "street", "suburb", "government_area", "market",
                                                   "country", "country_code", "location_type", "is_location_exact",
                                                   "amenities"]).corr()

        st.dataframe(df_vel_sel_corr)

        df_val_sel_gr = pd.DataFrame(df_vel_sel.groupby("accommodates")[
                                     ["cleaning_fee", "bedrooms", "beds", "extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace=True)

        fig_1 = px.bar(df_val_sel_gr, x="accommodates", y=["cleaning_fee", "bedrooms", "beds"], title="ACCOMMODATES",
                       hover_data="extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=800)
        st.plotly_chart(fig_1)

        room_ty_l = st.selectbox(
            "Select the Room Type based on location", df_vel_sel["room_type"].unique())

        df_val_sel_rt = df_vel_sel[df_vel_sel["room_type"] == room_ty_l]

        fig_2 = px.bar(df_val_sel_rt, x=["street", "host_location", "host_neighbourhood"], y="market", title="MARKET",
                       hover_data=["name", "host_name", "market"], barmode='group', orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
        st.plotly_chart(fig_2)

        fig_3 = px.bar(df_val_sel_rt, x="government_area", y=["host_is_superhost", "host_neighbourhood", "cancellation_policy"], title="GOVERNMENT_AREA",
                       hover_data=["guests_included", "location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
        st.plotly_chart(fig_3)


def Geo_visualization():
    st.title("Geo visualization")

    fig_geo = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                                color_continuous_scale="rainbow", hover_name='name', range_color=(0, 49000), mapbox_style="carto-positron",
                                zoom=0)
    fig_geo.update_layout(width=800, height=600,
                          title='Geospatial Distribution of Listings')
    st.plotly_chart(fig_geo)


with st.sidebar:
    st.title("Airbnb analysis")

    st.title("Press the option to view the presentation")
    show_table = st.radio("press the option", ["Home", "Data Analysis", "Geo visualization"],
                          )

if show_table == "Home":
    # show_channels_table()
    st.write("home")

elif show_table == "Data Analysis":
    Data_Analysis()

elif show_table == "Geo visualization":
    Geo_visualization()
